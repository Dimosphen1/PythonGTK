import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


# Here we will customize header of our program, add some cool icons and attach functionality to them

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Header Bar")
        self.set_border_width(10)
        # if you have a set amount of content that you will display in your window, it is possible to set default size
        # of the window, so it will be the same in every case the user opens a program
        self.set_default_size(500, 400)

        header_bar = Gtk.HeaderBar()
        # now we want to make sure that the user can close the window
        header_bar.set_show_close_button(True)
        # now we can change a title in properties of a program in this way
        # this will add a title to the header bar or simply to the window
        header_bar.props.title = "Awesome music player"
        # here we will set out tile bar by default to our header bar
        self.set_titlebar(header_bar)

        # now we will start adding some buttons

        # Audio button on right
        audio_button = Gtk.Button()
        # actually, there are different ways to upload icons, but here we will use built-in icons
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        # after we have an icon we need to convert it to an image
        # in this function we will specify the icon we just created and what was the icon size
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        # now we can add that image to a button itself
        audio_button.add(image)
        # now we have to add button to the header bar
        header_bar.pack_end(audio_button)

        # now we will see how to create linked items
        # Create box of linked items
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        # now we will say that everything what we put to this box will be linked together
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # now we will create arrows to show that items are really related
        # Left arrow
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(arrow_type="left", shadow_type=False))
        box.add(left_arrow)

        # Right arrow
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(arrow_type="right", shadow_type=False))
        box.add(right_arrow)

        # now we need to add this entire box to the header
        header_bar.pack_start(box)
        # and now we will add some text area to type to
        self.add(Gtk.TextView())



window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()