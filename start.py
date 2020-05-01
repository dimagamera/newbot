from lib.settings import *
import telebot
import requests
URL = "https://api.covid19api.com/summary"
bot = telebot.TeleBot(token)


def request(URL):
    responce = requests.get(URL)
    return responce.json()


coron = requests.get(URL)
coron = coron.json()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Симптоми COVID-19')
    keyboard.row('Як користуватись ботом?')
    bot.send_sticker(
        message.chat.id, 'CAACAgIAAxkBAAJHnV6XFGmleFAuqbkOCpPyOb1AWAODAAILAANuM_gRBymXN2LhKucYBA', reply_markup=keyboard)
    bot.send_message(
        message.chat.id, '1️⃣Щоб переглянути статистику, напишіть назву країни. Наприклад: 𝐔𝐤𝐫𝐚𝐢𝐧𝐞, 𝐈𝐭𝐚𝐥𝐲, 𝐂𝐡𝐢𝐧𝐚, 𝐑𝐮𝐬𝐬𝐢𝐚𝐧 𝐅𝐞𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧, або по коду 𝐔𝐀, 𝐈𝐓, 𝐂𝐍, 𝐑𝐔', reply_markup=keyboard)
    bot.send_voice(message.chat.id, "http://d.zaix.ru/iK2U.mp3")


@bot.message_handler(content_types=['text'])
def handler_text(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Симптоми COVID-19')
    keyboard.row('Як користуватись ботом?')
    cout = message.text
    for item in coron["Countries"]:
        if item["Country"] == cout or item["CountryCode"] == cout:
            Country = item["Country"]
            CountryCode = item["CountryCode"]
            Slug = item["Slug"]
            NewConfirmed = item["NewConfirmed"]
            TotalConfirmed = item["TotalConfirmed"]
            NewDeaths = item["NewDeaths"]
            TotalDeaths = item["TotalDeaths"]
            NewRecovered = item["NewRecovered"]
            TotalRecovered = item["TotalRecovered"]

            if item["Country"] == cout or item["CountryCode"] == cout:
                if message.text == cout:
                    cout = message.text
                    bot.send_message(message.chat.id, "Оперативна інформація про поширення коронавірусної інфекції 🌏 [𝐂𝐎𝐕𝐈𝐃-19] 🌏\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"+"\n✈️ Країна ✈️ → " +
                                     str(Country) + "\n🤧 Кількість захворювань 🤧 → "+str(TotalConfirmed)+"\n🤧 Кількість захворювань за добу 🤧 → " + str(NewConfirmed) +
                                     "\n☠️ Кількість смертей ☠️ → " +
                                     str(TotalDeaths) + "\n☠️ Кількість смертей за добу ☠️ →  " + str(NewDeaths) +
                                     "\n💊 Кількість вилікуваних 💊 → " + str(TotalRecovered) + "\n💊 Кількість вилікуваних за добу 💊 → " + str(NewRecovered))
                    bot.send_sticker(
                        message.chat.id, "CAACAgIAAxkBAAJHrV6XFbrPmHvDNA2ynmPIGzpvUhU9AALOAQACVp29Cq2jmuzmnvpMGAQ", reply_markup=keyboard)
            else:
                print("1")
    if message.text == "Симптоми COVID-19":
        bot.send_photo(
            message.chat.id, "http://i.piccy.info/i9/7333fbd68a014010173ed8f1a74969f0/1587472373/401901/1374142/43_Algorytm_d_1110_i_za_p_1110_dozry_COVID_19.jpg", reply_markup=keyboard)
    elif message.text == "Як користуватись ботом?":
        bot.send_message(
            message.chat.id, "1️⃣Щоб переглянути статистику, напишіть назву країни. Наприклад: 𝐔𝐤𝐫𝐚𝐢𝐧𝐞, 𝐈𝐭𝐚𝐥𝐲, 𝐂𝐡𝐢𝐧𝐚, 𝐑𝐮𝐬𝐬𝐢𝐚𝐧 𝐅𝐞𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧, або по коду 𝐔𝐀, 𝐈𝐓, 𝐂𝐍, 𝐑𝐔", reply_markup=keyboard)


bot.polling(none_stop=True)
