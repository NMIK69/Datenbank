import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

company_symbol_list = ["IBM", "TSLA", "MSFT", "AMZN", "AAPL"]
selection_symbol_list = ["open", "high", "low", "close", "volume"]


def graph_multiple(data, companies, selection):

    volume = [[] for x in range(5)]
    open = [[] for x in range(5)]
    close = [[] for x in range(5)]
    high = [[] for x in range(5)]
    low = [[] for x in range(5)]
    year = [[] for x in range(5)]
    month = [[] for x in range(5)]

    x_axis = [[] for x in range(5)]

    for x in data:
        if(x[2] == "IBM"):
            x_axis[0].append(x[0] + (1/12 * x[1]))
            volume[0].append(x[7])
            high[0].append(x[4])
            low[0].append(x[5])
            open[0].append(x[3])
            close[0].append(x[6])
            month[0].append(x[1])
            year[0].append(x[0])

        elif(x[2] == "TSLA"):
            x_axis[1].append(x[0] + (1/12 * x[1]))
            volume[1].append(x[7])
            high[1].append(x[4])
            low[1].append(x[5])
            open[1].append(x[3])
            close[1].append(x[6])
            month[1].append(x[1])
            year[1].append(x[0])

        elif(x[2] == "MSFT"):
            x_axis[2].append(x[0] + (1/12 * x[1]))
            volume[2].append(x[7])
            high[2].append(x[4])
            low[2].append(x[5])
            open[2].append(x[3])
            close[2].append(x[6])
            month[2].append(x[1])
            year[2].append(x[0])

        elif(x[2] == "AMZN"):
            x_axis[3].append(x[0] + (1/12 * x[1]))
            volume[3].append(x[7])
            high[3].append(x[4])
            low[3].append(x[5])
            open[3].append(x[3])
            close[3].append(x[6])
            month[3].append(x[1])
            year[3].append(x[0])

        elif(x[2] == "AAPL"):
            x_axis[4].append(x[0] + (1/12 * x[1]))
            volume[4].append(x[7])
            high[4].append(x[4])
            low[4].append(x[5])
            open[4].append(x[3])
            close[4].append(x[6])
            month[4].append(x[1])
            year[4].append(x[0])
    
    all_data = []
    all_data.append(open)
    all_data.append(high)
    all_data.append(low)
    all_data.append(close)
    all_data.append(volume)

    plt.style.use('fivethirtyeight')
    ax = plt.axes()


    for x in companies:
        for sel in selection:
            ax.plot(x_axis[x], all_data[sel][x], label=company_symbol_list[x]+" "+selection_symbol_list[sel])


    ax.xaxis.grid(True, which='minor')
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.tick_params(which='minor', width=5, length=10, color='r')


    ax.set_ylabel("Price in $")
    ax.set_xlabel("Date")

    plt.legend(loc="upper left")
    plt.show()


def graph_two(data, companies, selection):

    a = [[] for x in range(5)]
    b = [[] for x in range(5)]


    x_axis = [[] for x in range(5)]

    for x in data:
        if(x[2] == "IBM"):
            x_axis[0].append(x[0] + (1/12 * x[1]))
            a[0].append(x[3])
            b[0].append(x[4])


        elif(x[2] == "TSLA"):
            x_axis[1].append(x[0] + (1/12 * x[1]))
            a[1].append(x[3])
            b[1].append(x[4])


        elif(x[2] == "MSFT"):
            x_axis[2].append(x[0] + (1/12 * x[1]))
            a[2].append(x[3])
            b[2].append(x[4])

        elif(x[2] == "AMZN"):
            x_axis[3].append(x[0] + (1/12 * x[1]))
            a[3].append(x[3])
            b[3].append(x[4])

        elif(x[2] == "AAPL"):
            x_axis[4].append(x[0] + (1/12 * x[1]))
            a[4].append(x[3])
            b[4].append(x[4])
    

    plt.style.use('fivethirtyeight')
    ax = plt.axes()

    for x in companies:
        ax.plot(x_axis[x], a[x], label=company_symbol_list[x]+" "+selection_symbol_list[selection[0]])
        ax.plot(x_axis[x], b[x], label=company_symbol_list[x]+" "+selection_symbol_list[selection[1]])
        ax.fill_between(x_axis[x], a[x], b[x], alpha=0.25)


    ax.xaxis.grid(True, which='minor')
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.tick_params(which='minor', width=5, length=10, color='r')


    ax.set_ylabel("Price in $")
    ax.set_xlabel("Date")

    plt.legend(loc="upper left")
    plt.show()


def graph_single(data, companies, selection):

    a = [[] for x in range(5)]



    x_axis = [[] for x in range(5)]

    for x in data:
        if(x[2] == "IBM"):
            x_axis[0].append(x[0] + (1/12 * x[1]))
            a[0].append(x[4])
     

        elif(x[2] == "TSLA"):
            x_axis[1].append(x[0] + (1/12 * x[1]))
            a[1].append(x[4])


        elif(x[2] == "MSFT"):
            x_axis[2].append(x[0] + (1/12 * x[1]))
            a[2].append(x[4])

        elif(x[2] == "AMZN"):
            x_axis[3].append(x[0] + (1/12 * x[1]))
            a[3].append(x[4])

        elif(x[2] == "AAPL"):
            x_axis[4].append(x[0] + (1/12 * x[1]))
            a[4].append(x[4])
    


    plt.style.use('fivethirtyeight')
    ax = plt.axes()

    for x in companies:
        ax.plot(x_axis[x], a[x], label=company_symbol_list[x]+" "+selection_symbol_list[selection])


    ax.xaxis.grid(True, which='minor')
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.tick_params(which='minor', width=5, length=10, color='r')


    ax.set_ylabel("Price in $")
    ax.set_xlabel("Date")

    plt.legend(loc="upper left")
    plt.show()