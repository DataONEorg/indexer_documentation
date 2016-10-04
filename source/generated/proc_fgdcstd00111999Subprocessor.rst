FGDC, v001.1-1999
=================

Describes parser configuration for: fgdcstd00111999Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Content Standard for Digital Geospatial Metadata, Biological Data Profile, version 001.1-1999
    | formatId: ``FGDC-STD-001.1-1999``


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

        /*[local-name() = 'metadata']/idinfo/descript/abstract/
        descendant::text()

      | Processor: `MergeSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/MergeSolrField.java>`_
      | Configuration: `fgdc.abstract`_


  * - :attr:`Index.beginDate`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/begdate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.beginDate`_
      | Converter: `FgdcDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/FgdcDateConverter.java>`_


  * - :attr:`Index.contactOrganization`
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/distinfo/distrib/cntinfo/
        cntperp/cntorg/text() | /*[local-name() = 
        'metadata']/distinfo/distrib/cntinfo/cntorgp/cntorg/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.contactOrganization`_


  * - :attr:`Index.eastBoundCoord`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/eastbc/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.eastBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.westBoundCoord`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/westbc/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.westBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.northBoundCoord`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/northbc/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.northBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.southBoundCoord`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/southbc/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.southBoundCoord`_
      | Converter: `SolrLongitudeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrLongitudeConverter.java>`_


  * - :attr:`Index.edition`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citeinfo/edition/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.edition`_


  * - :attr:`Index.endDate`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/enddate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.endDate`_
      | Converter: `FgdcDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/FgdcDateConverter.java>`_


  * - :attr:`Index.gcmdKeyword`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme[themekt=
        'GCMD Science Keywords']/themekey/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.gcmdKeyword`_


  * - :attr:`Index.keywords`
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme/
        themekey/text() | /*[local-name() = 'metadata']/
        idinfo/keywords/place/placekey/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.keywords`_


  * - :attr:`Index.geoform`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.geoform`_


  * - :attr:`Index.genus`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Genus"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.genus`_


  * - :attr:`Index.kingdom`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Kingdom"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.kingdom`_


  * - :attr:`Index.order`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Order"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.order`_


  * - :attr:`Index.phylum`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Phylum"]/text() | //taxoncl/
        taxonrv[../taxonrn="Division"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.phylum`_


  * - :attr:`Index.species`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Species"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.species`_


  * - :attr:`Index.family`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Family"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.family`_


  * - :attr:`Index.class`
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Class"]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.class`_


  * - :attr:`Index.scientificName`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.scientificName`_


  * - :attr:`Index.origin`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.origin`_


  * - :attr:`Index.placeKey`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/place/
        placekey/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.placeKey`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        pubdate/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.pubDate`_
      | Converter: `FgdcDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/FgdcDateConverter.java>`_


  * - :attr:`Index.purpose`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/descript/purpose/
        descendant::text()

      | Processor: `MergeSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/MergeSolrField.java>`_
      | Configuration: `fgdc.purpose`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        title/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.title`_


  * - :attr:`Index.webUrl`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        onlink/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.web_url`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `fgdc.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - 
    - 
    - 
      | Processor: `AggregateSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/AggregateSolrField.java>`_
      | Configuration: `fgdc.fullText`_
      | Converter: 


  * - :attr:`Index.presentationCat`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.presentationCat`_


  * - :attr:`Index.author`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.author`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.authorSurNameSort`_


  * - :attr:`Index.investigator`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.investigator`_


  * - :attr:`Index.site`
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/descgeog/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.site`_


  * - :attr:`Index.attributeName`
    - True
    - False
    - ::

        //attr/attrlabl/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.attributeName`_


  * - :attr:`Index.attributeLabel`
    - True
    - False
    - ::

        //attr/attalias/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.attributeLabel`_


  * - :attr:`Index.attributeDescription`
    - True
    - False
    - ::

        //attr/attrdef/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.attributeDescription`_


  * - :attr:`Index.attributeUnit`
    - True
    - False
    - ::

        //attr/attrdomv//attrunit/text() | //attr//attrdomv//edomv/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `fgdc.attributeUnit`_


  * - :attr:`Index.attribute`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.attributeText`_


  * - :attr:`Index.geohash_1`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash1`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_2`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash2`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_3`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash3`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_4`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash4`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_5`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash5`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_6`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash6`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_7`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash7`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_8`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash8`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_9`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `fgdc.geohash9`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_



Bean Configurations
-------------------


fgdc.abstract
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.abstract" class="org.dataone.cn.indexer.parser.MergeSolrField">
	  <constructor-arg name="name" value="abstract"/>
	  <constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/descript/abstract/descendant::text()"/>
	  <constructor-arg name="delimiter" value=" "/>
	  <property name="multivalue" value="false"/>
	  <property name="dedupe" value="false"/>
	</bean>
	
	




fgdc.beginDate
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.beginDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="beginDate"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/rngdates/begdate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="fgdcDateConverter"/>
	</bean>
	
	




fgdc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="contactOrganization"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/distinfo/distrib/cntinfo/cntperp/cntorg/text() | /*[local-name() = 'metadata']/distinfo/distrib/cntinfo/cntorgp/cntorg/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>	

	




fgdc.eastBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="eastBoundCoord"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/spdom/bounding/eastbc/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>
	
	




fgdc.westBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="westBoundCoord"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/spdom/bounding/westbc/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>		
	
		




fgdc.northBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="northBoundCoord"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/spdom/bounding/northbc/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>	
	
	




fgdc.southBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="southBoundCoord"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/spdom/bounding/southbc/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="solrLongitudeConverter"/>
	</bean>	
	
	




fgdc.edition
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.edition" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="edition"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citeinfo/edition/text()"/>
		<property name="multivalue" value="false"/>
	</bean>	

	




fgdc.endDate
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.endDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="endDate"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/rngdates/enddate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="fgdcDateConverter"/>
	</bean>

	




fgdc.gcmdKeyword
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.gcmdKeyword" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="gcmdKeyword"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/keywords/theme[themekt='GCMD Science Keywords']/themekey/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
 	
	




fgdc.keywords
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/keywords/theme/themekey/text() | /*[local-name() = 'metadata']/idinfo/keywords/place/placekey/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
		<property name="disallowedValues">
			<list>
				<value>none</value>
			</list>
		</property>
	</bean>

	




fgdc.geoform
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geoform" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="geoform"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/geoform/text()"/>
		<property name="multivalue" value="false"/>
	</bean>	
	
	




fgdc.genus
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.genus" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="genus"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Genus&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>		
	
	




fgdc.kingdom
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.kingdom" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="kingdom"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Kingdom&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>	
	
	




fgdc.order
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.order" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="order"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Order&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.phylum
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.phylum" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="phylum"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Phylum&quot;]/text() | //taxoncl/taxonrv[../taxonrn=&quot;Division&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.species
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.species" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="species"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Species&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.family
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.family" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="family"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Family&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.class
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.class" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="class"/>
		<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Class&quot;]/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.scientificName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.scientificName" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="fgdc.scientificNameRoot">
			<constructor-arg name="name" value="scientificName"/>
	</bean>
	
	




fgdc.origin
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.origin" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="origin"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/origin/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.placeKey
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.placeKey" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="placeKey"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/keywords/place/placekey/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.pubDate
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/pubdate/text()"/>
		<property name="multivalue" value="false"/>
		<property name="converter" ref="fgdcDateConverter"/>
	</bean>
	
	




fgdc.purpose
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.purpose" class="org.dataone.cn.indexer.parser.MergeSolrField">
	  <constructor-arg name="name" value="purpose"/>
	  <constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/descript/purpose/descendant::text()"/>
	  <constructor-arg name="delimiter" value=" "/>
	  <property name="multivalue" value="false"/>
	  <property name="dedupe" value="false"/>
	</bean>

	




fgdc.title
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/title/text()"/>
		<property name="multivalue" value="false"/>
	</bean>

	




fgdc.web_url
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.web_url" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="webUrl"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/onlink/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.fileID
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>
	
	




fgdc.fullText
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.fullText" class="org.dataone.cn.indexer.parser.AggregateSolrField">
		<property name="name" value="text"/>
		<property name="solrFields">
	   		<list>
	       		<ref bean="fgdc.text"/>
	      	</list>
	  	</property>
	</bean>





fgdc.presentationCat
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.presentationCat" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="presentationCat"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/geoform/text()"/>
		<property name="multivalue" value="false"/>
	</bean>
	
	




fgdc.author
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.author" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="author"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/origin/text()"/>
		<property name="multivalue" value="false"/>
	</bean>

	




fgdc.authorSurName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/origin[1]/text()"/>
		<property name="multivalue" value="false"/>
	</bean>

	




fgdc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/origin[1]/text()"/>
		<property name="multivalue" value="false"/>
	</bean>
	
	




fgdc.investigator
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/citation/citeinfo/origin/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.site
~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.site" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="site"/>
		<constructor-arg name="xpath" value="/*[local-name() = 'metadata']/idinfo/spdom/descgeog/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




fgdc.attributeName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeName"/>
		<constructor-arg name="xpath" value="//attr/attrlabl/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




fgdc.attributeLabel
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeLabel" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeLabel"/>
		<constructor-arg name="xpath" value="//attr/attalias/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




fgdc.attributeDescription
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeDescription" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeDescription"/>
		<constructor-arg name="xpath" value="//attr/attrdef/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>
	
	




fgdc.attributeUnit
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeUnit" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="attributeUnit"/>
		<constructor-arg name="xpath" value="//attr/attrdomv//attrunit/text() | //attr//attrdomv//edomv/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="false"/>
	</bean>

	




fgdc.attributeText
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeText" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="fgdc.attributeTextRoot">
			<constructor-arg name="name" value="attribute"/>
	</bean>
	
	




fgdc.geohash1
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_1"/>
		<property name="converter" ref="geohashConverter_1"/>
	</bean>
	
	




fgdc.geohash2
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_2"/>
		<property name="converter" ref="geohashConverter_2"/>
	</bean>
	
		




fgdc.geohash3
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_3"/>
		<property name="converter" ref="geohashConverter_3"/>
	</bean>
	
		




fgdc.geohash4
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_4"/>
		<property name="converter" ref="geohashConverter_4"/>
	</bean>
	
		




fgdc.geohash5
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_5"/>
		<property name="converter" ref="geohashConverter_5"/>
	</bean>
	
		




fgdc.geohash6
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_6"/>
		<property name="converter" ref="geohashConverter_6"/>
	</bean>
	
		




fgdc.geohash7
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_7"/>
		<property name="converter" ref="geohashConverter_7"/>
	</bean>
	
		




fgdc.geohash8
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_8"/>
		<property name="converter" ref="geohashConverter_8"/>
	</bean>
	
		




fgdc.geohash9
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">
		<constructor-arg name="name" value="geohash_9"/>
		<property name="converter" ref="geohashConverter_9"/>
	</bean>

	




