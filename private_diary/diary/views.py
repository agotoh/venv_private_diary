from django.shortcuts import render
from django.views import generic
from django.template import loader
from django.http import HttpResponse


# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     template = loader.get_template('index.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
#     form_class = InquiryForm
