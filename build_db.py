import sqlite3

import db_editor
import global_constants


class ConstructDatabase:
    """
    Used to create all functional and user tables and format them
    """

    def __init__(self):
        self.all_functional_tables = global_constants.ALL_FUNCTIONAL_TABLES
        self.required_user_tables = global_constants.REQUIRED_USER_TABLES
        self.initial_user_tables = global_constants.INITIAL_USER_TABLES

    def arrange_db_table_creation(self, table, columns):
        """
        Arranges communication with the database to create the given tables 
        """

        # Create database connection
        try:
            db_edit = db_editor.DBEditor()
        except:
            raise

        # Alter the database
        try:
            db_edit.create_table(table, columns)
        except:
            #TODO log exception
            db_edit.db_rollback()
            db_edit.db_close()
            raise 

        # Commit the changes and close connection
        db_edit.db_commit()
        db_edit.db_close()

    def create_all_functional_tables(self):
        """
        Creates all functional tables from the list in global constants
        """

        for table in self.all_functional_tables:
            column_list = self.all_functional_tables[table]
            columns = ", ".join(column_list)

            try:
                self.arrange_db_table_creation(table, columns)
            except:
                raise

    def create_required_user_tables(self):
        """
        Creates all the required user tables from the list in global constants
        """

        for table in self.required_user_tables:
            column_list = self.required_user_tables[table]
            columns = ", ".join(column_list)

            try:
                self.arrange_db_table_creation(table, columns)
            except:
                raise


class PopulateDatabase:
    """
    Used to populate the created functional tables with the functional data
    """
    def __init__(self):
        self.pepper = "Love is the salt of life."
        self.dressing = global_constants.SALAD

    def put_pepper_and_dressing_in_database(self):
        """
        Puts the **** in the ********
        :return:
        """
        try:
            db_edit = db_editor.DBEditor()
        except:
            raise

        # Alter the database
        try:
            db_edit.put_pepper_and_dressing(self.pepper, self.dressing)
        except:
            # TODO log exception
            db_edit.db_rollback()
            db_edit.db_close()
            raise

            # Commit the changes and close connection
        db_edit.db_commit()
        db_edit.db_close()