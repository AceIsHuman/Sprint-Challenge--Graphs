from room import Room
from player import Player
from world import World
from roomgraph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
def get_unvisited(room, visited):
    exits = room.get_exits()
    return [e for e in exits if visited[room.id][e] == '?']

def generate_path(p):
    visited = Graph()
    path = []

    while len(visited.rooms) != len(room_graph):
        curr_room = p.current_room
        if curr_room.id not in visited.rooms:
            visited.add_room(curr_room)

        unvisited_exits = get_unvisited(curr_room, visited.rooms)

        if len(unvisited_exits) == 0:
            directions = visited.get_path_to_unvisited(curr_room.id)
            for direction in directions:
                p.travel(direction)
                path.append(direction)

        else:
            direction = random.choice(unvisited_exits)
            p.travel(direction)
            next_room = p.current_room

            path.append(direction)
            visited.connect_rooms(curr_room, next_room, direction)

    return path


# traversal_path = ['n', 'n']
traversal_path = generate_path(player)



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
