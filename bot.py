import random
import telebot


TOKEN = ''
bot = telebot.TeleBot(TOKEN)

ids = []    # telegram users id
old_ids = [el for el in ids]
random.shuffle(ids)

# check if user don't get him-self
count = 0
while True:
    if True not in [old_ids[i] == ids[i] for i in range(len(ids))]:
        break
    else:
        count += 1
        random.shuffle(old_ids)
print('oops', count, '\n')

# send messages to secret Santas
for i in range(len(ids)):
    bot.send_message(old_ids[i], f'Your secret friend is @{bot.get_chat(ids[i]).username}')


