from django.urls import path
from . import views
urlpatterns = [
    path('',views.index_view,name='index'),
    path('add-task',views.add_task,name='add'),
    path('edit-task/<int:id>/',views.edit_task,name='edit'),
    path('delete-task/<int:id>/',views.delete_task,name='delete'),

    path('do-task/<int:id>/',views.done_task_view,name='done'),
    path('undo-task/<int:id>/',views.undo_task_view,name='undo'),

]
