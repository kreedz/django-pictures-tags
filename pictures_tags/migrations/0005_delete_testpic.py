# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures_tags', '0004_testpic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testpic',
        ),
    ]
