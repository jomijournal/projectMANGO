# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20150630_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='articleID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='volume',
            field=models.IntegerField(default=2014),
        ),
    ]
