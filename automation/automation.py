import re

def sort_email(email):
  total_ord_value_for_email = []
  for char in email[:]:
    value = ord(char) - 97
    total_ord_value_for_email.append(value)

  return total_ord_value_for_email

def sort_number(number):
  regex = r"[0-9]"
  phone_check = ''
  while len(phone_check)<3:
    for char in number:
      if re.match(regex,char):
        phone_check += char
  return int(phone_check)

def get_emails_and_phone_numbers(path):
  with open(f"{path}") as file:
    potential_contact_text = file.read()

  regex_email = r"\w+[@]\w+[.]\w{3}"

  all_emails = re.findall(regex_email,potential_contact_text)
  all_emails = list(set(all_emails))
  all_emails.sort(key=sort_email)
  email_list = ''
  for email in all_emails:
    email_list +=f"{str(email)}\n"
  # print(email_list)

  regex_phone = r"\(?\d{3}\)?[ -.]\d{3}[ -.]\d{4}"

  phone_numbers = re.findall(regex_phone,potential_contact_text)
  phone_numbers = list(set(phone_numbers))
  phone_numbers.sort(key=sort_number)
  phone_list = ''
  for numbers in phone_numbers:
    phone_list +=f"{str(numbers)}\n"

  with open('automation/phone_numbers.txt','w') as phone_file:
    phone_file.write(phone_list)

  with open('automation/emails.txt','w') as email_file:
    email_file.write(email_list)

if __name__ == "__main__":
  
  get_emails_and_phone_numbers("automation/potential_contacts.txt")
