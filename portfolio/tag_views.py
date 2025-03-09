import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from portfolio.forms import PortfolioTagForm
from portfolio.models import PortFolio, Tag

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Index
class PortfolioTagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'portfolio/tag/index.html', {'tags': tags})
index = PortfolioTagListView.as_view()


# Create
class PortfolioTagCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('portfolio.add_tag')
    
    def get(self, request, pk=None):
        if pk:
            tag = Tag.objects.get(pk=pk)
            form = PortfolioTagForm(instance=tag)
        else:
            form = PortfolioTagForm()

        return render(request, 'portfolio/tag/create.html', {'form': form, 'pk': pk})

    def post(self, request, pk=None):
        form = PortfolioTagForm(request.POST)
        if form.is_valid():
            if pk:
                tag = Tag.objects.get(pk=pk)
                tag.name = form.cleaned_data['name']
                tag.save()
                return redirect('tag')
            else:
                form.save()
                return redirect('tag')

        return render(request, 'portfolio/tag/create.html', {'form': form, 'error': '入力内容が正しくありません'})
create = PortfolioTagCreateView.as_view()

class PortfolioTagDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.has_perm('portfolio.delete_tag')
    
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return redirect('tag')
    
delete = PortfolioTagDeleteView.as_view()