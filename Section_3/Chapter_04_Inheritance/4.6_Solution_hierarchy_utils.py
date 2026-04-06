def show_hierarchy(cls):
    # TODO: Print the class hierarchy for the given class
    # TODO: Print "Class hierarchy for [class name]:"
    # TODO: Use cls.__mro__ to iterate through and print each class name in the hierarchy
    print(f"Class hierarchy for {cls.class_name}:")

    cls_mro_list = cls.__mro__
    for i in cls_mro_list:
        print(i.__name__)
