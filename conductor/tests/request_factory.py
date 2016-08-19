from rest_framework.test import APIRequestFactory


class RequestFactory(APIRequestFactory):

    def get(self, path='/', **kwargs):
        """Override the default get to avoid providing a meaningless path."""
        return super(RequestFactory, self).get(path, **kwargs)

    def post(self, path='/', **kwargs):
        """Override the default post to avoid providing a meaningless path."""
        return super(RequestFactory, self).post(path, **kwargs)
