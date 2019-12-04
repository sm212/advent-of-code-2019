input_file = open('./input/03.txt')
input_data = input_file.read()
data = input_data.split('\n')
wire1, wire2 = data[0].split(','), data[1].split(',')

dir_x = {'L' : -1, 'R' : 1, 'U' : 0, 'D' : 0}
dir_y = {'L' : 0, 'R' : 0, 'U' : 1, 'D' : -1}

def get_points(wire):
	"Make a list of all points traced by a wire"

	x, y = 0, 0
	points = []
	for move in wire:
		direction = move[0]
		steps = int(move[1:])

		for step in range(steps):
			x += dir_x[direction]
			y += dir_y[direction]
			point = complex(x, y)
			points.append(point)

	return(points)

def min_intersection(wire1, wire2):
	"Finds the point of intersection closest to the origin"

	points1 = set(get_points(wire1))
	points2 = set(get_points(wire2))
	both = points1.intersection(points2)

	distances = [abs(p.real) + abs(p.imag) for p in both]
	return(min(distances))

def test():
	assert min_intersection('R8,U5,L5,D3'.split(','), 'U7,R6,D4,L4'.split(',')) == 6
	assert min_intersection('R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(','),
							'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')) == 159
	assert min_intersection('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(','),
							'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')) == 135

	print('Tests pass!')

test()

print(min_intersection(wire1, wire2))