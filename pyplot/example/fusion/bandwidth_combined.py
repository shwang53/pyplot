import subprocess, sys
root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip()
sys.path.append(root_dir)

from src.multiple_histogram import MultipleHisogram

def plot():

    # Initialize the style of histograms
    color = list()
    color.append('#3F51B5')
    color.append('#EF6C00')
    color.append('#009688')
    color.append('#4CAF50')
    color.append('#424242')

    # Initialize the patterns of histograms
    patterns = ["/" , "o" , "|" , "*" , "+" , "x", "\\", "O", ".", "-"]

    # declare the processor
    dp = MultipleHisogram(datFile = root_dir + '/data/bandwidth_com_stddev.dat', 
           clusterSize = 2,
           yLimit = 400,
           legends = ['1Gbps', '10Mbps'],
           ylabel = 'bandwidth (MB)',
           grid = True,
           color = color,
           fontFamily = 'normal',
           fontWeight = 'normal',
           fontSize = 16,
           stdDev = True,
           patterns = patterns,
           use_pattern = True)

    dp.process()
    dp.plot()
    dp.show()

if __name__ == '__main__':
    plot()
