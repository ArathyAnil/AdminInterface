from django.urls import path
from .views import userLogin,logoutUser,TestModelView,dashboardView

urlpatterns = [
    path('',userLogin,name='login-user'),
    path('logout',logoutUser,name='logout-user'),
    path('dashboard',dashboardView,name='sections-dashboard'),
    path('add',TestModelView.as_view(),name='add-entry'),
    path('getList',TestModelView.as_view(),name='display-list'),
    path('getList/<int:pk>',TestModelView.as_view(),name='put-entry')

]