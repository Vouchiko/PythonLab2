import os
import csv


def create_annotation(class_name: str, annotation_name: str) -> None:
    """This function creates a cvs file with three parameters: the absolute path to the file, the relative path to the
    file and the class label """
    path_class = os.path.join('dataset', class_name)
    class_names = os.listdir(path_class)
    with open(annotation_name, mode="w", encoding="UTF-16", newline='') as file:
        file_writer = csv.writer(file, delimiter=',')
        for name in class_names:
            file_writer.writerow([os.path.abspath(name), os.path.join(path_class, name), class_name])


def run1(class_name: str, annotation_name: str) -> None:
    create_annotation(class_name, annotation_name)
