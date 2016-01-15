from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from .models import *
from .forms.forms import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import re
from django.views.decorators.csrf import csrf_exempt
from random import shuffle
import json


def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        print("test1")
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            print('form is valid')
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # print(username)
            # salt = hashlib.sha1(random.random().encode('utf-16')).hexdigest()[:5]
            # print(salt)
            # activation_key = hashlib.sha1(salt+email).hexdigest()
            # print(activation_key)
            # key_expires = datetime.datetime.today() + datetime.timedelta(2)
            # print(key_expires)

            #Get user by username
            user = User.objects.get(username=username)

            # user = user_form.save()
            user.set_password(user.password)
            user.save()

            new_user = MyUser(user=user)
            new_user.save()
            print(user)

            # Create and save user profile
            # new_profile = MyUser(user=user, activation_key=activation_key,
            #     key_expires=key_expires)
            # new_profile.save()

            # Send email with activation key
            # email_subject = 'Account confirmation'
            # email_body = "Hey %s, thanks for signing up! To activate your account, click this link within \
            # 48 hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)

            # send_mail(email_subject, email_body, 'secretparcelexchange@gmail.com',
            #     [email], fail_silently=False)

            return HttpResponseRedirect('/login')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('register.html', args, context_instance=RequestContext(request))

@csrf_exempt
def login_user(request):
    username = password = ""

    # if request.user.is_authenticated():
        # return redirect('/home/')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect('/home/')
    return render(request, 'login.html', context_instance=RequestContext(request))


@login_required(login_url='/login')
def user_logout(request):
    """Logs out user"""
    logout(request)

    return redirect('/login/')


def home(request):
    return render(request, 'home.html')


def new_exchange(request, game_name):
    """ Create exchange"""
    user = request.user

    # person = Participate(giveruser=user)
    # person.save()
    
    gift_exchange = Group(group_name=game_name)
    gift_exchange.save()

    # gift_exchange.elf.add(person)
    # gift_exchange.save()

    addelf(gift_exchange, user)

    # print(gift_exchange.id)

    # print(gift_exchange.group_name)
    # print(gift_exchange.id)

    # print(gift_exchange.group_name)


    return gift_exchange.id


def exchange(request):
    """ gets data and get's input name, sends it to helper
    function that will create exchange and redirects to exchange page """

    if request.method == 'POST':
        game_name = request.POST.get("gameName")

        # print(game_name)

        exchange_id = new_exchange(request, game_name)

        return HttpResponseRedirect(reverse('exchange_urls:exchange', kwargs={'exchange_id': exchange_id}))
        # return redirect('/invite/')
    else:
        return redirect('/invite/')


def sendprofile(request):

    user_nameid = request.user.id

    return HttpResponseRedirect(reverse('profile_urls:profile', kwargs={'user_nameid': user_nameid}))


def profile(request, user_nameid):
    """ gets data and get's input name, sends it to helper
    function that will create exchange and redirects to exchange page """

    user = request.user

    user_id = request.user.id

    otheruser = User.objects.get(id=user_nameid)

    username = otheruser.username

    participate = Participate.objects.filter(giveruser=user)

    groups = Group.objects.filter(elf=participate)

    test = zip(participate, groups)


    iuser = MyUser.objects.get(user=otheruser)

    # my_user = iuser.user_set.get(id= user_nameid)

    # for i in my_user:


    # my_user = User.myuser_set.get(id= user_nameid)

    # user_likes = my_user.likes
    #
    # user_dislikes = my_user.dislikes

    return render(request, 'profile.html', {'user': user,
                                            'test':test,
                                            'user_id':str(user_id),
                                            'user_nameid':user_nameid,
                                            'username':username,
                                            'iuser':iuser})

def exchangeprofile(request, exchange_id):
    exchanges = Group.objects.get(id=exchange_id)

    elf = exchanges.elf.filter()


    return render(request, 'exchange.html', {'id': exchange_id, 'exchanges':exchanges, 'elf':elf})

def joinexchange(request):

    if request.method == 'POST':
        exchange_pass = request.POST.get("gamePass")

        exchange_num = int(re.search(r'\d+', exchange_pass).group())

        jointheexchange(request, exchange_num)

        return HttpResponseRedirect(reverse('exchange_urls:exchange', kwargs={'exchange_id': exchange_num}))

    else:
        return redirect('/invite/')


def jointheexchange(request, exchange_num):
    user = request.user

    gift_exchange = Group.objects.get(id=exchange_num)

    addelf(gift_exchange, user)

    # exchange.par

def addelf(gift_exchange, user):

    person = Participate(giveruser=user)
    person.save()

    gift_exchange.elf.add(person)
    gift_exchange.save()

@csrf_exempt
def addsanta(request, exchange_id):
    if request.method == 'POST':
        # print('0')
        people_id = request.POST.getlist('peopleId[]')
        # group_id = request.POST.getlist('groupNum')
        # print(people_id)
        # group = Group.objects.get(id=group_id)

        # people_id.shuffle()

        # num = 0

        while len(people_id) >= 0:
            # print('1')
            check_full(people_id)
            first_num = people_id[0]
            print("Printing list of ids")
            print(people_id)

            print("printing length of list of ids")
            print(len(people_id))

            print("printing first num of list of ids")
            print(first_num)

            print("printing last num of list of ids")
            print(people_id[-1])
            elf = Participate.objects.get(id=first_num)
            last_elf = Participate.objects.get(id=people_id[-1])
            # print('2')

            if elf.getting is None:
                # print('3')
                if last_elf.giving is None:
                    # print(elf.giveruser)
                    # print(last_elf)
                    # print('4')
                    elf.getting = last_elf
                    last_elf.giving = elf
                    elf.save()
                    last_elf.save()
                    check_full(people_id)
                else:
                    # print('5')
                    second_to_last = Participate.objects.get(id=people_id[-2])
                    elf.getting = second_to_last
                    second_to_last.giving = elf

                    elf.save()
                    second_to_last.save()

                    check_full(people_id)
                    # if second_to_last.getting is not None and second_to_last.giving is not None:
                        # people_id.pop()
            if elf.giving is None:
                # print('6')
                if len(people_id) >= 3:
                    # print('7')
                    second_to_last = Participate.objects.get(id=people_id[-2])
                    elf.giving = second_to_last
                    elf.save()

                    second_to_last.getting = elf
                    second_to_last.save()

                    check_full(people_id)
                else:
                    # print('8')
                    elf.giving = last_elf
                    elf.save()

                    last_elf.getting = elf
                    last_elf.save()
                    check_full(people_id)
            else:
                # print('9')
                check_full(people_id)
                # people_id.pop(0)
                # elf.giving.add()
    else:
        return redirect('/home/')

            # while num < 1:


def check_full(people_id):
    # print('10')
    num = 0
    for i in people_id:
        elf = Participate.objects.get(id=i)
        if elf.getting is not None and elf.giving is not None:
            print('full')
            people_id.pop(num)
        num += 1


@csrf_exempt
def updateadress(request, user_nameid):
    if request.method == 'POST':
        update = request.POST.get("text")

        # print("hello")

        print(update)

        print(user_nameid)

        user = User.objects.get(id=user_nameid)

        myuser = MyUser.objects.get(user=user)

        myuser.address = update
        myuser.save()

        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )


@csrf_exempt
def updateprofile(request, user_nameid):
    if request.method == 'POST':
        update = request.POST.get("text")

        # print("hello")

        print(update)

        print(user_nameid)

        user = User.objects.get(id=user_nameid)

        myuser = MyUser.objects.get(user=user)

        myuser.likes = update
        myuser.save()

        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )


@csrf_exempt
def updatedislike(request, user_nameid):
    if request.method == 'POST':
        update = request.POST.get("text")

        user = User.objects.get(id=user_nameid)

        myuser = MyUser.objects.get(user=user)

        myuser.dislikes = update
        myuser.save()

        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"})
        )

# Create Participate from request.user

# def register_confirm(request, activation_key):
#     #check if user is already logged in and if he is redirect him to some other url, e.g. home
#     if request.user.is_authenticated():
#         HttpResponseRedirect('/home')
#
#     # check if there is UserProfile which matches the activation key (if not then display 404)
#     user_profile = get_object_or_404(MyUser, activation_key=activation_key)
#
#     #check if the activation key has expired, if it hase then render confirm_expired.html
#     if user_profile.key_expires < timezone.now():
#         return render_to_response('user_profile/confirm_expired.html')
#     #if the key hasn't expired save user and set him as active and render some template to confirm activation
#     user = user_profile.user
#     user.is_active = True
#     user.save()
#     return render_to_response('user_profile/confirm.html')


# def register_success(request):
#     print("Boop")