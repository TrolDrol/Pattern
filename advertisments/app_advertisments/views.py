from django.shortcuts import render, redirect # Для отправки HTML по запросу пользователя
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertismentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def test(request):
    return HttpResponse('Успешно')
def index(request):
    title = request.GET.get('query')
    if title:
        advertisments = Advertisement.objects.filter(title=title)
    else:
        advertisments = Advertisement.objects.all()
    context = {'advertisments': advertisments,
               'title': title}
    return render(request, "app_adv/index.html", context)

def top_sellers(request):
    return render(request, "app_adv/top-sellers.html")

@login_required(login_url=reverse_lazy('login'))
def advertisment_post(request):
    if request.method == 'POST':
        form = AdvertismentForm(request.POST, request.FILES)
        if form.is_valid():
            advertisment = Advertisement(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertismentForm()
        context = {'form': form}
        return render(request, 'app_adv/advertisement-post.html', context)

def advertisment_datail(request, pk):
    advertisment = Advertisement.objects.get(id=pk)
    context = {'advertisments': advertisment}
    return render(request, 'app_adv/advertisement', context)