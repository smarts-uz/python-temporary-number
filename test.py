import temporary_number

# number = temporary_number.get_number()
# print(number)
# number2 = temporary_number.get_number(country="UK")
# for i in range(100):
#     number = temporary_number.get_number(country='Netherlands')
#     print(i + 1, number)


# 3197010523354

messages = temporary_number.get_messages("+3197010523354")
from pprint import pprint
# pprint(messages)
for message in messages:
  print(f"{message.time} | From {message.frm}")
  print(message.content)