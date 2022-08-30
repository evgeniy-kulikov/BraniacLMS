# from django.http import HttpResponse
# from django.shortcuts import render

# # Использование функции
# # def hello_world(request):
# #     return HttpResponse("Hello world")
#
# from django.views import View
#
# # Использование класса
# class HelloWorldView(View):
#     def get(self, *args):
#         return HttpResponse("Hello world")
#
# def check_kwargs(request, **kwargs):
#     return HttpResponse(f"kwargs:<br>{kwargs}")
import json
import os
from datetime import datetime
from django.views.generic import TemplateView

from config.settings import BASE_DIR

file_ = open(os.path.join(BASE_DIR, 'mainapp/news.json'))


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data (собственные переменные проекта)
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()

        context["params"] = ['django', 'python']
        with file_:
            news_data = json.load(file_)
            context["news_data"] = news_data
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
