# Generated by Django 5.0.6 on 2024-07-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('article', models.TextField(blank=True, null=True)),
                ('views', models.IntegerField()),
            ],
        ),
    ]
