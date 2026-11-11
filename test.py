from maze import Maze
from pprint import pprint


maze= Maze()





# maze.update(distance_sensors.get_directional_distances(),x,y,direction,color.getColour())

maze.update(
    {
    "left": [0.03],
    "front":[0.23],
    "right":[0.10],
    "back": [0.10],
    }, 0,0,"front","red")
print()

# maze.update(
#         {
#     "left": [0.03],
#     "front":[0.22],
#     "right":[0.03],
#     "back": [0.10],
#     }, 0,0,"front","red"
# )

print(maze.exportMap())


# DIRS={
#     "left":{
#         "dirName":"left",
#         "oppositeName":"right",
#         "x":-1,
#         "y":0
#         },
        
#     "right":{
#         "dirName":"right",
#         "oppositeName":"left",
#         "x":1,
#         "y":0
#         },
#     "up":{
#         "dirName":"up",
#         "oppositeName":"down",
#         "x":0,
#         "y":1
#         },
#     "down":{
#         "dirName":"down",
#         "oppositeName":"up",
#         "x":0,
#         "y":-1
#         }
# }


# for dir in DIRS:
#     dir=DIRS[dir]
#     print(dir)
    