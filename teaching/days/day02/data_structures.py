"""Day 2: predict each result, then run this file. No Pygame required.
A data structure organizes related values and defines how we access them.
"""
# Tuple: an ordered sequence whose entries cannot be replaced.
position = (200, 180)
print('Tuple:', position, 'x:', position[0], 'y:', position[1])
# position[0] = 250 would raise TypeError. Create a new tuple instead.
position = (250, position[1])
print('New tuple:', position)

# List: an ordered sequence whose entries can be changed, added or removed.
names = ['Scout', 'Cruiser']
names.append('Carrier')
print('List:', names, 'first:', names[0], 'count:', len(names))

# Dictionary: values accessed by unique keys, rather than numbered positions.
ship = {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True}
ship['x'] = ship['x'] + 40
print('Dictionary:', ship, 'x:', ship['x'])

# A list can hold dictionaries. It stores references to those records.
fleet = [ship, {'name': 'Cruiser', 'x': 500, 'y': 300, 'vertical': False}]
fleet[0]['x'] = 300
print('Nested access:', fleet[0]['name'], fleet[0]['x'])
print('Same record:', ship['x'])  # 300: ship refers to fleet[0]'s dictionary.

# Optional: a set stores distinct values, with no positional order.
targets = {(2, 3), (2, 3), (4, 1)}
print('Unique target count:', len(targets))  # 2; do not rely on print order.
print('Already tried (2, 3):', (2, 3) in targets)
print('Empty dictionary:', type({}).__name__, 'empty set:', type(set()).__name__)
