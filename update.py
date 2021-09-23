from datetime import datetime
from dateutil import relativedelta


birthDate = datetime(1991, 7, 4)
currentDate = datetime(
  datetime.today().year,
  datetime.today().month, 
  datetime.today().day
)
delta = relativedelta.relativedelta(currentDate, birthDate)

def formatNumeralConcord():
    concord = []
    concord.append('month') if delta.months <= 1 else concord.append('months')
    concord.append('day') if delta.days <= 1 else concord.append('days')
    return concord

def formatUptimeString():
    days = formatNumeralConcord()[1]
    months = formatNumeralConcord()[0]
    return 'Uptime: "{} years, {} {}, {} {}"\n'.format(delta.years, delta.months, months, delta.days, days)

def overwriteFile():
    with open('README.md', 'r+') as file:
        data = file.readlines()
        data[20] = formatUptimeString()
        file.seek(0)
        file.writelines(data)
        file.truncate()


if __name__ == '__main__':
    overwriteFile()
