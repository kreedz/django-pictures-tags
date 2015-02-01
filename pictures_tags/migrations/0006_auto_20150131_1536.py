# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures_tags', '0005_delete_testpic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='path',
        ),
        migrations.DeleteModel(
            name='Path',
        ),
    ]
