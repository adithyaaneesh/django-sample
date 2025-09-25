from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('home/', views.index,name='home'),
    path('home/details/<int:id>',views.details, name='details'),
    path('testing/',views.testing),
    path('add/',views.add, name='add'),
    path('add_record/',views.add_record, name='add_record'),
    path('update/<int:id>/',views.update, name='update'),
    path('delete/<int:id>/',views.delete, name='delete')
]
