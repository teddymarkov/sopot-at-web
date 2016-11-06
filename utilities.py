import db_editor
import global_constants


class Print:
    """
    Parent class. Holds common functions. Prepares everything for printing and prints.
    """
    def print_template(self, content, arguments={}):
        """
        Given the content name which is the be printed, adds the arguments and prints it.
        :param content: The name of hte content to be printed;
        :param arguments: Dictionary which holds all the arguments for the place holders in the content;
        """
        print content % arguments


class PrintPublic(Print):
    """
    Child class to Public. Holds methods and data specific for Public print.
    """
    def __init__(self):
        # Get and store all templates
        self.head = Templates().read_from_template("head")
        self.header = Templates().read_from_template("header")
        self.menu_section = Templates().read_from_template("menu")
        self.left_sidebar = Templates().read_from_template("left_sidebar")
        self.right_sidebar = Templates().read_from_template("right_sidebar")
        self.footer = Templates().read_from_template("footer")
        self.end = Templates().read_from_template("end")

class PrintCMS(Print):
    """
    Child class to Public. Holds methods and data specific for CMS print.
    """
    def __init__(self):
        # Get and store all templates
        self.cms_head = Templates().read_from_template("head")
        self.cms_header = Templates().read_from_template("cms_header")
        self.cms_menu = Templates().read_from_template("cms_menu")
        #        self.cms_content = Templates().read_from_template("cms_content")
        self.cms_footer = Templates().read_from_template("cms_footer")
        self.end = Templates().read_from_template("end")

        self.install_form = Templates().read_from_template("installation_form")


class Utilities:
    """
    Holds functions for processing.
    """
    def __init__(self):
        self.menu_items = global_constants.MENU_CONTENT
        self.button_format = global_constants.MENU_BUTTON_FORMAT
        self.cms_menu_items = global_constants.CMS_MENU_CONTENT
        self.cms_button_format = global_constants.CMS_MENU_BUTTON_FORMAT

    def print_template(self, content, arguments={}):
        """
        Given the content name which is the be printed, adds the arguments and prints it.
        :param content: The name of hte content to be printed;
        :param arguments: Dictionary which holds all the arguments for the place holders in the content;
        """
        print content % arguments

    def construct_menu(self):
        """
        Uses the content of menu_items dictionary to populate the menu button template.
        :return: a list with formatted menu buttons
        """
        menu_list = []
        for menu_item in self.menu_items:
            menu_list.append(self.button_format % {"target_link": self.menu_items[menu_item],
                                                   "button_name": menu_item})

        menu = "\n".join(menu_list)

        return menu

    def construct_cms_menu(self):
        """
        Uses the content of cms_menu_items dictionary to populate the CMS menu button template.
        :return: a list with formatted menu buttons
        """
        cms_menu_list = []
        for menu_item in self.cms_menu_items:
            for menu in menu_item:
                cms_menu_list.append(self.cms_button_format % {"target_link": menu_item[menu],
                                                               "button_name": menu})

        menu = "\n".join(cms_menu_list)

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
        with open("%s%s.html" % (self.html_path, template_name), 'r') as self.infile:
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
