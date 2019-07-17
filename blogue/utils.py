from django.utils.text import slugify

from datetime import datetime
from random import randint
from string import ascii_letters

def unique_slug(instance, new_slug=None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title, instance.id)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()

	if qs_exists:
		random_int = str(randint(0,100))
		new_slug = f"{slug}-{random_int}"

		return unique_slug(instance, new_slug=new_slug)
	return slug

def comment_slug(instance, new_slug=None):
	rchar = "".join([x for x in range(20) for x in ascii_letters[randint(0,20)]])

	date = str(datetime.now())[:10].split('-')
	hour = str(datetime.now())[11:16].split(':')
	datehour = ''.join(date)+''.join(hour)+''.join(rchar)

	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.post, datehour)
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(slug=slug).exists()

	if qs_exists:
		random_int = str(randint(0,100))
		new_slug = f"{slug}-{random_int}"

		return unique_slug(instance, new_slug=new_slug)
	return slug

def name_to_hash(instance, name=None):
    tags = instance.tag_name

    if tags is not None:
        tag_slug = slugify(instance.tag_name)

    Klass = instance.__class__

    while Klass.objects.filter(tag_slug = tag_slug).exists():
        tag_pk = Klass._default_manager.filter(tag_slug = tag_slug).latest('pk').id
        tag_pk = tag_pk + 1

        tag_slug = f"{tag_slug}{tag_pk}"

    return tag_slug
