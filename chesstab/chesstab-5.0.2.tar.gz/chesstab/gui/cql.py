# cql.py
# Copyright 2016 Roger Marsh
# Licence: See LICENCE (BSD licence)

"""Widget to display a Chess Query Language (ChessQL) statement.

ChessQL statements obey the syntax published for CQL version 6.0.1 (by Gady
Costeff).

The CQL class displays a ChessQL statement.

An instance of this class fits into the user interface in two ways: as an
item in a panedwindow of the main widget, or as the only item in a new toplevel
widget.

The cqledit module provides a subclass which allows editing in the main
application window.

The cqldbshow and cqldbedit modules provide subclasses used in a
new toplevel widget to display or edit ChessQL statements.

The cqldbdelete module provides a subclass used in a new toplevel widget
to allow deletion of ChessQL statements from a database.

"""

import tkinter

from .cqltext import CQLText
from .eventspec import EventSpec


class CQL(CQLText):

    """ChessQL statement widget.

    master is used as the master argument for the tkinter Frame widget passed
    to superclass.

    boardfont is no longer used. (A relic of pre-CQL syntax days.)

    See superclass for ui, items_manager, and itemgrid, arguments.  These may
    be, or have been, absorbed into **ka argument.

    """

    def __init__(
        self,
        master=None,
        boardfont=None,
        ui=None,
        items_manager=None,
        itemgrid=None,
        **ka
    ):
        """Create Frame and delegate to superclass, then set grid geometry
        manager.
        """

        panel = tkinter.Frame(master, borderwidth=2, relief=tkinter.RIDGE)
        panel.bind("<Configure>", self.try_event(self.on_configure))
        panel.grid_propagate(False)
        super().__init__(
            panel, ui=ui, items_manager=items_manager, itemgrid=itemgrid, **ka
        )
        self.scrollbar.grid(column=1, row=0, rowspan=1, sticky=tkinter.NSEW)
        self.score.grid(column=0, row=0, rowspan=1, sticky=tkinter.NSEW)
        if not ui.visible_scrollbars:
            panel.after_idle(self.hide_scrollbars)
        self.configure_cql_statement_widget()

        # The popup menus specific to CQL (placed same as Game equivalent)

        # self.primary_activity_popup.add_cascade(
        #    label='Database', menu=self.database_popup)

        # For compatibility with Game when testing if item has focus.
        self.takefocus_widget = self.score

    def destroy_widget(self):
        """Destroy the widget displaying ChessQL statement."""
        self.panel.destroy()

    def get_top_widget(self):
        """Return topmost widget for ChessQL statement display.

        The topmost widget is put in a container widget in some way
        """
        return self.panel

    def on_configure(self, event=None):
        """Reconfigure widget after container has been resized."""
        self.configure_cql_statement_widget()

    def configure_cql_statement_widget(self):
        """Configure widgets for a ChessQL statement display."""
        self.panel.grid_rowconfigure(0, weight=1)
        self.panel.grid_columnconfigure(0, weight=1)
        self.panel.grid_columnconfigure(1, weight=0)

    def hide_scrollbars(self):
        """Hide the scrollbars in the ChessQL statement display widgets."""
        self.scrollbar.grid_remove()
        self.score.grid_configure(columnspan=2)
        self.configure_cql_statement_widget()

    def show_scrollbars(self):
        """Show the scrollbars in the ChessQL statement display widgets."""
        self.score.grid_configure(columnspan=1)
        self.scrollbar.grid_configure()
        self.configure_cql_statement_widget()

    def takefocus(self, take=True):
        """Configure game widget takefocus option."""

        # Hack because I misunderstood meaning of takefocus: FALSE does not
        # stop the widget taking focus, just stops tab traversal.
        if take:
            # self.takefocus_widget.configure(takefocus=tkinter.TRUE)
            self.takefocus_widget.configure(takefocus=tkinter.FALSE)
        else:
            self.takefocus_widget.configure(takefocus=tkinter.FALSE)

    def set_database_navigation_close_item_bindings(self, switch=True):
        self.set_event_bindings_score(
            self.get_database_events(), switch=switch
        )
        self.set_event_bindings_score(
            self.get_navigation_events(), switch=switch
        )
        self.set_event_bindings_score(
            self.get_close_item_events(), switch=switch
        )

    def set_score_pointer_widget_navigation_bindings(self, switch):
        """Set or unset pointer bindings for widget navigation."""
        self.set_event_bindings_score(
            (
                (EventSpec.control_buttonpress_1, ""),
                (EventSpec.buttonpress_1, self.give_focus_to_widget),
                (EventSpec.buttonpress_3, self.post_inactive_menu),
            ),
            switch=switch,
        )

    def set_colours(self, sbg, bbg, bfg):
        """Set colours and fonts used to display ChessQL statement.

        sbg == True - set game score colours
        bbg == True - set board square colours
        bfg == True - set board piece colours

        """

    def create_primary_activity_popup(self):
        popup = super().create_primary_activity_popup()
        self.create_widget_navigation_submenu_for_popup(popup)
        return popup

    def export_partial(self, event=None):
        """Export displayed partial position definition."""
        exporters.export_single_position(
            self.score.get("1.0", tkinter.END),
            self.ui.get_export_filename_for_single_item(
                "Partial Position", pgn=False
            ),
        )
