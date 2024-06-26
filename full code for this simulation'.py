# Command Pattern: Define commands as objects
class Command:
    def execute(self, rover):
        pass

class MoveCommand(Command):
    def execute(self, rover):
        rover.move()

class TurnLeftCommand(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRightCommand(Command):
    def execute(self, rover):
        rover.turn_right()

# Rover class
class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

# Composite Pattern: Create a Grid class to represent the grid and obstacles
class Grid:
    def __init__(self, size_x, size_y, obstacles):
        self.size_x = size_x
        self.size_y = size_y
        self.obstacles = obstacles

    def is_obstacle_at(self, x, y):
        return (x, y) in self.obstacles

# Client code
def main():
    grid = Grid(10, 10, [(2, 2), (3, 5)])
    rover = Rover(0, 0, 'N')

    commands = ['M', 'M', 'R', 'M', 'L', 'M']

    for command_char in commands:
        if command_char == 'M':
            command = MoveCommand()
        elif command_char == 'L':
            command = TurnLeftCommand()
        elif command_char == 'R':
            command = TurnRightCommand()

        # Check for obstacle before executing the command
        new_x, new_y = rover.x, rover.y
        if command_char == 'M':
            if rover.direction == 'N':
                new_y += 1
            elif rover.direction == 'S':
                new_y -= 1
            elif rover.direction == 'E':
                new_x += 1
            elif rover.direction == 'W':
                new_x -= 1

            if grid.is_obstacle_at(new_x, new_y):
                print("Obstacle detected. Rover cannot move.")
                continue

        command.execute(rover)

    # Print final position and status report
    print(f"Final Position: ({rover.x}, {rover.y}, {rover.direction})")
    print("Status Report: Rover is at ({}, {}) facing {}. No Obstacles detected.".format(rover.x, rover.y, rover.direction))

if __name__ == "__main__":
    main()
