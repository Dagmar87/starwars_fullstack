from rest_framework.routers import DefaultRouter
from .views import CharacterViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)

urlpatterns = router.urls