{#
This Jinja2 template is used by the generator to output a matrix cross referencing
formatId with solr field
#}

Field x FormatId Cross Reference
================================

.. list-table::
   :header-rows: 1
   :widths: 1 5

   * - Index
     - FormatId
   {%for entry in ffmatrix.colmeta%}* - {{loop.index}}
     - {{entry}}
   {% endfor %}


The following table indicates which formatIds have processing rules defined to set index field values when processing
metadata. In the table, an "S" means the property is set from system metadata, an "X" means there is a rule defined
to set the value, and blank indicates no rules are setting the field value (though Solr copy fields are not considered
here).

.. csv-table:: FormatId x Solr Field
   :header: {{csvheader}}

   {%for row in csvrows%}{{row}}
   {% endfor %}


