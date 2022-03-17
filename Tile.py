class Tile:
    def __init__(self, terrain, move_cost, Unit):
        """
            The coordinates of a tile are its x and y indexes of the 2D map array
        """
        self.terrain = terrain
        self.move_cost = move_cost
        self.Unit = Unit
