# Generated by Django 3.2.14 on 2022-07-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerized_app', '0006_alter_item_itempicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemPicture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='media', verbose_name='itemPicture'),
        ),
    ]