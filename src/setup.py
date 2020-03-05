from distutils.core import setup
setup(
    name="random-facts",
    version="1.0.4",
    description="A powerfull , flexible and modern python module to retrieve random useless facts from the mighty web . View more on the github page",
    url="https://github.com/Jakeisbored/random-facts",
    author="Jake",
    author_email="jstyle07072004@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=["requests"]
)