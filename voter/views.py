from django.shortcuts import render

from .models import Uchwala


def index(request):
    ostatnie_uchwaly = Uchwala.objects.order_by('id')[:5]
    context = {'ostatnie_uchwaly': ostatnie_uchwaly}
    return render(request, 'index.html', context)