from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category
# Create your views here.

def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(),
		'posts': Post.objects.all()[:5]
		})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Post, slug=slug)
		})

def view_category(request,slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category
		'posts' : Post.objects.filter(category=category)[:5]
		})

def like(request):
	if request.method == 'POST':
		slug = request.POST.get('slug', None)

		post = get_object_or_404(Post, slug=slug)

		post.likes += 1;

		