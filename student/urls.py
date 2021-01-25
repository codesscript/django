from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
   path('',views.student_form),
   path('student_info',views.student_info),
   path('show/',views.show),
   path('edit/<int:id>',views.edit),
   path('update/<int:id>',views.update),
   path('delete/<int:id>',views.delete)
]