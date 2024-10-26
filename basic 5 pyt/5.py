from functools import reduce
rooms = [
{"name": "Kitchen", "length": 6, "width": 4},
{"name": "Room 1", "length": 5.5, "width": 4.5},
{"name": "Room 2", "length": 5, "width": 4},
{"name": "Room 3", "length": 7, "width": 6.3},
]

def calculate_area(room):
  return room ["length"] * room["width"]

areas = map(calculate_area, rooms)

total_area = reduce(lambda x, y: x + y, areas)

print(f"Общая плоащдь квартиры: {total_area:.2f} квад. метров")

  
