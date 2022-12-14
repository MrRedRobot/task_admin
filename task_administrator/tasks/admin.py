from django.contrib import admin
from tasks.models.task import Task
from tasks.models.comentary import Comentary

# Register your models here.
admin.site.register(Task)
admin.site.register(Comentary)