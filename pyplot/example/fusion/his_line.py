import subprocess, sys
root_dir = subprocess.check_output("git rev-parse --show-toplevel", shell=True).rstrip()
sys.path.append(root_dir)

from src.bar_and_line_processor import BarAndLine

def plot():

    color1 = list()
    color1.append('#3F51B5')
    color1.append('#EF6C00')
    color2 = list()
    color2.append('#009688')
    color2.append('#4CAF50')
    color2.append('#424242')

    style = list()
    style.append('^')
    style.append('*')
    dp = BarAndLine(hdatFile = root_dir + '/data/bandwidth_com.dat',
            ldatFile = root_dir + '/data/delay_com.dat', 
            hclusterSize = 2, 
            lclusterSize = 2, 
            hyLimit = 400, 
            lyLimit = 80, 
            hlegend = ['RF-bandwidth', 'TT-bandwidth'],
            llegend=['RF-delay', 'TT-delay'],
            hylabel='bandwidth (Kbps)',
            lylabel='delay(s)',
            grid = True,
            color1 = color1,
            color2 = color2,
            marker = style,
            fontFamily = 'normal',
            fontWeight = 'normal',
            fontSize = 16,
            stdDev = False)

    dp.process()
    dp.plot()
    dp.show()

if __name__ == '__main__':
    plot()
