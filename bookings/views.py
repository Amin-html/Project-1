from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from tracks.models import Track

@login_required
def booking_create(request, track_pk):
    track = get_object_or_404(Track, pk=track_pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            # проверяем пересечение времени
            conflict = Booking.objects.filter(
                track=track,
                date=date,
                start_time__lt=start_time, # начало раньше нашего конца
                end_time__gt=end_time,  # конец позже нашего начала
            ).exists()
            if conflict:
                form.add_error(None, 'Это время уже занято! Выберите другое.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.track = track
                hours = end_time.hour - start_time.hour
                booking.total_price = hours * track.price_per_hour
                booking.save()
                return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_create.html', {
        'form': form,
        'track': track,
    })

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def booking_cancel(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')
    return render(request, 'bookings/booking_cancel.html', {'booking': booking})
# Create your views here.