#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  signals.py
#
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

{% if cookiecutter.models != "Comma-separated list of models" -%}

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import ({% for model in cookiecutter.models.split(',') %}
	{{ model.strip() }},{% endfor %}
)

{% set views = [
	'CreateView',
	'DeleteView',
	'DetailView',
	'UpdateView',
	'ListView'
] -%}

{% for model in cookiecutter.models.split(',') -%}
{% for view in views %}
class {{ model.strip() }}{{ view }}({{ view }}):

    model = {{ model.strip() }}

{% endfor -%}
{% endfor -%}
{% endif -%}
