# Generated by Django 2.2.13 on 2020-07-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('first_met', models.CharField(max_length=100)),
                ('home_town', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('createddate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateddate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
