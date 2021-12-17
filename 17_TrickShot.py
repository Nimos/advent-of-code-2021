from aoc import get_input

import re

def get_trickshot(area):
    trajectories = []
    
    for x in range(0, area[1]+1):
        for y in range(area[2], 400):
            max_y = trajectory_in_area(x,y,*area)
            if max_y is not False:
                trajectories.append((x,y, max_y))
    
    return trajectories

def trajectory_in_area(vx, vy, x1, x2, y1, y2):
    pos_x = 0
    pos_y = 0
    
    max_y = 0

    while True:
        pos_x += vx 
        pos_y += vy   

        max_y = max(pos_y, max_y)

        if vx != 0:
            vx += 1 if vx < 0 else -1
        vy -= 1 

        if pos_x >= x1 and pos_x <= x2 and pos_y >= y1 and pos_y <= y2:
            return max_y
        elif pos_x > x2*2 or pos_y < y2*2:
            return False
        

if __name__ == "__main__":
    data = get_input(17, small=False)
    
    exp = re.compile("target area: x=([\-0-9]+)\.\.([\-0-9]+), y=([\-0-9]+)\.\.([\-0-9]+)")
    match = exp.match(data)
    area = [int(n) for n in match.groups()]

    trajectories = get_trickshot(area)

    print("Part 1:")
    print(max([t[2] for t in trajectories]))

    print("Part 2:")
    print(len(trajectories))