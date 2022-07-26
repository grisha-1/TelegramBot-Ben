import telebot
import benconfig
from random import choice as c

bot = telebot.TeleBot(benconfig.token)
answer = ('yes', 'no', 'hah', 'grh')


@bot.message_handler(content_types=['voice'])
def question_And_Answer(message):
    text_answer = c(answer)
    if text_answer == 'yes':
        audio_yes = open('yes.mp3', 'rb')
        bot.send_audio(message.chat.id, audio_yes)
        audio_yes.close()
    if text_answer == 'no':
        audio_yes = open('no.mp3', 'rb')
        bot.send_audio(message.chat.id, audio_yes)
        audio_yes.close()
    if text_answer == 'hah':
        audio_yes = open('hohoho.mp3', 'rb')
        bot.send_audio(message.chat.id, audio_yes)
        audio_yes.close()
    if text_answer == 'grh':
        audio_yes = open('grh.mp3', 'rb')
        bot.send_audio(message.chat.id, audio_yes)
        audio_yes.close()
    print(message)


bot.polling(none_stop=True, interval=0)
