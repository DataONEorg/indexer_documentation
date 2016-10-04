Dublin Core, Qualified
======================

Describes parser configuration for: qualifiedDublicCoreSubprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Unknown
    | formatId: ``http://dublincore.org/schemas/xmls/qdc/2008/02/11/qualifieddc.xsd``



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
    - XPath

  * - :attr:`Index.abstract`
    - False
    - False
    - ::

        //*[local-name() = 'abstract'][1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.abstract`_


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


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        //*[local-name() = 'dateSubmitted']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


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


  * - :attr:`Index.beginDate`
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.beginDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.endDate`
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.endDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.site`
    - True
    - True
    - ::

        //*[local-name() = 'spatial'][not(@xsi:type = 'dcterms:Box')
         and not(@xsi:type = 'dc:Box') and not(@xsi:type = 
        'Box')]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dc.site`_


  * - :attr:`Index.northBoundCoord`, :attr:`Index.southBoundCoord`, :attr:`Index.eastBoundCoord`, :attr:`Index.westBoundCoord`
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]

      | Processor: `DublinCoreSpatialBoxBoundingCoordinatesSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/DublinCoreSpatialBoxBoundingCoordinatesSolrField.java>`_
      | Configuration: `dc.boxSpatialBoundCoordinates`_


  * - :attr:`Index.geohash_1`, :attr:`Index.geohash_2`, :attr:`Index.geohash_3`, :attr:`Index.geohash_4`, :attr:`Index.geohash_5`, :attr:`Index.geohash_6`, :attr:`Index.geohash_7`, :attr:`Index.geohash_8`, :attr:`Index.geohash_9`
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]

      | Processor: `DublinCoreSpatialBoxGeohashSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/DublinCoreSpatialBoxGeohashSolrField.java>`_
      | Configuration: `dc.boxSpatialGeohash`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `dc.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `dc.fullText`_



Bean Configurations
-------------------


dc.abstract
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.abstract" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="abstract"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'abstract'][1]/text()"/>
	</bean>
	
	




dc.author
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.author" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="author"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator'][1]/text()"/>
	</bean>
	
	




dc.authorSurName
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator'][1]/text()"/>
		<property name="multivalue" value="false"/>
	</bean>

	




dc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator'][1]/text()"/>
		<property name="multivalue" value="false"/>
	</bean>
	
	




dc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="contactOrganization"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator']/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>	
	
	




dc.investigator
~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator']/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	




dc.origin
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.origin" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="origin"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'creator']/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	




dc.pubDate
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'dateSubmitted']/text()"/>
		<property name="converter" ref="dateConverter"/>
	</bean>

	




dc.title
~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="(//*[local-name() = 'title'][1]/text())[1]"/>
	</bean>

	




dc.keywords
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'subject']/text()"/>
		<property name="multivalue" value="true"/>
	</bean>

	




dc.beginDate
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.beginDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="beginDate"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'temporal'][not(@xsi:type='dcterms:Period') and not(@xsi:type='dc:Period') and not(@xsi:type='Period')]/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="dateConverter"/>
	</bean>

	




dc.endDate
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.endDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="endDate"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'temporal'][not(@xsi:type='dcterms:Period') and not(@xsi:type='dc:Period') and not(@xsi:type='Period')]/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
	




dc.site
~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.site" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="site"/>
		<constructor-arg name="xpath" value="//*[local-name() = 'spatial'][not(@xsi:type = 'dcterms:Box') and not(@xsi:type = 'dc:Box') and not(@xsi:type = 'Box')]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>	

	




dc.boxSpatialBoundCoordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.boxSpatialBoundCoordinates" class="org.dataone.cn.indexer.parser.DublinCoreSpatialBoxBoundingCoordinatesSolrField">
		<constructor-arg name="xpath" value="//*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]"/>
	</bean>
	
	




dc.boxSpatialGeohash
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.boxSpatialGeohash" class="org.dataone.cn.indexer.parser.DublinCoreSpatialBoxGeohashSolrField">
		<constructor-arg name="xpath" value="//*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]"/>
	</bean>

	




dc.fileID
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>
	
	




dc.fullText
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dc.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">
		<constructor-arg name="name" value="text"/>
		<constructor-arg name="xpath" value="//*/text()"/>
		<property name="combineNodes" value="true"/>
	</bean>





