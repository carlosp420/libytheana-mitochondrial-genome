This folder contains all the derived data.

Derived data is data that can be regenerated by running the analysis
scripts. If this folder is deleted, its entire content should be fully
generated again when running the whole pipeline.

Typically, this content will also depend on some primary data stored in
data/primary/. It might be also that derived data is generated by a script
downloading data from a public database (e.g. script sending a query to
GenBank).

This folder should not be backed up nor version-controlled since it can be
generated from the primary data and the analysis scripts. However, if the
derived data depends on some remote database which can be updated between
analyses, it might be necessary to back up or version-control some of these
files to ensure reproducibility to a previous state.