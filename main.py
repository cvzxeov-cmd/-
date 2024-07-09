from telegram.ext import Updater, CommandHandler
from config import TOKEN, CHANNEL_USERNAME

# Обработчик команды /start
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f'Привет, {user.first_name}! Отправьте заявку на вступление в канал.')

# Обработчик команды для заявки на вступление
def join_channel(update, context):
    user = update.message.from_user

    try:
        # Добавляем пользователя в канал
        context.bot.add_chat_member(chat_id=CHANNEL_USERNAME,
                                    user_id=user.id,
                                    can_send_messages=False)  # пользователь может отправлять сообщения
        update.message.reply_text(f'Добро пожаловать в канал, {user.first_name}!')
    except Exception as e:
        update.message.reply_text('Что-то пошло не так. Попробуйте позже.')

def main():
    # Создаем экземпляр Updater и передаем ему токен вашего бота
    updater = Updater(token=TOKEN, use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("join", join_channel))

    # Начинаем поиск обновлений
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
