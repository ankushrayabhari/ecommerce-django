# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(null=True, to='authenticate.Customer')),
                ('product', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
