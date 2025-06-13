from django.db import migrations, models
from django.utils.translation import gettext_lazy as _


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_rustdesdevice_cpu_alter_rustdesdevice_hostname_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rustdesdevice",
            options={
                "ordering": ("-rid",),
                "verbose_name": _("Device"),
                "verbose_name_plural": _("Device List"),
            },
        ),
        migrations.AlterModelOptions(
            name="rustdeskpeer",
            options={
                "ordering": ("-username",),
                "verbose_name": _("Peers"),
                "verbose_name_plural": _("Peers List"),
            },
        ),
        migrations.AlterModelOptions(
            name="rustdesktag",
            options={
                "ordering": ("-uid",),
                "verbose_name": _("Tags"),
                "verbose_name_plural": _("Tags List"),
            },
        ),
        migrations.AlterModelOptions(
            name="rustdesktoken",
            options={
                "ordering": ("-username",),
                "verbose_name": _("Token"),
                "verbose_name_plural": _("Token List"),
            },
        ),
        migrations.AlterModelOptions(
            name="sharelink",
            options={
                "ordering": ("-create_time",),
                "verbose_name": _("Share Link"),
                "verbose_name_plural": _("Link List"),
            },
        ),
        migrations.AlterModelOptions(
            name="userprofile",
            options={
                "permissions": (
                    ("view_task", _("Can see available tasks")),
                    ("change_task_status", _("Can change the status of tasks")),
                    ("close_task", _("Can remove a task by setting its status as closed")),
                ),
                "verbose_name": _("User"),
                "verbose_name_plural": _("User List"),
            },
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="create_time",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name=_("Device Registration Time")
            ),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="hostname",
            field=models.CharField(max_length=100, verbose_name=_("Hostname")),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="memory",
            field=models.CharField(max_length=100, verbose_name=_("Memory")),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="os",
            field=models.CharField(max_length=100, verbose_name=_("Operating System")),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="rid",
            field=models.CharField(blank=True, max_length=60, verbose_name=_("Client ID")),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="username",
            field=models.CharField(
                blank=True, max_length=100, verbose_name=_("System Username")
            ),
        ),
        migrations.AlterField(
            model_name="rustdesdevice",
            name="version",
            field=models.CharField(max_length=100, verbose_name=_("Client Version")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="alias",
            field=models.CharField(max_length=30, verbose_name=_("Alias")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="hostname",
            field=models.CharField(max_length=30, verbose_name=_("Operating System Name")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="platform",
            field=models.CharField(max_length=30, verbose_name=_("Platform")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="rhash",
            field=models.CharField(
                max_length=60, verbose_name=_("Device Connection Password")
            ),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="rid",
            field=models.CharField(max_length=60, verbose_name=_("Client ID")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="tags",
            field=models.CharField(max_length=30, verbose_name=_("Tag")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="uid",
            field=models.CharField(max_length=16, verbose_name=_("User ID")),
        ),
        migrations.AlterField(
            model_name="rustdeskpeer",
            name="username",
            field=models.CharField(max_length=20, verbose_name=_("System Username")),
        ),
        migrations.AlterField(
            model_name="rustdesktag",
            name="tag_color",
            field=models.CharField(blank=True, max_length=60, verbose_name=_("Tag Color")),
        ),
        migrations.AlterField(
            model_name="rustdesktag",
            name="tag_name",
            field=models.CharField(max_length=60, verbose_name=_("Tag Name")),
        ),
        migrations.AlterField(
            model_name="rustdesktag",
            name="uid",
            field=models.CharField(max_length=16, verbose_name=_("Belongs to User ID")),
        ),
        migrations.AlterField(
            model_name="rustdesktoken",
            name="access_token",
            field=models.CharField(
                blank=True, max_length=60, verbose_name=_("Access Token")
            ),
        ),
        migrations.AlterField(
            model_name="rustdesktoken",
            name="create_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name=_("Login Time")),
        ),
        migrations.AlterField(
            model_name="rustdesktoken",
            name="uid",
            field=models.CharField(max_length=16, verbose_name=_("User ID")),
        ),
        migrations.AlterField(
            model_name="rustdesktoken",
            name="username",
            field=models.CharField(max_length=20, verbose_name=_("Username")),
        ),
        migrations.AlterField(
            model_name="rustdesktoken",
            name="uuid",
            field=models.CharField(max_length=60, verbose_name=_("UUID")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="create_time",
            field=models.DateTimeField(auto_now_add=True, verbose_name=_("Creation Time")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="is_expired",
            field=models.BooleanField(default=False, verbose_name=_("Is Expired")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="is_used",
            field=models.BooleanField(default=False, verbose_name=_("Is Used")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="peers",
            field=models.CharField(max_length=20, verbose_name=_("Machine ID List")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="shash",
            field=models.CharField(max_length=60, verbose_name=_("Link Key")),
        ),
        migrations.AlterField(
            model_name="sharelink",
            name="uid",
            field=models.CharField(max_length=16, verbose_name=_("User ID")),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="deviceInfo",
            field=models.TextField(blank=True, verbose_name=_("Login Information:")),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name=_("Is Activated")),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="is_admin",
            field=models.BooleanField(default=False, verbose_name=_("Is Admin")),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="username",
            field=models.CharField(max_length=50, unique=True, verbose_name=_("Username")),
        ),
    ]