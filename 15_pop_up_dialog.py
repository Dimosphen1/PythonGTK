import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Here we will create a simple plain pop up

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Dialog example")
        self.set_default_size(200, 100)
        self.set_border_width(30)

        button = Gtk.Button("Open a PopUp")
        button.connect("clicked", self.button_clicked)
        self.add(button)

    def button_clicked(self, widget):
        # here we will create a variable that will be equal to PopUp class
        # this class will be responsible for another window
        dialog = PopUp(self)
        # in a case it will be a window which requires yes/no answer, we will store that value at the response
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("You clicked the OK button")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked the CANCEL button")

        dialog.destroy()

# instead of creating a class as an instance of window class, we will inherit it from Dialog,
# because it has several built-in useful properties for a pop-up menu
class PopUp(Gtk.Dialog):
    # parent is a reference to the main window
    def __init__(self, parent):
        # MODAL means that user will not be able to do anything with the main program until they do smth with a PopUp

        # in () we will add two buttons
        # each button shows what text you want to appear on that button and what response should be when user
        # clicks that button
        Gtk.Dialog.__init__(self, "PopUp Title", parent, Gtk.DialogFlags.MODAL, (
            "Custom cancel text", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK  # Gtk.STOCK_OK is incredibly lazy way of printing OK
        ))

        # here you will also add such attributes as these, just like in the main window
        self.set_default_size(200, 100)
        self.set_border_width(30)

        # to give a text to describe what this pop up is all about, we can make the following
        area = self.get_content_area()
        area.add(Gtk.Label(label="Wow, this popup is so amazing!"))
        self.show_all()


window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()