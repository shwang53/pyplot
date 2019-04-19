from multiple_histogram import MultipleHisogram 
from multiple_line import MultipleLine

class BarAndLine(object):
    def __init__(self, hdatFile, ldatFile, hclusterSize, lclusterSize, hyLimit, lyLimit, hlegend, llegend, hylabel, lylabel, grid, color1, color2, marker, fontFamily, fontWeight, fontSize, stdDev):
        self.dp = MultipleHisogram(datFile = hdatFile,
               clusterSize = hclusterSize,
               yLimit = hyLimit,
               legends = hlegend,
               ylabel = hylabel,
               grid = grid,
               share = False,
               color = color1,
               fontFamily = fontFamily,
               fontWeight = fontWeight,
               fontSize = fontSize,
               stdDev = stdDev)

        self.dp1 = MultipleLine(datFile = ldatFile,
               clusterSize = lclusterSize,
               yLimit = lyLimit,
               legends = llegend,
               ylabel = lylabel,
               grid = grid,
               share = True,
               color = color2,
               style = marker,
               fontFamily = fontFamily,
               fontWeight = fontWeight,
               fontSize = fontSize,
               stdDev = stdDev)

    def process(self):
        self.dp.process()
        self.dp1.process()

    def plot(self):
        self.dp.plot()
        fig, ax = self.dp.getFigandAx()
        handles, legends = self.dp.getHandleLabels()
        self.dp1.plot(fig, ax, handles, legends)

    def show(self):
        self.dp.show()
