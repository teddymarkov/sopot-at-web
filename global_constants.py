# -< Indentation templates >-
indent_x_1 = "    "
indent_x_2 = "        "
indent_x_3 = "            "
indent_x_4 = "                "
indent_x_5 = "                    "
# -< ITMPL >-

# -< Paths >-
DEFAULT_PYTHON_PATH = "./"
DEFAULT_HTML_PATH = "./html/"
JS_FILE_PATH = "./js/"
DB_PATH = "./db/"
DB_NAME = "sopot.db"
INSTALL_STYLE_FILE_NAME = "install_style.css"
INSTALL_JS_FILE_NAME = "install_page.js"
CMS_PYTHON_PATH = "./"
CMS_HTML_PATH = "./html/"
CMS_STYLE_FILE_NAME = "cms_style.css"
CMS_COMMON_JS_FILE_NAME = "cms_common_functions.js"

# -< PTH >-

# -< OUT OF USER OUTPUT >-
INSTALL_PAGE_TITLE = "Sopot Install"
CMS_PAGE_TITLE = "Sopot Management"
# -< OOUO >-

# -< HARD CODED VALUES >-
# Username requirements
USERNAME_MIN_LENGTH = 5
USERNAME_MAX_LENGTH = 40
USERNAME_REGEX = ""
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 200
PASSWORD_REGEX = ""
EMAIL_MIN_LENGTH = 3
EMAIL_MAX_LENGTH = 200
WEBSITE_DOMAIN_MIN_LENGTH = 4
WEBSITE_DOMAIN_MAX_LENGTH = 200
# -< HCV >-

# -< Templates >-
MENU_BUTTON_FORMAT = indent_x_3 + '<a id="menu_button" href="%(target_link)s">%(button_name)s</a>'
CMS_MENU_BUTTON_FORMAT = indent_x_3 + '<a class="cms_menu_buttons" href="%(target_link)s">%(button_name)s</a>'
# Defines the names and the links for the menu
MENU_CONTENT = ""
CMS_MENU_CONTENT = ({"New Article": ""},
                    {"Articles": ""},
                    {"New Page": ""},
                    {"Pages": ""},
                    {"Settings": ""},
                    {"Design": ""})
# -< TMPL >-

# -< DATABASE >-
ALL_FUNCTIONAL_TABLES = {"users": ["email text PRIMARY KEY", "is_active integer"],
                         "user_data": ["email text PRIMARY KEY", "first_name text",
                                       "last_name text"],
                         "user_roles": ["email text PRIMARY KEY", "role text"],
                         "sdrowsap": ["email text PRIMARY KEY", "password text"],
                         "pepper": ["pepper text", "dressing"],
                         "display_content": ["item text PRIMARY KEY", "content"]
                         }
REQUIRED_USER_TABLES = {"pages": ["page_id integer PRIMARY KEY", "is_active integer"],
                        "page_status": ["page_id integer", "status text"],
                        "page_data": ["page_id integer PRIMARY KEY", "title text", "content text"],
                        "articles": ["article_id integer PRIMARY KEY", "is_active integer"],
                        "article_status": ["article_id PRIMARY KEY", "status text"],
                        "article_data": ["article_id integer PRIMARY KEY", "title text", "content text"]
                        }
INITIAL_USER_TABLES = ["menu", "articles", "pages", "site_meta"]
# -< DB >-

# -< ******** >-
SALAD = "Eat vegan you people!"
