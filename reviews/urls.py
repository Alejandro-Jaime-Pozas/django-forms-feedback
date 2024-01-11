from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ReviewView.as_view()), # this for view class view
    # path('', views.ReviewView2.as_view()), # this for view class view
    path('', views.ReviewView3.as_view()), # this for view class view
    # path('', views.review), # this for fn view
    # path('thank-you', views.thank_you), # this for fn view
    path('thank-you', views.ThankYouView.as_view()), # this for class view
    # path('reviews', views.ReviewsListView.as_view()), # for template view
    path('reviews', views.ReviewsListView2.as_view()), # for list view
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    # path('reviews/<int:id>', views.SingleReviewView.as_view()), # for template view
    path('reviews/<int:pk>', views.SingleReviewView2.as_view()), # for detail view, need to change the 'id' to 'pk' for it to work
]