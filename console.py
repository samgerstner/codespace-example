from toh import toh


def console():
    """call toh from console"""
    try:
        print()
        discs_to_move = int(input("How many disks do you want to move?"))
    except ValueError:
        print()
        print("discCount is not a number... defaulting to 3")
        discs_to_move = 3

    print()
    print("Moving", discs_to_move, "discs from rod A to rod C", end="\n\n")
    steps = []
    toh(steps, discs_to_move, 'A', 'C', 'B')
    for __, step in enumerate(steps):
        print("Move disc", step[0], "from rod", step[1], "to rod", step[2])

    print(steps)


console()
