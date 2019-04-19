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
    # color.append('#009688')
    # color.append('#4CAF50')
    # color.append('#424242')
    # color.append('#00AB00')
    pattern_style = list()
    pattern_style.append(markers[0])
    pattern_style.append(markers[1])
    # style.append('x')
    # style.append('+')
    # style.append('O')
    # style.append('|')
    line_style = list()
    line_style.append('-')
    line_style.append('--')



    # declare the processor
    dp = MultipleLine(datFile = root_dir + '/data/prefetch_delay.dat', 
           clusterSize = 2,
           yLimit = 35,
           legends = ['1Gbps', '10Mbps'],           
           grid = True,
           color = color,
           pattern_style = pattern_style,
           line_style = line_style,
           fontFamily = 'normal',
           fontWeight = 'normal',
           fontSize = 22,
           stdDev = False,
           legend_loc = "lower left"
           )

    dp.process()
    dp.plot()
    # plt.tick_params(axis='x', which='major', labelsize=18)
    plt.get_current_fig_manager().resize(1200 , 600)    
    plt.xlabel('Prefetch rate', weight='bold')
    plt.ylabel('Normalized delay(second)', weight='bold')
    dp.show()

if __name__ == '__main__':
    plot()
