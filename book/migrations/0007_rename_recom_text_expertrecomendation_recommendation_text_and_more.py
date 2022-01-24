# Generated by Django 4.0.1 on 2022-01-24 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_expertrecomendation_expert'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expertrecomendation',
            old_name='recom_text',
            new_name='recommendation_text',
        ),
        migrations.AlterField(
            model_name='expertrecomendation',
            name='books',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_recommendation', to='book.book'),
        ),
    ]
