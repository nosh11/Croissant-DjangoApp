from django.shortcuts import redirect, render
from django.views import View

from novel.forms import NovelForm
from novel.models import Novel

# Create your views here.

class NovelListView(View):
    def get(self, request):
        novels = Novel.objects.all()
        return render(request, 'novel/index.html', {'novels': novels})

index = NovelListView.as_view()

# 
class NovelCreateView(View):
    def get(self, request, pk = None):
        if (pk):
            novel = Novel.objects.get(pk=pk)
            form = NovelForm(instance=novel)
        else:
            form = NovelForm()
        context = {
            'form': form,
            'pk': pk
            }
        return render(request, 'novel/create.html', context)

    def post(self, request, pk = None):
        form = NovelForm(request.POST)
        if form.is_valid():
            print(pk)
            # edit処理
            if (pk):
                novel = Novel.objects.get(pk=pk)
                novel.title = form.cleaned_data['title']
                novel.author = form.cleaned_data['author']
                novel.description = form.cleaned_data['description']
                novel.letter_body = form.cleaned_data['letter_body']
                novel.save()
                return redirect('index')

            # create処理
            else:
                form.save()
                return redirect('index')
        return render(request, 'novel/create.html', {'form': form})

create = NovelCreateView.as_view()

class NovelInfoView(View):
    def get(self, request, pk):
        if (Novel.objects.filter(pk=pk).exists() == False):
            return render(request, '404.html')
        novel = Novel.objects.get(pk=pk)
        return render(request, 'novel/info.html', {'novel': novel})

info = NovelInfoView.as_view()


class NovelDeleteView(View):
    def get(self, request, pk):
        if (Novel.objects.filter(pk=pk).exists() == False):
            return render(request, '404.html')

        novel = Novel.objects.get(pk=pk)
        novel.delete()
        return redirect('index')

delete = NovelDeleteView.as_view()