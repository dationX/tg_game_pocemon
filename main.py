import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")        


@bot.message_handler(commands=['attack'])
def attack(message):
    enemy_username = message.reply_to_message.from_user.username
    my_username = message.from_user.username

    if enemy_username not in Pokemon.pokemons:
        bot.reply_to(message, "У этого человека нет покемона. Создать его можно с помощью /go")
    
    elif my_username not in Pokemon.pokemons:
        bot.reply_to(message, "У вас нет покемона. Создайте его с помощью /go")
    
    else:
        my_pokemon = Pokemon.pokemons[my_username]
        enemy_pokemon = Pokemon.pokemons[enemy_username]
        
        result = my_pokemon.attack(enemy_pokemon)

        bot.reply_to(message, result)


@bot.message_handler(commands=['info'])
def info(message):
    user = message.from_user.username

    if user in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[user]

        text = Pokemon.info(pokemon)
        result = ""

        for value in text:
            result += f"{value}: {text[value]}\n"

        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "Создайте покемона, с помощью /go")


@bot.message_handler(commands=['feed'])
def info(message):
    user = message.from_user.username

    if user in Pokemon.pokemons:
        pokemon:Pokemon = Pokemon.pokemons[user]

        feed_pokemon = pokemon.feed()

        bot.send_message(message.chat.id, feed_pokemon)
    else:
        bot.send_message(message.chat.id, "Создайте покемона, с помощью /go")
        

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
