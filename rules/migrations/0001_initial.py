# Generated by Django 5.1.2 on 2024-10-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_string', models.TextField()),
                ('ast', models.JSONField()),
            ],
        ),
    ]
