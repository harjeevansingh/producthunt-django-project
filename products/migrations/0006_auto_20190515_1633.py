# Generated by Django 2.2 on 2019-05-15 11:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_auto_20190515_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 5, 15, 16, 33, 31, 51243))),
                ('location', models.CharField(max_length=200)),
                ('votes_total', models.IntegerField(default=1)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
