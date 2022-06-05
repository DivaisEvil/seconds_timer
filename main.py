import ptbot
import os
from pytimeparse import parse

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def reply(text):
    time = parse(text)
    message = 'Таймер запущен на, {},секунд' .format(time)
    message_id = bot.send_message(CHAT_ID, message)
    bot.create_timer(time, notify)
    bot.create_countdown(time, notify_progress, message_id=message_id, time=time)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration,)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left, message_id, time):
    countdown_counter = 'Осталось секунд:, {}\n{}' .format(secs_left, render_progressbar(time, time-secs_left))
    bot.update_message(CHAT_ID, message_id, countdown_counter)


def notify():
    bot.send_message(CHAT_ID, "Время вышло")

if __name__ == '__main__':
    bot = ptbot.Bot(TOKEN)
    bot.send_message(CHAT_ID, " На сколько запустить таймер? ")
    bot.reply_on_message(reply)
    bot.run_bot()
