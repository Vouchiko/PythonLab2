import random
import os
import shutil
import csv
from typing import Optional


def create_dir(name_dir: str) -> str:
    """This function create directory "dataset2" where we must copy our dataset"""
    if not os.path.isdir(name_dir):
        os.mkdir(name_dir)
    return name_dir


def get_element(name_class: str) -> Optional[str]:
    """this function returns us a list of names in the dataset class"""
    for name_file in os.listdir(os.path.join("dataset", name_class)):
        yield name_file


def create_randname_file(name_annotation: str, dir_copy: str) -> None:
    """This function creates a copy of the dataset so that each file from the source dataset receives a random number
    from 0 to 10000, and the dataset is the following structure dataset/number.jpg. """
    number_file = list(range(10001))
    random.shuffle(number_file)
    count = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir("dataset"):
        for name_file in get_element(dataset_class):
            shutil.copy(os.path.join(os.path.join("dataset", dataset_class), name_file),
                        os.path.join(dir_copy, f"{number_file[count]}.jpg"))
            with open(os.path.join(dir_copy, name_annotation), mode="a", encoding="UTF-16", newline='') as file:
                file_writer = csv.writer(file, delimiter="|")
                file_writer.writerow([f"{number_file[count]}.jpg", dataset_class])
            count += 1


def run3(annotation_name: str, dir_copy: str) -> None:
    create_randname_file(annotation_name, dir_copy)
