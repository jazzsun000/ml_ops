import argparse

def choose_linter():
    # replace this with your code to choose a linter
    linter = "flake8"
    return linter

def choose_coding_style():
    # replace this with your code to choose a coding style
    coding_style = "PEP 8"
    return coding_style

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--linter", help="choose a linter")
    parser.add_argument("--coding_style", help="choose a coding style")
    args = parser.parse_args()

    linter = args.linter or choose_linter()
    coding_style = args.coding_style or choose_coding_style()

    print("Linter: ", linter)
    print("Coding Style: ", coding_style)
