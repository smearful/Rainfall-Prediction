from django.urls import path
from . import views  # Import all views

urlpatterns = [
    path("", views.redirect_to_home),
    path("home/", views.home, name='home'),  
    path("predict/", views.predict_rainfall, name='predict'),  
]
# Append static URL patterns for development (after defining `urlpatterns`)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)