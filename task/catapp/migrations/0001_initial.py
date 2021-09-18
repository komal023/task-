# Generated by Django 3.2.7 on 2021-09-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catmodel',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cat_breed', models.CharField(blank=True, max_length=50, null=True)),
                ('cat_desc', models.TextField(blank=True, null=True)),
                ('cat_image', models.ImageField(upload_to='static/images/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
