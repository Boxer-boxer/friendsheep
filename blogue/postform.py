from django import forms

from .models import blog, BlogComment, Tag


class PostForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = blog
		fields = ['title', 'body']


class BlogCommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = BlogComment
		fields = ['comment']

class TagForm(forms.ModelForm):
    post = blog.objects.all()

    tag_name = forms.CharField()
    tag_post = forms.ModelMultipleChoiceField(queryset = post, required = False)

    class Meta:
        model = Tag
        fields = ['tag_name', 'tag_post']

