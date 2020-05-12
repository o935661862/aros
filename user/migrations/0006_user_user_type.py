# Generated by Django 3.0.5 on 2020-04-26 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserType'),
        ),
    ]
