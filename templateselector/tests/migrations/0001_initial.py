# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import templateselector.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f', templateselector.fields.TemplateField(display_name=templateselector.fields.nice_display_name, match='^admin/.+\\.html$', verbose_name="test 'f'")),
            ],
        ),
    ]
