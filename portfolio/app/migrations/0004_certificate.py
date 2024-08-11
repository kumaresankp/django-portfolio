# Generated by Django 5.1 on 2024-08-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_project_banner_alter_project_icon"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("url", models.URLField()),
                ("image", models.ImageField(upload_to="Media/certificates/")),
                ("tag", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
