from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(
        label='Your Name', 
        max_length=100, 
        error_messages={ # to allow specific error msgs to show user
            'required': 'Your name must not be empty!',
            'max_length': 'Please enter a shorter name!',
        },
        # required=False # use this if not req field, default is true
        )
    review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea) # widget allows you to set the look of something like text field into a charfield
    rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)
