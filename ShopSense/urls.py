from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from shoppy import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenresViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
