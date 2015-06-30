# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accountType', models.IntegerField(default=0, help_text=b"The account type which affects what a user can do.                             This is mostly for JoMI's internal records because the                             User type already includes a group that we can define.", choices=[(0, b'Other'), (1, b'Doctor'), (2, b'Resident'), (3, b'Medical Student'), (4, b'Librarian'), (5, b'Attending'), (6, b'Premed'), (7, b'Veterinarian')])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('displayName', models.CharField(help_text=b"The user's nickname.", max_length=32)),
                ('image', models.URLField(help_text=b'A link to an image of the author.')),
                ('specialty', models.CharField(help_text=b"The author's specialty.", max_length=64)),
                ('position', models.CharField(help_text=b"The author's position.", max_length=64)),
                ('account', models.ForeignKey(to='core.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name of the institution(e.g. Massachusetts General Hospital).', max_length=64)),
                ('location', models.CharField(help_text=b'Where the institution is located', max_length=256)),
                ('IPrange', models.TextField(help_text=b'Range of the IP addresses associated with the institution.')),
                ('pointsOfContact', models.TextField(help_text=b'Librarians or other users who should have special access. This will likely include access to Counter reports.')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='institution',
            field=models.ForeignKey(help_text=b'Institution associated with the user.', to='core.Institution'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
