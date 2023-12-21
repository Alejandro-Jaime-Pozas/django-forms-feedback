from django import forms
from.models import Review

# less efficient forms model
# class ReviewForm(forms.Form):
#     username = forms.CharField(
#         label='Your Name', 
#         max_length=100, 
#         error_messages={ # to allow specific error msgs to show user
#             'required': 'Your name must not be empty!',
#             'max_length': 'Please enter a shorter name!',
#         },
#         # required=False # use this if not req field, default is true
#         )
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea) # widget allows you to set the look of something like text field into a charfield
#     rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)


# this forms.ModelForm connects the form to a specified model so that both are linked, to reduce amount of code
class ReviewForm(forms.ModelForm):
    class Meta: # to specify related model
        model = Review
        # fields = ['username', 'review_text', 'rating'] # this to allow specified fields from model
        fields = '__all__' # this to create form fields for all model fields
        # exclude = ['owner_comment'] # combine this with '__all__' to only exculde a few fields
        # can also overwrite default labels that django provides for fields:
        labels = {
            'username': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating',
        }
        # can also include error_messages
        error_messages = {
            'username': {
                'required': 'Your name must not be empty!!!',
                'max_length': 'Please enter a shorter name!',
            }
        }