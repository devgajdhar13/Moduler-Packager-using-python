import importlib


def explore_module():

    module_name = input("Enter module name to explore: ")

    try:

        module = importlib.import_module(module_name)

        attributes = dir(module)

        print(f"\nAvailable Attributes in "f"{module_name} module:")

        print(attributes)

    except ModuleNotFoundError:

        print("Module not found!")

    except Exception as error:

        print("Error:",error)