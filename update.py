from datetime import datetime
from dateutil import relativedelta


birthDate = datetime(1991, 7, 4)
currentDate = datetime(
    datetime.today().year,
    datetime.today().month,
    datetime.today().day
)
delta = relativedelta.relativedelta(currentDate, birthDate)


def formatUptimeString():
    days = 'day' if delta.days <= 1 else 'days'
    months = 'month' if delta.months <= 1 else 'months'
    return f'Uptime: "{delta.years} years, {delta.months} {months}, {delta.days} {days}"\n'


def overwriteFile():
    with open('README.md', 'r+') as file:
        data = file.readlines()
        data[25] = formatUptimeString()
        file.seek(0)
        file.writelines(data)
        file.truncate()


if __name__ == '__main__':
    overwriteFile()
