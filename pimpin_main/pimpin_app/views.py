from django.shortcuts import render
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='index.html',
        )

class FureverView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='furever.html',
        )


class PawfrenceView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='pawfrence.html',
        )