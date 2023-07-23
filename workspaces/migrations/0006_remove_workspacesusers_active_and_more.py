# Generated by Django 4.2.3 on 2023-07-23 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0005_workspaces_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspacesusers',
            name='active',
        ),
        migrations.RemoveField(
            model_name='workspacesusers',
            name='username',
        ),
        migrations.AddField(
            model_name='workspacesusers',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='workspace_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]