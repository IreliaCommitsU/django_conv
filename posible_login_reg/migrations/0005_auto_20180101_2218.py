# Generated by Django 2.0 on 2018-01-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posible_login_reg', '0004_auto_20180101_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='imgs/profilePics/usuarios/no-img.png', null=True, upload_to='usuarios/'),
        ),
    ]