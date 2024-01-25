# Generated by Django 4.2.4 on 2024-01-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, unique=True, verbose_name='blog title')),
                ('description', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('view_count', models.PositiveBigIntegerField()),
                ('published', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'post',
                'ordering': ['posted_at'],
            },
        ),
    ]