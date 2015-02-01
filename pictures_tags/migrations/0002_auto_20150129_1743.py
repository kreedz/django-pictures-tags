# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures_tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='path',
            field=models.CharField(unique=True, max_length=4096),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
    ]
