# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import users,company,industry,evaluator,period,senior_index,junior_index
from .models import interval,ind_model,val_model
admin.site.register(users)
admin.site.register(company)
admin.site.register(industry)
admin.site.register(evaluator)
admin.site.register(senior_index)
admin.site.register(junior_index)
admin.site.register(period)
admin.site.register(ind_model)
admin.site.register(val_model)
admin.site.register(interval)
