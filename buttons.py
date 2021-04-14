import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    # here we call a constructor
    def __init__(self):
        # and now we are calling a superclass constructor, where we can add several parameters
        # here we set title of the window
        Gtk.Window.__init__(self, title="Some title")

        # after that we will create a button

        # Button
        self.button = Gtk.Button(label="Click this button!")
        # and now we will connect a "clicked" signal after clicking that button
        # after that the next parameter is what do you want to (name of the function)
        self.button.connect("clicked", self.button_clicked)
        # last thing we have to do is to add that button to the screen
        self.add(self.button)

    # User clicks button
    def button_clicked(self, widget):
        print("This button is clicked!")

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()

