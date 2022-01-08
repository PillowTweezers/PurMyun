class Weights:
    def __init__(self, square: int, cross: int, parallel: int, tripod: int, anchoring: int, macrame: int, size: int):
        self.square = square
        self.cross = cross
        self.parallel = parallel
        self.tripod = tripod
        self.anchoring = anchoring
        self.macrame = macrame
        self.size = size

    def __init__(self):
        self.square = -1
        self.cross = -1
        self.parallel = -1
        self.tripod = -1
        self.anchoring = -1
        self.macrame = -1
        self.size = -1

    def __str__(self):
        return "Square: {}, Cross: {}, Parallel: {}, Tripod: {}, Anchoring: {}, Macrame: {}".format(self.square,
                                                                                                    self.cross,
                                                                                                    self.parallel,
                                                                                                    self.tripod,
                                                                                                    self.anchoring,
                                                                                                    self.macrame)
