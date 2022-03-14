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
    path('list-users', views.list_users, name="list-users"),
    path('user-detail/<str:pk>', views.user_detail, name="user-detail"),
    path('create-user', views.create_user, name="create-user"),
    path('update-user/<str:pk>', views.update_user, name="update-user"),
    path('delete-user/<str:pk>', views.delete_user, name="delete-user"),

    path('list-places', views.list_places, name="list-places"),
    path('user-places/<str:pk>', views.list_user_places, name="user-places"),
    path('create-place', views.create_place, name="create-place"),
    path('update-place/<str:pk>', views.update_place, name="update-place"),
    path('delete-place/<str:pk>', views.delete_place, name="delete-place"),
    path('get-active-user', views.get_active_user, name="get-active-user"),
    path('set-active-user/<str:pk>', views.set_active_user, name="set-active-user"),

    path('delete-device/<str:pk>', views.delete_device, name="delete-device"),
    path('post-place-weather', views.post_place_weather, name="post-place-weather"),
    path('get-place-weather/lat=<str:lat>&lon=<str:lon>', views.get_place_weather, name="get-place-weather")
]
