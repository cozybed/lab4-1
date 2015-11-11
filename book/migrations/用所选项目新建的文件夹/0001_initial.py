# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorID', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=40)),
                ('publisher', models.CharField(max_length=30)),
                ('publishDate', models.DateField()),
                ('price', models.IntegerField()),
                ('author', models.ForeignKey(to='book.author')),
            ],
        ),
    ]
