Namespaces Referenced
=====================

A compilation of XML namespaces and their abbrievations used by the Index Parser.

.. list-table::
    :widths: 1, 5
    :header-rows: 1

    * - Prefix
      - Namespace
{% for ns in namespaces[0].p['namespaces'] %}    * - {{ ns.p['prefix'] }}
      - {{ ns.p['namespace'] }}
{% endfor %}


