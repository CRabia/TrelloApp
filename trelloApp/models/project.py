import datetime

from django.contrib.auth import get_user_model
from trelloApp.choices import TASK_STATUS
from django.db import models

User = get_user_model()


class Color(models.Model):
    code = models.CharField(max_length=7)


class TaskTag(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey(Color, related_name='taskTags', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    creator = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    startDate = models.DateField(default=datetime.date.today(), null=True)
    endDate = models.DateField(null=True)

    def __str__(self):
        return self.name


class TaskList(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='takLists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ForeignKey(TaskTag, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    startDate = models.DateTimeField(default=datetime.datetime.now())
    endDate = models.DateTimeField()
    status = models.CharField(choices=TASK_STATUS, max_length=11)
    madeBy = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    taskList = models.ForeignKey(TaskList, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
