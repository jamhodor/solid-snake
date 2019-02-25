# Generated by Django 2.1.4 on 2019-02-23 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190221_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='updated',
            new_name='updated_on',
        ),
        migrations.RemoveField(
            model_name='post',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='posted',
        ),
        migrations.AddField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime),
        ),
    ]
