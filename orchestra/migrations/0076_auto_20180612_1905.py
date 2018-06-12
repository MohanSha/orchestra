# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-12 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import orchestra.models.core.mixins
import orchestra.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0075_add_sanity_checks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChecklistTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_deleted', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('todos', jsonfield.fields.JSONField(default={'list': []})),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='orchestra.Worker')),
            ],
            bases=(orchestra.models.core.mixins.ChecklistTemplateMixin, orchestra.utils.models.DeleteMixin, models.Model),
        ),
        migrations.AddField(
            model_name='todo',
            name='log',
            field=jsonfield.fields.JSONField(default={'actions': []}),
        ),
        migrations.AddField(
            model_name='todo',
            name='parent_todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='orchestra.Todo'),
        ),
        migrations.AddField(
            model_name='todo',
            name='skipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='template', to='orchestra.ChecklistTemplate'),
        ),
    ]