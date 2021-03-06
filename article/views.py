# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from article.models import Article, Category
from datetime import datetime, timedelta
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from .forms import ContactForm

def home(request):
	posts = Article.objects.all()   #获取全部Article对象
	paginator = Paginator(posts, 4)     #每页显示五篇文章
	page = request.GET.get('page')
	try:
		post_list = paginator.page(page)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.paginator(paginator.num_pages)
	context = {
		'category_list': Category.objects.all(),
		'post_list': post_list
	}
	return render(request, 'home.html', context)

def detail(request, id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	context = {
		'category_list': Category.objects.all(),
		'post': post
	}
	return render(request, 'post.html', context)

def archives(request):
	try:
		post_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	context = {
		'category_list': Category.objects.all(),
		'post_list': post_list,
		'error': False
	}
	return render(request, 'archives.html',  context)


def about_me(request):
	context = {
		'category_list': Category.objects.all()
	}

	return render(request, 'aboutme.html', context)

def search_tag(request, tag):
	try:
		post_list = Article.objects.filter(category__name__iexact = tag) #contains
	except Article.DoesNotExist:
		raise Http404
	context = {
		'category_list': Category.objects.all(),
		'post_list': post_list
	}
	return render(request, 'home.html', context)

def blog_search(request):
	if 's' in request.GET:
		s = request.GET['s']
		if not s:
			return render(request, 'home.html')
		else:
			post_list = Article.objects.filter(title__icontains = s)
			if len(post_list) == 0:
				return render(request, 'archives.html', {'post_list': post_list, 'error': True})
			else:
				return render(request, 'archives.html', {'post_list': post_list, 'error': False})
	return redirect('/')
	

class RSSFeed(Feed):
	title = "RSS feed - article"
	link = "feeds/posts/"
	description = "RSS feed - blog posts"

	def items(self):
		return Article.objects.order_by('-date_time')

	def item_title(self, item):
		return item.title

	def item_pubdate(self, item):
		return item.date_time

	def item_description(self, item):
		return item.content


def contact_me(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			#process the data in form.cleaned_data as required
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			cc_myself = form.cleaned_data['cc_myself']

			recipients = ['tangwang1993@qq.com']
			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
			# redirect to a new URL:
			return HttpResponseRedirect('/time/plus/0/')

	# if a GET(or any other method) we'll create a blank form
	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form': form})


