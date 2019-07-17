from django.urls import reverse
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from .models import blog, BlogComment, Tag
from .postform import BlogCommentForm, TagForm

################# TO-DO LIST ################
# Configurate some of the messages


#CHECK!
def homepage(request):

    post = blog.objects.all()


    context = {
	    'post': post,
	    }

    return render(request, 'blogue/blog_list.html', context)

#CHECK!
def post_detail(request, slug):

	post = get_object_or_404(blog, slug=slug)
	comment = BlogComment.objects.filter(post=post)


	if request.method == 'POST':
		form = BlogCommentForm(request.POST)

		if form.is_valid():
			user_comment = form.save(commit=False)
			user_comment.post = post
			user_comment.user = request.user
			user_comment.save()

			return redirect('postdetail', slug = post.slug )
	else:
		form = BlogCommentForm()

	context = {
		'post': post,
		'comment': comment,
		'form':form,
	}
	return render(request, 'blogue/post_detail.html', context)

#CHECK!
class PostCreate(UserPassesTestMixin, SuccessMessageMixin, CreateView):
	model = blog
	fields = ['title', 'body']
	template_name = 'blogue/blog_post_create.html'
	success_message = "Post was created successfuly!"

	def test_func(self):
	    return self.request.user.is_superuser

#CHECK!
class PostEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = blog
	fields = ['title', 'body']
	template_name_suffix = '_post_edit'
	success_message = "Post was edited successfuly!"

	def test_func(self):
	    return self.request.user.is_superuser

# Delete post = Author or Superuser
def post_delete(request, slug):
    post = get_object_or_404(blog, slug=slug)

    if request.user.is_superuser:
        if request.method == 'POST': #ADICIONAR SUPERUSER PERMISSÕES
        	if 'Cancelar' in request.POST:
        		return redirect('postdetail', slug=post.slug)

        	else:
        		post.delete()
        		message = messages.success(request, 'post was deleted successfuly')
        		return redirect('homepage')

        context = {
        	'post': post,
        }

        return render(request, 'blogue/snippets/post_delete.html', context)

    else:
        return redirect('homepage')


# edit comments == Author
class CommentEdit(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
	model = BlogComment
	fields = ['comment']
	template_name = 'blogue/snippets/comment_edit.html'
	success_message = " O seu comentário foi editado! "

	def test_func(self):
	    obj = self.get_object()
	    return obj.user == self.request.user

# Delete comments == Author
def comment_delete(request, pk):
	comment = get_object_or_404(BlogComment, pk=pk)

	if request.method == 'GET' and request.user == comment.user:
		if 'Cancelar' in request.POST:
		    return redirect('postdetail', slug=comment.post.slug)

		else:
		    comment.delete()
		    message = messages.success(request, 'Comment was deleted successfuly')
		    return redirect('postdetail', slug=comment.post.slug)

	else:
	    return redirect('postdetail', slug=comment.post.slug)

	context = {
        'comment':comment
        }

	return render(request, 'blogue/snippets/comment_delete.html', context)

#######################  hashtags  #######################
#CHECK!

def tag_create(request):
    post = blog.objects.latest('timestamp')

    if request.method == 'POST' and request.user.is_superuser:
        form = TagForm(request.POST)

        if form.is_valid():
            hashtags = form.cleaned_data.get('tag_name')
            hashtags_list = hashtags.split()
            for htags in hashtags_list:
                Tag.objects.get_or_create(tag_name=htags)
                final_tag = Tag.objects.filter(tag_name = htags)[0].id
                post.tags.add(final_tag)

            post.save()

            return redirect('homepage')

    else:
        form = TagForm()


    context = {
        'form': form,
        }

    return render(request, 'blogue/tag_create.html', context)

#######################  blog search  #######################
#CHECK!

def blogsearch(request, tag_slug):
    tag = get_object_or_404(Tag, tag_slug=tag_slug)

    post = blog.objects.filter(tags = tag.id)

    context = {
        'post' : post
        }

    return render(request, 'blogue/blog_search.html', context)

