import tkinter as tk
from PIL import Image, ImageTk
from database_request import database_request
from graph import graph_multiple, graph_single, graph_two


def stock():
    data = []
    graph_mode = 0
    company_sel = []
    selection_sel = []

    for i in range(len(company_checkvars)):
        if(company_checkvars[i].get() == 1):
            company_sel.append(i)

            query = "select * from stocks where company=" + "'" + company_symbols[i] + "'" +  "order by year desc, month desc"#limit 100"
            data += database_request(query)


    for i in range(len(stock_checkvars) - 1):
        if(stock_checkvars[i].get() == 1):
            selection_sel.append(i)
            graph_mode += 1

    if(graph_mode == 1):
        graph_single(data, company_sel, selection_sel[0])
    
    elif(graph_mode == 2):
        graph_two(data, company_sel, selection_sel)

    elif(graph_mode > 2):
        graph_multiple(data, company_sel, selection_sel)
    


window = tk.Tk()
window.rowconfigure(10, minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], minsize=50, weight=1)
window.geometry("750x270")



company_symbols = ["IBM", "TSLA", "MSFT", "AMZN", "AAPL"]
company_checkvars = []
for i in range(5):
    company_checkvars.append(tk.IntVar())


option_symbols = ["Stocks"]
stock_checkvars = []
for i in range(6):
    stock_checkvars.append(tk.IntVar())


# left side companies start
lbl_companies_select = tk.Label(master=window, text="Select Companies")
lbl_companies_select.grid(row=0, column=2, sticky='nsew')

cbtn_ibm = tk.Checkbutton(window, text="IBM", variable=company_checkvars[0], onvalue=1, offvalue=0)
cbtn_ibm.grid(row=1, column=0)

cbtn_tsla = tk.Checkbutton(window, text="TSLA", variable=company_checkvars[1], onvalue=1, offvalue=0)
cbtn_tsla.grid(row=1, column=1)

cbtn_msft = tk.Checkbutton(window, text="MSFT", variable=company_checkvars[2], onvalue=1, offvalue=0)
cbtn_msft.grid(row=1, column=2)

cbtn_amzn = tk.Checkbutton(window, text="AMZN", variable=company_checkvars[3], onvalue=1, offvalue=0)
cbtn_amzn.grid(row=1, column=3)

cbtn_aapl = tk.Checkbutton(window, text="AAPL", variable=company_checkvars[4], onvalue=1, offvalue=0)
cbtn_aapl.grid(row=1, column=4)

btn_companies_show = tk.Button(master=window, text="Show", command=stock)
btn_companies_show.grid(row=5, column=3, sticky='nswe')


## stock select
lbl_action_select = tk.Label(master=window, text="Select Stock Data")
lbl_action_select.grid(row=3, column=2, sticky='nsew')

cbtn_open = tk.Checkbutton(window, text="open", variable=stock_checkvars[0], onvalue=1, offvalue=0)
cbtn_open.grid(row=5, column=2, sticky="w")

cbtn_close = tk.Checkbutton(window, text="close", variable=stock_checkvars[3], onvalue=1, offvalue=0)
cbtn_close.grid(row=6, column=2, sticky="w")

cbtn_high = tk.Checkbutton(window, text="high", variable=stock_checkvars[1], onvalue=1, offvalue=0)
cbtn_high.grid(row=7, column=2, sticky="w")

cbtn_low = tk.Checkbutton(window, text="low", variable=stock_checkvars[2], onvalue=1, offvalue=0)
cbtn_low.grid(row=8, column=2, sticky="w")

cbtn_volume = tk.Checkbutton(window, text="volume", variable=stock_checkvars[4], onvalue=1, offvalue=0)
cbtn_volume.grid(row=9, column=2, sticky="w")

cbtn_volume = tk.Checkbutton(window, text="volume", variable=stock_checkvars[4], onvalue=1, offvalue=0)
cbtn_volume.grid(row=9, column=2, sticky="w")


window.mainloop()
