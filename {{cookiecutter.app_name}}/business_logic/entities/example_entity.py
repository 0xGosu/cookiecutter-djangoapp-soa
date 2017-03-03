#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  budget_entity.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#
from django.utils.translation import ugettext as __, ugettext_lazy as _
import logging

logger = logging.getLogger(__name__)

{% if cookiecutter.models != "Comma-separated list of models" %}
from ...models import {{ cookiecutter.models }}

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}Entity({{ model.strip() }}):
    class Meta:
        proxy = True

    @classmethod
    def get_by_pk(cls, pk):
        return cls.objects.filter(pk=pk).first()

    def save(self, *args, **kwargs):
        
        return super({{ model.strip() }}Entity, self).save(*args, **kwargs)
    
{% endfor %}
{% endif %}

