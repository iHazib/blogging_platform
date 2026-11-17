from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import JsonResponse
from accounts.views import CustomLoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def health_check(request):
    return JsonResponse({"status": "ok", "message": "Server is running perfectly!"})

urlpatterns = [
    path('admin/', admin.site.urls),

    path('health/', health_check), 
    
    # For login
    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # For blogs app
    path('api/blogs/', include('blog.urls')),

    # For accounts app
    path('api/accounts/', include('accounts.urls')),

    # For api docs and UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 

]