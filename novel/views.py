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
                Novel.objects.filter(pk=pk).update(**form.cleaned_data)
                return redirect('index')

            # create処理
            else:
                form.save()
                return redirect('index')
        return render(request, 'novel/create.html', {'form': form})

create = NovelCreateView.as_view()

class NovelInfoView(View):
    def get(self, request, pk):
        novel = Novel.objects.get(pk=pk)
        return render(request, 'novel/info.html', {'novel': novel})

info = NovelInfoView.as_view()


class NovelDeleteView(View):
    def get(self, request, pk):
        novel = Novel.objects.get(pk=pk)
        novel.delete()
        return redirect('index')

delete = NovelDeleteView.as_view()