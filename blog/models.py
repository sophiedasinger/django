from django.db import models
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return('view_blog_category', None, {'slug': self.slug})

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	pub_date = models.DateField(db_index=True, auto_now_add=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField(blank=True)
	category = models.ManyToManyField(Category)
	likes = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, blank=True)

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.id:
            # Newly created object, so set slug
			self.slug = slugify(self.title)

		super(Post, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-pub_date']


