"""
WSGI config for senate_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, site

if os.path.exists("/var/django/senate/"):
    site.addsitedir('/var/django/senate/env/local/lib/python2.7/site-packages')

    sys.path.append('/var/django/senate/')
    sys.path.append('/var/django/senate/senate-website/')

    #Activate your virtual env
    activate_env=os.path.expanduser("/var/django/senate/env/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))


from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("senate_website"))

application = get_wsgi_application()
