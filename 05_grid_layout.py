import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        # this is a type of layout that uses columns and rows to place elements
        grid = Gtk.Grid()
        self.add(grid)

        # Create buttons
        # Here basically we will create a bunch of widgets and place them accordingly to each other
        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        button7 = Gtk.Button(label="Button 7")
        button8 = Gtk.Button(label="Button 8")


        # Now we will place them
        # By default, the first button is placed on the top left,
        # this button will be a reference point for other buttons we are going to add
        grid.add(button1)

        # Button takes within 5 parameters, the first is the button itself, 2nd - to what column,
        # 3rd - to what row, 4th - width, 5th - high
        # this button will appear at the first column, zero row, will be twice wide and be the same high
        grid.attach(button2, 1, 0, 2, 1)

        # you can also position widgets relative to other widgets with the use of attach_next_to
        # here is will be placed at the bottom relative to button1, will have width 1 and twice high
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

        # my added buttons
        grid.attach(button7, 0, 3, 2, 1)
        grid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 1, 2)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
