from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


class YoutubeDownloader:

    def __init__(self, window):
        window.title('video and audio downloader')
        # window.geometry('520x150')
        mainframe = ttk.Frame(window)
        window.config(padx=15, pady=15,)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S),)

        ttk.Label(mainframe, text='Link', font=('Arial', 12,)).grid(column=0, row=0)

        self.link = StringVar()
        self.link_entry = ttk.Entry(mainframe, width=50, textvariable=self.link, )
        self.link_entry.grid(column=1, row=0, columnspan=3, sticky=(W))

        ttk.Label(mainframe, text='Salvar em', font=('Arial', 12)).grid(column=0, row=2)
        self.save_as = StringVar()
        self.salvar_entry = ttk.Entry(mainframe, width=50, textvariable=self.save_as,).grid(column=1, row=2, columnspan=3)
        self.escolha_button = ttk.Button(mainframe, text='Navegar', command=self.escolher_pasta).grid(column=4, row=2)

        ttk.Label(mainframe, text='Opções', font=('Arial', 12)).grid(column=0, row=3)
        self.only_audio = BooleanVar()
        self.audio_checkbox = ttk.Checkbutton(mainframe, text='Apenas áudio', variable=self.only_audio).grid(column=1, row=3)

        ttk.Button(mainframe, text='Baixar', command=self.download).grid(column=1, row=4, columnspan=2)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def escolher_pasta(self):
        folder_path = filedialog.askdirectory()
        self.save_as.set(folder_path)
        # print(YouTube(self.link_entry.get()).streams)

    def download(self, a=0, b=0, c=0):

        if self.only_audio.get():
            yt = YouTube(self.link_entry.get()).streams.get_audio_only().download(self.save_as.get())
        else:
            yt = YouTube(self.link_entry.get()).streams.get_highest_resolution().download(self.save_as.get())

        print('download completo')


window = Tk()
YoutubeDownloader(window)
window.mainloop()
