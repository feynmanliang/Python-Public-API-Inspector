# Spark ML/MLlib Public Python API Listing Tool

A tool for listing the public API of a Python module. Currently used for
reviewing Apache Spark's MLlib / ML Pipeline Python API, but could be
easily adapted to suit your needs by modifying the `module`s iterated
over in `listPublicApis()`.

Iterates over all modules under `pyspark.ml` and `pyspark.mllib`.

For each module, iterates over all classes.

For each class, iterates over all public functions (i.e. not prefixed by
"\_") and prints out the full path to the function and the argument
list.

## Directions

Requires Python 2.7.

 1. `cp listPublicAPIs.py /path/to/spark/python`
 2. `cd /path/to/spark && python listPublicAPIs.py > apiListing.txt`
