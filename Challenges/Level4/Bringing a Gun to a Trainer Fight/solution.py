from math import sqrt, ceil, floor, atan2

def in_range(point, origin, distance):
    return sqrt(((point[0] - origin[0]) ** 2) + ((point[1] - origin[1]) ** 2)) <= distance
    
def get_dist(point):
    return sqrt((point[0] ** 2) + (point[1] ** 2))
    
def mirror(dimensions, your_position, trainer_position, distance):
    num_mirror_x = int(ceil((your_position[0] + distance + 1)/dimensions[0]))
    num_mirror_y = int(ceil((your_position[1] + distance + 1)/dimensions[1]))
    first_quad= []
    left = [your_position[0], trainer_position[0]]
    right = [dimensions[0] - your_position[0], dimensions[0] - trainer_position[0]]
    down = [your_position[1], trainer_position[1]]
    up = [dimensions[1] - your_position[1], dimensions[1] - trainer_position[1]]
    for i in range(num_mirror_x+1):
        l, r  = 2 * floor(float(i)/2), 2 * ceil(float(i)/2)
        left_player = l * left[0]
        right_player = r * right[0]
        left_target = l * left[1]
        right_target = r * right[1]
        for j in range(num_mirror_y+1):
            u, d = 2 * ceil(float(j)/2), 2 * floor(float(j)/2)
            up_player = u * up[0]
            down_player = d * down[0]
            up_target = u * up[1]
            down_target = d * down[1]
            new_player = [your_position[0] + left_player + right_player, your_position[1] + up_player + down_player]
            new_target =[trainer_position[0] + left_target + right_target, trainer_position[1] + up_target + down_target]
            first_quad.append([new_player[0], new_player[1], 0])
            first_quad.append([new_target[0], new_target[1], 1])
    return first_quad

def reflect(first_quad, src, distance):
    reflections = []
    for point in first_quad:
        x, y, t = point[0], point[1], point[2]
        if in_range([x,y], src, distance):
            reflections.append([x-src[0], y-src[1], t])
        if in_range([-x,y], src, distance):
            reflections.append([-x-src[0], y-src[1], t])
        if in_range([-x,-y], src, distance):
            reflections.append([-x-src[0], -y-src[1], t])
        if in_range([x,-y], src, distance):
            reflections.append([x-src[0], -y-src[1], t])
    return (reflections[1:])

def get_count(points):
    count = 0
    angles = {}
    for point in points:
        dist = get_dist(point)
        angle = atan2(point[1], point[0])
        if angle not in angles:
            angles[angle] = [point, dist]
        elif dist  < angles[angle][1]:
            angles[angle] = [point, dist]
            
    for angle in angles:
        count += angles[angle][0][2]
                        
    return count
    
def solution(dimensions, your_position, trainer_position, distance):
    first_quad = mirror(dimensions, your_position, trainer_position, distance)
    points = reflect(first_quad, your_position, distance)
    return get_count(points)
