# Don't forget to run the tests (and create some of your own)

# Part 1
def is_character_match(string1, string2):
	# using the sorted method
	# return sorted(string1.lower()) == sorted(string2.lower())

	#without using the sorted method
	string1_lower = string1.lower()
	string2_lower = string2.lower()
	dict1 = {}
	dict2 = {}

	if len(string1_lower) != len(string2_lower) :
		return False 

	for letter in string1_lower:
		dict1[letter] = 1

	for letter in string2_lower:
		dict2[letter] = 1

	for key in dict1:
		if dict1[key] == dict2[key]:
			return True
		
	return False




print(is_character_match('charm', 'march'))
print(is_character_match('zach', 'attack'))
print(is_character_match('CharM', 'mARcH'))
print(is_character_match('abcde2', 'c2abed'))


# Part 2
def anagrams_for(word, list_of_words):
	# your code here
	pass
