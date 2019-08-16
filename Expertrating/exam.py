import string

input_str = raw_input()



for i in range(1,6):
  password = input_str[i]
  if (password)<5:
    return False
  if " " in password:
    return False
  if "*" or "#" or "+" or "@" in
  