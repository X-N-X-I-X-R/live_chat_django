# Generated by Django 5.0.4 on 2024-05-04 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=50)),
                ('room_description', models.TextField()),
                ('room_users', models.ManyToManyField(to='chat.users')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('message_content', models.TextField()),
                ('message_time', models.DateTimeField(auto_now_add=True)),
                ('message_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat_room')),
                ('message_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.users')),
            ],
        ),
    ]