from rest_framework.routers import DefaultRouter
from .views.comentary_viewset import  ComentaryViewSet

router = DefaultRouter()

router.register(r'comentarys',ComentaryViewSet)

urlpatterns = router.urls