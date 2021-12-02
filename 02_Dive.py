from aoc import get_input


class Submarine(object):

    pos_x = 0
    pos_z = 0

    def forward(self, n):
        self.pos_x += n

    def up(self, n):
        self.pos_z -= n

    def down(self, n):
        self.pos_z += n

    def controls(self, data):
        data = data.split("\n")
        data = map(lambda line: line.split(" "), data)

        operations = {
            "forward": self.forward,
            "up": self.up,
            "down": self.down
        }

        for line in data:
            operations[line[0]](int(line[1]))
        
        return self.pos_x, self.pos_z, self.pos_x * self.pos_z

class AimSubmarine(Submarine):
    aim_z = 0
    def up(self, n):
        self.aim_z -= n

    def down(self, n):
        self.aim_z += n

    def forward(self, n):
        self.pos_x += n
        self.pos_z += n * self.aim_z

            
if __name__ == "__main__":
    data = get_input(2)
    
    print("Part 1:")
    submarine = Submarine()
    print(submarine.controls(data))

    print("Part 2:")
    submarine = AimSubmarine()
    print(submarine.controls(data))