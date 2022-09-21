# Generated by Django 3.2.14 on 2022-07-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerized_app', '0003_auto_20220710_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Category',
            field=models.CharField(default='No category', max_length=1000, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='item',
            name='Description',
            field=models.CharField(default='No description', max_length=1000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='item',
            name='Price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='itemPicture',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media/', verbose_name='itemPicture'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='name'),
        ),
    ]