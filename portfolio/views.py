import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from portfolio.forms import PortfolioForm
from portfolio.models import PortFolio, Tag

import requests
from bs4 import BeautifulSoup

# Index
def index(request, tag_id=None):
    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        portfolios = PortFolio.objects.filter(tags=tag)
    else:
        portfolios = PortFolio.objects.all()
    tags = Tag.objects.all()
    return render(request, 'portfolio/index.html', {'portfolios': portfolios, 'tags': tags, 'selected_tag_id': tag_id})

# Create
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PortfolioCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('portfolio.add_portfolio')

    def get(self, request, pk=None):
        if pk:
            portfolio = PortFolio.objects.get(pk=pk)
            form = PortfolioForm(instance=portfolio)
        else:
            form = PortfolioForm()
        
        tags = Tag.objects.all()

        return render(request, 'portfolio/create.html', {'form': form, 'pk': pk, 'tags': tags})

    def post(self, request, pk=None):
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            if pk:
                portfolio = PortFolio.objects.get(pk=pk)
                portfolio.title = form.cleaned_data['title']
                portfolio.description = form.cleaned_data['description']
                portfolio.image = form.cleaned_data['image']
                portfolio.url = form.cleaned_data['url']
                portfolio.tags.set(form.cleaned_data['tags'])
                
                portfolio.save()
                return redirect('index')
            else:
                form.save()
                return redirect('index')
        
        return render(request, 'portfolio/create.html', {'form': form, 'error': '入力内容が正しくありません'})

class PortfolioDetailView(View):
    def get(self, request, pk):
        if not pk:
            return redirect('index')
        portfolio = PortFolio.objects.get(pk=pk)
        return render(request, 'portfolio/detail.html', {'portfolio': portfolio})
detail = PortfolioDetailView.as_view()


class DeletePortfolioView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('portfolio.delete_portfolio')
    
    def get(self, request, pk):
        if not pk:
            return redirect('index')

        portfolio = PortFolio.objects.get(pk=pk)
        portfolio.delete()

        return redirect('index')