import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


window = Gtk.Window()

# now we will create a simple widget
# it will be a label that actually represents a text in a window

# at first it is blank
label = Gtk.Label()
# and now we can set some text for it
label.set_label("This is a text of this label, WOW!")
# you can also angle text that appears with this label
label.set_angle(30)
# this shows how the text appears
label.set_halign(Gtk.Align.END)
# after you defined how text is needed to appear, you need to add it to the window
window.add(label)

# also, if we want to get specific properties of smth, instead of .set_... we need to use .get_..., as here:
print(label.get_properties("angle"))

window.connect("delete_event", Gtk.main_quit)
window.show_all()
Gtk.main()
