# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='creditcard',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='expiration',
        ),
    ]
