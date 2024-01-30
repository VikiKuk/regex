import re
import csv
from pprint import pprint


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# соединяем ФИО
for record in contacts_list:
  full_name = ''.join([record[0], ' ', record[1], ' ', record[2]]).replace('  ', ' ')
  result = full_name.split(' ')
  record[0] = result[0]
  record[1] = result[1]
  record[2] = result[2]

# ищем дубли и объединяем их
for index, record in enumerate(contacts_list):
  for index2, comparison in enumerate(contacts_list[index+1:], start=index+1):
    if record[0] == comparison[0] and record[1] == comparison[1]:
      print(f'Найденные дубли {record[0], record[1]}')
      for index3, i in enumerate(record):
        if len(i) > 0:
          continue
        else:
          if len(comparison[index3]) > 0:
            record[index3] = comparison[index3]
      del contacts_list[index2]
pprint(contacts_list)

# изменяем паттерн номеров телефонов
pattern = r'\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?'
for phone in contacts_list:
  phone[5] = re.sub(pattern, r'+7(\2)\3-\4-\5 \6 \7', phone[5])
pprint(contacts_list)


# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
