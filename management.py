#!/usr/bin/python
import cgi
import global_constants
import utilities

print "Content-type:text/html\n"


def build_output(content_item="new_article_form.html"):
    """
    Builds the code for output and prints it.
    """
    # Instantiate objects
    util = utilities.Utilities()
    print_ins = util.print_template
    item_loader = utilities.PrintCMS()

    # Output the head
    page_title = global_constants.CMS_PAGE_TITLE
    style_path = global_constants.DEFAULT_HTML_PATH + global_constants.CMS_STYLE_FILE_NAME
    cms_js_functions = global_constants.JS_FILE_PATH + global_constants.CMS_COMMON_JS_FILE_NAME
    head_arguments = {'page_title': page_title,
                      'stylesheet_path': style_path,
                      'install_js_path': cms_js_functions}
    print_ins(item_loader.cms_head, head_arguments)

    # Output the header
    heading_title = '<h1 id="heading_title_cms">SOPOT<span id="heading_title_part_two_cms">@WEB'\
                    '<span id="heading_title_part_three_cms">v.1.0.0.d | Content Management Panel'\
                    '</span></span></h1>'
    header_arguments = {'web_title': heading_title,
                        'sub_title': ""}
    print_ins(item_loader.cms_header, header_arguments)

    # Output the menu
    cms_buttons = {'menu_buttons': util.construct_cms_menu()}
    print_ins(item_loader.cms_menu, cms_buttons)

    # Output the content
    # The content is being output depending on the request by the URL

    # Output the footer
    print_ins(item_loader.cms_footer)

    # Output the end
    print_ins(item_loader.end)


def main():
    """
    Main function.
    """
    # Instantiate form handler
#    passed_data = cgi.FieldStorage()
#    content_item = passed_data["content"].value

    build_output()#content_item=content_item)


if __name__ == "__main__":
    main()
