# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_publish', 'can publish artcles, reserved for editorial staff'), ('can_annotate', 'can annotate any article'), ('can_view_production', 'can view articles in production'), ('can_annotate_own', 'can annotate own article (for authors)'), ('can_view_own', 'can view own article (for authors)'))},
        ),
        migrations.AddField(
            model_name='article',
            name='annotations',
            field=models.TextField(default=b'', help_text=b'Stores annotations for viewing by the author and editorial team in XML'),
        ),
        migrations.AlterField(
            model_name='article',
            name='revisions',
            field=models.TextField(help_text=b'Store the author, publication time,and filWename for each change in XML'),
        ),
    ]
