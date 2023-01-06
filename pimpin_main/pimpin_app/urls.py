from django.urls import path

from pimpin_app.views import HomeView, FureverView, PawfrenceView

urlpatterns = [
    path('', HomeView.as_view(), name='pimpin'),
    path('', PawfrenceView.as_view(), name='pawfrence'),
    path('', FureverView.as_view(), name='furever'),

]