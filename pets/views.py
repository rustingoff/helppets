from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import MainSlider, About, RoadMap, Service, DonationCase, News, SubscribeForm, Subscribe


def index(request):
    about = About.objects.last()
    main_slider = MainSlider.objects.all().order_by('-id')[:3]
    road_map = RoadMap.objects.all().order_by('-id')[:3]
    service = Service.objects.last()
    donation_case = DonationCase.objects.all().order_by('-id')[:3]
    news = News.objects.all().order_by('-id')[:3]

    context = {
        'about': about,
        'main_slider': main_slider,
        'road_map': road_map,
        'service': service,
        'donation_case': donation_case,
        'news': news,
    }

    return render(request, 'selected/index.html', context)


def get_subscription(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            s = Subscribe()
            s.email = form.cleaned_data['your_email']
            s.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
