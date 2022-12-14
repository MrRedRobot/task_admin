#from rest_framework import routers
from django.urls import path
#from .views.task_api_view import TaskViewSet, TaskAPIView, 
#from .views.task_api_view import task_api_view, task_detail_api_view
from .views.task_list_view import TaskListAPIView
from .views.task_create_view import TaskCreateAPIView
from .views.task_retrieve_view import TaskRetrieveAPIView
from .views.task_destroy_view import TaskDestroyAPIView
from .views.task_update_view import TaskUpdateAPIView
from .views.task_list_create_view import TaskListCreateAPIView
from .views.task_retrieve_update_destroy_view import TaskRetrieveUpdateDestroyAPIView

#router = routers.DefaultRouter()

#router.register('api/tasks', TaskViewSet, 'tasks')

#urlpatterns = router.urls

#urlpatterns = [
#    path('apiview/', TaskAPIView.as_view(), name='task_api')
#]

#urlpatterns = [
#    path('apiview/', task_api_view, name='task_api'),
#    path('apiview/<int:pk>/', task_detail_api_view, name='task_detail_api_view')
#]

urlpatterns = [
    path('tasks/',TaskListAPIView.as_view(), name='task_list'),
    path('tasks/create/',TaskCreateAPIView.as_view(), name='task_create'),
    path('tasks/retrieve/<int:pk>/',TaskRetrieveAPIView.as_view(), name='task_retrieve'),
    path('tasks/destroy/<int:pk>/',TaskDestroyAPIView.as_view(), name='task_destroy'),
    path('tasks/update/<int:pk>/',TaskUpdateAPIView.as_view(), name='task_update'),
    path('tasks/list-create/',TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/retreve-update-destroy/<int:pk>/',TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy'),

]