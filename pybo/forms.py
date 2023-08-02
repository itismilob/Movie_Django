from django import forms
from pybo.models import Movie_info

class add_movie_Form(forms.ModelForm):
    class Meta:
        model = Movie_info
        fields = ['title', 'year', 'poster', 'tags', 'rating', 'link']
    def __init__(self, *args, **kwargs):
        super(add_movie_Form, self).__init__(*args, **kwargs)
        self.fields['poster'].required = False