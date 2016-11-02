#!/usr/bin/python

import build_db
import db_editor
import utilities

print "Content-type:text/html\n"


def main():
    """
    Call all needed functions to start the application
    """

    # -< Establish database connection >-
    # Check database is healthy:
    is_db_healthy = db_editor.DBValidator()
    if not is_db_healthy.make_db_validation():
        pass
    # -< EDBC >-

    # -< Print to browser >-
    display = utilities.Print()
    display.print_all()
    # -< PTB >-


if __name__ == "__main__":
    # main()

    # -< TEST >-
    db_editor = db_editor.DBEditor()
    a = build_db.ConstructDatabase()
    b = build_db.PopulateDatabase()
    a.create_all_functional_tables()
    a.create_required_user_tables()
    b.put_pepper_and_dressing_in_database()
    # -< TEST >-
