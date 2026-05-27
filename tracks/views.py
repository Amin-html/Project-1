from django.shortcuts import render, get_object_or_404
from .models import Track

def track_list(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/track_list.html', {'tracks': tracks})

def track_detail(request, pk):
    track = get_object_or_404(Track, pk=pk)
    return render(request, 'tracks/track_detail.html', {'track': track})
# Create your views here.
