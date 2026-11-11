"""
maze will have this structure
maze={
    (x,y):
        {
        left:
        right:
        up:
        down:
        color:
        visited:
        },
}

"""


class Maze:
    def __init__(self,):

        self.maze={},
    
    
    def addTile(self,tile):
        self.maze[(tile.x,tile.y)]={
            "left":tile.left,
            "right":tile.right,
            "up":tile.up,
            "down":tile.down,
            "color":tile.color,
            "visited":tile.visited
            }
    def updateTile(self,tile):
        pass

    def getTile(self,tile):
        return self.maze[tile.x,tile.y]

    def updateMaze(self,sensorValues):
        pass
    