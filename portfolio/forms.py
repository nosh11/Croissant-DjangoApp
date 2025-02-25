from portfolio.models import PortFolio, Tag
from django import forms


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortFolio
        fields = ['title', 'description', 'image', 'url']


class PortfolioTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']