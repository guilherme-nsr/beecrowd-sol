NUMBER_DAYS_EACH_MONTH_2016 = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

def calc_remaining_days(start_month, start_day, end_month, end_day):
  if start_month == end_month and start_day > end_day:
    return -1

  current_month = start_month
  current_day = start_day
  remaining_days = 0

  while current_month <= end_month:
    number_days_current_month = NUMBER_DAYS_EACH_MONTH_2016[current_month-1]

    while current_day < number_days_current_month:
      if current_day == end_day and current_month == end_month:
        break

      remaining_days += 1
      current_day += 1

    current_month += 1
    current_day = 0

  return remaining_days

def get_message(remaining_days):
  if remaining_days == 1:
    return "E vespera de natal!"
  elif remaining_days == -1:
    return "Ja passou!"
  elif remaining_days == 0:
    return "E natal!"
  else:
    return "Faltam %d dias para o natal!" % (remaining_days)


christmas_month = 12
christmas_day = 25

while True:
  try:
    month, day = map(int, input().split())

    message = get_message(calc_remaining_days(month, day, christmas_month, christmas_day))
    print(message)
  except EOFError:
    break
