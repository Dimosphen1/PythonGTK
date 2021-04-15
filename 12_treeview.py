import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Tree View is a kind of layout that uses columns and rows to place elements
# it has a lot of functions to build-in functionality on how to sort columns, filter data, etc.

# List of tuples (this is the model, aka the data that will be displayed by the TreeView)
people = [
    ("Ivan Petrov", 25, "Programmer"),
    ("Johny Ives", 45, "Nurse"),
    ("Alina Trinova", 33, "Physician"),
    ("Emma Whatson", 27, "SpiderWoman"),
    ("Peter Dinklage", 35, "FreshMan")
]


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="People Finder")
        layout = Gtk.Box()
        self.add(layout)

        # Convert data to ListStore (lists that TreeViews can display)
        # here you need to pass the data that these tuples hold
        people_list_store = Gtk.ListStore(str, int, str)
        # now we will loop through this list and add people to the people_list_store
        for item in people:
            people_list_store.append(list(item))

        # you can access data if you need to
        for row in people_list_store:
            print(row[:])

        # TreeView is the item that is displayed
        # we will not later bother ourselves with changing data here because we need only
        # to change data in the people list
        people_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(["Name", "Age", "Profession"]):
            # Render means how to draw the data
            # this is needed because you want to decide how to display data inside of specific cell
            render = Gtk.CellRendererText()

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, render, text=i)

            # Add column to TreeView
            people_tree_view.append_column(column)

        # Add TreeView to the main layout
        layout.pack_start(people_tree_view, True, True, 0)





window = MyWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()