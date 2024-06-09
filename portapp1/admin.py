# portfolio/admin.py
from django.contrib import admin
from .models import Project, Skill, BlogPost

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(BlogPost)
