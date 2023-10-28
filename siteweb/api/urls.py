from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('message', views.get_messages, name='api_find_all'),
    path('message/new', views.new_message),
    path('message/<str:id>', views.get_message),
    path('message/update/<str:id>', views.update_Message),
    path('message/delete/<str:id>', views.delete_Message),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]
