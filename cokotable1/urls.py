from django.urls import path

from cokotable1 import views

urlpatterns = [
    path('',views.Index),
    path('create',views.create),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('edit/update/<int:id>',views.update)
]