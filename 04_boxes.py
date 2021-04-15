import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# box is an invisible container where you can stick widgets inside of

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")

        # Box
        # creating box
        # one of properties that you can add here is spacing, they will spaced by 10 px
        self.box = Gtk.Box(spacing=1000)
        self.add(self.box)

        # Bacon button
        # creating new button
        self.bacon_button = Gtk.Button(label="Bacon")
        self.bacon_button.connect("clicked", self.bacon_clicked)
        # now we will make sure that this button goes inside of that box, after that goes actual button
        # and some other setting like pad, fill
        self.box.pack_start(self.bacon_button, True, True, 0)

        # Tuna button
        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.tuna_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

    def bacon_clicked(self, widget):
        print("You clicked bacon!")

    def tuna_clicked(self, widget):
        print("You clicked tuna!")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
