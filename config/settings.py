from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-q8$1^k7t36@2_o#ddypqs2xn(0vsn07y6g@ynj_gq9zzo$_)2)"

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django_browser_reload",
    'django.contrib.contenttypes',
    "django.contrib.staticfiles",
    'django.contrib.auth',
    "django_htmx",
    'tailwind',
    'ui',
    "django_cotton.apps.SimpleAppConfig",
    "template_partials.apps.SimpleAppConfig",
]

TAILWIND_APP_NAME = 'ui'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "loaders": [
                (
                    "template_partials.loader.Loader",
                    [
                        (
                            "django.template.loaders.cached.Loader",
                            [
                                "django_cotton.cotton_loader.Loader",
                                "django.template.loaders.filesystem.Loader",
                                "django.template.loaders.app_directories.Loader",
                            ],
                        )
                    ],
                )
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "django_cotton.templatetags.cotton",
                "template_partials.templatetags.partials",
            ],
        },
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    "django_htmx.middleware.HtmxMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "config.urls"
