from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
from .models import User
from Message.models import Message
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.templatetags.static import static


# Create your views here.


class LoginClass(View):
    def get(self, request):
        logout(request)
        request.session['user_login'] = None
        request.session.modified = True
        return render(request, "login.html", {'login': LoginForm(), })

    def post(self, request):
        uname = request.POST.get('username')
        pw = request.POST.get('password')
        u_login = authenticate(username=uname, password=pw)


        if u_login is None:
            return render(request, "login.html", {'login': LoginForm(), 'message': 'Wrong infomation!!!'})

        login(request, u_login)
        u = User.objects.all()
        us = User.objects.filter(username=uname)[0]
        u = list(u)
        u.remove(us)

        request.session['user_login'] = us.id
        return redirect('/')


class ChatHomeClass(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        u = User.objects.all()
        us = User.objects.filter(pk=request.session['user_login'])[0]
        u = list(u)
        u.remove(us)

        for user in u:
            user.images = user.images.name


            m1 = Message.objects.filter(sender=user, receiver=us)
            m2 = Message.objects.filter(sender=us, receiver=user)
            messages = list(m1) + list(m2)
            messages = sorted(messages, key=lambda x: x.id, reverse=True)

            if len(messages) > 0:
                if messages[0].sender != us:
                    if len(messages[0].message) > 35:
                        user.message = messages[0].message[0:30] + "..."
                    else:
                        user.message = messages[0].message
                else:
                    if len(messages[0].message) > 30:
                        user.message = "You: " + messages[0].message[0:25] + "..."
                    else:
                        user.message = "You: " + messages[0].message
            else:
                user.message = "No message!"

            print(user.images)

        name = us.first_name + " " + us.last_name
        if len(name) > 13: name = name[0:12] + "..."

        return render(request, "userList.html", {'user': us, 'users': u,
                                                 'imguser':  us.images.name, 'name': name})


class RegisterClass(View):
    def get(self, request):
        return render(request, "register.html", {'l': UserForm(), })

    def post(self, request):

        create = User(phone=request.POST.get('phone'), first_name=request.POST.get('first_name'),
                      last_name=request.POST.get('last_name'), username=request.POST.get('username'),
                      email=request.POST.get('email'), password = make_password(request.POST.get('password')))

        create.save()
        return redirect('/login')
        # return render(request, "login.html", {'login': LoginForm(), })


class ChatClass(LoginRequiredMixin, View):
    login_url = "/login"
    def get(self, request, userID):
        us = User.objects.filter(pk=userID)[0]
        m1 = Message.objects.filter(sender=us, receiver=request.session['user_login'])
        m2 = Message.objects.filter(sender=request.session['user_login'], receiver=us)
        messages = list(m1) + list(m2)

        if len(messages) == 0:
            return render(request, "chat.html",
                          {'messages': messages, 'user': request.session['user_login'],
                           'user1': us, 'empty': True, 'imguser':us.images.name})
        return render(request, "chat.html",
                      {'messages': messages, 'user': request.session['user_login'],
                       'empty': False, 'user1': us, 'imguser': us.images.name})

    def post(self, request, userID):
        us = User.objects.filter(id=userID)[0]
        senderr = User.objects.filter(id=request.session['user_login'])[0]

        chat = Message(message=request.POST.get('message'), receiver=us, sender=senderr)
        chat.save()

        m1 = Message.objects.filter(sender=us, receiver=request.session['user_login'])
        m2 = Message.objects.filter(sender=request.session['user_login'], receiver=us)
        messages = list(m1) + list(m2)


        x = 'chat/' + str(userID)
        print(x)

        return redirect('/chat/' + str(userID))

        # return render(request, "chat.html",
        #               {'messages': messages, 'user': request.session['user_login'], 'empty': False, 'user1': us})


class SearchUser(LoginRequiredMixin, View):
    login_url = "/login"
    def get(self, request):
        relative =  request.GET.get('relative')
        u1 = User.objects.filter(first_name__contains= relative)
        u2 = User.objects.filter(last_name__contains=relative)
        us = User.objects.filter(pk=request.session['user_login'])[0]
        u = list(u1) + list(u2)
        if us in u: u.remove(us)

        for user in u:
            user.images = static('images/' + user.images.name)

            m1 = Message.objects.filter(sender=user, receiver=us)
            m2 = Message.objects.filter(sender=us, receiver=user)
            messages = list(m1) + list(m2)
            messages = sorted(messages, key=lambda x: x.id, reverse=True)

            if len(messages) > 0:
                if messages[0].sender != us:
                    if len(messages[0].message) > 35:
                        user.message = messages[0].message[0:30] + "..."
                    else:
                        user.message = messages[0].message
                else:
                    if len(messages[0].message) > 30:
                        user.message = "You: " + messages[0].message[0:25] + "..."
                    else:
                        user.message = "You: " + messages[0].message
            else:
                user.message = "No message!"
                
        name = us.first_name + " " + us.last_name
        if len(name) > 13: name = name[0:12] + "..."

        return render(request, "userList.html", {'user': us, 'users': u,
                                                 'imguser': us.images.name, 'name': name})


class InforUser(LoginRequiredMixin, View):
    login_url = "/login"
    def get(self, request):
        us = User.objects.filter(pk=request.session['user_login'])[0]
        return render(request, "update.html", {'u': us, })
    def post(self, request):

        u = User.objects.filter(pk=request.session['user_login'])[0]
        u.first_name = request.POST.get('first_name')
        u.last_name = request.POST.get('last_name')
        u.email = request.POST.get('email')
        if u.username != request.POST.get('username'): u.username = request.POST.get('username')
        if u.password != request.POST.get('password'): u.password = make_password(request.POST.get('password'))
        u.phone = request.POST.get('phone')
        u.images = request.POST.get('image')
        u.save()



        return redirect('/')


