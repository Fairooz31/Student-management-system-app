from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name = "add_student"),
    path('show_student/', views.show_student, name = "show_student"),
    path('delete_student/<int:id>', views.delete_student, name = "delete_student"),
    path('view_student/<int:id>', views.view_student, name = "view_student"),
    path('edit_student/', views.edit_student, name = "edit_student"),

]