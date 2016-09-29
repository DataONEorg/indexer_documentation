.. module:: Index

.. currentmodule:: Index

Solr Fields Defined
===================

A list of the fields defined in the solr search index used by the Coordinating Nodes.

.. list-table::
   :header-rows: 1
   :widths: 3, 2, 1, 1, 1, 10

   * - Field
     - Type
     - MV
     - Store
     - Index
     - Description
{% for fld in fields %}   * - .. attribute:: {{fld.name}}
     - {{fld.type}}
     - {{fld.multiValued}}
     - {{fld.stored}}
     - {{fld.indexed}}
     - {{fld.name|solrFieldDescription}}
{% endfor %}

