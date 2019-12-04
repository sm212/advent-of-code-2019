input_file = open('./input/02_01.txt')
input_data = input_file.read()
data = [int(d) for d in input_data.split(',')]

def run_code(intcode):
	"Runs an intcode"

	index = 0
	while intcode[index] != 99:

		op = intcode[index]
		val1 = intcode[intcode[index + 1]]
		val2 = intcode[intcode[index + 2]]
		out_index = intcode[index + 3]

		if op not in (1, 2, 99):
			raise ValueError('Invalid operator at position {}. Expected 1, 2, or 99. Got {}'.format(index, op))

		if op == 1:
			intcode[out_index] = val1 + val2
		if op == 2:
			intcode[out_index] = val1 * val2

		index += 4

	return(intcode)

# Which parameters (values at position 1 & 2) result in 19690720 in position 0?
for noun in range(0, 100):
	for verb in range(0, 100):
		test_code = data[:]
		test_code[1], test_code[2] = noun, verb

		if run_code(test_code)[0] == 19690720:
			print(100 * noun + verb)
			break