#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  example_serializer.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

import logging
from rest_framework import serializers, generics, mixins, permissions, exceptions, viewsets, status, filters
from ..entities import *

logger = logging.getLogger(__name__)


{% if cookiecutter.models != "Comma-separated list of models" %}

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {{ model.strip() }}Entity
        # fields = []
    
{% endfor %}
{% endif %}


