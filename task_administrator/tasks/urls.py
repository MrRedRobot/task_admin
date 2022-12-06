from rest_framework import routers
from .views.task_api_view import TaskViewSet

router = routers.DefaultRouter()

router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls
