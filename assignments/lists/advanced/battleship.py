# Possible improvements
# - Validate input can be parsed (coordinates, orientations)
# - Validate that input satisfies game constraints (coordinates within grid, no ships overlap, ships within grid)
# - Make this a humans vs computer game

SHIPS_AND_SIZES = (
    ("carrier", 5),
    ("battleship", 4),
    ("destroyer", 3),
    ("submarine", 3),
    ("patrol boat", 2),
)


def get_occupied_tiles(coordinate: str, orientation: str, size: int) -> list:
    row = coordinate[0].upper()
    column = int(coordinate[1:])
    if orientation.lower() == "horizontal":
        return [f"{row}{c}" for c in range(column, column + size)]
    elif orientation.lower() == "vertical":
        start_index = ord(row)
        return [f"{chr(r)}{column}" for r in range(start_index, start_index + size)]
    else:
        raise ValueError(orientation + " is not a recognized orientation")


def gather_fleet_positions() -> list:
    print(
        "Specify the location of each ship in your fleet by providing the top/left coordinate and orientation."
    )
    print("Examples: 'A2 vertical' or 'C3 horizontal'")
    positions = []
    for ship, size in SHIPS_AND_SIZES:
        location = input(f"Location and orientation of your {ship}: ")
        coordindate, orientation = location.split()
        occupied_tiles = get_occupied_tiles(coordindate, orientation, size)
        positions.append((ship, occupied_tiles, []))
    return positions


def is_afloat(ship: tuple) -> bool:
    name, occupied_tiles, hits = ship
    for tile in occupied_tiles:
        if tile not in hits:
            return True
    return False


def something_is_still_afloat(fleet: list) -> bool:
    for ship in fleet:
        if is_afloat(ship):
            return True
    return False


def ask_where_to_attack() -> str:
    coordinate = input("Where to attack: ")
    return coordinate.strip().upper()


def hit_test(ship: tuple, coordinate: str) -> bool:
    name, occupied_tiles, hits = ship
    for tile in occupied_tiles:
        if coordinate == tile:
            return True
    return False


def get_ship_at(coordinate: str, fleet: list):
    for ship in fleet:
        if hit_test(ship, coordinate):
            return ship
    return None


def report_hit(ship: tuple, coordinate: str):
    name, occupied_tiles, hits = ship
    hits.append(coordinate)
    if is_afloat(ship):
        print(f"Hit, {name}")
    else:
        print(f"You have sunk my {name}")


def report_miss():
    print("Miss")


fleet = gather_fleet_positions()
while something_is_still_afloat(fleet):
    coordinate = ask_where_to_attack()
    ship = get_ship_at(coordinate, fleet)
    if ship:
        report_hit(ship, coordinate)
    else:
        report_miss()

print("The entire fleet has been sunk")
