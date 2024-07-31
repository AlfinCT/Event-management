# Generated by Django 4.2.8 on 2024-07-10 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0003_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=700)),
                ('booking_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.work')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event_type', 'booking_date')},
            },
        ),
    ]