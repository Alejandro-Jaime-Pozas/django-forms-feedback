from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View # checkout docs, multiple View classes
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

# create view: don't need a form, it creates and submits form for you
class ReviewView3(CreateView):
    model = Review # specify the form for create view to create form
    form_class = ReviewForm # specify form so django handles errors/labels
    # fields = '__all__' # indicate the fields you want
    template_name = 'reviews/index.html' # this takes care of the GET logic, as well as POST logic
    success_url = '/thank-you' # need url to redirect to 


# form view
class ReviewView2(FormView):
    form_class = ReviewForm # specify the form
    template_name = 'reviews/index.html' # this takes care of the GET logic, as well as POST logic
    success_url = '/thank-you' # need url to redirect to 
    def form_valid(self, form):
        form.save() # need to save form prior
        return super().form_valid(form)
    

# review view as a class; django will handle incoming request based on function name ie 'get()'
class ReviewView(View):

    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/index.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST) # request as parameter and its POST value to access the form's input contents
        if form.is_valid(): # checks if user input is valid/not empty
            print(form) # cleaned_data returns a dict
            print(form.cleaned_data) # cleaned_data returns a dict
            form.save() # since form is connected to model, can save form inputs directly
            return HttpResponseRedirect('/thank-you')
        
        return render(request, 'reviews/index.html', {
            'form': form
        })



# review view as a fn
def review(request):
    # if method is post, do something with input and redirect to other page. for post requests, don't return a rendered html template, instead redirect
    if request.method == 'POST':
        # entered_username = request.POST['username']
        # print(entered_username)
        form = ReviewForm(request.POST) # request as parameter and its POST value to access the form's input contents
        # form = ReviewForm(request.POST, instance=Review.objects.get(id=1)) # alternative to update existing data like PUT
        if form.is_valid(): # checks if user input is valid/not empty
            print(form) # cleaned_data returns a dict
            print(form.cleaned_data) # cleaned_data returns a dict
            # # ID USING MODELFORM, DO NOT NEED CODE BELOW
            # form_data = form.cleaned_data
            # review = Review(username=form_data['username'], 
            #                 review_text=form_data['review_text'],
            #                 rating=form_data['rating']
            # )
            # review.save()
            form.save() # since form is connected to model, can save form inputs directly
            return HttpResponseRedirect('/thank-you')

    else:
        form = ReviewForm()

    return render(request, 'reviews/index.html', {
        'form': form
    })

    
# thank_you view as a template class
class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html' # django auto returns get() req for url
    # you should return the context that is exposed to template, so dict
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # this is a dict
        context['message'] = 'This works!'
        return context

# # thank_you view as a class
# class ThankYouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thank_you.html')

# thank_you view as a fn
def thank_you(request):
    return render(request, 'reviews/thank_you.html')


# returning a list in list view
class ReviewsListView2(ListView):
    template_name = 'reviews/review_list.html' # django auto returns get() req for url
    model = Review 
    context_object_name = 'reviews' # need to assign a list name here
    # # you can perform filters, sorts on the data by using fn get_queryset
    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset() 
    #     final = base_query.filter(rating__gt=4)
    #     return final
    

# returning a list in template view
class ReviewsListView(TemplateView):
    template_name = 'reviews/review_list.html' # django auto returns get() req for url
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context
    

class SingleReviewView2(DetailView):
    template_name = 'reviews/single_review.html'
    model = Review 
    # to access the returned data in html templates, use model name in lowercase


# returning a single obj view in template view
class SingleReviewView(TemplateView):
    template_name = 'reviews/single_review.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['review'] = Review.objects.get(id=kwargs['id']) # can get kwargs from path() which contains the 'id' in its url
        print(kwargs)
        return context 