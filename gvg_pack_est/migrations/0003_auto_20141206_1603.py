# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gvg_pack_est', '0002_auto_20141205_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimator',
            name='n_comm_excl',
        ),
        migrations.RemoveField(
            model_name='estimator',
            name='n_epic_excl',
        ),
        migrations.RemoveField(
            model_name='estimator',
            name='n_leg_excl',
        ),
        migrations.RemoveField(
            model_name='estimator',
            name='n_rare_excl',
        ),
        migrations.RemoveField(
            model_name='estimator',
            name='n_trials',
        ),
    ]
