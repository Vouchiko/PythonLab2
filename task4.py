import os
from typing import Optional


def get_element(class_tag: str) -> Optional[str]:
    """This function gets the class label and returns the next class element"""
    path = os.path.join("dataset", class_tag)
    names_file = os.listdir(path)
    names_file.append(None)
    for i in range(len(names_file)):
        yield names_file[i]

