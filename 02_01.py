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

def test():
	assert run_code([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
	assert run_code([1,0,0,0,99]) == [2,0,0,0,99]
	assert run_code([2,3,0,3,99]) == [2,3,0,6,99]
	assert run_code([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
	assert run_code([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
	print('Tests pass!')

test()

# Update puzzle input according to problem text, then get first number
data[1], data[2] = 12, 2
answer = run_code(data)[0]

print(answer)