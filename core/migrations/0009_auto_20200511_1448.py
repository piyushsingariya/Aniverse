# Generated by Django 3.0.6 on 2020-05-11 14:48

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=''),
        ),
    ]
