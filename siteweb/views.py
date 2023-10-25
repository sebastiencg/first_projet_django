from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message

# relative import of forms
from .forms import MessageForm


# Create your views here.


def index(request):
    context = {
        "message": "coucou"
    }

    return render(request, 'siteweb/home.html', context)


def bidule(request):
    return render(request, 'siteweb/bidule.html', {
        "bidule": "un nouveau message"
    })


def findAll(request):
    data = Message.objects.all()

    return render(request, 'siteweb/findAllMessage.html', {
        "messages": data
    })


def show_message(request, id):
    message = Message.objects.get(id=id)

    return render(request, 'siteweb/show.html', {"message": message})


def newMessage(request):
    context = {}

    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("messageAll",)

    context['form'] = form

    return render(request, "siteweb/newMessage.html", context)


def deleteMessage(request, id):

    message = Message.objects.get(id=id)

    if message:
        message.delete()

        return redirect("messageAll",)

    return render(request, "siteweb/deleteMessage.html")


def updateMessage(request, id):

    context = {}

    obj = get_object_or_404(Message, id=id)

    form = MessageForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("messageAll")

    context["form"] = form

    return render(request, "siteweb/updateMessage.html", context)
