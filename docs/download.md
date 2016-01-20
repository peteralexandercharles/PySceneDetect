
# Obtaining PySceneDetect

PySceneDetect is completely free software, and can be downloaded from the links below.  See the [license and copyright information](copyright.md) page for details.  PySceneDetect is written in a portable manner, and works cross-platform wherever a Python interpreter and OpenCV can run.  If you have problems running PySceneDetect, ensure that you have all the required dependencies listed in the System Requirements section below.

## Download

###  Source (All Platforms) &nbsp; <span class="fa fa-windows"></span> &nbsp; <span class="fa fa-linux"></span> &nbsp; <span class="fa fa-apple"></span>

<div class="danger">
<h3><span class="fa fa-forward"></span> Latest Release: <b>v0.3.0.1-beta</b></h3>
<h4><span class="fa fa-calendar"></span>&nbsp; Release Date:&nbsp; <b>January 20, 2016</b></h4>
<a href="https://github.com/Breakthrough/PySceneDetect/releases" class="btn btn-success" role="button"><span class="fa fa-download"></span>&nbsp; Download</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="../changelog/" class="btn btn-info" role="button"><span class="fa fa-reorder"></span>&nbsp; Changelog</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="#installation" class="btn btn-warning" role="button"><span class="fa fa-gear"></span>&nbsp; Installation Instructions</a>
</div>

Once you've downloaded the source files, extract them to a location of your choice, and make sure you obtain the following system requirements before installing PySceneDetect.  PySceneDetect can then be installed by calling `python setup.py install` from the location of the extracted files (see [the Installation section](#installation) below for details), after which you can call PySceneDetect from any terminal by typing `scenedetect`.  Try running `scenedetect --version` to verify that everything was installed correctly.


## Installation

Start by downloading the latest release of PySceneDetect and extracting it to a location of your choice.  Then, follow the instructions below under [Installing Dependencies](#installing-dependencies) to ensure you have all the system requirements.  Finally, run the commands in [Installing PySceneDetect](#installing-pyscenedetect) to install the program, allowing you to run the `scenedetect` command from any terminal/command prompt.


### Installing Dependencies

PySceneDetect requires [Python 2 or 3](https://www.python.org/) (tested on 2.7.X, untested but should work on 3.X) and the following libraries ([quick install guide](http://breakthrough.github.io/Installing-OpenCV/)):

 - [OpenCV](http://opencv.org/) (compatible with both 2.X or 3.X) and the Python module (`cv2`)
 - [Numpy](http://sourceforge.net/projects/numpy/) Python module (`numpy`)

You can [click here](http://breakthrough.github.io/Installing-OpenCV/) for a quick guide (OpenCV + Numpy on Windows & Linux) on installing the latest versions of OpenCV/Numpy on [Windows (using pre-built binaries)](http://breakthrough.github.io/Installing-OpenCV/#installing-on-windows-pre-built-binaries) and [Linux (compiling from source)](http://breakthrough.github.io/Installing-OpenCV/#installing-on-linux-compiling-from-source).  If the Python module that comes with OpenCV on Windows is incompatible with your system architecture or Python version, [see this page](http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv) to obtain a pre-compiled (unofficial) module.

Note that some Linux package managers still provide older, dated builds of OpenCV (pre-3.0).  PySceneDetect is compatible with both versions, but if you want to ensure you have the latest version, it's recommended that you [build and install OpenCV from source](http://breakthrough.github.io/Installing-OpenCV/#installing-on-linux-compiling-from-source) on Linux.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
To ensure you have all the requirements installed, open a `python` interpreter, and ensure you can run `import numpy` and `import cv2` without any errors.  Once this is done, you're ready to instalL PySceneDetect!


### Installing PySceneDetect

Go to the folder you extracted the PySceneDetect source code to, and run the following command (may require root):

```rst
python setup.py install
```

Once finished, PySceneDetect will be installed, and you should be able to run the `scenedetect` command.  To verify that everything was installed properly, try calling the following command:

```rst
scenedetect --version
```

To get familiar with PySceneDetect, try running `scenedetect --help`, or continue onwards to the [Getting Started: Basic Usage](examples/usage.md) section.  If you encounter any runtime errors while running PySceneDetect, ensure that you have all the required dependencies listed in the System Requirements section above (again, you should be able to `import numpy` and `import cv2`).  PySceneDetect is still beta software, so feel free to [report any bugs or share some feature requests/ideas](contributing.md) and help make PySceneDetect even better.
