# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='publish_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', db_index=True, blank=True),
        ),
    ]
