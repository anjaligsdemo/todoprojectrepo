from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('classbaseviewhome/', views.TodoListView.as_view(), name='classbaseviewhome'),
    path('classbaseviewdetail/<int:pk>/', views.TodoDetailView.as_view(), name='classbaseviewdetail'),
    path('classbaseviewupdate/<int:pk>/', views.TodoUpdateView.as_view(), name='classbaseviewupdate'),
    path('classbaseviewdelete/<int:pk>/', views.TodoDeleteView.as_view(), name='classbaseviewdelete')

]