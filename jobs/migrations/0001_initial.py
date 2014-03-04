# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('linkedin_id', models.IntegerField(default=0)),
                ('logo_url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer', models.ForeignKey(to='jobs.Employer', to_field=u'id')),
                ('linkedin_id', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('close_date', models.DateTimeField(verbose_name='date closed')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
