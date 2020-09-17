import setuptools

setuptools.setup(
    name                            = "tutorial-resource",
    description                     = "Other metrics for models in orquestra.",
    url                             = "https://github.com/luisguiserrano/other-metrics",
    packages                        = setuptools.find_packages(where = "python"),
    package_dir                     = {"" : "python"},
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "sklearn",
        "numpy",
   ],
)