class Weights:
    def __init__(self, team_name="", square=-1, cross=-1, parallel=-1, tripod=-1, anchoring=-1, macrame=-1, size=-1):
        self.square = square
        self.cross = cross
        self.parallel = parallel
        self.tripod = tripod
        self.anchoring = anchoring
        self.macrame = macrame
        self.size = size
        self.name = team_name

    def __str__(self):
        return "Square: {}, Cross: {}, Parallel: {}, Tripod: {}, Anchoring: {}, Macrame: {}".format(self.square,
                                                                                                    self.cross,
                                                                                                    self.parallel,
                                                                                                    self.tripod,
                                                                                                    self.anchoring,
                                                                                                    self.macrame)
