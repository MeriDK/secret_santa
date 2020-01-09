import random

import telebot


TOKEN = '964330098:AAEVEGcVmp4oZTJJ9s2VyyrQQTK9wwd_u8c'
bot = telebot.TeleBot(TOKEN)

updates = bot.get_updates()
for mess in updates:
    try:
        print(mess.message.from_user.id, mess.message.from_user.username, mess.message.text)
    except:
        print(mess)
print()

ids = [227190186, 391835327, 641170928, 234245907, 422000390, 384955663]
old_ids = [el for el in ids]
random.shuffle(ids)
count = 0
while True:
    if True not in [old_ids[i] == ids[i] for i in range(len(ids))]:
        break
    else:
        count += 1
        old_ids = [el for el in ids]
        random.shuffle(ids)
print('oops', count, '\n')

for i in range(len(ids)):
    bot.send_message(old_ids[i], f'Your secret friend is @{bot.get_chat(ids[i]).username}')


