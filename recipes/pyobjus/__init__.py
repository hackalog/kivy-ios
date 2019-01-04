from toolchain import CythonRecipe

class PyobjusRecipe(CythonRecipe):
    version = "llf_stable"
    url = "https://github.com/learnleapfly/pyobjus/archive/{version}.zip"
    library = "libpyobjus.a"
    depends = ["python"]
    pre_build_ext = True


recipe = PyobjusRecipe()
