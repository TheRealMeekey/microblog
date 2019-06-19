from django import forms
from app_microblog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'materialize-textarea'})
