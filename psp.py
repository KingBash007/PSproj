def get_all_substrings(input_string):
	# base case 1: if the input string is empty, return an empty list
	if len(input_string) == 0:
		return []
	
	# base case 2: if the input string contains only one character, return a list with that character
	elif len(input_string) == 1:
		return [input_string]
	
	# recursive case: if the input string contains multiple characters
	else:
		# create an empty list to store the resulting substrings
		output = []
		
		# use nested loops to generate all possible substrings of the input string
		for i in range(len(input_string)):
			for j in range(i+1, len(input_string)+1):
				output.append(input_string[i:j])
		
		# recursively call the function with the input string sliced from the second character to the end
		# and concatenate the resulting list of substrings with the list generated from the current call
		return output + get_all_substrings(input_string[1:])

# test the function with an example string
my_string = "hello"
substrings = get_all_substrings(my_string)
print(substrings)
