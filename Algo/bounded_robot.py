class BoundedRobot:
    _offset_left = {
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0),
        (1, 0): (0, 1),
    }

    _offset_right = {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }

    def is_bounded(self, instructions: str) -> bool:
        current_x = 0
        current_y = 0
        current_offset = (0, 1)

        for i in instructions:
            if i == 'G':
                current_x += current_offset[0]
                current_y += current_offset[1]
            elif i == 'L':
                current_offset = self._offset_left.get(current_offset)
            elif i == 'R':
                current_offset = self._offset_right.get(current_offset)
        if current_x == 0 and current_y == 0:
            return True
        # If offset doesn't change after following instructions once,
        # then it will never return.
        elif current_offset == (0, 1):
            return False
        return True


if __name__ == '__main__':
    ins1 = 'GGLLGG'
    ins2 = 'GL'
    ins3 = 'GLR'
    robot = BoundedRobot()
    print('ins1', robot.is_bounded(ins1))
    print('ins2', robot.is_bounded(ins2))
    print('ins3', robot.is_bounded(ins3))
