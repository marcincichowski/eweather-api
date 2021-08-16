"""from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_user', views.save_user, name='save_user'),
    path('save_place', views.save_place, name='save_place'),
]"""

from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('list-users', views.listUsers, name="list-users"),
    path('user-detail/<str:pk>', views.userDetail, name="user-detail"),
    path('create-user', views.createUser, name="create-user"),
    path('update-user/<str:pk>', views.updateUser, name="update-user"),
    path('delete-user/<str:pk>', views.updateUser, name="delete-user"),

    path('list-places', views.listPlaces, name="list-places"),
    path('user-places/<str:pk>', views.listUserPlaces, name="user-places"),
    path('create-place', views.createPlace, name="create-place"),
    path('update-place/<str:pk>', views.updatePlace, name="update-place"),
    path('delete-place/<str:pk>', views.deletePlace, name="delete-place"),
]