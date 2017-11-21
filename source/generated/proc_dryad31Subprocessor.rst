Dryad 3.1
=========

Describes parser configuration for: dryad31Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Dryad Metadata Application Profile Version 3.1
    | formatId: ``http://datadryad.org/profile/v3.1``


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

        //dcterms:description[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.abstract`_


  * - :attr:`Index.author`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.author`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorSurNameSort`_


  * - :attr:`Index.authorGivenName`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorGivenName`_


  * - :attr:`Index.authorGivenNameSort`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorGivenNameSort`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        //dcterms:creator/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.investigator`_


  * - :attr:`Index.keywords`
    - True
    - False
    - ::

        //dcterms:subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.keywords`_


  * - :attr:`Index.origin`
    - True
    - True
    - ::

        //dcterms:creator/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.origin`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        //dcterms:dateSubmitted/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.site`
    - True
    - False
    - ::

        //dcterms:spatial/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.site`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        //dcterms:title[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.title`_


  * - :attr:`Index.scientificName`
    - True
    - False
    - ::

        //dwc:scientificName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.scientificName`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `dryad.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `dryad.fullText`_



Bean Configurations
-------------------


dryad.abstract
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.abstract" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="abstract"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:description[1]/text()"/>\n\t</bean>\n\n\t\n'


dryad.author
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.author" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="author"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>\n\t</bean>\n\t\n\t\n'


dryad.authorSurName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\n\t\n\t\n'


dryad.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\t\n\t\n\t\n'


dryad.authorGivenName
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenName"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>\n\t\t<property name="substringAfter" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\n\t\n\t\n'


dryad.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenNameSort"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>\n\t\t<property name="substringAfter" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\t\n\t\n\t\n'


dryad.investigator
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


dryad.keywords
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:subject/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


dryad.origin
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.origin" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="origin"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:creator/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


dryad.pubDate
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.pubDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="pubDate"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:dateSubmitted/text()"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\t\n \t\n'


dryad.site
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.site" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="site"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:spatial/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\t\n\t\n'


dryad.title
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="//dcterms:title[1]/text()"/>\n\t</bean>\n \n \t\n'


dryad.scientificName
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.scientificName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="scientificName"/>\n\t\t<constructor-arg name="xpath" value="//dwc:scientificName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\n\t\n'


dryad.fileID
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t<constructor-arg name="name" value="fileID"/>\n\t</bean>\n\t\n\t\n'


dryad.fullText
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">\n\t\t<constructor-arg name="name" value="text"/>\n\t\t<constructor-arg name="xpath" value="//*/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t</bean>\n\t\n\n'


