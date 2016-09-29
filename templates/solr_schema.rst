Solr Fields Defined
===================

A list of the fields defined in the solr search index used by the Coordinating Nodes.

.. list-table::
   :header-rows: 1

   * - Field
     - Type
     - MV
     - Store
     - Index
{% for fld in fields %}   * - {{fld.name}}
     - {{fld.type}}
     - {{fld.multiValued}}
     - {{fld.stored}}
     - {{fld.indexed}}
{% endfor %}

