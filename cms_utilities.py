import db_editor
import global_constants


class Print:
    """
    Prepares everything for printing and prints.
    """

    def __init__(self):
        # Get and store all templates
        self.cms_head = Templates().read_from_template("head")
        self.cms_header = Templates().read_from_template("cms_header")
        self.cms_menu = Templates().read_from_template("cms_menu")
        self.cms_content = Templates().read_from_template("cms_content")
        self.cms_footer = Templates().read_from_template("cms_footer")
        self.end = Templates().read_from_template("end")

        self.install = Templates().read_from_template("installation_form")

    def print_cms_head(self, title, stylesheet_path, install_js_path):
        """
        Given the title, prints the head.
        :param title: The title of the page in the browser
        :param stylesheet_path: The path to the stylesheet which is going to be used (eg. for CMS or for user output)
        :param install_js_path: The path to the js file for installation page specially
        """
        print self.cms_head % {'page_title': title, 'stylesheet_path': stylesheet_path, 'install_js_path': install_js_path}

    def print_cms_header(self, title, sub_title):
        """
        Prints the header.
        :param title: the page title.
        :param sub_title: the page subtitle
        """
        print self.cms_header % {'web_title': title, 'sub_title': sub_title}

    def print_cms_menu(self, buttons):
        """
        Prints the menu field for the content management system
        :param buttons: The buttons to display
        """
        print self.cms_menu % {"menu_buttons": buttons}

    def print_cms_content(self):
        """
        Prints the content field for the content management system
        :return:
        """
        print self.cms_content

    def print_cms_footer(self):
        """
        Prints the footer area for the content managements system
        :return:
        """
        print self.cms_footer

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
        self.cms_menu_items = global_constants.CMS_MENU_CONTENT
        self.cms_button_format = global_constants.CMS_MENU_BUTTON_FORMAT

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
