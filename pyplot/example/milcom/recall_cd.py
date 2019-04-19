import subprocess, sys
root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip()
sys.path.append(root_dir)

from src.multiple_line import MultipleLine
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def plot():

    markers = []
    for m in Line2D.markers:
        try:
            if len(m) == 1 and m != ' ':
                markers.append(m)
        except TypeError:
            pass

    # Initialize the style of histograms
    color = list()
    color.append('#3F51B5')
    color.append('#EF6C00')
    color.append('#009688')
    # color.append('#4CAF50')
    # color.append('#424242')
    # color.append('#00AB00')
    pattern_style = list()
    pattern_style.append(markers[0])
    pattern_style.append(markers[1])
    pattern_style.append(markers[3])
    # style.append('x')
    # style.append('+')
    # style.append('O')
    # style.append('|')
    line_style = list()
    line_style.append('-')
    line_style.append('--')
    line_style.append('-.')



    # declare the processor
    dp = MultipleLine(datFile = root_dir + '/data/milcom/recall(M3-M5).dat', 
           clusterSize = 3,
           yLimit = 1.0,
           legends = ['M-3', 'M-4', 'M-5'],           
           grid = True,
           color = color,
           pattern_style = pattern_style,
           line_style = line_style,
           fontFamily = 'normal',
           fontWeight = 'normal',
           fontSize = 22,
           stdDev = False,
           legend_loc = "top left"
           )

    dp.process()
    dp.plot()
    # plt.tick_params(axis='x', which='major', labelsize=18)
    plt.get_current_fig_manager().resize(1200 , 600)    
    plt.xlabel('Confidence level in delay prediction ($C_d$)', weight='bold')
    plt.ylabel('Recall', weight='bold')
    dp.show()

if __name__ == '__main__':
    plot()
