#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  signals.py
#
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

from django.conf.urls import url
from django.views.generic import TemplateView

from .views import example_views as views

urlpatterns = [
    {% if cookiecutter.models == "Comma-separated list of models" -%}
    url(r'', TemplateView.as_view(template_name="base.html")),
    {% else -%}
	{% for model in cookiecutter.models.split(',') -%}
    url(
        regex="^{{ model.strip() }}/~create/$",
        view=views.{{ model.strip() }}CreateView.as_view(),
        name='{{ model.strip() }}_create',
    ),
    url(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/~delete/$",
        view=views.{{ model.strip() }}DeleteView.as_view(),
        name='{{ model.strip() }}_delete',
    ),
    url(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/$",
        view=views.{{ model.strip() }}DetailView.as_view(),
        name='{{ model.strip() }}_detail',
    ),
    url(
        regex="^{{ model.strip() }}/(?P<pk>\d+)/~update/$",
        view=views.{{ model.strip() }}UpdateView.as_view(),
        name='{{ model.strip() }}_update',
    ),
    url(
        regex="^{{ model.strip() }}/$",
        view=views.{{ model.strip() }}ListView.as_view(),
        name='{{ model.strip() }}_list',
    ),
	{% endfor -%}
    {% endif -%}
]
