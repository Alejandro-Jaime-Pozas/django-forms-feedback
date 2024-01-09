from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            'form': form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES['user_image']) # this removes the need to write a file to disk
            profile.save()
            return HttpResponseRedirect('/profiles')
        
        return render(request, "profiles/create_profile.html", {
            'form': submitted_form
        })
    

# # basic static approach to store a file into hard disk (not ideal since limited file types)
# def store_file(file):
#     with open('temp/me.jpg', 'wb+') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
    
# # basic approach to uploading file
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             'form': form
#         })

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             store_file(request.FILES['image']) # gives access to the request's files, with html element name set to 'image'
#             return HttpResponseRedirect('/profiles')
        
#         return render(request, "profiles/create_profile.html", {
#             'form': submitted_form
#         })