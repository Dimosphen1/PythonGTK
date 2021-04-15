import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# Here we will create a program with actual tabs, not linked buttons like it was before

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Testing layout")
        self.set_border_width(10)
        # here we will use a notebook layout, it is quite popular
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # actual windows with some data are called pages
        # now we will create a bunch of pages and add them one by one to the notebook

        # First page
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        # here we will set text that will appear on the main page
        self.page1.add(Gtk.Label(label='Here is the text from the main area.'))
        # now we have to add this page to a notebook and set a title
        self.notebook.append_page(self.page1, Gtk.Label(label='First Tab'))

        # Second page
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label(label="Here there, it is page two!"))
        # now here we can also get an icon by using a specific method
        icon = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio", Gtk.IconSize.MENU)
        self.notebook.append_page(self.page2, icon)




window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()