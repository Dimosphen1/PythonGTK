import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Here we will create menus that will have menus with several drop-down items

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu example")
        self.set_default_size(400, 300)
        layout = Gtk.Box()
        self.add(layout)

        # Main container that we will stick inside our layout
        main_menu_bar = Gtk.MenuBar()

        # Drop down menu (the main icon on the icon layout)
        file_menu = Gtk.Menu()
        # now we will create the actual dropdown
        file_menu_dropdown = Gtk.MenuItem(label="File")

        # File menu items
        file_new = Gtk.MenuItem(label="New...")
        file_open = Gtk.MenuItem(label="Open")
        file_exit = Gtk.MenuItem(label="Exit")

        file_menu_dropdown.set_submenu(file_menu)
        file_menu.append(file_new)
        file_menu.append(file_open)
        file_menu.append(Gtk.SeparatorMenuItem())  # add a separator inside of a menu
        file_menu.append(file_exit)

        main_menu_bar.append(file_menu_dropdown)

        layout.pack_start(main_menu_bar, True, True, 0)



window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()