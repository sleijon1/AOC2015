class Vehicle:
    def __init__(self, velocity, rest, bf_rest):
        self.active = 0
        self.velocity = velocity
        self.fatigue = None
        self.mileage = 0
        self.rest = rest
        self.before_rest = bf_rest
        self.points = 0
    def tick(self):
        if self.fatigue:
            self.fatigue -= 1
        else:
            self.mileage += self.velocity
            self.active += 1
            if self.active == self.before_rest:
                self.active = 0
                self.fatigue = self.rest


reindeers = []
with open("input.txt") as INP:
    lines = INP.readlines()
    for line in lines:
        split_line = line.split()
        speed, bf_rest, rest = \
            split_line[3], split_line[6], split_line[-2]
        reindeers.append(Vehicle(int(speed), int(rest), int(bf_rest)))


for _ in range(2503):
    for reindeer in reindeers:
        reindeer.tick()
        max_rd = max(reindeers, key=lambda r: r.mileage)
    max_rd.points += 1

max_rd = max(reindeers, key=lambda r: r.mileage)
max_rd_pts = max(reindeers, key=lambda r: r.points)
print(f"Solution part 1: {max_rd.mileage}")
print(f"Solution part 2: {max_rd_pts.points}")
