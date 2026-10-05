"""materialhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from materialhub import settings
from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('add_material_get/',views.add_material_get),
    path('add_material_post/',views.add_material_post),
    path('edit_material_get/<id>',views.edit_material_get),
    path('edit_material_post/',views.edit_material_post),
    path('view_material_get/',views.view_material_get),
    path('deletematerial_get/<id>',views.deletematerial_get),
    path('add_stock_get/',views.add_stock_get),
    path('add_stock_post/',views.add_stock_post),
    path('edit_stock_get/<id>',views.edit_stock_get),
    path('deletestock_get/<id>',views.deletestock_get),
    path('edit_stock_post/',views.edit_stock_post),
    path('view_stock_get/',views.view_stock_get),
    path('delete_stock_get/',views.delete_stock_get),
    path('add_driver_get/',views.add_driver_get),
    path('add_driver_post/',views.add_driver_post),
    path('edit_driver_get/<id>',views.edit_driver_get),
    path('edit_driver_post/',views.edit_driver_post),
    path('view_driver_get/',views.view_driver_get),
    path('delete_driver_get/<id>',views.delete_driver_get),
    # path('delete_driver_get/',views.delete_driver_get),
    path('view_user_request_get/',views.view_user_request_get),
    path('approve_user_request/<id>',views.approve_user_request),
    path('reject_user_request/<id>',views.reject_user_request),
    path('view_approve_user_request/',views.view_approve_user_request),
    path('view_rejected_user_request/',views.view_rejected_user_request),
    path('view_complaint_get/',views.view_complaint_get),
    path('sentreply_get/',views.sentreply_get),
    path('sentreply_post/',views.sentreply_post),
    path('changepassword_get/',views.changepassword_get),
    path('changepassword_post/',views.changepassword_post),
    path('adminhome_get/',views.adminhome_get),
    path('allocationclient_get/<id>',views.allocationclient_get),
    path('allocationclient_post/',views.allocationclient_post),




    # driver
    path('d_changepassword_get/',views.d_changepassword_get),
    path('driverhome_get/',views.driverhome_get),
    path('updatestatus/<id>',views.updatestatus),
    path('d_changepassword_post/',views.d_changepassword_post),
    path('viewallocation_get/',views.viewallocation_get),
    path('viewprofile_get/',views.viewprofile_get),


    #user
    path('editprofile_get/<id>',views.editprofile_get),
    path('userhome_get/',views.userhome_get),
    path('viewrequeststatus/',views.viewrequeststatus),
    path('userviewprofile_get/',views.userviewprofile_get),
    path('editprofile_post/',views.editprofile_post),
    path('materialclient_get/',views.materialclient_get),
    path('mmaterialclientquntyy_get/<id>',views.mmaterialclientquntyy_get),
    path('mmaterialclientquntyy_post/',views.mmaterialclientquntyy_post),
    path('paymenthistoryclient_get/',views.paymenthistoryclient_get),
    path('sendcomplaint_get/',views.sendcomplaint_get),
    path('sendcomplaint_post/',views.sendcomplaint_post),
    path('signupclient_get/',views.signupclient_get),
    path('signupclient_post/',views.signupclient_post),
    path('userchangepassword_get/',views.userchangepassword_get),
    path('userchangepassword_post/',views.userchangepassword_post),
    path('view_reply_get/',views.view_reply_get),
]
