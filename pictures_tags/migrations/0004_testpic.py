# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures_tags', '0003_picture_subpath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testpic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'test')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
