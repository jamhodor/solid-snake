# Generated by Django 2.1.4 on 2019-02-20 07:25

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
                ('picture', models.ImageField(blank=True, max_length=60, upload_to='images/blog/')),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='notes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='picture',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
