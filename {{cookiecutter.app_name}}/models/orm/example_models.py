#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  __init__.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

{% if cookiecutter.models != "Comma-separated list of models" %}
from django.db import models

from model_utils.models import TimeStampedModel

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(TimeStampedModel):
    pass
    
{% endfor %}
{% endif %}
