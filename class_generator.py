import numpy as np
from library import *


class SimpleClassGenerator:
    def __init__(self, name="", attribute_names=[], default_val=[], wrepr=False):
        self.name = name
        self.attribute_names = attribute_names
        self.default_val = default_val
        self.wrepr = wrepr

    def dump(self, filename):
        with open(filename, "w") as f:
            f.write(self.dumps())

    def input_default_val():
        default = input("Default value: ")
        if "'" in default or '"' in default:
            return default
        return eval(default)

    def generate():
        n = int(input("Classes: "))
        for i in range(n):
            cname = input("Class name: ")
            latrr = int(input("Number of atrributes: "))
            [attribute_names, default_val] = transpose(
                [
                    [
                        input("Attribute name: "),
                        SimpleClassGenerator.input_default_val(),
                    ]
                    for x in range(latrr)
                ]
            )
            wrepr = input("With repr[Y/N]: ").upper() == "Y"
            cl = SimpleClassGenerator(cname, attribute_names, default_val, wrepr)
            cl.dump(input("Folder: ") + cname + ".py")
            print("Saved")
            print("\n\nResult:\n")
            print(cl, "\n")

    def dumps(self):
        text = (
            f"class {self.name}:\n"
            "    def __init__(self, "
            + ", ".join(
                [
                    name + "=" + default.__repr__()
                    for name, default in zip(self.attribute_names, self.default_val)
                ]
            )
            + "):\n        "
            + "\n        ".join(
                ["self." + name + " = " + name for name in self.attribute_names]
            )
            + "\n"
        )
        if self.wrepr:
            text = (
                text
                + "    def __repr__(self):\n"
                + "        return "
                + ' + "\\n" + \\\n               '.join(
                    [
                        '"' + name + ': " + self.' + name + ".__repr__()"
                        for name in self.attribute_names
                    ]
                )
                + "\n"
            )
        return text

    def __repr__(self):
        return (
            self.name
            + ":\n  Atrributes:\n    "
            + "\n    ".join(
                [
                    name + ": " + default.__repr__()
                    for name, default in zip(self.attribute_names, self.default_val)
                ]
            )
            + "\n  With repr:"
            + "Yes" * int(self.wrepr)
            + "No" * int(not (self.wrepr))
            + "\n"
        )


if __name__ == "__main__":
    SimpleClassGenerator.generate()
