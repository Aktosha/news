from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet
from . import views

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('news', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', include(router.urls)),
    # path('admin/', admin.site.urls),
    # path('news-list/', views.NewsListAPIView.as_view()),
    # path('news-detail/<int:pk>/', views.NewsRetriveAPIView.as_view()),
    # path('new-delete/<int:pk>', views.NewDestroyAPIview.as_view()),
    # path('news-set/', views.NewViewSet.as_view()),
    # path('update-list/<int:pk>/', views.NewUpdateAPIView.as_view()),
    # path('create-list/', views.NewCreateAPIView.as_view()),
]