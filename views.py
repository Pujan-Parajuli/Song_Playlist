from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm

def song_list(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(title__icontains=query) | Song.objects.filter(artist__icontains=query)
    else:
        songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'songs/song_form.html', {'form': form})

def edit_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm(instance=song)
    return render(request, 'songs/song_form.html', {'form': form})

def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, 'songs/song_confirm_delete.html', {'song': song})
