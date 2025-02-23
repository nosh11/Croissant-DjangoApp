from portfolio.models import PortFolio
from django import forms


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortFolio
        fields = ['title', 'description', 'image', 'url']