from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('loginn/', views.loginn,name='loginn'),
    path('signup/', views.signup,name='signup'),
    path('home/', views.home,name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('owner/', views.owner, name='owner'),
    path('owner/deleted/<int:id>/', views.deleted, name='deleted'),
    path('owner/updata/<int:id>/', views.updata, name='updata'),
    path('owner/data/<int:id>/', views.data, name='data'),
    path('addmem/', views.addmem, name='addmem'),
]
