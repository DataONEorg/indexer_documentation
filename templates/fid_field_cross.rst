{#
This Jinja2 template is used by the generator to output a matrix cross referencing
formatId with solr field
#}

Field x FormatId Cross Reference
================================

.. csv-table:: FormatId x Solr Field
   :header: {{csvheader}}

   {%for row in csvrows%}{{row}}
   {% endfor %}

