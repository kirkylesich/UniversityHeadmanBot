# Generated by Django 3.1.2 on 2020-11-23 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lessonlink'),
        ),
    ]
