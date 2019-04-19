import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class MultipleHisogram(object):

    def __init__(self, **kwargs):
        self.init_default_arg()

        for key in kwargs:
            if key is "datFile":
                self.datFile = kwargs[key]
            elif key is "clusterSize":
                self.N = kwargs[key]
                self.container = [[] for _ in range(self.N)]
                self.width = 0.7 / self.N 
            elif key is "yLimit":
                self.ylimit = kwargs[key]
            elif key is "legends":
                self.legends = kwargs[key]
            elif key is "ylabel":
                self.ylabel = kwargs[key]
            elif key is "grid":
                self.grid = kwargs[key]
            elif key is "share":
                self.share = kwargs[key]
            elif key is "color":
                self.color = kwargs[key]
            elif key is "fontFamily":
                self.fontFamily = kwargs[key]
            elif key is "fontWeight":
                self.fontWeight = kwargs[key]
            elif key is "fontSize":
                self.fontSize = kwargs[key]
            elif key is "stdDev":
                self.stdDev = kwargs[key]
                self.stdDevCont = [[] for _ in range(self.N)]
            elif key is "patterns":
                self.patterns = kwargs[key]
            elif key is "use_pattern":
                self.usePattern = kwargs[key]
            elif key is "legend_loc":
                self.legend_loc = kwargs[key]         
            else:
                raise Exception("Unknown attribute.")


    def init_default_arg(self):
        self.xticklabels = list()
        self.N = -1
        self.container = None
        self.width = -1
        self.ind = None
        self.datFile = None
        self.ylimit = 100
        self.legends = None
        self.ylabel = None
        self.grid = False
        self.fig = None
        self.color = None
        self.clusterNum = 0
        self.share = False
        self.color = None
        self.patterns = None
        self.usePattern = False

        self.fontFamily = 'normal'
        self.fontWeight = 'normal'
        self.fontSize = 12

        self.stdDev = False
        self.stdDevCont = None
        self.legend_loc = "upper right"


    def process(self):
        
        self.configureFont()

        dataIn = np.loadtxt(self.datFile, dtype=object)

        for line in dataIn:
            self.xticklabels.append(line[0])
            for i in xrange(1, self.N + 1):
                self.container[i - 1].append(float(line[i]))
            self.clusterNum += 1

            if self.stdDev:
                for i in xrange(self.N + 1, 2 * self.N + 1):
                    self.stdDevCont[i - self.N - 1].append(float(line[i]))

        self.ind = np.arange(self.clusterNum)  # the x locations for the groups


    def configureFont(self):
        font = {'family' : self.fontFamily,
                'weight' : self.fontWeight,
                'size'   : self.fontSize,
                # 'weight' : 'bold'
                }
        matplotlib.rc('font', **font)


    def plotSingle(self, ax, i):
        if self.N % 2 is 1:
            xpos = self.ind + (1 - self.N / 2 + i) * self.width
        else:
            xpos = self.ind + (1.5 - self.N / 2 + i) * self.width
        yerr = self.stdDevCont[i] if self.stdDev else None
        pattern = self.patterns[i] if self.usePattern else None
        ax.bar(xpos, self.container[i], self.width, label = self.legends[i], color=self.color[i], yerr = yerr, hatch = pattern, ecolor = "black")        


    def getFigandAx(self):
        return self.fig, self.ax

    def getHandleLabels(self):
        return self.ax.get_legend_handles_labels()

    def plot(self, fig = None, ax = None, handles = None, legends = None):
        if not self.share:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111)            
        else:
            self.fig = fig            
            self.ax = ax.twinx()

        self.ax.set_ylim([0, self.ylimit])
        self.ax.set_ylabel(self.ylabel)

        for i in xrange(0, self.N):
            self.plotSingle(self.ax, i)

        self.ax.set_xticks(self.ind+self.width*1.5)
        self.ax.set_xticklabels(self.xticklabels)    
        # self.ax.set_xticklabels(["None", "Vehicle type", "Vehicle type\nHideout", "Vehicle type\nHideout\nTarget type"])

        if self.grid:
            plt.grid(linestyle = '--', axis='y')            

        self.handles, self.legends = self.getHandleLabels() 

        if self.share:
            handles = handles + self.handles
            legends = legends + self.legends
        else:
            handles = self.handles
            legends = self.legends

        handles = [h[0] for h in handles] # remove the errorbars

        # plt.legend(handles, legends, loc='upper right')
        plt.legend(handles, legends, loc=self.legend_loc)
        self.ax.legend().set_visible(False)


    def show(self):
        plt.show()

