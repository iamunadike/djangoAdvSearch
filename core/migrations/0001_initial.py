# Generated by Django 2.2.13 on 2020-06-14 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Author Name')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('publish_date', models.DateTimeField(verbose_name='Publish Date')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('reviewed', models.BooleanField(default=False, verbose_name='Reviewed')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Author', verbose_name='Author')),
                ('categories', models.ManyToManyField(to='core.Category', verbose_name='Categories')),
            ],
        ),
    ]
