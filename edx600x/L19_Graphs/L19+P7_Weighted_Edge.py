class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return str(self.src)+ '->' +str(self.dest)+ ' (' +str(self.weight) + ')'