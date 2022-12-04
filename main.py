from task1 import run1
from task2 import run2
from task3 import run3
from task4 import get_element


if __name__ == '__main__':
    run1('brown bear', 'annotation.csv')
    run2('dataset-copy', 'annotation.csv')
    run3('annotation.csv', 'dataset2')
    for i in get_element('polar bear'):
        print(i)
