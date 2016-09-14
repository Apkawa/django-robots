# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rule',
            options={'ordering': ['order'], 'verbose_name': 'rule', 'verbose_name_plural': 'rules'},
        ),
        migrations.AddField(
            model_name='rule',
            name='order',
            field=models.PositiveIntegerField(default=1000, verbose_name='order'),
        ),
    ]
