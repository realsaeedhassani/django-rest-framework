r"""
Django REST FRAMEWORK
"""

import django

__title__ = 'Django REST framework'
__version__ = '3.12.4'
__author__ = 'Tom Christie'
__license__ = 'BSD 3-Clause'
__copyright__ = 'Copyright 2011-2019 Encode OSS Ltd'

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'


if django.VERSION < (3, 2):
    default_app_config = 'rest_framework.apps.RestFrameworkConfig'


class RemovedInDRF313Warning(DeprecationWarning):
    pass


class RemovedInDRF314Warning(PendingDeprecationWarning):
    pass
