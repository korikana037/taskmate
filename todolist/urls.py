from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist1, name='todolist1'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    
]