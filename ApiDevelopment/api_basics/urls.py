from django.urls import path, include
from .views import ArticleListAPIView, AddArticle, ArticleByID, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')      # 1st arg - prefix (could be any) and basename - too

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('article/', ArticleListAPIView.as_view()),
    path('generic/article/<int:pk>/', GenericAPIView.as_view()),
    path('article/add', AddArticle.as_view()),
    path('article/getBy/<int:pk>/', ArticleByID.as_view()),
]
