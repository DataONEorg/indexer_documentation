README for index_processor_doc
==============================

This script generates documentation for the DataONE index processor, describing the mapping from source metadata to
solr index fields. It does this by examining the java bean definitions being used for different metadata formats and
generating restructured text documentation showing how solr fields are populated from different content types.

To generate the documentation from a fresh checkout::

  cd index_processor_doc
  make initialize
  make generate
  make html

