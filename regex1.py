import re
def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	else:
		return None
# print(extract_phone("My number is 555 801-9654"))
# print(extract_phone("My number is 4404289551051"))
# print(extract_phone("555 801-9654"))
# print(extract_phone("555 801-965 is my phone number"))

def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# print(extract_all_phones("My number is 555 801-965555 801-965 and her number is 281 330-8004 while his is 330-876-5309"))
# print(extract_all_phones("My number is 5556 801-965 and her number is 2810 330-8004 while his is 9330-876-5309"))

def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	else:
		return False


#second way to do the same thing. Without ^ or $ but same result
def is_valid_phone(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	else:
		return False

print(is_valid_phone("281 330-8004"))
print(is_valid_phone("281 330-8004 I like dogs"))
