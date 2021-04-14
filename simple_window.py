import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# creates a blank window object
window = Gtk.Window()
# now we need to connect smth to that window, here is means closing of a window
window.connect("delete-event", Gtk.main_quit)
# this line of code shows window to the user
window.show_all()
# before we start this file we need keep the window opened
Gtk.main()
