from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('create',views.create,name='create'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('go/<str:token>',views.redirector,name='redirector')
]
