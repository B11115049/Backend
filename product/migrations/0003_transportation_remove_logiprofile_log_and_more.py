# Generated by Django 4.2.3 on 2023-07-23 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_logtprofile_transportation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('carbonEmission', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RemoveField(
            model_name='logiprofile',
            name='log',
        ),
        migrations.RemoveField(
            model_name='logiprofile',
            name='product',
        ),
        migrations.RemoveField(
            model_name='logtprofile',
            name='log',
        ),
        migrations.RemoveField(
            model_name='logtprofile',
            name='transportation',
        ),
        migrations.DeleteModel(
            name='LogI',
        ),
        migrations.DeleteModel(
            name='LogT',
        ),
        migrations.AlterField(
            model_name='abstractlog',
            name='logType',
            field=models.CharField(choices=[('TRANSPORTATION', 'transportation'), ('ITEM', 'item')], default='TRANSPORTATION', editable=False, max_length=50),
        ),
        migrations.CreateModel(
            name='LogI',
            fields=[
                ('abstractlog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.abstractlog')),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Item Log',
                'verbose_name_plural': 'Item Logs',
            },
            bases=('product.abstractlog',),
        ),
        migrations.CreateModel(
            name='LogT',
            fields=[
                ('abstractlog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.abstractlog')),
                ('distance', models.FloatField(blank=True, default=0.0)),
                ('transportation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='product.transportation')),
            ],
            options={
                'verbose_name': 'Transportation Log',
                'verbose_name_plural': 'Transportation Logs',
            },
            bases=('product.abstractlog',),
        ),
        migrations.DeleteModel(
            name='LogIProfile',
        ),
        migrations.DeleteModel(
            name='LogTProfile',
        ),
    ]
