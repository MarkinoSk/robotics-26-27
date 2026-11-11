import config
import json

DIRS={
    "left":{
        "dirName":"left",
        "oppositeName":"right",
        "x":-1,
        "y":0
        },
        
    "right":{
        "dirName":"right",
        "oppositeName":"left",
        "x":1,
        "y":0
        },
    "front":{
        "dirName":"front",
        "oppositeName":"back",
        "x":0,
        "y":1
        },
    "back":{
        "dirName":"back",
        "oppositeName":"front",
        "x":0,
        "y":-1
        }
}


class Maze:
    def __init__(self,):

        self.maze={}
    
    

    def addTile(self,x,y,noWall=[],colour=None,visited=False):
        self.maze[(x,y)]={
            "colour":colour,
            "visited":visited,
            "created":True
            }
        for wall in noWall:
            self.maze[(x,y)].setdefault(wall,False)

        
        return self.maze[(x,y)]
        
    def updateTile(self,tile):
        pass

    def getMaze(self):
        return self.maze

    def exportMap(self):
        return json.dumps([
            {"x": x, "y": y, **data}
            for (x, y), data in self.maze.items()
        ])

    def getTile(self,x,y):
        return self.maze.get((x, y), {"created": False})

    def checkWalls(self,sensorValues,x,y,direction):
        thisTile=self.getTile(x,y)
        
        for dirName in DIRS:
            dir=DIRS[dirName]
            if sensorValues[dir["dirName"]][0]>config.FIRST_WALL_DISTANCE_THRESHOLD:
                #nieje scena
                thisTile[dir["dirName"  ]]=False

                #chcek tile there
                closeX=x+dir["x"]
                closeY=y+dir["y"]

                if not self.getTile(closeX,closeY)["created"]:
                    #create side tile
                    closeTile=self.addTile(closeX,closeY,[dir["oppositeName"]])
                
                elif not self.getTile(closeX,closeY)["visited"]: 
                    if sensorValues[dir["dirName"]][0]<config.SECOND_WALL_DISTANCE_THRESHOLD:
                        closeTile.setdefault(dir["oppositeName"],True)
                    else:#vidim este do dalsej tile

                        farTileX=x+dir["x"]*2
                        farTileY=y+dir["y"]*2
                        print("A")
                        if not self.getTile(farTileX,farTileY)["created"]:
                            #vytvor
                            print("B")
                            farTile=self.addTile(farTileX,farTileY,[dir["oppositeName"]])
                        elif not self.getTile(farTileX,farTileY)["visited"]:
                            farTile.setdefault(dir["oppositeName"],False)
                        else:
                            #farTile bola navstivena
                            pass
                else:
                    #closeTile bola navstivena
                    pass
            else:
                #je stena
                thisTile[dir["dirName"]]=True



    def update(self,sensorValues,x,y,direction,colour):

        if self.getTile(x,y)["created"]: 
            
            if not self.getTile(x,y)["visited"]:
                #navstivena #nic nerob
                return
            else:
                #thisvytvorena nenavstivena
                self.checkWalls(sensorValues,x,y,direction)
                pass

        else:
            #this nevytvorena
            thisTile=self.addTile(x,y,[],colour,True)

            self.checkWalls(sensorValues,x,y,direction)
            

                        


