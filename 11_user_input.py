import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# here we will work with user input, get data from there and use it further

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="User Input")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)

        # Username
        # Here we will use an entry class, it is basically an input area
        self.username = Gtk.Entry()
        # also you need to add a label from the left side and also input field from the right
        # in this case it will display Username inside of that box
        self.username.set_text("Username")
        vbox.pack_start(self.username, True, True, 0)

        # Password
        # Now we will see how to have a hidden text
        self.password = Gtk.Entry()
        self.password.set_text("Password")
        # now this text will be covered with *****
        self.password.set_visibility(False)
        vbox.pack_start(self.password, True, True, 0)

        # Sign In Button
        self.button = Gtk.Button(label="Sign In")
        # now we will pass the signal clicked and also create a function sign_in which will display a user input
        self.button.connect("clicked", self.sign_in)
        # and now we will add this to the layout
        vbox.pack_start(self.button, True, True, 0)

    # here we pass an instance of a class inside of a widget
    def sign_in(self, widget):
        # if you want to display the name, you specify according variable and replace set with get
        print(self.username.get_text())
        print(self.password.get_text())

window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()