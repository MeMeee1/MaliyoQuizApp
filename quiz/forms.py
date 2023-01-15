from django import forms
from quiz.models import UserResponse


class UserResponseCreateForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ["question", "selected_options", "user_value", "user_ip"]


# class Question
