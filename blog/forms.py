import itertools
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .models import Comment,Blog

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model  = User
        fields = ('username', 'first_name', 'last_name', 'email','birth_date','password1', 'password2')

class CommentForm(forms.ModelForm):
    blog_id = forms.CharField(widget=forms.HiddenInput())
    name    = forms.CharField(label="Your Name", max_length=255)
    email   = forms.CharField(label="Email",max_length=255)
    comment = forms.CharField( widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
        model  = Comment
        fields = ('blog_id','name','email','comment')

class BlogForm(forms.ModelForm):
    title  = forms.CharField(label="Title", max_length=255)
    body   = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':100}))
    tags   = forms.CharField(label="Tags", max_length=255)
    status = forms.ChoiceField(label="Status",choices=[(1,"Enable"),(2,"Desable")])
    class Meta:
        model  = Blog
        fields = ('title','body','tags','status')

    def save(self,user_id,commit=True):
        instance = super(BlogForm, self).save(commit=False)
        #Creating Slug
        slug = slugify(instance.title)
        instance.author_id = user_id

        max_length = Blog._meta.get_field('url').max_length
        instance.url = orig = slugify(instance.title)[:max_length]

        for x in itertools.count(1):
            if not Blog.objects.filter(url=instance.url).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.url = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)
        instance.save()
        return instance;