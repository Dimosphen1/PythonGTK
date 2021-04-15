import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# now we will learn how to select different files and also how to select whole directories
# we will try to include everything inside of this class

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(30)
        layout = Gtk.Box(spacing=6)
        self.add(layout)

        button = Gtk.Button("Choose File")
        button.connect("clicked", self.on_file_clicked)
        layout.add(button)

    # users clicked the choose file button
    def on_file_clicked(self, widget):
        # FileChooserDialog allows user to choose a file or a directory
        # Gtk.FileChooserAction.OPEN means that this is a pop-up that lets a user to pick a file
        # in case of Gtk.FileChooserAction.SELECT_FOLDER means that this is just select a path
        # inside of () we will add default buttons
        dialog = Gtk.FileChooserDialog("Hey, select a file", self, Gtk.FileChooserAction.OPEN,
                                       ("Cancel", Gtk.ResponseType.CANCEL,
                                        "Ok", Gtk.ResponseType.OK))

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("You clicked the Open button")
            print("File selected", dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("User didn't choose any file")

        dialog.destroy()





window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
