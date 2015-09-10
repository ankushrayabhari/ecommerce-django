# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=3000)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
        ),
    ]
