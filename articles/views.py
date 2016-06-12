from django.shortcuts import render
from .models import Articles
from .models import Coment
from .forms import ComentForm
from django.core.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.


def base (request):
	return render(request, 'base.html',{})

def post_list(request):
	all_articles = Articles.objects.all()
	return render(request, 'post_list.html', {'all_articles':all_articles})

def post_single(request, article_id):
	post_single= Articles.objects.get(id=article_id)
	return render(request, 'post_single.html',{'post_single':post_single })

def add_coment (request, article_id):
	art = Articles.objects.get(id=article_id)

	if request.method == "POST":
		cf = ComentForm(request.POST)
		if cf.is_valid():
			coment = cf.save(commit=False)
			coment.add_date = timezone.now()
			coment.article = art
			coment.save()

			return HttpResponseRedirect('/article/%s' % article_id)

	else:
		cf = ComentForm()

	args = {}
	args.update(csrf(request))
	args['article'] = art
	args['form'] = cf
	return render(request, 'add_coment.html',{})

