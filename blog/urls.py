from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
urlpatterns = router.urls

# urlpatterns = [
#     path('hello/', views.hello_world, name='hello_world'),  
#     # path('api/posts/', views.post_list_create, name='post-list'),
#     # path('api/posts/<int:pk>/', views.post_detail, name='post-detail'),
#     # path('api/posts/my/', views.my_posts, name='my-posts'),
# ]
