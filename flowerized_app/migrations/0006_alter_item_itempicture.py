# Generated by Django 3.2.14 on 2022-07-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerized_app', '0005_alter_item_itempicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemPicture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='https://flowerized-backend.herokuapp.com/media/', verbose_name='itemPicture'),
        ),
    ]
