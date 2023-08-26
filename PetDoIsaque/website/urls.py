from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register, name = 'register' ),
    path('produto/<int:pk>', views.cliente_produto, name = 'produto'),
    path('deletar_produto/<int:pk>', views.deletar_produto, name = 'deletar_produto'),
    path('adicionar_produto/', views.adicionar_produto, name = 'adicionar_produto'),
    path('editar_produto/<int:pk>', views.editar_produto, name = 'editar_produto'),
]