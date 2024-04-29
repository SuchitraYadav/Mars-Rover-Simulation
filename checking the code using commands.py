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
