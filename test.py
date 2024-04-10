#!/usr/bin/python3
from bootstrap import *
from window import *


win = Window(
	window_name="ValNut", 
	window_position=WINDOW_CENTERED,
	window_size="800x800"
)
root = win.get_root()

b = Box(root)
b.scroll()
b.append()

win.display()
