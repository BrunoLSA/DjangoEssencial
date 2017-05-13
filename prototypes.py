import os
import sys

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)

SITE_PAGES_DIRECTORY = os.path.join(BASE_DIR, 'pages')

settings.configure(
    DEBUG=True,
    SECRET_KEY='pqqhhvo*t=8p@)hy5o!5yqm&!ban6lpc&)3@qg2%7%$pm^n3bc',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'sitebuilder/templates'),
                SITE_PAGES_DIRECTORY,
            ],
        },
    ),
    SITE_PAGES_DIRECTORY=SITE_PAGES_DIRECTORY,
    STATIC_URL='/static/',
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)