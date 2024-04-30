from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import activate


class SetLanguageMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        expect_language = request.META.get("HTTP_ACCEPT_LANGUAGE", None)
        if expect_language in dict(settings.LANGUAGES):
            activate(expect_language.split(",")[0])
