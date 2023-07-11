# Generated by Django 4.2.3 on 2023-07-11 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0013_alter_telegrambotcommand_database_record'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegrambotuser',
            options={'verbose_name': 'Пользователя Telegram бота', 'verbose_name_plural': 'Пользователи Telegram ботов'},
        ),
        migrations.AlterField(
            model_name='telegrambotuser',
            name='date_activated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата активации'),
        ),
        migrations.AlterField(
            model_name='telegrambotuser',
            name='full_name',
            field=models.CharField(max_length=129, null=True, verbose_name='Полное имя пользователя'),
        ),
        migrations.AlterField(
            model_name='telegrambotuser',
            name='is_allowed',
            field=models.BooleanField(default=False, verbose_name='Разрешён'),
        ),
        migrations.AlterField(
            model_name='telegrambotuser',
            name='telegram_bot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='telegram_bot.telegrambot', verbose_name='Telegram бот'),
        ),
        migrations.AlterField(
            model_name='telegrambotuser',
            name='user_id',
            field=models.BigIntegerField(verbose_name='Telegram ID пользователя'),
        ),
    ]
