from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('/')

    return render(request, 'accounts/signup.html')


