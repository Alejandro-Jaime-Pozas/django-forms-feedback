from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review

# Create your views here.

def review(request):
    # if method is post, do something with input and redirect to other page. for post requests, don't return a rendered html template, instead redirect
    if request.method == 'POST':
        # entered_username = request.POST['username']
        # print(entered_username)
        form = ReviewForm(request.POST) # request as parameter and its POST value to access the form's input contents
        if form.is_valid(): # checks if user input is valid/not empty
            print(form.cleaned_data) # cleaned_data returns a dict
            form_data = form.cleaned_data
            review = Review(username=form_data['username'], 
                            review_text=form_data['review_text'],
                            rating=form_data['rating']
            )
            return HttpResponseRedirect('/thank-you')

    else:
        form = ReviewForm()

    return render(request, 'reviews/index.html', {
        'form': form
    })

def thank_you(request):
    return render(request, 'reviews/thank_you.html')