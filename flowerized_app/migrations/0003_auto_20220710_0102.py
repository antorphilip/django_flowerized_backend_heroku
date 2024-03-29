# Generated by Django 2.2.13 on 2022-07-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerized_app', '0002_alter_item_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=1000, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=1000, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=1000, verbose_name='Email')),
                ('phoneNumber', models.CharField(max_length=1000, verbose_name='phoneNumber')),
                ('password', models.CharField(max_length=2000, verbose_name='password')),
                ('confirmPassword', models.CharField(max_length=2000, verbose_name='repassword')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
