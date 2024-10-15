from django import forms
from review.models import ReviewModel


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["reveiw_body"]
        labels = {
            "Review": "reveiw_body",
        }
        widgets = {
            "reveiw_body": forms.Textarea(
                attrs={
                    "class": "w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Write your review here...",
                    "rows": 4,
                }
            ),
        }
