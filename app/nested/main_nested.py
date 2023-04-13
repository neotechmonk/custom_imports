"""Its clunky to import super modules from the app package.
Can be done with absolute path, but this not required from a practice point of  view
"""
import os
import sys

# Get the absolute path of the current module file
current_file = os.path.abspath(__file__)

# Get the absolute path of the parent directory of the current module file
current_dir = os.path.dirname(current_file)

# Get the absolute path of the parent directory of the app package
app_dir = os.path.dirname(current_dir)

# Add the parent directory of the app package to the Python path
sys.path.append(app_dir)


print(sys.path)
from helper.helper1 import get_help
from insider import insider_response  # Relative path
from mymod import byenow, heythere


def main():
    print("Hello World!")
    heythere()  # from mymod
    byenow()  # from mymod
    get_help()  # from helper/helper1
    insider_response()


if __name__ == "__main__":
    main()
