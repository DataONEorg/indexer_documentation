README for indexer_documentation
================================

Generates `indexer-documentation.rtfd.io`_ documentation from d1_cn_index_processor_.

This script generates documentation for the DataONE index processor, describing the mapping from source metadata to
solr index fields. It does this by examining the java bean definitions being used for different metadata formats and
generating restructured text documentation showing how solr fields are populated from different content types.

To generate the documentation from a fresh checkout::

  cd indexer_documentation
  make initialize
  make generate
  make html

Generated documents are available for viewing at `indexer-documentation.rtfd.io`_ after pushing changes to GitHub.

.. _indexer-documentation.rtfd.io: http://indexer-documentation.rtfd.io
.. _d1_cn_index_processor: https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/
