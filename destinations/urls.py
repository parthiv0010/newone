from django.urls import path
from . views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('create/',DestCreate.as_view(),name="create"),
    path("details/<int:pk>/",DestDetails.as_view(),name="details"),
    path("update/<int:pk>/",DestUpdate.as_view(),name="update"),
    path("delete/<int:pk>/",DestDelete.as_view(),name="delete"),
    path("search/<str:Title>",DestSearch.as_view(),name="search"),


    path("",views.list_dest,name='listdest'),
    path('create_mov/',views.dest_create,name='createdest'),
    path('mov_fetch/<int:id>/',views.dest_fetch,name='destfetch'),
    path('mov_update/<int:id>/',views.update_dest,name='updatedest'),
    path('mov_delete/<int:id>/',views.dest_delete,name='destdelete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('destination/<int:destination_id>/review/', add_review, name='add_review'),




]