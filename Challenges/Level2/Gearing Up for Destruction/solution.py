def solution(pegs):
	
	delta_pegs = [pegs[i+1] - pegs[i] for i in range(len(pegs) - 1)]
	alt_sum = 0
	for delta in delta_pegs:
		alt_sum = delta - alt_sum

	# odd pegs: rad = -2 * alt_sum
	# even pegs: rad = alt_sum * 2 / 3
	if len(pegs) % 2 != 0:
		rad = [alt_sum * -2, 1]
	else:
		# float.as_integer_ratio() didnt work
		if (alt_sum * 2) % 3 == 0:
			rad = [alt_sum * 2 / 3, 1]
		else:
			rad = [x * 2, 3]
			
	# Verify each peg is valid
	radii = [rad[0]/rad[1]]
	curr_rad = radii[0]
	for delta in delta_pegs:
		curr_rad = delta - curr_rad
		radii.append(curr_rad)
	if min(radii) < 1:
		return [-1, -1]
	return rad
