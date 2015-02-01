# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures_tags', '0002_auto_20150129_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='subPath',
            field=models.CharField(max_length=4096, null=True),
            preserve_default=True,
        ),
    ]
