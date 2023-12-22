from django.urls import path

from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()), # this for class view
    # path('', views.review), # this for fn view
    # path('thank-you', views.thank_you), # this for fn view
    path('thank-you', views.ThankYouView.as_view()), # this for class view
    path('reviews', views.ReviewsListView.as_view()),
    path('reviews/<int:id>', views.SingleReviewView.as_view()),
]