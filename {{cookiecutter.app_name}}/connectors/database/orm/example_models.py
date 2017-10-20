#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  example_models.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.company_name }}. All rights reserved.
#

{% if cookiecutter.models != "Comma-separated list of models" %}
from django.db import models

from model_utils.models import TimeStampedModel

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(TimeStampedModel):
    pass
    
{% endfor %}
{% endif %}
