from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register('', views.CatsViewSet)


urlpatterns = [
    path('', views.main, name='main'),
    path(r'api/', include(router.urls)),
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
]
