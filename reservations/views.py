from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Reservation, Comment
from .forms import EventForm, ReservationForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def event_list(request):
    query = request.GET.get('q')
    if query:
        events = Event.objects.filter(name__icontains=query)
    else:
        events = Event.objects.all()
    return render(request, 'reservations/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    reservations = Reservation.objects.filter(event=event)
    comments = event.comments.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('event_detail', pk=event.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'reservations/event_detail.html', {
        'event': event,
        'reservations': reservations,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'reservations/event_edit.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'reservations/event_edit.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')

@login_required
def reservation_new(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.event = event
            reservation.user = request.user  # Asegúrate de asignar el usuario autenticado aquí
            reservation.save()
            # Send Email
            send_mail(
                'Reservation Confirmation',
                f'Your reservation for {event.name} has been confirmed.',
                settings.DEFAULT_FROM_EMAIL,
                [reservation.user.email],  # Usar el email del usuario
                fail_silently=False,
            )
            messages.success(request, "Reservation created successfully.")
            return redirect('event_detail', pk=event.pk)
        else:
            messages.error(request, "There was an error with your reservation.")
    else:
        form = ReservationForm(initial={'event': event})
    return render(request, 'reservations/reservation_edit.html', {'form': form, 'event': event})

@login_required
def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            # Enviar correo electrónico
            send_mail(
                'Reservation Updated',
                f'Your reservation for {reservation.event.name} has been updated.',
                settings.DEFAULT_FROM_EMAIL,
                [reservation.user.email],  # Usar el email del usuario
                fail_silently=False,
            )
            messages.success(request, "Reservation updated successfully.")
            return redirect('event_detail', pk=reservation.event.pk)
        else:
            messages.error(request, "There was an error updating the reservation.")
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_edit.html', {'form': form, 'event': reservation.event})

@login_required
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    event_pk = reservation.event.pk
    reservation.delete()
    messages.success(request, "Reservation deleted successfully.")
    return redirect('event_detail', pk=event_pk)




