import subprocess, sys
root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip()
sys.path.append(root_dir)

from src.multiple_histogram import MultipleHisogram
import matplotlib.pyplot as plt

def plot():

    # Initialize the style of histograms
    color = list()    
    color.append('#3F51B5')
    color.append('#EF6C00')
    # color.append('#009688')
    # color.append('#4CAF50')
    # color.append('#424242')

    # Initialize the patterns of histograms
    patterns = ["/" , "." , "|" , "*" , "+" , "x", "o", ".", "-"]

    # declare the processor
    dp = MultipleHisogram(datFile = root_dir + '/data/anticipation_bw.dat', 
           clusterSize = 2,
           yLimit = 250,
           legends = ['1Gbps', '10Mbps'],
           # ylabel = 'Bandwidth (MB)',
           # xlabel = 'Scheduling algorithms',
           grid = True,
           color = color,
           fontFamily = 'normal',
           fontWeight = 'normal',
           fontSize = 22,
           stdDev = False,
           patterns = patterns,
           use_pattern = True,
           legend_loc = "upper right"
           )

    dp.process()
    dp.plot()    
    # plt.tick_params(axis='x', which='major', labelsize=18)        
    plt.get_current_fig_manager().resize(1200 , 600)
    # plt.tight_layout()  
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.xlabel('Correct hints', weight='bold')
    plt.ylabel('Bandwidth consumption(MB)', weight='bold')      
    dp.show()

if __name__ == '__main__':
    plot()
