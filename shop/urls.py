from django.urls import path
from shop import views

urlpatterns = [
    path('login', views.login , name='ShopHome'),
    path('game', views.game , name='ShopHome'),
    path('2048', views.firstg , name='ShopHome'),
    path('reg', views.reg , name='ShopHome'),
    path('logout', views.logout_view , name='ShopHome'),    
]