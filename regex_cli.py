"""
"""
import re
from colorama import Fore


def check_regex_validity(regex,query_string):
    try:
        pattern = re.compile(regex)
        is_valid = True
    except re.error as e:
        print(re.error)
        is_valid = False

    if re.match(pattern,query_string) != None and is_valid:
        print(f"{Fore.GREEN} Query String Is Valid")
        return True

    else:
        print(f"{Fore.RED} Query String Is Invalid")
        return False
 

if __name__ == "__main__":
    regex = input("Please enter your regex expression: ")

    query_string = input("Please enter the query string: ")
    check_regex_validity(regex,query_string)