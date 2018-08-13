from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model, password_validation

from conductor.vendor.services import stripe_gateway

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        required=True, max_length=User._meta.get_field("username").max_length
    )
    email = forms.EmailField(
        required=True, max_length=User._meta.get_field("email").max_length
    )
    password = forms.CharField(required=True)
    stripe_token = forms.CharField(required=True)
    postal_code = forms.CharField(required=False)

    def clean_email(self) -> str:
        """Ensure email uniqueness."""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "The email address is owned by another account."
            )
        return email

    def clean_username(self) -> str:
        """Ensure username uniqueness."""
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That username is unavailable.")
        return username

    def clean(self) -> None:
        """Validate the password.

        This happens outside of a clean_password method
        because the validators need to validate against
        a user instance so other form data is needed.
        """
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        # Only check if the required fields were provided.
        # Otherwise, the form is already failing.
        if email and username and password:
            user = User(email=email, username=username)
            try:
                password_validation.validate_password(password, user)
            except forms.ValidationError as error:
                self.add_error("password", error)

    def save(self) -> settings.AUTH_USER_MODEL:
        """Create the user.

        This will add a new user and start the subscription.
        """
        user = User(
            email=self.cleaned_data["email"], username=self.cleaned_data["username"]
        )
        user.set_password(self.cleaned_data["password"])

        # Before persisting anything, make sure that the customer creation
        # happens with Stripe.
        stripe_customer_id = stripe_gateway.create_customer(
            user, self.cleaned_data["stripe_token"]
        )

        user.save()

        user.profile.stripe_customer_id = stripe_customer_id
        if self.cleaned_data["postal_code"]:
            user.profile.postal_code = self.cleaned_data["postal_code"]
        user.profile.save()

        return user
