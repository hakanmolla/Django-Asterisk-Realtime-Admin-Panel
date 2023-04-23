# Generated by Django 4.2 on 2023-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsjsipAdd',
            fields=[
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True)),
                ('transport', models.CharField(blank=True, max_length=40, null=True)),
                ('aors', models.CharField(blank=True, max_length=200, null=True)),
                ('auth', models.CharField(blank=True, max_length=40, null=True)),
                ('context', models.CharField(blank=True, max_length=40, null=True)),
                ('disallow', models.CharField(blank=True, max_length=200, null=True)),
                ('allow', models.CharField(blank=True, max_length=200, null=True)),
                ('direct_media', models.CharField(blank=True, max_length=3, null=True)),
                ('mailboxes', models.CharField(blank=True, max_length=40, null=True)),
                ('deny', models.CharField(blank=True, max_length=95, null=True)),
                ('permit', models.CharField(blank=True, max_length=95, null=True)),
                ('max_contacts', models.IntegerField(blank=True, null=True)),
                ('qualify_frequency', models.IntegerField(blank=True, null=True)),
                ('auth_type', models.CharField(blank=True, max_length=12, null=True)),
                ('password', models.CharField(blank=True, max_length=80, null=True)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]