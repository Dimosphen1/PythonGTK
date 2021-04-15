import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# here will create a stack, which is used to switch between different areas of your program
# tabs are called stack switcher
# main area is called a stack

# here first tab will have a checkbox and second will have some text in it


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Switcher")
        # first what we will do is add padding around all content outside of that window
        self.set_border_width(10)
        # what I will do next is to add box to separate content from tabs
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Stack
        # now we will create two different pages and a switcher to control them
        main_area = Gtk.Stack()
        # now we will set a transition type when switching to a new tab
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        # always when you have transition like that you want to set transition duration
        # here it will last for 2 seconds
        main_area.set_transition_duration(500)

        # Checkbox
        check_button = Gtk.CheckButton(label="Do not press me")
        main_area.add_titled(check_button, "check_name", "Check Box")

        # Label
        label = Gtk.Label()
        # for label we can also set markup
        # in Gtk it reminds HTML, but has some different rules
        label.set_markup("<big>OMG this text is huge!</big>")
        main_area.add_titled(label, "label_name", "Big Label")

        # StackSwitcher
        # Now we have to build actual tabs to switch between them
        stack_switcher = Gtk.StackSwitcher()
        # now we have to give a stack, or in other words what will be an area that it controls
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)

window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
