import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NewWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cheeseburger Machine")

        # using listbox layout is really good for displaying several items in a list
        # by placing them row by row

        # at first we will set borders around our layout
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        # think about it as a list
        # Now we will set selection mode to None
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        # after that we need to add that to the window
        self.add(listbox)

        # now we will add items to that list
        # in each row we will have a box and we will place items inside of that box
        # with the help of this it is possible to add invisible spaces around the text

        # Checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label = Gtk.Label(label="Check if you love cheeseburgers")
        check = Gtk.CheckButton()
        # now we have to add them to the box
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        # and now we have to add box to the list row
        listbox.add(row_1)

        # Toggle Swift
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label = Gtk.Label(label="Burger making machine:")
        # here we will add a switch
        switch = Gtk.Switch()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)


window = NewWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

