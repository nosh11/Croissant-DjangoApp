from django.shortcuts import render
from django.views import View

# create root view
class RootView(View):
    def get(self, request):
        return render(request, 'index.html')
    
root = RootView.as_view()
