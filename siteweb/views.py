from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Message, User

# relative import of forms
from .forms import MessageForm, RegisterForm, ResponseForm


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
    responseForm = ResponseForm()

    return render(request, 'siteweb/show.html', {"message": message, "responseForm": responseForm})


@login_required(login_url='login')
def newMessage(request):
    context = {}

    form = MessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.author = request.user
        message.save()
        return redirect("messageAll", )

    context['form'] = form

    return render(request, "siteweb/newMessage.html", context)


@login_required(login_url='login')
def deleteMessage(request, id):
    message = Message.objects.get(id=id)
    if message.author != request.user:
        return redirect('messageAll')
    if message:
        message.delete()

        return redirect("messageAll", )

    return render(request, "siteweb/deleteMessage.html")


@login_required(login_url='login')
def updateMessage(request, id):
    context = {}

    obj = get_object_or_404(Message, id=id)
    if obj.author != request.user:
        return redirect('all_messages')
    form = MessageForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("messageAll")

    context["form"] = form

    return render(request, "siteweb/updateMessage.html", context)


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            return redirect('messageAll')

    return render(request, 'siteweb/register.html', {"form": form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            return redirect('home')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'siteweb/login.html')


def logout_user(request):
    logout(request)
    return redirect('messageAll')


@login_required(login_url='login')
def add_response(request, id):
    message = Message.objects.get(id=id)
    if message is None:
        return redirect('all_messages')
    if request.method == 'POST':
        form = ResponseForm(data=request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.message = message
            response.author = request.user
            response.save()

    return redirect('show_message', message.id)
