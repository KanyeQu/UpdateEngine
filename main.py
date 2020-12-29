import os
import sys
from typing import List

TESTDIR = "C:\\Users\\Administrator\\Desktop\\TestDir"
DESKTOP = "C:\\Users\\Administrator\\Desktop"
print("UpdateEngine: to help you identify outdated files in current work dir. Author: Zixi QU")
print()


def get_all_file(dir: str) -> List[str]:
    """
    return all items recursively in <path>.
    """
    result = []
    for each in os.listdir(dir):
        if os.path.isdir(each):
            subpath = get_all_file(each)
            for subfiles in subpath:
                result.append(each + "\\" +subfiles)
        else:
            result.append(each)
    return result


def get_difference(master: List, client: List) -> (List, List):
    """ given the list of file list <lst>. Return the difference in tuple.
    @:return: redundant list, extra list
    """
    redundant = []
    extra = []
    for each in master:
        if each not in client:
            extra.append(each)
    for each in client:
        if each not in master:
            redundant.append(each)
    return redundant, extra


def read_ue_file(f) -> List:
    """ return the master list by reading file <f>"""
    result = []
    for each in f:
        result.append(each.strip())
    return result


def make_ue_file(master: List) -> bool:
    """ make the .ue file under <path> with information <master> list
    If path is not valid, return
    """
    try:
        with open("master.ue", "w") as f:
            for each in master:
                f.write(each + "\n")
        print("successfully created a .ue file on " + os.getcwd())
        return True
    except Exception as e:
        print("failed to create a .ue file on " + os.getcwd())
        return False


def main():
    """ wish to implement with GUI

    working float:

    """
    dir = TESTDIR
    # dir = input("dir?:")

    if os.path.exists(dir):
        os.chdir(dir)

    else:
        print("failed: dir not exist")

    print(os.getcwd())


if __name__ == "__main__":
    # main()
    os.chdir(TESTDIR)
    lst = get_all_file(os.getcwd())

    os.chdir(DESKTOP)
    make_ue_file(lst)

    # with open("master.ue") as f:
    #     for each in f:
    #         print(each.strip())




