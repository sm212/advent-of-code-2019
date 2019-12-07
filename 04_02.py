import re
lower, upper = 147981, 691423

def possible_passwords(lower, upper):
	"Find all possible  passwords between lower & upper inclusive"

	passwords = []
	for n in range(lower, upper + 1):
		password = str(n)

		if contains_double(password) and not decreasing(password):
			passwords.append(password)

	return(passwords)

def contains_double(password):
	matches = re.findall(r'00+|11+|22+|33+|44+|55+|66+|77+|88+|99+', password)
	if matches and min([len(match) for match in matches]) == 2:
		return(True)
	else:
		return(False)


def decreasing(password):
	numbers = [int(letter) for letter in list(password)]

	answer = False
	for i in range(1, len(numbers)):
		if numbers[i] - numbers[i - 1] < 0:
			answer = True
			break

	return(answer)

def test():
	assert contains_double('122345') is True
	assert contains_double('111123') is False
	assert contains_double('135679') is False
	assert contains_double('111111') is False
	assert contains_double('123789') is False
	assert contains_double('112233') is True
	assert contains_double('123444') is False
	assert contains_double('111122') is True

	assert decreasing('122345') is False
	assert decreasing('111123') is False
	assert decreasing('135679') is False
	assert decreasing('111111') is False
	assert decreasing('223450') is True

	print('Tests pass!')

test()
print(len(possible_passwords(lower, upper)))