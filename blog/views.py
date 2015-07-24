from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from .forms import LoginForm, PostForm
import sys
import datetime

def index(request):
	if request.user.is_authenticated():
		form = PostForm
		context = RequestContext(request)
		if request.method == 'POST':
			form = PostForm(request.POST)
			if form.is_valid():
				new_post = form.save(commit=False)
				new_post.user = request.user 
				new_post.save()
				return HttpResponseRedirect('')
		return render_to_response('index.html', {
			'categories': Category.objects.all(),
			'posts': Post.objects.all(),
			'username': request.user.username,
			'form': form,
			}, context)
	return HttpResponseRedirect('/login')

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post': get_object_or_404(Post, slug=slug)
		})

def view_category(request,slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Post.objects.filter(category=category)[:5]
		})

def like(request):
	post_id = None
	if request.method == 'GET':
		post_id= request.GET['post_id']


	likes = 0
	if post_id:
		post = Post.objects.get(pk=int(post_id))
		if post:
			likes = post.likes + 1
			post.likes =likes
			post.save()

	return HttpResponse(likes)

def login_user(request):
	state = ""
	form = LoginForm(request.POST)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				state = "Success!"
				return HttpResponseRedirect('/')
			else:
				state = "Inactive account!"
		else:
			state="Your username and password were incorrect."

	return render_to_response(
		'login.html',
		{'state':state,
		 'form':form,
		 },
		 context_instance=RequestContext(request)
	)

def logout_user(request):

	logout(request)

	return HttpResponseRedirect('/login')

def create_post(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = PostForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors
	else:
		form = PostForm()

	return render_to_response('create_post.html', {'form': form}, context)
