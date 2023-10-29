# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
from tkinter import *

import suricate_graphs as graph_data_func


LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "Interface1")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SP500, SP500Mini, DowJones, DowJonesMini, NASDAQ, NASDAQMini, RUSSEL2000, NIKKEI, VIX, YearBond, YearNote, YearNote, YearNote, FederalFunds, UltraUSTBonds, Ultra10yearUSTNotes, BitCoin, Euro, AustralischerDollar, BrasilianischerReal, BritischesPfund, JapanischerYen, KanadischerDollar, MexikanischerPeso, NeuseelandDollar, RussischerRubel, SchweizerFranken, MonateEuroDollar, USDollarIndex, Gold, Silber, Platin, Palladium, Kupfer, Aluminium, Stahl, Kohle, RoholWTI, Benzin, Heizol, Erdgas, Ethanol, ChicagoEthanol, Mais, WeizenSRW, WeizenHRW, Reis, Hafer, Sojabohnen, SojabohnenMehl, Sojabohnenol, Raps, Kakao, Baumwolle, Orangensaft, Kaffee, Zucker, Bauholz, Lebendrind, Mastrind, Magerschwein, Butter, FettarmeMilch, MilchIII, MilchIV, Kase):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=2, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="S&P 500",
                            command=lambda: controller.show_frame(SP500))
        button.place(x=0, y=0)


        button = ttk.Button(self, text="S&P 500 Mini",
                            command=lambda: controller.show_frame(SP500Mini))
        button.place(x=100, y=0)


        button = ttk.Button(self, text="Dow Jones",
                            command=lambda: controller.show_frame(DowJones))
        button.place(x=200, y=0)


        button = ttk.Button(self, text="Dow Jones Mini",
                            command=lambda: controller.show_frame(DowJonesMini))
        button.place(x=300, y=0)


        button = ttk.Button(self, text="NASDAQ",
                            command=lambda: controller.show_frame(NASDAQ))
        button.place(x=400, y=0)


        button = ttk.Button(self, text="NASDAQ Mini",
                            command=lambda: controller.show_frame(NASDAQMini))
        button.place(x=0, y=40)


        button = ttk.Button(self, text="RUSSEL 2000",
                            command=lambda: controller.show_frame(RUSSEL2000))
        button.place(x=100, y=40)


        button = ttk.Button(self, text="NIKKEI",
                            command=lambda: controller.show_frame(NIKKEI))
        button.place(x=200, y=40)


        button = ttk.Button(self, text="VIX",
                            command=lambda: controller.show_frame(VIX))
        button.place(x=300, y=40)


        button = ttk.Button(self, text="30 Year Bond",
                            command=lambda: controller.show_frame(YearBond))
        button.place(x=400, y=40)

        button = ttk.Button(self, text="2 Year Note",
                            command=lambda: controller.show_frame(YearNote))
        button.place(x=0, y=80)


        button = ttk.Button(self, text="5 Year Note",
                            command=lambda: controller.show_frame(YearNote))
        button.place(x=100, y=80)



        button = ttk.Button(self, text="10 Year Note",
                            command=lambda: controller.show_frame(YearNote))
        button.place(x=200, y=80)


        button = ttk.Button(self, text="Federal Funds",
                            command=lambda: controller.show_frame(FederalFunds))
        button.place(x=300, y=80)


        button = ttk.Button(self, text="Ultra U.S. T-Bonds",
                            command=lambda: controller.show_frame(UltraUSTBonds))
        button.place(x=400, y=80)


        button = ttk.Button(self, text="Ultra 10-year U.S. T-Notes",
                            command=lambda: controller.show_frame(Ultra10yearUSTNotes))
        button.place(x=0, y=120)


        button = ttk.Button(self, text="BitCoin",
                            command=lambda: controller.show_frame(BitCoin))
        button.place(x=100, y=120)


        button = ttk.Button(self, text="Euro",
                            command=lambda: controller.show_frame(Euro))
        button.place(x=200, y=120)


        button = ttk.Button(self, text="Australischer Dollar",
                            command=lambda: controller.show_frame(AustralischerDollar))
        button.place(x=300, y=120)


        button = ttk.Button(self, text="Brasilianischer Real",
                            command=lambda: controller.show_frame(BrasilianischerReal))
        button.place(x=400, y=120)


        button = ttk.Button(self, text="Britisches Pfund",
                            command=lambda: controller.show_frame(BritischesPfund))
        button.place(x=0, y=160)


        button = ttk.Button(self, text="Japanischer Yen",
                            command=lambda: controller.show_frame(JapanischerYen))
        button.place(x=100, y=160)


        button = ttk.Button(self, text="Kanadischer Dollar",
                            command=lambda: controller.show_frame(KanadischerDollar))
        button.place(x=200, y=160)


        button = ttk.Button(self, text="Mexikanischer Peso",
                            command=lambda: controller.show_frame(MexikanischerPeso))
        button.place(x=300, y=160)


        button = ttk.Button(self, text="Neuseeland Dollar",
                            command=lambda: controller.show_frame(NeuseelandDollar))
        button.place(x=400, y=160)


        button = ttk.Button(self, text="Russischer Rubel",
                            command=lambda: controller.show_frame(RussischerRubel))
        button.place(x=0, y=200)


        button = ttk.Button(self, text="Schweizer Franken",
                            command=lambda: controller.show_frame(SchweizerFranken))
        button.place(x=100, y=200)


        button = ttk.Button(self, text="3 Monate Euro Dollar",
                            command=lambda: controller.show_frame(MonateEuroDollar))
        button.place(x=200, y=200)


        button = ttk.Button(self, text="U.S. Dollar Index",
                            command=lambda: controller.show_frame(USDollarIndex))
        button.place(x=300, y=200)


        button = ttk.Button(self, text="Gold",
                            command=lambda: controller.show_frame(Gold))
        button.place(x=400, y=200)


        button = ttk.Button(self, text="Silber",
                            command=lambda: controller.show_frame(Silber))
        button.place(x=0, y=240)


        button = ttk.Button(self, text="Platin",
                            command=lambda: controller.show_frame(Platin))
        button.place(x=100, y=240)


        button = ttk.Button(self, text="Palladium",
                            command=lambda: controller.show_frame(Palladium))
        button.place(x=200, y=240)


        button = ttk.Button(self, text="Kupfer",
                            command=lambda: controller.show_frame(Kupfer))
        button.place(x=300, y=240)


        button = ttk.Button(self, text="Aluminium",
                            command=lambda: controller.show_frame(Aluminium))
        button.place(x=400, y=240)


        button = ttk.Button(self, text="Stahl",
                            command=lambda: controller.show_frame(Stahl))
        button.place(x=0, y=280)


        button = ttk.Button(self, text="Kohle",
                            command=lambda: controller.show_frame(Kohle))
        button.place(x=100, y=280)


        button = ttk.Button(self, text="Rohöl WTI",
                            command=lambda: controller.show_frame(RoholWTI))
        button.place(x=200, y=280)


        button = ttk.Button(self, text="Benzin",
                            command=lambda: controller.show_frame(Benzin))
        button.place(x=300, y=280)


        button = ttk.Button(self, text="Heizöl",
                            command=lambda: controller.show_frame(Heizol))
        button.place(x=400, y=280)


        button = ttk.Button(self, text="Erdgas",
                            command=lambda: controller.show_frame(Erdgas))
        button.place(x=0, y=320)


        button = ttk.Button(self, text="Ethanol",
                            command=lambda: controller.show_frame(Ethanol))
        button.place(x=100, y=320)


        button = ttk.Button(self, text="Chicago Ethanol",
                            command=lambda: controller.show_frame(ChicagoEthanol))
        button.place(x=200, y=320)


        button = ttk.Button(self, text="Mais",
                            command=lambda: controller.show_frame(Mais))
        button.place(x=300, y=320)


        button = ttk.Button(self, text="Weizen SRW",
                            command=lambda: controller.show_frame(WeizenSRW))
        button.place(x=400, y=320)


        button = ttk.Button(self, text="Weizen HRW",
                            command=lambda: controller.show_frame(WeizenHRW))
        button.place(x=0, y=360)


        button = ttk.Button(self, text="Reis",
                            command=lambda: controller.show_frame(Reis))
        button.place(x=100, y=360)


        button = ttk.Button(self, text="Hafer",
                            command=lambda: controller.show_frame(Hafer))
        button.place(x=200, y=360)


        button = ttk.Button(self, text="Sojabohnen",
                            command=lambda: controller.show_frame(Sojabohnen))
        button.place(x=300, y=360)


        button = ttk.Button(self, text="Sojabohnen Mehl",
                            command=lambda: controller.show_frame(SojabohnenMehl))
        button.place(x=400, y=360)


        button = ttk.Button(self, text="Sojabohnen Öl",
                            command=lambda: controller.show_frame(Sojabohnenol))
        button.place(x=0, y=400)


        button = ttk.Button(self, text="Raps",
                            command=lambda: controller.show_frame(Raps))
        button.place(x=100, y=400)


        button = ttk.Button(self, text="Kakao",
                            command=lambda: controller.show_frame(Kakao))
        button.place(x=200, y=400)


        button = ttk.Button(self, text="Baumwolle",
                            command=lambda: controller.show_frame(Baumwolle))
        button.place(x=300, y=400)


        button = ttk.Button(self, text="Orangensaft",
                            command=lambda: controller.show_frame(Orangensaft))
        button.place(x=400, y=400)


        button = ttk.Button(self, text="Kaffee",
                            command=lambda: controller.show_frame(Kaffee))
        button.place(x=0, y=440)


        button = ttk.Button(self, text="Zucker",
                            command=lambda: controller.show_frame(Zucker))
        button.place(x=100, y=440)


        button = ttk.Button(self, text="Bauholz",
                            command=lambda: controller.show_frame(Bauholz))
        button.place(x=200, y=440)


        button = ttk.Button(self, text="Lebendrind",
                            command=lambda: controller.show_frame(Lebendrind))
        button.place(x=300, y=440)


        button = ttk.Button(self, text="Mastrind",
                            command=lambda: controller.show_frame(Mastrind))
        button.place(x=400, y=440)


        button = ttk.Button(self, text="Magerschwein",
                            command=lambda: controller.show_frame(Magerschwein))
        button.place(x=0, y=480)


        button = ttk.Button(self, text="Butter",
                            command=lambda: controller.show_frame(Butter))
        button.place(x=100, y=480)


        button = ttk.Button(self, text="Fettarme Milch",
                            command=lambda: controller.show_frame(FettarmeMilch))
        button.place(x=200, y=480)


        button = ttk.Button(self, text="Milch III",
                            command=lambda: controller.show_frame(MilchIII))
        button.place(x=300, y=480)


        button = ttk.Button(self, text="Milch IV",
                            command=lambda: controller.show_frame(MilchIV))
        button.place(x=400, y=480)


        button = ttk.Button(self, text="Käse",
                            command=lambda: controller.show_frame(Kase))
        button.pack(side = BOTTOM)


class Gold(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Gold", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        gold_data = graph_data_func.build_graph(name='Gold')

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(gold_data[2], gold_data[3])
        cursor1 = FollowDotCursor(a[1], gold_data[2], gold_data[3])
        a[0].plot(gold_data[0], gold_data[1])
        cursor1 = FollowDotCursor(a[0], gold_data[0], gold_data[1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class SP500(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="S&P 500", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='S&P 500')
        except Exception as e:
            print(e, 'S&P 500')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)

        a[1].set_xticks(graph_data[2], graph_data[4])
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        cursor1 = FollowDotCursor(a[1], gold_data[2], gold_data[3])

        a[0].set_xticks(graph_data[0], graph_data[5])
        a[0].plot(graph_data[0], graph_data[1], label ='cs')
        cursor1 = FollowDotCursor(a[0], gold_data[0], gold_data[1])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class SP500Mini(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="S&P 500 Mini", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='S&P 500 Mini')
        except Exception as e:
            print(e, 'S&P 500 Mini')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class DowJones(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dow Jones", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Dow Jones')
        except Exception as e:
            print(e, 'Dow Jones')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class DowJonesMini(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Dow Jones Mini", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Dow Jones Mini')
        except Exception as e:
            print(e, 'Dow Jones Mini')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class NASDAQ(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NASDAQ", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='NASDAQ')
        except Exception as e:
            print(e, 'NASDAQ')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class NASDAQMini(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NASDAQ Mini", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='NASDAQ Mini')
        except Exception as e:
            print(e, 'NASDAQ Mini')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class RUSSEL2000(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="RUSSEL 2000", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='RUSSEL 2000')
        except Exception as e:
            print(e, 'RUSSEL 2000')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class NIKKEI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="NIKKEI", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='NIKKEI')
        except Exception as e:
            print(e, 'NIKKEI')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class VIX(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="VIX", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='VIX')
        except Exception as e:
            print(e, 'VIX')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class YearBond(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="30 Year Bond", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='30 Year Bond')
        except Exception as e:
            print(e, '30 Year Bond')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class YearNote(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="2 Year Note", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='2 Year Note')
        except Exception as e:
            print(e, '2 Year Note')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class YearNote(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="5 Year Note", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='5 Year Note')
        except Exception as e:
            print(e, '5 Year Note')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class YearNote(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="10 Year Note", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='10 Year Note')
        except Exception as e:
            print(e, '10 Year Note')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class FederalFunds(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Federal Funds", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Federal Funds')
        except Exception as e:
            print(e, 'Federal Funds')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class UltraUSTBonds(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ultra U.S. T-Bonds", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Ultra U.S. T-Bonds')
        except Exception as e:
            print(e, 'Ultra U.S. T-Bonds')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Ultra10yearUSTNotes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ultra 10-year U.S. T-Notes", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Ultra 10-year U.S. T-Notes')
        except Exception as e:
            print(e, 'Ultra 10-year U.S. T-Notes')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class BitCoin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BitCoin", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='BitCoin')
        except Exception as e:
            print(e, 'BitCoin')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Euro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Euro", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Euro')
        except Exception as e:
            print(e, 'Euro')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class AustralischerDollar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Australischer Dollar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Australischer Dollar')
        except Exception as e:
            print(e, 'Australischer Dollar')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class BrasilianischerReal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Brasilianischer Real", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Brasilianischer Real')
        except Exception as e:
            print(e, 'Brasilianischer Real')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class BritischesPfund(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Britisches Pfund", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Britisches Pfund')
        except Exception as e:
            print(e, 'Britisches Pfund')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class JapanischerYen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Japanischer Yen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Japanischer Yen')
        except Exception as e:
            print(e, 'Japanischer Yen')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class KanadischerDollar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kanadischer Dollar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Kanadischer Dollar')
        except Exception as e:
            print(e, 'Kanadischer Dollar')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MexikanischerPeso(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Mexikanischer Peso", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Mexikanischer Peso')
        except Exception as e:
            print(e, 'Mexikanischer Peso')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class NeuseelandDollar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Neuseeland Dollar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Neuseeland Dollar')
        except Exception as e:
            print(e, 'Neuseeland Dollar')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class RussischerRubel(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Russischer Rubel", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Russischer Rubel')
        except Exception as e:
            print(e, 'Russischer Rubel')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class SchweizerFranken(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Schweizer Franken", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Schweizer Franken')
        except Exception as e:
            print(e, 'Schweizer Franken')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MonateEuroDollar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="3 Monate Euro Dollar", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='3 Monate Euro Dollar')
        except Exception as e:
            print(e, '3 Monate Euro Dollar')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class USDollarIndex(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="U.S. Dollar Index", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='U.S. Dollar Index')
        except Exception as e:
            print(e, 'U.S. Dollar Index')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Gold(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Gold", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Gold')
        except Exception as e:
            print(e, 'Gold')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Silber(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Silber", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Silber')
        except Exception as e:
            print(e, 'Silber')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Platin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Platin", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Platin')
        except Exception as e:
            print(e, 'Platin')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Palladium(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Palladium", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Palladium')
        except Exception as e:
            print(e, 'Palladium')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Kupfer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kupfer", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Kupfer')
        except Exception as e:
            print(e, 'Kupfer')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Aluminium(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Aluminium", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Aluminium')
        except Exception as e:
            print(e, 'Aluminium')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Stahl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Stahl", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Stahl')
        except Exception as e:
            print(e, 'Stahl')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Kohle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kohle", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Kohle')
        except Exception as e:
            print(e, 'Kohle')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class RoholWTI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Rohöl WTI", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Rohöl WTI')
        except Exception as e:
            print(e, 'Rohöl WTI')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Benzin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Benzin", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Benzin')
        except Exception as e:
            print(e, 'Benzin')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Heizol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Heizöl", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Heizöl')
        except Exception as e:
            print(e, 'Heizöl')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Erdgas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Erdgas", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Erdgas')
        except Exception as e:
            print(e, 'Erdgas')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Ethanol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ethanol", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Ethanol')
        except Exception as e:
            print(e, 'Ethanol')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class ChicagoEthanol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Chicago Ethanol", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Chicago Ethanol')
        except Exception as e:
            print(e, 'Chicago Ethanol')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Mais(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Mais", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Mais')
        except Exception as e:
            print(e, 'Mais')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class WeizenSRW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Weizen SRW", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Weizen SRW')
        except Exception as e:
            print(e, 'Weizen SRW')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class WeizenHRW(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Weizen HRW", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Weizen HRW')
        except Exception as e:
            print(e, 'Weizen HRW')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Reis(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Reis", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Reis')
        except Exception as e:
            print(e, 'Reis')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Hafer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hafer", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Hafer')
        except Exception as e:
            print(e, 'Hafer')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Sojabohnen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sojabohnen", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Sojabohnen')
        except Exception as e:
            print(e, 'Sojabohnen')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class SojabohnenMehl(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sojabohnen Mehl", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Sojabohnen Mehl')
        except Exception as e:
            print(e, 'Sojabohnen Mehl')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Sojabohnenol(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sojabohnen Öl", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Sojabohnen Öl')
        except Exception as e:
            print(e, 'Sojabohnen Öl')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Raps(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Raps", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Raps')
        except Exception as e:
            print(e, 'Raps')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Kakao(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kakao", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Kakao')
        except Exception as e:
            print(e, 'Kakao')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Baumwolle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Baumwolle", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Baumwolle')
        except Exception as e:
            print(e, 'Baumwolle')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Orangensaft(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Orangensaft", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Orangensaft')
        except Exception as e:
            print(e, 'Orangensaft')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Kaffee(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Kaffee", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Kaffee')
        except Exception as e:
            print(e, 'Kaffee')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Zucker(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Zucker", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Zucker')
        except Exception as e:
            print(e, 'Zucker')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Bauholz(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Bauholz", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Bauholz')
        except Exception as e:
            print(e, 'Bauholz')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Lebendrind(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Lebendrind", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Lebendrind')
        except Exception as e:
            print(e, 'Lebendrind')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Mastrind(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Mastrind", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Mastrind')
        except Exception as e:
            print(e, 'Mastrind')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Magerschwein(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Magerschwein", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Magerschwein')
        except Exception as e:
            print(e, 'Magerschwein')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Butter(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Butter", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Butter')
        except Exception as e:
            print(e, 'Butter')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class FettarmeMilch(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Fettarme Milch", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Fettarme Milch')
        except Exception as e:
            print(e, 'Fettarme Milch')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MilchIII(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Milch III", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Milch III')
        except Exception as e:
            print(e, 'Milch III')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class MilchIV(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Milch IV", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Milch IV')
        except Exception as e:
            print(e, 'Milch IV')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Kase(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Käse", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        try:
            graph_data = graph_data_func.build_graph(name='Käse')
        except Exception as e:
            print(e, 'Käse')
            graph_data = [[1,3,1],[1,3,1],[1,3,1],[1,3,1]]

        f = Figure(figsize=(5,5), dpi=100)
        a = f.subplots(2)
        a[1].plot(graph_data[2], graph_data[3], label='osz')
        a[0].plot(graph_data[0], graph_data[1], label ='cs')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = SeaofBTCapp()
app.mainloop()