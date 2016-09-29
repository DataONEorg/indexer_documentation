{{sp.p['bid']}}
{{sp.p['bid']|U1}}

Format IDs Processed
--------------------

{% for fid in sp.p['matchDocuments'] %}
  * {{ fid }}
{% endfor %}


Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath
{% for fld in sp.p['fields'] %}
  * - {{ fields[fld].p['field_name']|attrList }} ({{fld}}, {{fields[fld].p['cname']|classnameLink}})
    - {{ fields[fld].p['multivalue'] }}
    - {{ fields[fld].p['dedupe'] }}
    - {% if fields[fld].p['xpath'] is defined %}::

        {{ fields[fld].p['xpath']|wrapXPath(60,0,8) }}
{% else %}{% endif %}

{% endfor %}
