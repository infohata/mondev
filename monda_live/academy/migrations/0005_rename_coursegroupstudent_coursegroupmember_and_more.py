# Generated by Django 4.2.2 on 2023-07-16 09:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0004_alter_course_code_alter_course_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseGroupStudent',
            new_name='CourseGroupMember',
        ),
        migrations.AlterModelOptions(
            name='coursegroup',
            options={'ordering': ('-starting_date', 'code'), 'verbose_name': 'course group', 'verbose_name_plural': 'course groups'},
        ),
    ]
