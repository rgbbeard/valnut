#!/usr/bin/python3

from window import *
from tkinter import ttk
from thread_maid import ThreadMaid
from logger import Logger
from c import C
from json_maid import JSONMaid

# encryption/decryption threads
cripta = C()
j = JSONMaid()
eThread = ThreadMaid()
dThread = ThreadMaid()

# main thread
wThread = ThreadMaid()
win = None

# records manager thread
rThread = ThreadMaid()
records = j.get_records()
lastCount = 0


def contextMenu():
	
	
	try:
        self.popup.selection = self.tree.set(self.tree.identify_row(event.y))
        self.popup.post(event.x_root, event.y_root)
    finally:
        # make sure to release the grab (Tk 8.0a1 only)
        self.popup.grab_release()


def recThread():
	global j, lastCount, tkinter, win

	credentials = j.get_records()

	while True:
		if j.records_count() != lastCount:
			lastCount = j.records_count()
			credentials = j.get_records()

			frame = tkinter.Frame(win, width=win.winfo_width(), height=win.winfo_height())
			frame.pack()

			scrollX = tkinter.Scrollbar(frame, orient='horizontal')
			scrollX.pack(side=tkinter.BOTTOM, fill=tkinter.X)

			table = ttk.Treeview(frame, xscrollcommand=scrollX.set)
			table.bind("<Button-3>", contextMenu)
			table.pack()

			scrollX.config(command=table.xview)

			table["columns"] = ("username", "password", "website", "description")

			for c in table["columns"]:
				table.column(c, anchor=tkinter.CENTER, width=80)
				table.heading(c, text=c, anchor=tkinter.CENTER)
			
			i = 0
			for r in credentials:
				cr = credentials.get(r)

				table.insert(
					parent='',
					index='end',
					iid=i,
					text='',
					values=(
						cr.get("username"), 
						"*"*len(cr.get("password")), 
						cr.get("website"), 
						cr.get("description")
					)
				)
				i += 1

			table.pack()


def storeCredentials(
	username: str,
	password: str,
	website: str = None,
	description: str = None
):
	j.put_record({
		username: username,
		password: password,
		website: website,
		description: description
	})


rThread.setup(target=recThread)


def winThread():
	global w, win

	w = Window(
		window_name="ValNut", 
		window_position=WINDOW_CENTERED,
		window_size="800x800"
	)
	win = w.get_root()

	rThread.run()

	w.display()


wThread.setup(target=winThread).run()
