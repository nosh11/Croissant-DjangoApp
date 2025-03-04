import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from portfolio.forms import PortfolioForm
from portfolio.models import PortFolio, Tag

import requests
from bs4 import BeautifulSoup

# Index
class PortfolioListView(View):
    def get(self, request, tags = None):
        portfolios = PortFolio.objects.all()
        if tags:
            portfolios = portfolios.filter(tags__name__in=tags)
        return render(request, 'portfolio/index.html', {'portfolios': portfolios})
index = PortfolioListView.as_view()

# Create
class PortfolioCreateView(View):
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
create = PortfolioCreateView.as_view()

class PortfolioDetailView(View):
    def get(self, request, pk):
        if not pk:
            return redirect('index')

        portfolio = PortFolio.objects.get(pk=pk)

        # portfolio.url が www.youtube.com -> embed url に変換しyoutube_urlを返す
        if not portfolio.url:
            tag = None
        elif ('www.youtube.com' in portfolio.url):
            tag = create_youtube_iframe(portfolio.url)
        else:
            tag = create_normal_atag(portfolio.url)

        return render(request, 'portfolio/detail.html', {'portfolio': portfolio, 'url_tag': tag})
detail = PortfolioDetailView.as_view()


class DeletePortfolioView(View):
    def get(self, request, pk):
        if not pk:
            return redirect('index')

        portfolio = PortFolio.objects.get(pk=pk)
        portfolio.delete()

        return redirect('index')
delete = DeletePortfolioView.as_view()


# create <iframe> tag for youtube video
def create_youtube_iframe(url: str) -> str:
    video_id = url.split('=')[-1]
    iframe = (
        f"<iframe width='560' height='315' src='https://www.youtube.com/embed/{video_id}' "
        "frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' "
        "allowfullscreen></iframe>"
    )
    return iframe

def get_page_title(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーが発生した場合に例外を発生させる
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except AttributeError:
        print("Title tag not found")
        return None



def create_normal_atag(url: str) -> str:
    title = get_page_title(url)
    if not title:
        return f"<a href='{url}'>Jump to page</a>"
    else:
        return f"<a href='{url}'>{title}</a>"

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fetch_thumbnail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        url = data.get('url')
        if 'youtube.com' in url:
            thumbnail_url = get_youtube_thumbnail(url)
            return JsonResponse({'thumbnail_url': thumbnail_url})
        return JsonResponse({'error': 'Invalid URL'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_youtube_thumbnail(url: str) -> str:
    video_id = url.split('=')[-1]
    return f"https://img.youtube.com/vi/{video_id}/sddefault.jpg"