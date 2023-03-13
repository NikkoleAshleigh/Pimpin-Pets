from django.urls import path
from pimpin_app.views import HomeView, PawfrenceView, MessageDetailView, FureverView, NeedingLoveView, signup, login_request, logout_request
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='pimpin'),
    path('pawfrence/', PawfrenceView.as_view(), name='pawfrence'),
    path('pawfrence/<int:message_id>', MessageDetailView.as_view(), name='message_detail'),
    path('furever/', FureverView.as_view(), name='furever'),
    path('furever/<int:post_id>', NeedingLoveView.as_view(), name='adoption'),    
    path('signup', signup, name='signup'),
    path("login", login_request, name="login"),
    path("logout", logout_request, name= "logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)