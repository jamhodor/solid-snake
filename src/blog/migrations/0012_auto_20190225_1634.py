# Generated by Django 2.1.4 on 2019-02-25 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190223_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='posted',
            new_name='posted_on',
        ),
    ]
