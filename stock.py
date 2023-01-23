import os
import telebot
import yfinance as yf


api_key = "Your_token"
bot = telebot.TeleBot(api_key)

@bot.message_handler(commands = ['Greet'])
def greet(msg):
    bot.reply_to(msg, "Welcome to Bryanet59 Bot!")

@bot.message_handler(commands=['stock'])
def get_stock(message):
    stock_ticker = message.text.split()[1]
    stock_info = yf.Ticker(stock_ticker).info
    bot.reply_to(message, f'{stock_ticker} Stock Information: \n'
                    f'Current Price: {stock_info["regularMarketPrice"]} \n'
                    f'Previous Close: {stock_info["regularMarketPreviousClose"]} \n'
                    f'52 Week High: {stock_info["fiftyTwoWeekHigh"]} \n'
                    f'52 Week Low: {stock_info["fiftyTwoWeekLow"]}')

bot.polling() 

