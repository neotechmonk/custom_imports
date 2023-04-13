from helper.helper1 import get_help
from insider import insider_response  # Relative path
from mymod import byenow, heythere

# from ..outsider.helper2 import lokirespose # wont work as outsider is the same level as app


def main():
    print("Hello World!")
    heythere()  # from mymod
    byenow()  # from mymod
    get_help()  # from helper/helper1
    insider_response()
    lokirespose()


if __name__ == "__main__":
    main()
