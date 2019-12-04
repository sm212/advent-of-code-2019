input_file = open('./input/03.txt')
input_data = input_file.read()
data = input_data.split('\n')
wire1, wire2 = data[0].split(','), data[1].split(',')

dir_x = {'L' : -1, 'R' : 1, 'U' : 0, 'D' : 0}
dir_y = {'L' : 0, 'R' : 0, 'U' : 1, 'D' : -1}

def get_distance(wire):
	"Make a dictionary of all points traced by a wire & the total number of steps from the origin"

	x, y, distance = 0, 0, 0
	points = {}
	for move in wire:
		direction = move[0]
		steps = int(move[1:])

		for step in range(steps):
			x += dir_x[direction]
			y += dir_y[direction]
			distance += 1

			point = complex(x, y)
			if point not in points:
				points[point] = distance

	return(points)

w1_distance = get_distance(wire1)
w2_distance = get_distance(wire2)

both = set(w1_distance.keys()).intersection(set(w2_distance.keys()))
print(min([w1_distance[p] + w2_distance[p] for p in both]))