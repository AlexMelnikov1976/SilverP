from google_api import read_main_data        # Импорт функции для чтения данных из Google Sheets
from analysis import analyze_last_day, forecast   # Импорт функций анализа

def main():
    """Точка входа: загружает данные и выводит отчёты на консоль."""
    df = read_main_data()                    # Загружаем данные из таблицы
    print("-" * 40)
    print("Отчёт за последний день:")        # Заголовок
    print(analyze_last_day(df))              # Печатаем анализ за день
    print("-" * 40)
    print("Прогноз на месяц:")               # Заголовок
    print(forecast(df))                      # Печатаем прогноз

if __name__ == "__main__":                   # Запуск при вызове main.py
    main()
