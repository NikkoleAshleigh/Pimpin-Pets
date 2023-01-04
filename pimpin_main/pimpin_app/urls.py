from django.urls import path

from pimpin_app.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]