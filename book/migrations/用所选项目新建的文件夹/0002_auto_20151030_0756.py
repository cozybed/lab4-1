# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.RemoveField(
            model_name='books',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='authorID',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='ISBN',
            field=models.CharField(max_length=30, serialize=False, primary_key=True),
        ),
    ]
