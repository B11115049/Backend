# Generated by Django 4.2.3 on 2023-07-29 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_material_unique_together_remove_material_ename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='CName',
            new_name='name',
        ),
    ]
