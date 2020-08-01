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

  def add_room(self, room_id, exits):
    self.rooms[room_id] = {}
    for exit in exits:
      self.rooms[room_id][exit] = '?'

  def connect_rooms(self, room_id_1, room_id_2, direction):
    self.rooms[room_id_1][direction] = room_id_2
    self.rooms[room_id_2][reverse_direction(direction)] = room_id_1

  def get_path_to_unvisited(self, room):
    q = Queue()
    q.enqueue(([room], []))
    while q.size():
      rooms, path = q.dequeue()
      room = rooms[-1]
      exits = self.rooms[room]
      for (direction, exit) in enumerate(exits):
        if exit == '?':
          return path + [direction]
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
