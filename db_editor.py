import sqlite3
import os
import time
import random

import global_constants
# import upgrade_db_version


class DBEditor:
    """
    Set of tools to work with the db
    """

    def __init__(self):
        self.db_path = global_constants.DB_PATH
        self.db_name = global_constants.DB_NAME
        self.conn = sqlite3.connect(self.db_path + self.db_name)
        self.cur = self.conn.cursor()

    def db_commit(self):
        """
        Commit the changes to the database
        """
        self.conn.commit()

    def db_rollback(self):
        """
        Rolls back any changes to the database in case of errors.
        """
        self.conn.rollback()

    def db_close(self):
        """
        close the connection to the database
        """
        self.conn.close()

    def create_table(self, table_name, columns):
        """
        Creates a database table.
        """
        self.cur.execute('CREATE TABLE IF NOT EXISTS ' + table_name + " (" + columns + ")")

#    def data_entry(self):
#        self.cur.execute('EXECUTE INTO table_name VALUES(124')
#        self.conn.commit()
#        self.cur.close()
#        self.conn.close()
#
#    def dynamic_data_entry(self):
#        unix = time.time()
#        date = str(datetime.datetime.fromtimestanmp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#        keyword = "Python"
#        value = random.randrange(0,10)
#        self.cur.execute("INSERT INTO table_name (unix, datestamp, keyword, value VALUES (?, ?, ?, ?)",
#                         (unix, date, keyword, value))
#        self.conn.commit()

    def create_sql_string(self, table_name, values):
        """
        Creates the SQL string request based on the values.
        :param values: A tuple containing all the values to be inserted in the table.
        :return request: The string to send to the SQL after adding the actual values.
        """
        place_holders = ",". join(["?" for item in values])
        request = "INSERT INTO %s VALUES (%s)" % (table_name, place_holders)

        return request

    def insert_into_table(self, table_name, values):
        """
        Inserts random information in a random table.
        :param table_name: The name of the table in a string format
        :param values: A tuple containing all the values to be inserted in the table
        :return:
        """
        # Format the SQL request
        request = self.create_sql_string(table_name, values)
        self.cur.execute(request, values)

    def put_pepper_and_dressing(self, pepper, dressing):
        """
        Inserts into the database the **** for the *********
        :param pepper:
        :param dressing:
        """
        self.cur.execute("INSERT INTO pepper VALUES (?, ?)", (pepper, dressing))


class DBValidator:
    """
    Set of tools to validate that the DB exists, is healthy and up to date
    """

    def __init__(self):
        self.db_path = global_constants.DB_PATH
        self.db_name = global_constants.DB_NAME
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def check_db_exists(self):
        """
        Checks if the main database exists
        :return: True if exists; False if not;
        """
        # Check if the DB file exists
        if os.path.isfile(self.db_path + self.db_name):
            return True

        return False

    def check_db_version(self):
        """
        Checks if the database in use version is the same as the latest version
        :return: True if is newest version; False if not;
        """
        pass

    def check_functional_tables_exist(self):
        """
        Checks if all tables from the functional tables list exist
        :return: True if exists; False if not;
        """
        pass

    def check_functional_tables_content(self):
        """
        Checks if the functional tables are healthy.
        Healthy includes that all required fields have values and
        those values are usable.
        :return: True if healthy; False if not;
        """
        pass

    def check_user_tables_exist(self):
        """
        Checks if all tables from the user tables list exist
        :return: True if exists; False if not;
        """
        pass

    def make_db_validation(self):
        """
        Calls all DB validation functions
        :return: True if DB is healthy; False if not;
        """
        if self.check_db_exists() and self.check_functional_tables_exist() and self.check_functional_tables_content() and self.check_user_tables_exist():
            return True
        else:
            # Call the database Inspection toolkit
            pass


class DBInspection:
    """
    Holds toolkit of functions to inspect detected DB issues
    """
    def __init__(self):
        self.db_path = global_constants.DB_PATH
        self.db_name = global_constants.DB_NAME
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
