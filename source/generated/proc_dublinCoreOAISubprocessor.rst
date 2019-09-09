dublinCoreOAISubprocessor
=========================

Describes parser configuration for: dublinCoreOAISubprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | OAI-PMH Dublin Core v2.0, with online related resource
    | formatId: ``http://www.openarchives.org/OAI/2.0/oai_dc/``


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

  * - :attr:`Index.abstract`
    - False
    - False
    - ::

        //*[local-name() = 'description'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.description`_


  * - :attr:`Index.originator`
    - True
    - True
    - ::

        //*[local-name() = 'publisher']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.publisher`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        //*[local-name() = 'date'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.date`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        //*[local-name() = 'contributor']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.contributor`_


  * - :attr:`Index.author`
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.author`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.authorSurNameSort`_


  * - :attr:`Index.contactOrganization`
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.contactOrganization`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.investigator`_


  * - :attr:`Index.origin`
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.origin`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        (//*[local-name() = 'title'][1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.title`_


  * - :attr:`Index.keywords`
    - True
    - False
    - ::

        //*[local-name() = 'subject']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.keywords`_


  * - :attr:`Index.serviceEndpoint`
    - True
    - False
    - ::

        //*[local-name() = 'relation']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc:relation`_


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `dc.fullText`_



Bean Configurations
-------------------


dc.description
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.description" class="org.dataone.cn.indexer.parser.SolrField">\n        <constructor-arg name="name" value="abstract"/>\n        <constructor-arg name="xpath" value="//*[local-name() = \'description\'][1]/text()"/>\n    </bean>\n    \n    \n'


dc.publisher
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.publisher" class="org.dataone.cn.indexer.parser.SolrField">\n        <constructor-arg name="name" value="originator"/>\n        <constructor-arg name="xpath" value="//*[local-name() = \'publisher\']/text()"/>\n        <property name="multivalue" value="true"/>\n        <property name="dedupe" value="true"/>\n    </bean>\n    \n    \n'


dc.date
~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.date" class="org.dataone.cn.indexer.parser.SolrField">\n        <constructor-arg name="name" value="pubDate"/>\n        <constructor-arg name="xpath" value="//*[local-name() = \'date\'][1]/text()"/>\n        <property name="converter" ref="dateConverter"/>\n    </bean>\n    \n    \n'


dc.contributor
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.contributor" class="org.dataone.cn.indexer.parser.SolrField">\n        <constructor-arg name="name" value="investigator"/>\n        <constructor-arg name="xpath" value="//*[local-name() = \'contributor\']/text()"/>\n        <property name="multivalue" value="true"/>\n        <property name="dedupe" value="true"/>\n    </bean>\n\n'


dc.author
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.author" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="author"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\'][1]/text()"/>\n\t</bean>\n\t\n\t\n'


dc.authorSurName
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\'][1]/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\n\t\n'


dc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\'][1]/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\t\n\t\n'


dc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="contactOrganization"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\']/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\t\n\t\n\t\n'


dc.investigator
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\']/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


dc.origin
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.origin" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="origin"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'creator\']/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


dc.title
~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="(//*[local-name() = \'title\'][1]/text())[1]"/>\n\t</bean>\n\n\t\n'


dc.keywords
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="//*[local-name() = \'subject\']/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\n\t\n'


dc:relation
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc:relation" class="org.dataone.cn.indexer.parser.SolrField">\n\t    <constructor-arg name="name" value="serviceEndpoint"/>\n        <constructor-arg name="xpath" value="//*[local-name() = \'relation\']/text()"/>\n        <property name="multivalue" value="true"/>\n    </bean>\n    \n    \n'


dc.fullText
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">\n\t\t<constructor-arg name="name" value="text"/>\n\t\t<constructor-arg name="xpath" value="//*/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t</bean>\n\n'


