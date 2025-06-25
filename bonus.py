from google_api import get_management_bonus_grid

def calc_manager_bonus(net_profit):
    """
    Возвращает процент и сумму бонуса управляющего по сетке (чистой прибыли).
    """
    bonus_df = get_management_bonus_grid("Управляющий")
    match = bonus_df[
        (bonus_df["Минимум"] <= net_profit) & (net_profit <= bonus_df["Максимум"])
    ]
    if not match.empty:
        percent = float(str(match.iloc[0]["Бонус"]).replace("%", "").replace(",", "."))
        bonus = net_profit * (percent / 100)
        return percent, bonus
    else:
        return 0, 0

def get_manager_bonus_line(net_profit, format_ruble_func):
    """
    Возвращает строку для отчёта с бонусом управляющего, красиво оформленную.
    """
    percent, bonus = calc_manager_bonus(net_profit)
    if percent > 0 and bonus > 0:
        return f"🎁 Бонус управляющего: {format_ruble_func(bonus)} ({percent}%)"
    else:
        return "🎁 Бонус управляющего: не начислен"
