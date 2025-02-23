from django.shortcuts import redirect, render
from django.views import View

from portfolio.forms import PortfolioForm
from portfolio.models import PortFolio

# Create your views here.


class PortfolioListView(View):
    def get(self, request):
        portfolios = PortFolio.objects.all()
        return render(request, 'portfolio/index.html', {'portfolios': portfolios})
    
index = PortfolioListView.as_view()

class PortfolioCreateView(View):
    def get(self, request):
        form = PortfolioForm()
        return render(request, 'portfolio/create.html', {'form': form})

    def post(self, request):
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'portfolio/create.html', {'form': form})
    
    
create = PortfolioCreateView.as_view()

class PortfolioDetailView(View):
    def get(self, request, pk):
        if not pk:
            return redirect('index')

        portfolio = PortFolio.objects.get(pk=pk)
        return render(request, 'portfolio/detail.html', {'portfolio': portfolio})
    
detail = PortfolioDetailView.as_view()
