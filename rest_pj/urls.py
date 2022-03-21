from django.conf.urls import url, include
from django.contrib import admin

from api_test.urls import router as rest_pj_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(rest_pj_router.urls)),
]