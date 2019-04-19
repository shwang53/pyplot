import subprocess, sys
root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip()
sys.path.append(root_dir)

from src.multiple_line import MultipleLine
import matplotlib.pyplot as plt

def plot():

    # Initialize the style of histograms
    color = list()
    color.append('#3F51B5')
    color.append('#EF6C00')
    color.append('#009688')
    color.append('#4CAF50')
    color.append('#424242')
    color.append('#00AB00')
    style = list()
    style.append('^')
    style.append('*')
    style.append('x')
    style.append('+')
    style.append('O')
    style.append('|')

    # declare the processor
    dp = MultipleLine(datFile = root_dir + '/data/delay_com_stddev.dat', 
           clusterSize = 2,
           yLimit = 60,
           legends = ['RF', 'TT'],
           ylabel = 'delay (s)',
           grid = True,
           color = color,
           style = style,
           fontFamily = 'normal',
           fontWeight = 'normal',
           fontSize = 16,
           stdDev = True)

    dp.process()
    dp.plot()

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    dp.show()

if __name__ == '__main__':
    plot()
