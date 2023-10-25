from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bidule', views.bidule, name='home_bidule'),
    path('messages', views.findAll, name='messageAll'),
    path('messages/new', views.newMessage, name='newMessage'),
    path('messages/delete/<str:id>', views.deleteMessage, name='delete_message'),
    path('messages/update/<str:id>', views.updateMessage, name='update_message'),
    path('messages/<str:id>', views.show_message, name='show_message'),

]
