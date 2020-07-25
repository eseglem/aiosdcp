import setuptools

setuptools.setup(
    name="pywattbox",
    version="0.0.1",
    author="Erik Seglem",
    author_email="erik.seglem@gmail.com",
    description="An async python wrapper for SDCP / PJ Talk.",
    url="https://github.com/eseglem/pywattbox",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=True,
)
