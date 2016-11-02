import db_editor
import global_constants


class Print:
    """
    Prepares everything for printing and prints.
    """
    def __init__(self):
        self.menu_buttons = Utilities().construct_menu()

        # Get and store all templates
        self.head = Templates().read_from_template("head")
        self.header = Templates().read_from_template("header")
        self.menu_section = Templates().read_from_template("menu")
        self.cms_menu = Templates().read_from_template("cms_menu")
        self.left_sidebar = Templates().read_from_template("left_sidebar")
        self.right_sidebar = Templates().read_from_template("right_sidebar")
        self.content = Templates().read_from_template("content")
        self.footer = Templates().read_from_template("footer")
        self.end = Templates().read_from_template("end")

        self.install = Templates().read_from_template("installation_form")

#TODO:
    # Probably wont be needed but might be used as a template
#    def print_all(self):
#        """
#        Prints everything that needs to be printed.
#        """
#
#        print self.head % "Kromleh"
#        print self.header % {'header_title': "Web development and design"}
#        print self.menu_section % {"menu_buttons": self.menu_buttons}
#        print self.left_sidebar
#        print self.right_sidebar
#        print self.content
#        print self.footer
#        print self.end

    def print_head(self, title, stylesheet_path, install_js_path):
        """
        Given the title, prints the head.
        :param title: The title of the page in the browser
        :param stylesheet_path: The path to the stylesheet which is going to be used (eg. for CMS or for user output)
        :param install_js_path: The path to the js file for installation page specially
        """
        print self.head % {'page_title': title, 'stylesheet_path': stylesheet_path, 'install_js_path': install_js_path}

    def print_header(self, title, sub_title):
        """
        Prints the header.
        :param title: the page title.
        :param sub_title: the page subtitle
        """
        print self.header % {'web_title': title, 'sub_title': sub_title}

    def print_cms_menu(self, buttons):
        """
        Prints the menu field for the content management system
        :param buttons: The buttons to display
        """
        print self.cms_menu

    def print_end(self):
        """
        Prints the end
        """
        print self.end

    def print_installation_form(self):
        """
        Prints the installation form
        """
        print self.install


class Utilities:
    """
    Holds functions for processing.
    """
    def __init__(self):
        self.menu_items = global_constants.MENU_CONTENT
        self.button_format = global_constants.MENU_BUTTON_FORMAT

    def construct_menu(self):
        """
        Uses the content of menu_items dictionary to populate the menu button template.
        :return: a list with formatted menu buttons
        """
        menu_list = []
        for menu_item in self.menu_items:
            menu_list.append(self.button_format % {"target_link": self.menu_items[menu_item], "button_name": menu_item})

        menu = "\n".join(menu_list)

        return menu


class Templates:
    """
    Holds all the functions for template processing.
    """

    def __init__(self):
        self.html_path = global_constants.DEFAULT_HTML_PATH

    def read_from_template(self, template_name):
        """
        Used to read from template files
        :param template_name: The name of the template
        :return: the result
        """
        with open("%s/%s.html" % (self.html_path, template_name), 'r') as self.infile:
            data = self.infile.read()

        return data


class DataVerification:
    """
    Verifies if passed data covers the requirements.
    """

    def __init__(self):
        pass

    def verify_username(self, username):
        pass
        

class DataSanitization:
    """
    If a passed data fails validation and qualifies for sanitization then
    sanitarization is performed.
    """

    def __init__(self):
        pass
