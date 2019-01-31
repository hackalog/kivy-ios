from toolchain import CythonRecipe

class PyobjusRecipe(CythonRecipe):
    version = "master"
    owner = "hackalog"
    url = "https://github.com/{owner}/pyobjus/archive/{version}.zip"
    library = "libpyobjus.a"
    depends = ["python"]
    pre_build_ext = True


recipe = PyobjusRecipe()
