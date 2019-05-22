from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=200)
    open = models.BooleanField(default=False)


class Question(models.Model):
    title = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)


class Choice(models.Model):
    title = models.CharField(max_length=200)
    value = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
