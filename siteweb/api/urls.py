from django.urls import path

from . import views

urlpatterns = [
    path('message', views.get_messages, name='api_find_all'),
    path('message/new', views.new_messages),
    path('message/<str:id>', views.get_message)

]
