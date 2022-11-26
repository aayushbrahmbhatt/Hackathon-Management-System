from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="index"),
    path('showUser',views.showUser,name = "showUser"),
    path('showHackathon_Detail',views.showHackathon_Detail, name="Hackathon_Detail"),
    path('InsertUser',views.InsertUser,name = "InsertUser"),
    path('sortUser',views.sortUser,name = "sortUser"),
    path('editUser/<str:id>',views.editUser,name = "editUser"),
    path('updateUser/<str:id>',views.updateUser,name = "updateUser"),
    path('showRunQuery',views.showRunQuery,name = "showRunQuery"),
    path('RunQuery',views.RunQuery,name = "RunQuery"),
    path('delUser/<str:id>',views.delUser,name = "delUser"),
    path('deletedUser/<str:id>',views.deletedUser,name = "deletedUser"),

]
