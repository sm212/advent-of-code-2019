input_file = open('./input/01_01.txt')
input_data = input_file.read()
data = [int(d) for d in input_data.split('\n')]

def fuel_calc(mass):
	"Calculate total fuel required to launch module & its fuel"
	
	fuels = []
	fuels.append(mass // 3 - 2)

	additional_fuel = fuels[0] // 3 - 2
	while additional_fuel > 0:
		fuels.append(additional_fuel)
		additional_fuel = additional_fuel // 3 - 2

	return(sum(fuels))

def test():
	assert fuel_calc(14) == 2
	assert fuel_calc(1969) == 966
	assert fuel_calc(100756) == 50346

	print('Tests pass')

test()

answer = sum(fuel_calc(mass) for mass in data)
print(answer)