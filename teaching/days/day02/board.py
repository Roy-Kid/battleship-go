"""Board rules using plain Python data, without Pygame. Coordinates: (column, row)."""

SIZE = 10
LENGTHS = {'Carrier': 4, 'Cruiser': 3, 'Scout': 2}


def cells(ship):
    """A ship stores its name, start cell and orientation; the rules determine its length."""
    length = LENGTHS[ship['name']]
    return [(ship['x'] + (0 if ship['vertical'] else i),
             ship['y'] + (i if ship['vertical'] else 0)) for i in range(length)]


def can_place(fleet, ship, ignore=None):
    proposed = cells(ship)
    occupied = {p for s in fleet if s['name'] != ignore for p in cells(s)}
    return all(0 <= x < SIZE and 0 <= y < SIZE and (x, y) not in occupied
               for x, y in proposed)
