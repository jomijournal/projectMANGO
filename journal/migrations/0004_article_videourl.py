# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20150630_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='videoURL',
            field=models.CharField(default=b'', max_length=128),
        ),
    ]
