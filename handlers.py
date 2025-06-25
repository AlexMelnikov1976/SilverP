<<<<<<< HEAD
from telegram import Update                     # Для типизации входящего сообщения
from telegram.ext import ContextTypes           # Для типизации контекста
from google_api import read_main_data           # Импорт функции чтения основной таблицы
from analysis import analyze_last_day, forecast # Импорт аналитических функций

async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /analyze — анализ за последний день."""
    df = read_main_data()                                      # Читаем данные из основной таблицы
    message = analyze_last_day(df)                             # Формируем отчет
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)    # Отправляем в Telegram

async def forecast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /forecast — прогноз на месяц."""
    df = read_main_data()                                      # Читаем данные из основной таблицы
    message = forecast(df)                                     # Формируем отчет по прогнозу
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)    # Отправляем в Telegram
=======
from telegram import Update                     # Для типизации входящего сообщения
from telegram.ext import ContextTypes           # Для типизации контекста
from google_api import read_main_data           # Импорт функции чтения основной таблицы
from analysis import analyze_last_day, forecast # Импорт аналитических функций

async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /analyze — анализ за последний день."""
    df = read_main_data()                                      # Читаем данные из основной таблицы
    message = analyze_last_day(df)                             # Формируем отчет
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)    # Отправляем в Telegram

async def forecast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /forecast — прогноз на месяц."""
    df = read_main_data()                                      # Читаем данные из основной таблицы
    message = forecast(df)                                     # Формируем отчет по прогнозу
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)    # Отправляем в Telegram
>>>>>>> 2c61133ba2a13db18adcd184084f73e370918660
