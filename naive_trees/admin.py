from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from naive_trees.models import Food, MpttFood

admin.site.register(Food)
admin.site.register(MpttFood, MPTTModelAdmin)