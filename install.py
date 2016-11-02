#!/usr/bin/env python

import cgi

import build_db
import db_editor
import global_constants
from utilities import Print

print "Content-type:text/html\n"
print ""


def check_all_forms_are_filled(form):
    """
    Checks if all the fields were filled with values.
    :return: True if they are filled, False if not
    """

    # Check if all the form fields have values
    if form.getvalue("first_name") and \
        form.getvalue("last_name") and \
        form.getvalue("email") and \
        form.getvalue("password_first") and \
        form.getvalue("password_second"):

        return True

    return False


def get_form_input_data(form):
    """
    Gets the input data from the form fields and a returns dictionary
    :return: input_data: dictionary with all the data
    """
    input_data = {}

    # Assign all input data
    # User's first name
    input_data['first_name'] = form.getvalue("first_name")
    # User's last name
    input_data['last_name'] = form.getvalue("last_name")
    # User's email address
    input_data['email'] = form.getvalue("email")
    # Password - first attempt
    input_data['password_first'] = form.getvalue("password_first")
    # Password - second attempt
    input_data['password_second'] = form.getvalue("password_second")

    # Validate input data
    return input_data


def publish_in_db(input_data):
    """
    Temporary function to publish the values from the input form to the database
    :param input_data: A dictionary with the user input data
    :return:
    """

    # Create database connection
    db_conn = db_editor.DBEditor()

    # Populate the "users" table
    # Form the string
    user = [input_data['email'], 1]
    # Insert into table
    db_conn.insert_into_table("users", user)

    # Populate the "user_data" table
    data_of_user = [input_data["email"], input_data["first_name"], input_data["last_name"]]
    db_conn.insert_into_table("user_data", data_of_user)

    # Populate the "user_role" table
    role_of_user = [input_data["email"], "owner"]
    db_conn.insert_into_table("user_roles", role_of_user)

    # Populate the password of the user
    pass_of_the_user = [input_data["email"], input_data["password_first"]]
    db_conn.insert_into_table("sdrowsap", pass_of_the_user)

    db_conn.db_commit()
    db_conn.db_close()


def build_output():
    """
    Builds the code for output and prints it.
    """

    style_path = global_constants.DEFAULT_HTML_PATH + global_constants.INSTALL_STYLE_FILE_NAME
    install_js_path = global_constants.CMS_JS_FILE_PATH + global_constants.CMS_INSTALL_PAGE_JS_FILE_NAME
    page_title = global_constants.INSTALL_PAGE_TITLE
    # Instantiate print utilities
    print_instance = Print()
    # Output the page content
    print_instance.print_head(page_title, style_path, install_js_path)
    print_instance.print_header('<h1 id="heading_title_install">SOPOT<span id="heading_title_part_two_install">@WEB <span id="heading_title_part_three_install">v.1.0.0.d</span></span></h1>', "")
    print_instance.print_installation_form()
    print_instance.print_end()


def initiate_installation(form):
    """
    After information has been provided by the owner, initiates the set up for Sopot@web
    """

    # Instantiate database connection
    db = db_editor.DBEditor()
    # Create all necessary tables
    a = build_db.ConstructDatabase()
    # Populate the tables with functional data
    b = build_db.PopulateDatabase()
    a.create_all_functional_tables()
    a.create_required_user_tables()
    b.put_pepper_and_dressing_in_database()
    db.db_commit()
    db.db_close()
    input_data = get_form_input_data(form)
    publish_in_db(input_data)
    print "CONGRATULATIONS! \nSuccessful install!"
    print "Continue to <a href=http://localhost/sopot/management.py>Control Panel</a>"


def main():
    """
    Main function.
    """

    # Instantiate form handler
    form = cgi.FieldStorage()

    # Check if all form fields have passed values
    if check_all_forms_are_filled(form):
        initiate_installation(form)

    else:
        build_output()

if __name__ == "__main__":
    main()
