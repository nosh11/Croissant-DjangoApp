from portfolio.models import PortFolio, Tag
from django import forms


class PortfolioForm(forms.ModelForm):
    title = forms.CharField(label='タイトル', max_length=100)
    description = forms.CharField(label='内容', widget=forms.Textarea, max_length=1000)
    url = forms.URLField(label='URL', required=False, max_length=200)
    image = forms.ImageField(label='イメージ', required=False)
    tags = forms.ModelMultipleChoiceField(
        label='タグ', 
        queryset=Tag.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = PortFolio
        fields = ['title', 'description', 'url', 'image', 'tags']



        


class PortfolioTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']