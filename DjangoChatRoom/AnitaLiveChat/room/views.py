from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Room, Message
import os
from django.conf import settings


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = reversed(room.messages.order_by('-date_added')[:50])

    if request.method == 'POST':
        content = request.POST.get('content')
        file = request.FILES.get('file')
        print("Content:", content)  # add this line to print the content of the message
        print("File:", file)  # add this line to print the file object
        if file:
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open('room/templates/room/static/upload'+ file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            file_url = os.path.join(settings.MEDIA_URL, file.name)
            Message.objects.create(room=room, user=request.user, content=file_url, file=file)
        else:
            Message.objects.create(room=room, user=request.user, content=content)

    return render(request, 'room/room.html', {'room': room, 'messages': messages})
