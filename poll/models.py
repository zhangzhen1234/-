#coding:utf-8
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.TextField(blank=False)
    pubtime=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.question_text
    class Meta:
        verbose_name="投票问题"
        verbose_name_plural="投票问题"

class Choice(models.Model):
    que=models.ForeignKey(Question)
    choicetext=models.TextField(blank=False)
    vote=models.IntegerField(default=0)

    def __unicode__(self):
        return self.choicetext
    class Meta:
        verbose_name="选项"
        verbose_name_plural="选项"
