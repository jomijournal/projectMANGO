# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Title of the article', max_length=256)),
                ('authorsXML', models.TextField(help_text=b'Store author indexand the position of that author in XML')),
                ('abstract', models.TextField(help_text=b'The abstract, in HTML format')),
                ('mainText', models.TextField(help_text=b'The main text, in a uniform andeasily parsed HTML format')),
                ('procedure', models.TextField(help_text=b'The procedure, in a uniform andeasily parsed HTML format')),
                ('videoContents', models.TextField(help_text=b'Store the labels and timesfor each section in the video')),
                ('comments', models.TextField(help_text=b'Store the comments in XML')),
                ('publicationDate', models.DateTimeField(help_text=b'The time of publication')),
                ('revisions', models.TextField(help_text=b'Store the author, publication time,and filename for each change in XML')),
                ('publicationStatus', models.IntegerField(default=0, help_text=b'Status of publication', choices=[(0, b'published'), (1, b'preprint'), (2, b'in production'), (3, b'coming soon')])),
                ('subject', models.IntegerField(default=0, help_text=b'Subject of articles', choices=[(0, b'General Surgery'), (1, b'Fundamentals'), (2, b'Orthopedics'), (3, b'Orthopedic Trauma'), (4, b'Vascular Surgery'), (5, b'Ophthalmalogy'), (6, b'Neurosurgery')])),
                ('tags', models.CharField(max_length=256)),
                ('institution', models.ForeignKey(to='core.Institution')),
            ],
        ),
    ]
