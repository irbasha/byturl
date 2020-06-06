from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import TeenyURLs

import urllib
import hashlib
import os


def home(request):
	return render(request, "home.html")


def createurl(request):
	print(
		request.META['HTTP_HOST'],
		request.scheme
	)
	url = request.GET['url']
	hash_object = hashlib.md5(url.encode())
	shortened_url_hash = hash_object.hexdigest()[:8]

	try:
		if TeenyURLs.objects.get(teeny_url=shortened_url_hash):
			None
	except TeenyURLs.DoesNotExist:
		entry = TeenyURLs(teeny_url=shortened_url_hash, origin_url=url)
		entry.save()

	shortened_url = conver_url_from_code(request, shortened_url_hash)
	return render(request, 'home.html', {'shortened_url': shortened_url})


def retrieve(request, input_url):
	target = get_object_or_404(TeenyURLs, teeny_url=input_url)
	target_url = target.origin_url
	return redirect(target_url)


def conver_url_from_code(request, code):
    return request.scheme + '://' + request.META['HTTP_HOST'] +'/%s' % (code)
