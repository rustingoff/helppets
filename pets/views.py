from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "data" : [1, 2, 3],
        "roadmap": [1, 2, 3, 4, 5, 6]
    }
    return render(request, 'selected/index.html', context)
