# Generated by Django 3.2.4 on 2021-07-01 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0006_auto_20210701_0838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='last_name',
            new_name='patient_last_name',
        ),
        migrations.AddField(
            model_name='consultations',
            name='patient_last_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aidApp.patients'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consultations',
            name='last_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aidApp.doctors'),
        ),
    ]