# Generated by Django 4.2.13 on 2024-05-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                ("category_name", models.CharField(max_length=255)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
