# Generated by Django 5.0.6 on 2024-06-02 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionChoice',
            fields=[
                ('choice_id', models.AutoField(primary_key=True, serialize=False)),
                ('choice_name', models.CharField(max_length=100)),
                ('extra_cost', models.IntegerField(default=0)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='order.options')),
            ],
            options={
                'db_table': 'option_choice',
            },
        ),
    ]