import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Gets the remaining calories for today
        # x is not a good name for a variable, it should explain what it is, ex: calories_remained
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'You can eat something else today,' \
                   f' but with a total calorie content of no more than {x} kcal'
        else:
            return('Stop eating!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # US dollar exchange rate.
    EURO_RATE = float(70)  # Euro exchange rate.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # Not an error, but it would be cleaner an easier to read if you used a dictionary instead of if/elif/else
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            cash_remained == 1.00  # this is not an assignment, it's a comparison
            currency_type = 'rub'
        if cash_remained > 0:
            # You are not returning the requested message
            # the message should be:
            # 'There are {cash_remained} {currency_type} left for today'
            # this way the currency type will also be displayed
            return (
                f'Left for today {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'No money, keep it up!'
        elif cash_remained < 0:
            return 'No money, keep it up:' \
                   ' your debt is - {0:.2f} {1}'.format(-cash_remained,
                                                        currency_type)

    def get_week_stats(self):
        # since you are using the same method from the parent class you don't need to implement it here, but if you do, you should return the result from the parent method, otherwise you will be returning None

        # return super().get_week_stats() -> like this
        # then again, you don't need to implement it here
        super().get_week_stats()
