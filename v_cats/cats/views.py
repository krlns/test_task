from rest_framework import generics, viewsets, authentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cats
from .permissions import IsOwnerOrReadOnly
from .serializers import CatsSerializer

from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'app/main.html')


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'app/main.html')
                else:
                    return HttpResponse("disabled account")
            else:
                return HttpResponse("invalid login")
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'app/main.html')
    else:
        user_form = RegistrationForm()

    return render(request, 'app/registration.html', {'user_form': user_form})


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cats.objects.all()
    serializer_class = CatsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Cats.objects.filter(user=user)
