from bitarray import bitarray

class ShiftBitarray(bitarray):
    """ extension to support << >> operators """
    def __lshift__(self, count):
        return self[count:] + type(self)('0') * count

    def __rshift__(self, count):
        return type(self)('0') * count + self[:-count]

    def __repr__(self):
        return "{}('{}')".format(type(self).__name__, self.to01())


def execute_instructions(registers={}, override=False):
    queue = []
    with open("input.txt") as INP:
        for line in INP.read().splitlines():
            op, dest = line.split('->')
            lh = op.strip(' ').split(' ')
            queue.append([lh, dest.strip(' ')])
    while queue:
        curr = queue[0]
        lh, dest = curr
        queue.pop(0)
        try:
            if len(lh) == 1:
                try:
                    if override and dest == 'b':
                        pass
                    else:
                        registers[dest] = ShiftBitarray(format(int(lh[0]), '016b'))
                except ValueError:
                    registers[dest] = registers[lh[0]]
            elif len(lh) == 3:
                if lh[1] == 'AND':
                    left, right = registers[lh[0]], registers[lh[2]]
                    registers[dest] = left & right
                elif lh[1] == 'OR':
                    left, right = registers[lh[0]], registers[lh[2]]
                    registers[dest] = left | right
                elif lh[1] == 'LSHIFT':
                    left, right = registers[lh[0]], int(lh[2])
                    registers[dest] = left << right
                elif lh[1] == 'RSHIFT':
                    left, right = registers[lh[0]], int(lh[2])
                    registers[dest] = left >> right
            elif len(lh) == 2:
                registers[dest] = ~registers[lh[1]]
        except KeyError:
            try:
                registers[lh[0]] = ShiftBitarray(format(int(lh[0]), '016b'))
            except ValueError:
                pass
            queue.append(curr)
    return registers


registers_01 = execute_instructions()
registers = {key: int(val.to01(), 2) for key, val in registers_01.items()}
print(f"Solution part 1: {registers['a']}")
registers_01_2 = execute_instructions(
    {'b': ShiftBitarray(format(int(registers['a']), '016b'))}, True)
registers_2 = {key: int(val.to01(), 2) for key, val in registers_01_2.items()}
print(f"Solution part 2: {registers_2['a']}")
