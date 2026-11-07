"""棋盘规则：只使用 Python 数据，不依赖 Pygame。坐标为 (列, 行)。"""
import random

SIZE = 10
LENGTHS = {'Carrier': 4, 'Cruiser': 3, 'Scout': 2}


def cells(ship):
    """船的状态只有名字、起点和朝向，长度由规则决定。"""
    length = LENGTHS[ship['name']]
    return [(ship['x'] + (0 if ship['vertical'] else i),
             ship['y'] + (i if ship['vertical'] else 0)) for i in range(length)]


def can_place(fleet, ship, ignore=None):
    proposed = cells(ship)
    occupied = {p for s in fleet if s['name'] != ignore for p in cells(s)}
    return all(0 <= x < SIZE and 0 <= y < SIZE and (x, y) not in occupied
               for x, y in proposed)


def validate_fleet(fleet):
    if not isinstance(fleet, list) or len(fleet) != len(LENGTHS):
        raise ValueError('Place all three ships first.')
    checked = []
    for ship in fleet:
        if not isinstance(ship, dict) or ship.get('name') not in LENGTHS:
            raise ValueError('Unknown ship.')
        if any(s['name'] == ship['name'] for s in checked):
            raise ValueError('Duplicate ship.')
        if any(type(ship.get(k)) is not int for k in ('x', 'y')) or type(ship.get('vertical')) is not bool:
            raise ValueError('Invalid ship coordinates.')
        if not can_place(checked, ship):
            raise ValueError('Ships overlap or leave the board.')
        checked.append({k: ship[k] for k in ('name', 'x', 'y', 'vertical')})
    return checked


def random_fleet(rng=None):
    rng = rng or random
    fleet = []
    for name in LENGTHS:
        choices = [{'name': name, 'x': x, 'y': y, 'vertical': vertical}
                   for x in range(SIZE) for y in range(SIZE)
                   for vertical in (False, True)]
        choices = [s for s in choices if can_place(fleet, s)]
        fleet.append(rng.choice(choices))
    return fleet


def fire(fleet, shots, x, y):
    """成功才记录。shots 的键用字符串，便于 JSON 传输。"""
    if type(x) is not int or type(y) is not int or not (0 <= x < SIZE and 0 <= y < SIZE):
        raise ValueError('Aim inside the board.')
    key = f'{x},{y}'
    if key in shots:
        raise ValueError('Already fired here. Choose another cell.')
    ship = next((s for s in fleet if (x, y) in cells(s)), None)
    result = {'kind': 'miss', 'ship': None}
    if ship:
        result = {'kind': 'hit', 'ship': ship['name']}
        if all(f'{a},{b}' in shots or (a, b) == (x, y) for a, b in cells(ship)):
            result['kind'] = 'sunk'
    shots[key] = result
    return result


def statistics(shots):
    hits = sum(s['kind'] != 'miss' for s in shots.values())
    sunk = sum(s['kind'] == 'sunk' for s in shots.values())
    return {'shots': len(shots), 'hits': hits, 'sunk': sunk,
            'accuracy': round(100 * hits / len(shots)) if shots else 0,
            'score': hits * 10 + sunk * 50}
