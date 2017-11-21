Ecological Markup Language, v2.0.1
==================================

Describes parser configuration for: eml201Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Ecological Metadata Language, version 2.0.1
    | formatId: ``eml://ecoinformatics.org/eml-2.0.1``


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


  * - :attr:`Index.authorLastName`
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `eml.author_lname`_


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

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.abstract" class="org.dataone.cn.indexer.parser.MergeSolrField">\n\t  <constructor-arg name="name" value="abstract"/>\n\t  <constructor-arg name="xpath" value="//dataset/abstract/descendant::text()"/>\n\t  <constructor-arg name="delimiter" value=" "/>\n\t  <property name="multivalue" value="false"/>\n\t  <property name="dedupe" value="false"/>\n\t</bean>\n\n\t\n'


eml.keywords
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="//dataset/keywordSet/keyword/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.title
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="//dataset/title/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\t\n\t\n'


eml.project
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.project" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="project"/>\n\t\t<constructor-arg name="xpath" value="//dataset/project/title/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\t\n\n\t\n'


eml.southBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="southBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/southBoundingCoordinate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLatitudeConverter"/>\n\t</bean>\n\n\t\n'


eml.northBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="northBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/northBoundingCoordinate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLatitudeConverter"/>\n\t</bean>\n\n\t\n'


eml.westBoundCoord
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="westBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/westBoundingCoordinate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\n\n\t\n'


eml.eastBoundCoord
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="eastBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/boundingCoordinates/eastBoundingCoordinate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\n\t\t\n\t\n'


eml.site
~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.site" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="site"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/geographicCoverage/geographicDescription/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


eml.beginDate
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.beginDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="beginDate"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/temporalCoverage/rangeOfDates/beginDate/calendarDate/text() | //dataset/coverage/temporalCoverage/singleDateTime/calendarDate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\n\t\n'


eml.endDate
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.endDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="endDate"/>\n\t\t<constructor-arg name="xpath" value="//dataset/coverage/temporalCoverage/rangeOfDates/endDate/calendarDate/text() | //dataset/coverage/temporalCoverage/singleDateTime/calendarDate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\t\n\t\n'


eml.pubDate
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.pubDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="pubDate"/>\n\t\t<constructor-arg name="xpath" value="//dataset/pubDate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\n\t\n'


eml.author
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.author" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="eml.authorNameRoot">\n\t\t\t<constructor-arg name="name" value="author"/>\n\t</bean>\n\t\n\t\n'


eml.authorGivenName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenName"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/givenName/text()"/>\n\t</bean>\n\n\t\n'


eml.authorSurName
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/surName/text()"/>\n\t</bean>\n\t\n\t\n'


eml.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenNameSort"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/givenName/text()"/>\n\t</bean>\n\n\t\n'


eml.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator[1]/individualName[1]/surName/text()"/>\n\t</bean>\n\t\n\t\n'


eml.author_lname
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.author_lname" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorLastName"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator/individualName/surName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


eml.investigator
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator/individualName/surName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


eml.origin
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.origin" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.originRoot">\n\t\t<constructor-arg name="name" value="origin"/>\n\t</bean>\n\t\n\t\n'


eml.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="contactOrganization"/>\n\t\t<constructor-arg name="xpath" value="//dataset/creator/organizationName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


eml.genus
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.genus" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="genus"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Genus&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.species
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.species" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="species"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Species&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.kingdom
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.kingdom" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="kingdom"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Kingdom&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.order
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.order" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="order"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Order&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.phylum
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.phylum" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="phylum"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Phylum&quot;]/text() | //taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Division&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\t\n\t\n'


eml.family
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.family" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="family"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Family&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


eml.class
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.class" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="class"/>\n\t\t<constructor-arg name="xpath" value="//taxonomicClassification/taxonRankValue[../taxonRankName=&quot;Class&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n\t\n'


eml.scientificName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.scientificName" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.scientificNameRoot">\n\t\t\t<constructor-arg name="name" value="scientificName"/>\n\t</bean>\n\t\n\t\n'


eml.attributeName
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeName"/>\n\t\t<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


eml.attributeLabel
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeLabel" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeLabel"/>\n\t\t<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeLabel/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


eml.attributeDescription
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeDescription" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeDescription"/>\n\t\t<constructor-arg name="xpath" value="//dataTable/attributeList/attribute/attributeDefinition/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


eml.attributeUnit
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeUnit" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeUnit"/>\n\t\t<constructor-arg name="xpath" value="//dataTable//standardUnit/text() | //dataTable//customUnit/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\n\t\n'


eml.attributeText
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.attributeText" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.attributeTextRoot">\n\t\t\t<constructor-arg name="name" value="attribute"/>\n\t</bean>\n\t\n\t\n'


eml.fileID
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t<constructor-arg name="name" value="fileID"/>\n\t</bean>\n\t\n\t\n'


eml.fullText
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.fullText" class="org.dataone.cn.indexer.parser.AggregateSolrField">\n\t\t<property name="name" value="text"/>\n\t\t<property name="solrFields">\n\t   \t\t<list>\n\t       \t\t<ref bean="eml.text"/>\n\t       \t\t<ref bean="eml.attributeName.noDupe"/>\n\t       \t\t<ref bean="eml.attributeLabel.noDupe"/>\n\t       \t\t<ref bean="eml.attributeDescription.noDupe"/>\n\t       \t\t<ref bean="eml.attributeUnit.noDupe"/>\n\t      \t</list>\n\t  \t</property>\n\t</bean>\n\t\n\t\n'


eml.geohash1
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_1"/>\n\t\t<property name="converter" ref="geohashConverter_1"/>\n\t</bean>\n\t\n\t\n'


eml.geohash2
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_2"/>\n\t\t<property name="converter" ref="geohashConverter_2"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash3
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_3"/>\n\t\t<property name="converter" ref="geohashConverter_3"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash4
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_4"/>\n\t\t<property name="converter" ref="geohashConverter_4"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash5
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_5"/>\n\t\t<property name="converter" ref="geohashConverter_5"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash6
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_6"/>\n\t\t<property name="converter" ref="geohashConverter_6"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash7
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_7"/>\n\t\t<property name="converter" ref="geohashConverter_7"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash8
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_8"/>\n\t\t<property name="converter" ref="geohashConverter_8"/>\n\t</bean>\n\t\n\t\t\n'


eml.geohash9
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="eml.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_9"/>\n\t\t<property name="converter" ref="geohashConverter_9"/>\n\t</bean>\n\n\t\n'


eml.isService
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.isService" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="isService"/>\n\t\t<constructor-arg name="xpath" value="boolean(//software/implementation/distribution/online/url)"/>\n\t</bean>\n\t\n\t\n'


eml.serviceTitle
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceTitle" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceTitle"/>\n\t\t<constructor-arg name="xpath" value="//software/title//text()[normalize-space()]"/>\n\t\t<property name="combineNodes" value="true"/>\n\t\t<property name="combineDelimiter" value=":"/>\n\t</bean>\n\t\n\t\n'


eml.serviceDescription
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceDescription" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceDescription"/>\n\t\t<constructor-arg name="xpath" value="//software/abstract//text()[normalize-space()]"/>\n\t\t<property name="combineNodes" value="true"/>\n\t\t<property name="combineDelimiter" value=":"/>\n\t</bean>\t\n\n\t\n'


eml.serviceEndpoint
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="eml.serviceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceEndpoint"/>\n\t\t<constructor-arg name="xpath" value="//software/implementation/distribution/online/url/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\t\n\t\n'


