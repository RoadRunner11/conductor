from django import test
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware


class RequestFactory(test.RequestFactory):
    def authenticated_get(self, user, **kwargs):
        request = self.get(**kwargs)
        request.user = user
        return request

    def get(self, path="/", session=False, **kwargs):
        """Override the default get to avoid providing a meaningless path."""
        request = super().get(path, **kwargs)
        request.user = AnonymousUser()
        request.query_params = request.GET

        if session:
            middleware = SessionMiddleware()
            middleware.process_request(request)
            request.session.save()

        return request

    def authenticated_post(self, user, **kwargs):
        request = self.post(**kwargs)
        request.user = user
        return request

    def post(self, path="/", format="multipart", session=False, **kwargs):
        """Override the default post to avoid providing a meaningless path."""
        request = super().post(path, format=format, **kwargs)
        request.user = AnonymousUser()

        if session:
            middleware = SessionMiddleware()
            middleware.process_request(request)
            request.session.save()

        return request
