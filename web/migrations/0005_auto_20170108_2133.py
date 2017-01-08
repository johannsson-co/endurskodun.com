# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-08 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_homepage_page3_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet1_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet1_title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet2_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet2_title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet3_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet3_title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_bullet_title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_sidebullet_text',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='page2_sidebullet_title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
