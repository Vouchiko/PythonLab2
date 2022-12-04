from email import generator
import os


def get_element(class_tag: str) -> generator:
    path = os.path.join("dataset", class_tag)
    names_list = os.listdir(path)
    names_list.append(None)
    mgenerator = (item for item in names_list)
    for i in mgenerator:
        yield i
