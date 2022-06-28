
from numpy import average


print('hello world!')


def count_letters(text)->dict:
    result = {}
    for letter in text:
        result[letter] = result.get(letter, 0) + 1
    return result

print(count_letters("my name is motasem"))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			if user in group_dictionary[group]:
				#add as string
				user_groups[user] = user_groups.get(user, "") + " "+group
	# convert string to list
	for user, groups in user_groups.items():
		user_groups[user] = groups.split()
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def format_address(address_string:str)->str:
  
  address_list = address_string.split()
  return "house number {} on street named {}".format(address_list[0], " ".join(address_list[1:]))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

def highlight_word(sentence:str, word:str)->str:	
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

def combine_guests(guests1:dict, guests2:dict)->dict:
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))
print(sorted(Rorys_guests.items(), reverse=True), "hello")#reverse keys and values and sort

def count_letters(text:str):
	res = {}
	for letter in text:
		if letter.isalnum():
			res[letter] = res.get(letter, 0) + 1
	return res

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


def combine_lists(list1:list, list2:list)->list:
  # Generate a new list containing the elements of list2
  list1.reverse()
  # Followed by the elements of list1 in reverse order
  list2.extend(list1)
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))



print(average([1,4,5,7]))

'''
sorted(dict().items(), key=dict.get)[:10]#used to get the top 10  common words in a text file
'''