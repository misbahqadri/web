# Generated by Django 2.2.4 on 2020-08-11 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0138_auto_20200810_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='bountyfulfillment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='dashboard.HackathonProject'),
        ),
    ]
