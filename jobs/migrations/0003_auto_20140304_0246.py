# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20140304_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='logo_url',
        ),
        migrations.RemoveField(
            model_name='employer',
            name='description',
        ),
    ]
