"""GameZoneApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('sortGame',views.sortGame,name="sortGame"),
    # path('showGame',views.showGame,name="showGame"),
    # path('insertGame',views.insertGame,name="insertGame"),
    # path('editGame/<int:id>',views.editGame,name="editGame"),
    path('',views.HomePage,name="index"),
    # path('updateGame/<int:id>',views.updateGame,name="updateGame"),
    # path('delGame/<int:id>',views.delGame,name="delGame"),
    # path('deletedGame/<int:id>',views.deletedGame,name="deletedGame"),
    # path('runQueryGame',views.runQueryGame,name="runQueryGame"),

    # path('showCustomer',views.showCustomer,name="showCustomer"),
    # path('insertCustomer',views.insertCustomer,name="insertCustomer"),
    # path('sortCustomer',views.sortCustomer,name="sortCustomer"),
    # path('editCustomer/<int:id>',views.editCustomer,name="editCustomer"),
    # path('updateCustomer/<int:id>',views.updateCustomer,name="updateCustomer"),
    # path('delCustomer/<int:id>',views.delCustomer,name="delCustomer"),
    # path('deletedCustomer/<int:id>',views.deletedCustomer,name="deletedCustomer"),
    # path('runQueryCustomer',views.runQueryCustomer,name="runQueryCustomer"),

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
