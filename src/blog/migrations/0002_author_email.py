# Generated by Django 2.1.4 on 2019-02-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='me@myself.com', max_length=30),
        ),
    ]
