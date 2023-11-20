#!/usr/bin/python3

from window import *
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


def winThread():
	w = Window(window_name="ValNut")

	window = w.get_root()

	w.display()


# records manager thread
rThread = ThreadMaid()
records = j.get_records()


def recThread():
	pass


def getCredentials():
	return j.get_records()


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


wThread.setup(target=winThread).run()
rThread.setup(target=recThread).run()