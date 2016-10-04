Ecological Markup Language, v2.0.0
==================================

Describes parser configuration for: eml200Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Ecological Metadata Language, version 2.0.0
    | formatId: ``eml://ecoinformatics.org/eml-2.0.0``


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
    - XPath

  * - :attr:`Index.abstract`
    - False
    - False
    - ::

        //dataset/abstract/descendant::text()

      | Processor: `MergeSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/MergeSolrField.java>`_
      | Configuration: `eml.abstract`_


  * - :attr:`Index.keywords`
    - True
    - True
    - ::

        //dataset/keywordSet/keyword/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.keywords`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        //dataset/title/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.title`_


  * - :attr:`Index.project`
    - False
    - False
    - ::

        //dataset/project/title/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.project`_


  * - :attr:`Index.southBoundCoord`
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        southBoundingCoordinate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.southBoundCoord`_
      | Converter: `SolrLatitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLatitudeConverter.java>`_


  * - :attr:`Index.northBoundCoord`
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        northBoundingCoordinate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.northBoundCoord`_
      | Converter: `SolrLatitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLatitudeConverter.java>`_


  * - :attr:`Index.westBoundCoord`
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        westBoundingCoordinate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.westBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.eastBoundCoord`
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        eastBoundingCoordinate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.eastBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.site`
    - True
    - False
    - ::

        //dataset/coverage/geographicCoverage/geographicDescription/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.site`_


  * - :attr:`Index.beginDate`
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/beginDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.beginDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.endDate`
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/endDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.endDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        //dataset/pubDate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.author`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.author`_


  * - :attr:`Index.authorLastName`
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.author_lname`_


  * - :attr:`Index.authorGivenName`
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.authorGivenName`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.authorSurName`_


  * - :attr:`Index.authorGivenNameSort`
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.authorGivenNameSort`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.authorSurNameSort`_


  * - :attr:`Index.investigator`
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.investigator`_


  * - :attr:`Index.origin`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.origin`_


  * - :attr:`Index.contactOrganization`
    - True
    - True
    - ::

        //dataset/creator/organizationName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.contactOrganization`_


  * - :attr:`Index.genus`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Genus"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.genus`_


  * - :attr:`Index.species`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Species"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.species`_


  * - :attr:`Index.kingdom`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Kingdom"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.kingdom`_


  * - :attr:`Index.order`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Order"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.order`_


  * - :attr:`Index.phylum`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Phylum"]/text() | //taxonomicClassification/
        taxonRankValue[../taxonRankName="Division"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.phylum`_


  * - :attr:`Index.family`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Family"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.family`_


  * - :attr:`Index.class`
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Class"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.class`_


  * - :attr:`Index.scientificName`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.scientificName`_


  * - :attr:`Index.attributeName`
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.attributeName`_


  * - :attr:`Index.attributeLabel`
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeLabel/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.attributeLabel`_


  * - :attr:`Index.attributeDescription`
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeDefinition/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.attributeDescription`_


  * - :attr:`Index.attributeUnit`
    - True
    - False
    - ::

        //dataTable//standardUnit/text() | //dataTable//customUnit/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.attributeUnit`_


  * - :attr:`Index.attribute`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.attributeText`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `eml.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - 
    - 
    - 
      | Processor: `AggregateSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/AggregateSolrField.java>`_
      | Configuration: `eml.fullText`_
      | Converter: 


  * - :attr:`Index.geohash_1`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash1`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_2`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash2`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_3`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash3`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_4`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash4`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_5`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash5`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_6`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash6`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_7`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash7`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_8`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash8`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_9`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `eml.geohash9`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.isService`
    - False
    - False
    - ::

        boolean(//software/implementation/distribution/online/url)

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.isService`_


  * - :attr:`Index.serviceTitle`
    - False
    - False
    - ::

        //software/title//text()[normalize-space()]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.serviceTitle`_


  * - :attr:`Index.serviceDescription`
    - False
    - False
    - ::

        //software/abstract//text()[normalize-space()]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.serviceDescription`_


  * - :attr:`Index.serviceEndpoint`
    - True
    - False
    - ::

        //software/implementation/distribution/online/url/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.serviceEndpoint`_



Bean Configurations
-------------------


eml.abstract
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.abstract" class="org.dataone.cn.indexer.parser.MergeSolrField">
	  <constructor-arg name="name" value="abstract"/>
	  <constructor-arg name="xpath" value="//dataset/abstract/descendant::text()"/>
	  <constructor-arg name="delimiter" value=" "/>
	  <property name="multivalue" value="false"/>
	  <property name="dedupe" value="false"/>
	</bean>

	




eml.keywords
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="//dataset/keywordSet/keyword/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.title
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="//dataset/title/text()"/>
		<property name="multivalue" value="false"/>
	</bean>
	
	




eml.project
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.project" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="project"/>
		<constructor-arg name="xpath" value="//dataset/project/title/text()"/>
		<property name="multivalue" value="false"/>
	</bean>	

	




eml.southBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="southBoundCoord"/>
		<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/southBoundingCoordinate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLatitudeConverter"/>
	</bean>

	




eml.northBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="northBoundCoord"/>
		<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/northBoundingCoordinate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLatitudeConverter"/>
	</bean>

	




eml.westBoundCoord
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="westBoundCoord"/>
		<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/westBoundingCoordinate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>

	




eml.eastBoundCoord
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="eastBoundCoord"/>
		<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/eastBoundingCoordinate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>
		
	




eml.site
~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.site" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="site"/>
		<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/geographicDescription/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




eml.beginDate
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.beginDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="beginDate"/>
		<constructor-arg name="xpath" value="//dataset/coverage/temporalCoverage/rangeOfDates/beginDate/calendarDate/text() | //dataset/coverage/temporalCoverage/singleDateTime/calendarDate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="dateConverter"/>
	</bean>

	




eml.endDate
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.endDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="endDate"/>
		<constructor-arg name="xpath" value="//dataset/coverage/temporalCoverage/rangeOfDates/endDate/calendarDate/text() | //dataset/coverage/temporalCoverage/singleDateTime/calendarDate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
	




eml.pubDate
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="//dataset/pubDate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="dateConverter"/>
	</bean>

	




eml.author
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.author" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="eml.authorNameRoot">
			<constructor-arg name="name" value="author"/>
	</bean>
	
	




eml.author_lname
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.author_lname" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorLastName"/>
		<constructor-arg name="xpath" value="//dataset/creator/individualName/surName/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




eml.authorGivenName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenName"/>
		<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/givenName/text()"/>
	</bean>

	




eml.authorSurName
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/surName/text()"/>
	</bean>
	
	




eml.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenNameSort"/>
		<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/givenName/text()"/>
	</bean>

	




eml.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/surName/text()"/>
	</bean>
	
	




eml.investigator
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="//dataset/creator/individualName/surName/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




eml.origin
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.origin" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.originRoot">
		<constructor-arg name="name" value="origin"/>
	</bean>
	
	




eml.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="contactOrganization"/>
		<constructor-arg name="xpath" value="//dataset/creator/organizationName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	




eml.genus
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.genus" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="genus"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Genus&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.species
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.species" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="species"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Species&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.kingdom
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.kingdom" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="kingdom"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Kingdom&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.order
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.order" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="order"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Order&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.phylum
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.phylum" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="phylum"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Phylum&quot;]/text() | //taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Division&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
		
	




eml.family
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.family" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="family"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Family&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	




eml.class
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.class" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="class"/>
		<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Class&quot;]/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	
	




eml.scientificName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.scientificName" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.scientificNameRoot">
			<constructor-arg name="name" value="scientificName"/>
	</bean>
	
	




eml.attributeName
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeName"/>
		<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




eml.attributeLabel
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeLabel" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeLabel"/>
		<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeLabel/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




eml.attributeDescription
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeDescription" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeDescription"/>
		<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeDefinition/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




eml.attributeUnit
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeUnit" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeUnit"/>
		<constructor-arg name="xpath" value="//dataTable//standardUnit/text() | //dataTable//customUnit/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>

	




eml.attributeText
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeText" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.attributeTextRoot">
			<constructor-arg name="name" value="attribute"/>
	</bean>
	
	




eml.fileID
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>
	
	




eml.fullText
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.fullText" class="org.dataone.cn.indexer.parser.AggregateSolrField">
		<property name="name" value="text"/>
		<property name="solrFields">
	   		<list>
	       		<ref bean="eml.text"/>
	       		<ref bean="eml.attributeName.noDupe"/>
	       		<ref bean="eml.attributeLabel.noDupe"/>
	       		<ref bean="eml.attributeDescription.noDupe"/>
	       		<ref bean="eml.attributeUnit.noDupe"/>
	      	</list>
	  	</property>
	</bean>
	
	




eml.geohash1
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_1"/>
		<property name="converter" ref="geohashConverter_1"/>
	</bean>
	
	




eml.geohash2
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_2"/>
		<property name="converter" ref="geohashConverter_2"/>
	</bean>
	
		




eml.geohash3
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_3"/>
		<property name="converter" ref="geohashConverter_3"/>
	</bean>
	
		




eml.geohash4
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_4"/>
		<property name="converter" ref="geohashConverter_4"/>
	</bean>
	
		




eml.geohash5
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_5"/>
		<property name="converter" ref="geohashConverter_5"/>
	</bean>
	
		




eml.geohash6
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_6"/>
		<property name="converter" ref="geohashConverter_6"/>
	</bean>
	
		




eml.geohash7
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_7"/>
		<property name="converter" ref="geohashConverter_7"/>
	</bean>
	
		




eml.geohash8
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_8"/>
		<property name="converter" ref="geohashConverter_8"/>
	</bean>
	
		




eml.geohash9
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">
		<constructor-arg name="name" value="geohash_9"/>
		<property name="converter" ref="geohashConverter_9"/>
	</bean>

	




eml.isService
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.isService" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="isService"/>
		<constructor-arg name="xpath" value="boolean(//software/implementation/distribution/online/url)"/>
	</bean>
	
	




eml.serviceTitle
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceTitle" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceTitle"/>
		<constructor-arg name="xpath" value="//software/title//text()[normalize-space()]"/>
		<property name="combineNodes" value="true"/>
		<property name="combineDelimiter" value=":"/>
	</bean>
	
	




eml.serviceDescription
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceDescription" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceDescription"/>
		<constructor-arg name="xpath" value="//software/abstract//text()[normalize-space()]"/>
		<property name="combineNodes" value="true"/>
		<property name="combineDelimiter" value=":"/>
	</bean>	

	




eml.serviceEndpoint
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceEndpoint"/>
		<constructor-arg name="xpath" value="//software/implementation/distribution/online/url/text()"/>
		<property name="multivalue" value="true"/>
	</bean>	
	
	




