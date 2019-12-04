input_file = open('./input/01_01.txt')
input_data = input_file.read()
data = [int(d) for d in input_data.split('\n')]

def fuel_calc(mass):
	"Calculate fuel needed to launch module"
	return(mass // 3 - 2)

def test():
	assert fuel_calc(12) == 2
	assert fuel_calc(14) == 2
	assert fuel_calc(1969) == 654
	assert fuel_calc(100756) == 33583

	print('Tests pass')

test()

answer = sum(fuel_calc(mass) for mass in data)
print(answer)