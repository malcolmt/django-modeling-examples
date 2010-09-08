from django.conf.urls.defaults import *     # pylint: disable-msg=W0401,W0614
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

