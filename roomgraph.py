class Queue:
  def __init__(self):
    self.queue = []
  def enqueue(self, value):
    self.queue.append(value)
  def dequeue(self):
    if self.size():
      return self.queue.pop(0)
    else:
      return None
  def size(self):
    return len(self.queue)


class Graph:
  def __init__(self):
    self.rooms = {}

  def add_room(self, room):
    self.rooms[room.id] = {}
    exits = room.get_exits()
    for exit in exits:
      self.rooms[room.id][exit] = '?'

  def connect_rooms(self, room_1, room_2, direction):
    self.rooms[room_1.id][direction] = room_2.id
    if room_2.id not in self.rooms:
      self.add_room(room_2)

    self.rooms[room_2.id][reverse_direction(direction)] = room_1.id

  def get_path_to_unvisited(self, room_id):
    q = Queue()
    q.enqueue(([room_id], []))
    visited = set()

    while q.size():
      rooms, path = q.dequeue()
      room = rooms[-1]

      if room not in visited:
        visited.add(room)
        exits = self.rooms[room]
        for (direction, exit) in exits.items():
          if exit == '?':
            return path
          elif exit in visited:
            continue
          exit_path = path + [direction]
          exit_rooms = rooms + [exit]
          q.enqueue((exit_rooms, exit_path))


def reverse_direction(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
    else:
        return None
