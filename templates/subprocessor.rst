{{ sp.p['bid']|subprocessorName}}

Describes parser configuration for: {{sp.p['bid']}}

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:

{% for fid in sp.p['matchDocuments'] %}
  * | {{ fid|describeFormatId }}
    | formatId: ``{{ fid }}``
{% endfor %}

A full list of DataONE format IDs can be found at https://cn.dataone.org/cn/v2/formats/

Fields
------

The following fields in the solr index are populated from values retrieved from this type of metadata document.
Note that these are in addition to the information extracted from :doc:`system_metadata`.

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - Source
{% for fld in sp.p['fields'] %}
  * - {{ fields[fld].p['field_name']|attrList }}
    - {{ fields[fld].p['multivalue'] }}
    - {{ fields[fld].p['dedupe'] }}
    - {% if 'xpath' in fields[fld].p %}::

        {{ fields[fld].p['xpath']|wrapXPath(60,0,8) }}
{% elif 'query' in fields[fld].p %}::

        {{ fields[fld].p['query']|sparqlTrim }}
{% else %}{% endif %}
      | Processor: {{fields[fld].p['cname']|classnameLink}}
      | Configuration: `{{fld}}`_
{% if fields[fld].p['converter'] != '' %}      | Converter: {{fields[fld].p['converter']|getConverterInfo|classnameLink }}
{% endif %}
{% endfor %}

Bean Configurations
-------------------

{% for fld in sp.p['fields'] %}
{{fld}}
{{fld|U3}}

.. code-block:: xml

   {{fields[fld].p['xml']}}

{% endfor %}

