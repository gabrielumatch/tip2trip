# Generated by Django 5.1.7 on 2025-03-29 16:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='placevisit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_visits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='placephoto',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.placevisit'),
        ),
        migrations.AlterUniqueTogether(
            name='placeamenity',
            unique_together={('place', 'amenity_type')},
        ),
        migrations.AddIndex(
            model_name='placevisit',
            index=models.Index(fields=['user', 'place'], name='places_plac_user_id_ecb32a_idx'),
        ),
        migrations.AddIndex(
            model_name='placevisit',
            index=models.Index(fields=['visit_date'], name='places_plac_visit_d_7d4921_idx'),
        ),
    ]
