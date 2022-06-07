"""SocietyManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from SocietyManagement import views as d
from societyAdmin import views as k
from user import views as h
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',d.home,name='home'),
    path('login/',k.adminLogin,name="login"),
    path('user_login/',h.userLogin,name="user_login"),
    path('registration',h.registration,name="registration"),
    path('profile/',k.AdminProfile,name="profile"),
    path('admin_logout/',k.AdminLogout,name="admin_logout"),
    path('carpenter/',k.carpenter,name="carpenter"),
    path('painter/',k.painter,name="painter"),
    path('plumber/',k.plumber,name="plumber"),
    path('roofer/',k.roofer,name="roofer"),
    path('electrician',k.electrician,name="electrician"),
    path('user_profile/',h.userProfile,name="user_profile"),
    path('painter_details/',h.PainterDetails,name="painter_details"),
    path('electrician_details/',h.ElectricianDetails,name="electrician_details"),
    path('plumber_details/',h.PlumberDetails,name="plumber_details"),
    path('roofer_details/',h.RooferDetails,name="roofer_details"),
    path('carpenter_details/',h.CarpenterDetails,name="carpenter_details"),
    path('user_logout',h.userLogout,name="user_logout"),
    path('report/',k.report,name='report'),
    path('delete/<int:id>/',k.deleteData,name="delete_plumber"),
    path('delete_painter/<int:id>/',k.deletePainter,name="delete_painter"),
    path('delete_electrician/<int:id>/',k.deleteDataElectrician,name="delete_electrician"),
    path('delete_carpenter/<int:id>/',k.deleteCarpenter,name="delete_carpenter"),
    path('delete_roofer/<int:id>/',k.deleteRoofers,name="delete_roofer"),
    path('update_plumber/<int:id>/',k.updatePlumber,name="update_plumber"),
    path('update_carpenter/<int:id>/',k.updateCarpenter,name="update_carpenter"),
    path('update_electrician/<int:id>/',k.updateElectrician,name="update_electrician"),
    path('update_roofer/<int:id>/',k.updateRoofer,name="update_roofer"),
    path('update_painter/<int:id>/',k.updatePainter,name="update_painter"),
    path('book_plumber/<int:id>',h.bookPlumber,name="book_plumber"),
    path('delPlBooking/<int:id>',h.delPlBooking,name="delPlBooking"),
    path('book_roffer/<int:id>',h.bookRoffer,name="book_roffer"),
    path('delRuBooking/<int:id>',h.delRuBooking,name="delRuBooking"),
    path('book_electrician/<int:id>',h.bookElectrician,name="book_electrician"),
    path('delElBooking/<int:id>',h.delElBooking,name="delElBooking"),
    path('book_carpenter/<int:id>',h.bookCarpenter,name="book_carpenter"),
    path('delCaBooking/<int:id>',h.delCaBooking,name="delCaBooking"),
    path('book_painter/<int:id>',h.bookPainter,name="book_painter"),
    path('delPiBooking/<int:id>',h.delPiBooking,name="delPiBooking"),
    path('services/',h.service,name="service"),
    path('user_info/',k.userInfo,name="user_info"),
    path('my_user/',h.myUser,name="my_user"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
