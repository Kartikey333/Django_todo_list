# todo_list/todo_app/admin.py

from django.contrib import admin
from todo_app.models import ToDoItem,ToDoList

admin.site.register(ToDoList)
admin.site.register(ToDoItem)

