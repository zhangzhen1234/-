# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choicetext', models.TextField()),
                ('vote', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u9009\u9879',
                'verbose_name_plural': '\u9009\u9879',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.TextField()),
                ('pubtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6295\u7968\u95ee\u9898',
                'verbose_name_plural': '\u6295\u7968\u95ee\u9898',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='que',
            field=models.ForeignKey(to='poll.Question'),
        ),
    ]
