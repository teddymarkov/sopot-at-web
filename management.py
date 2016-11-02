#!/usr/bin/python
import cgi
import global_constants
import utilities

print "Content-type:text/html\n"


def build_output():
    """
    Builds the code for output and prints it.
    """

    style_path = global_constants.DEFAULT_HTML_PATH + global_constants.CMS_STYLE_FILE_NAME
    cms_js_functions = global_constants.CMS_JS_FILE_PATH + global_constants.CMS_INSTALL_PAGE_JS_FILE_NAME
    page_title = global_constants.CMS_PAGE_TITLE
    # Instantiate print utilities
    print_instance = utilities.Print()
    # Output the page content
    print_instance.print_head(page_title, style_path, cms_js_functions)
    print_instance.print_header('<h1 id="heading_title_cms">SOPOT<span id="heading_title_part_two_cms">@WEB <span id="heading_title_part_three_cms">v.1.0.0.d</span></span></h1>', "")
    print_instance.print_cms_menu()
    print_instance.print_end()


def main():
    """
    Main function.
    """

    build_output()

if __name__ == "__main__":
    main()