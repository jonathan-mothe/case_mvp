from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views as api_views


router = routers.DefaultRouter()
router.register(r'demandas', api_views.DemandaList)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
#    path('rest-auth/', include('rest_auth.urls')),
#    path('rest-auth/registration/', include('rest_auth.registration.urls')),


]
