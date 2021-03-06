{#
This Jinja2 template is used by the generator to create the solr field list
restructured text document.
#}
.. module:: Index

.. currentmodule:: Index

Solr Index Fields
=================

A list of the fields defined in the solr search index used by the Coordinating Nodes.

These fields are populated by the index processor using values drawn from
:class:`API:Types.SystemMetadata`, :term:`Science Metadata`, and :term:`Resource Map`
documents.

.. note:: For Editors

   Definitions are drawn from the `solr configuration file`_ and descriptions for each
   field are contained in a separate properties file
   (``dataone-cn-solr/usr/share/dataone-cn-solr/debian/queryFieldDescriptions.properties``). After editing
   descriptions, the document source must be regenerated and committed to GitHub for
   the public facing documentation to be updated.

Static Fields
-------------

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

Dynamic Fields
--------------

.. list-table::
   :header-rows: 1
   :widths: 3, 2, 1, 1, 1, 10

   * - Field
     - Type
     - MV
     - Store
     - Index
     - Description
{% for fld in dynfields %}   * - .. attribute:: {{fld.name}}
     - {{fld.type}}
     - {{fld.multiValued}}
     - {{fld.stored}}
     - {{fld.indexed}}
     - {{fld.name|solrFieldDescription}}
{% endfor %}

.. _solr configuration file: {{"resources/index-solr-schema.xml"|svnRepoLink}}
