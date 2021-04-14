# Generated by Django 3.2 on 2021-04-09 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_language_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese, etc.)", max_length=200),
        ),
    ]
