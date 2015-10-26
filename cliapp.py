import shutil

class CliApp(object):
    def __init__(self):
        self.max_width = 180
        self.cell_width = 20
        self.cell_no = 6

    def guess_widths(self):
        """
        Guess Default Cell Width, and Max Console Width
        """

        self.max_width = shutil.get_terminal_size()[0] - (self.cell_no + 1)
        self.cell_width = (self.max_width / self.cell_no) - 2
        return {"max_width": self.max_width, "cell_width": self.cell_width}

    def display_cell(self, stringer):
        """
        Display a padded cell of text
        """

        # Truncate strings that are too big for display
        if len(stringer) > self.cell_width:
            stringer = stringer[:int(self.cell_width - 3)] + "..."
        # Insert padding
        while len(stringer) < (self.cell_width - 2):
            stringer = " " + str(stringer) + " "
        # If too much padding got inserted, remove it
        while len(stringer) > self.cell_width:
            stringer = stringer[:-1]
        # If there isn't enough padding, insert it
        while len(stringer) < self.cell_width:
            stringer = stringer + " "
        return stringer

    def display_line(self, lister, seperator):
        """
        Display a line with several cells.
        """

        if type(lister) != type(list()):
            raise TypeError
        built_string = "" + str(seperator)
        item_tracker = 0
        for item in lister:
            item_tracker = item_tracker + 1
            if item_tracker == self.cell_no + 1:
                built_string = built_string + "\n" + str(seperator)
                item_tracker = 0
            built_string = built_string + self.display_cell(str(item)) + str(seperator)
        return built_string

    def display_titles(self, lister, seperator):
        """
        Display a list of titles.
        """

        if type(lister) != type(list()):
            raise TypeError
        if len(lister) < 7:
            length = 0
            for item in lister:
               length = length + len(item)
            self.max_width = (shutil.get_terminal_size()[0] - (self.cell_no + 1)) - length
            self.cell_no = len(lister)
            self.cell_width = (self.max_width / self.cell_no) - 2
        else:
            self.guess_widths()
        string_built = self.display_line(lister, seperator) + "\n"
        iter = self.max_width
        while iter > 1:
            string_built = string_built + "-"
            iter = iter - 1
        return string_built


if __name__ == "__main__":
    """
    Demonstration Application
    """

    app = CliApp()
    #app.guess_widths()
    test_list = ["Awesome"]
    iter = 6
    while iter > 0:
        print(app.display_titles(test_list,":"))
        print(app.display_line([str(x).replace("Awesome","Totally Rad") for x in test_list],"|"))
        print("\n")
        test_list.append("Awesome")
        iter = iter - 1
