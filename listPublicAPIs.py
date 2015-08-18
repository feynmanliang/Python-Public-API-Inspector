import inspect
import types
import pkgutil
import importlib

import pyspark.ml
import pyspark.mllib

def genFunctions(module):
    """
    For every class inside `module` and public function (i.e. not prefixed by
    "_") inside each class, prints the full path to the function as well as the
    argument list.
    """
    moduleDict = module.__dict__
    for name in dir(module):
        if name.startswith('_'): continue # filter out private modules
        clazz = moduleDict[name]
        if isinstance(clazz, types.TypeType): # only iterate over classes
            for (key, element) in clazz.__dict__.items():
                if isinstance(element, types.FunctionType): # only iterate over methods
                    if element.__name__.startswith('_'): continue # fitler out private methods
                    argSpec = inspect.getargspec(element)
                    argList = argSpec.args
                    print("{}.{}({})".format(module.__name__, element.__name__, ", ".join(argList)))


def listPublicApis():
    for module in [pyspark.ml, pyspark.mllib]:
        for importer, modname, ispkg in pkgutil.walk_packages(module.__path__, module.__name__ + "."):
            if "tests" not in modname:
                mod = importlib.import_module(modname)
                genFunctions(mod)

if __name__ == "__main__":
    listPublicApis()
