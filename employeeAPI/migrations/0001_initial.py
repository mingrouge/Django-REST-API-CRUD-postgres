# Generated by Django 2.2.13 on 2020-07-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=5)),
                ('mobile', models.CharField(max_length=10)),
                ('createddate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateddate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
