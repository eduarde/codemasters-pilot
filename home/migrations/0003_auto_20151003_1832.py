# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to='E:\\Development workspace\\codemasters-pilot\\images'),
        ),
    ]
