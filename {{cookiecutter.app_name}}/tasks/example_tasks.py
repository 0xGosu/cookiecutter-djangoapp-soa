#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  example_tasks.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from ..conf.apps import MyAppConfig


@shared_task(name='%s.tasks.do_smthing_task' % MyAppConfig.name)
def do_smthing_task(*args, **kwargs):
    pass
