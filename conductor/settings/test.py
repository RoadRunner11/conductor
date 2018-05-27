from conductor.settings.base import *  # noqa

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


class DisableMigrations(object):
    """Disable migrations for apps.

    Forcing migrations to run during testing is super annoying
    when the migration hasn't been generated yet.
    Skip migrations for tests.
    """

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Circle CI doesn't seem to like the ManifestStaticFilesStorage
# and blows up on the first static asset that it encounters.
# I don't care about testing against the manifested versions.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
