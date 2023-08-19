# Generated by Django 2.2.9 on 2023-08-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('use_clearcache', "Can see clearcache UI in Admin, and use the 'clearcache_admin' view."),),
                'managed': False,
                'default_permissions': (),
            },
        ),
    ]