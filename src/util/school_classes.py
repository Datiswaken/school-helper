from os import listdir
from os.path import isfile, join


def get_school_class_names():
    path = "school_classes"
    school_classes = listdir(path)
    relevant_classes = [
        school_class
        for school_class
        in school_classes
        if isfile(join(path, school_class)) and school_class[-4:] == ".txt"
    ]
    return [school_class[:-4] for school_class in relevant_classes]
