import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# here we will create a program which has one horizontal box and three vertical boxes inside
# of the horizontal one

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Text styles")
        self.set_border_width(20)
        self.set_default_size(500, 300)

        # Boxes
        # hbox will be main horizontal row
        hbox = Gtk.Box(spacing=20)
        # when the homogeneus is set to True, it means that all children will have the same space
        hbox.set_homogeneous(False)
        # now we will start adding columns and change the orientation of them
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_right.set_homogeneous(False)

        # Pack the two columns
        # now we have to organize everything
        # basically we created three invisible boxes and said that hey,
        # we will stick vbox_left and vbox_right inside of hbox
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        # Normal label
        # here we will add a label to identify a page
        label = Gtk.Label(label="This is a default label")
        vbox_left.pack_start(label, True, True, 0)

        # Left aligned
        # here we will make an aligned text
        label = Gtk.Label()
        # instead of writing text to a label you can set it in this way
        label.set_text("This is a left aligned text.\nOh wooow, this is multiple lines, sooo great!!!")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        # Right aligned
        label = Gtk.Label(label="Hey, this is right aligned text!\nSo magnificent)")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        # Line wrap
        # to test it better use the next label with a lot of text
        # label = Gtk.Label("Hi, my name is Dima, nice to meet you! "
        #                   "Hi, my name is Dima, nice to meet you! "
        #                   "Hi, my name is Dima, nice to meet you! "
        #                   "Hi, my name is Dima, nice to meet you! "
        #                   "Hi, my name is Dima, nice to meet you!")
        label = Gtk.Label(label="Hi, my name is Dima, nice to meet you!")
        # here will be displayed a wrong way of doing things
        # vbox_right.pack_start(label, True, True, 0)
        # to not make software one mile wide, it is better to do the next
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)

        # Fill (newspaper)
        # here we will make a column-like effect, so all words will be equally spaced
        label = Gtk.Label(label="Hi, my name is Dima, nice to meet you! "
                          "Hi, my name is Dima, nice to meet you! "
                          "Hi, my name is Dima, nice to meet you! ")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        # Markup
        # now we will see markup, so we will wrap text in HTML flavor and it will be displayed differently
        label = Gtk.Label()
        label.set_markup("<small>Small text</small>\n"
                         "<big>Big text</big>\n"
                         "<b>This is  bold text\n</b>"
                         "<i>Italics is cool too\n</i>"
                         # or place a URL
                         # in that title will be a text which displays when you put a mouse on it
                         "<a href=\"https://www.softserveinc.com/uk-ua\" title=\"Hover text\">SoftServe site</a>")
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)


        # now we will add everything to the MyWindow
        self.add(hbox)




window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()