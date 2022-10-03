from django.shortcuts import render
from .models import MainSlider, About, RoadMap, Service, DonationCase, News


def index(request):
    about = About.objects.last()
    main_slider = MainSlider.objects.all().order_by('-id')[:3]
    road_map = RoadMap.objects.all().order_by('-id')[:3]
    service = Service.objects.all().order_by('-id')[:3]
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
