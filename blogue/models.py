from django.db import models
from django.db.models.signals import pre_save
#from django.utils.text import slugify
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth.models import User

from tinymce.models import HTMLField

from blogue.utils import unique_slug, comment_slug, name_to_hash


class Tag(models.Model):
    tag_name = models.CharField(max_length=550)
    tag_slug = models.SlugField(max_length=660, null=True, blank=True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('homepage')

    def __str__(self):
        return self.tag_name

@receiver(pre_save, sender=Tag)
def tag_slug(sender, instance, *args, **kwargs):
    if not instance.tag_slug:
        instance.tag_slug = name_to_hash(instance)


class blog(models.Model):
	title = models.CharField(max_length=300)
#	download tinymce files, install etc.
#	body = models.CharField(max_length=4000)
	body = HTMLField()
	slug = models.SlugField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)

	class Meta:
		ordering = ["-timestamp"]

	def get_absolute_url(self, *args, **kwargs):
		return reverse('createtags')

	def __str__(self):
		return self.title

@receiver(pre_save, sender=blog)
def slug_save(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug(instance)


class BlogComment(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=600)
	post = models.ForeignKey(blog, on_delete=models.CASCADE)
	comment = models.CharField(max_length=1500)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-timestamp"]

	def get_absolute_url(self, *args, **kwargs):
		return reverse('postdetail', kwargs={'slug':self.post.slug})

@receiver(pre_save, sender=BlogComment)
def comment_slug_save(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = comment_slug(instance)
