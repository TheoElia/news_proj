from django.urls import path
from accounts import views


urlpatterns = [
path('',views.index,name="home"),
path('signup/', views.CreateUserView.as_view(), name='signup'),
]