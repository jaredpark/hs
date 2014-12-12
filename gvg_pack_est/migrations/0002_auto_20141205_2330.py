# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gvg_pack_est', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimator',
            name='n_comm_excl',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimator',
            name='n_epic_excl',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimator',
            name='n_leg_excl',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimator',
            name='n_rare_excl',
            field=models.IntegerField(default=0, max_length=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estimator',
            name='n_trials',
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=True,
        ),
    ]
