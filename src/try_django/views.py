from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.utils import timezone

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
	#qs = BlogPost.objects.all()[:5]
	now = timezone.now()
	qs = BlogPost.objects.filter(publish_date__lte=now)
	context = {"title": "Welcome To Try Django", "blog_list": qs}
	# template_name = "title.txt"
	# template_obj = get_template(template_name)
	# rendered_string = template_obj.render(context)
	# print(rendered_string)
	return render(request, "home.html", context)


def about_page(request):
	return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		"title": "Contact Us",
		"form": form
	}
	return render(request, "form.html", context)

def example_page(request):
	template_name = "hello_world.html"
	context = {"title": "example"}
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item)