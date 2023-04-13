import os
import sys

# Get the absolute path to the 'src' directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(src_path)  # Add the 'src' directory to the Python path

# Absolute import
# folder.module
from helper.helper1 import get_help
from mymod import byenow, heythere

# __init__.py must be in `outsider` folder
from outsider import lokirespose

# Relative import


# no need for __init__.py must be in `outsider` folder
# from outsider.helper2 import lokirespose


def main():
    print("Hello World!")
    heythere()  # from mymod
    byenow()  # from mymod
    get_help()  # from helper/helper1
    lokirespose()


if __name__ == "__main__":
    main()
