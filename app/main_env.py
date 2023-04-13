import os
import sys

from dotenv import load_dotenv

load_dotenv()

project_root = str(os.environ.get("PROJECT_ROOT"))

outsider_mod_path = os.path.join(project_root, "")  # nothing to add here. but can
sys.path.append(project_root)


from helper.helper1 import get_help
from mymod import byenow, heythere

from outsider import lokirespose  # using the .env setting


def main():
    print("Hello World!")
    heythere()  # from mymod
    byenow()  # from mymod
    get_help()  # from helper/helper1
    lokirespose()


if __name__ == "__main__":
    main()
