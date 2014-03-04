# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AddField(
            model_name='employer',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
