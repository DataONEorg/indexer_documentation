System Metadata Parser
======================


Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath
{% for fld in sp.p['fieldList'] %}
  * - {{ fields[fld].p['field_name']|attrList }}
    - {{ fields[fld].p['multivalue'] }}
    - {{ fields[fld].p['dedupe'] }}
    - {% if fields[fld].p['xpath'] is defined %}::

        {{ fields[fld].p['xpath']|wrapXPath(60,0,8) }}
{% else %}{% endif %}
      | Processor: {{fields[fld].p['cname']|classnameLink}}
      | Configuration: `{{fld}}`_
{% if fields[fld].p['converter'] != '' %}      | Converter: {{fields[fld].p['converter']|getConverterInfo|classnameLink }}
{% endif %}
{% endfor %}

Bean Configurations
-------------------

{% for fld in sp.p['fieldList'] %}
{{fld}}
{{fld|U3}}

.. code-block:: xml

   {{fields[fld].p['xml']}}


{% endfor %}

