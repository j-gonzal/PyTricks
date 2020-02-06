words = ['goodbye', 'cruel', 'world']

lengths = [len(x) for x in words]

# Not the pythonic way!
lengths = []
for word in words:
	lengths.append(len(word))

# 1. Dictionary copmrehension
data = {word: len(word) for word in words}

# zip two lists together
words = ["hello", "old", "friend"]
lengths = [len(word) for word in words]
data = dict(zip(words, lengths))

# 2. Filtering
words = ['deified', 'radar', 'guns']
palindromes = [word for word in words if word == word[::-1]]

# 3. Generators
text = open("bigdata.txt", "r")
lines = (line for line in text if line.startswith("2020-01-01"))

def average_line_length(lines):
	num_lines = 0
	total_length = 0
	for line in lines:
		num_lines += 1
		total_length += len(line)
	return total_length / num_lines

result = average_line_length(lines)

