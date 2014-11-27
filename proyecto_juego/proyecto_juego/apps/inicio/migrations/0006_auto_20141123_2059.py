# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_auto_20141122_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='respuesta_opcional_1',
            field=models.CharField(default='prueva', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respuesta_opcional_2',
            field=models.CharField(default='prueva', max_length=500),
            preserve_default=False,
        ),
    ]
