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
    - Source

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

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.abstract" class="org.dataone.cn.indexer.parser.MergeSolrField">\n\t  <constructor-arg name="name" value="abstract"/>\n\t  <constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/descript/abstract/descendant::text()"/>\n\t  <constructor-arg name="delimiter" value=" "/>\n\t  <property name="multivalue" value="false"/>\n\t  <property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.beginDate
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.beginDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="beginDate"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/timeperd/timeinfo/rngdates/begdate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="fgdcDateConverter"/>\n\t</bean>\n\t\n\t\n'


fgdc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="contactOrganization"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/distinfo/distrib/cntinfo/cntperp/cntorg/text() | /*[local-name() = \'metadata\']/distinfo/distrib/cntinfo/cntorgp/cntorg/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\t\n\n\t\n'


fgdc.eastBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="eastBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/spdom/bounding/eastbc/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\n\t\n\t\n'


fgdc.westBoundCoord
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="westBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/spdom/bounding/westbc/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\t\t\n\t\n\t\t\n'


fgdc.northBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="northBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/spdom/bounding/northbc/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\t\n\t\n\t\n'


fgdc.southBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="southBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/spdom/bounding/southbc/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="solrLongitudeConverter"/>\n\t</bean>\t\n\t\n\t\n'


fgdc.edition
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.edition" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="edition"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citeinfo/edition/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\t\n\n\t\n'


fgdc.endDate
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.endDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="endDate"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/timeperd/timeinfo/rngdates/enddate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="fgdcDateConverter"/>\n\t</bean>\n\n\t\n'


fgdc.gcmdKeyword
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.gcmdKeyword" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="gcmdKeyword"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/keywords/theme[themekt=\'GCMD Science Keywords\']/themekey/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n \t\n\t\n'


fgdc.keywords
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/keywords/theme/themekey/text() | /*[local-name() = \'metadata\']/idinfo/keywords/place/placekey/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t\t<property name="disallowedValues">\n\t\t\t<list>\n\t\t\t\t<value>none</value>\n\t\t\t</list>\n\t\t</property>\n\t</bean>\n\n\t\n'


fgdc.geoform
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geoform" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="geoform"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/geoform/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\t\n\t\n\t\n'


fgdc.genus
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.genus" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="genus"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Genus&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\t\n\t\n\t\n'


fgdc.kingdom
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.kingdom" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="kingdom"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Kingdom&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\t\n\t\n'


fgdc.order
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.order" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="order"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Order&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.phylum
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.phylum" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="phylum"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Phylum&quot;]/text() | //taxoncl/taxonrv[../taxonrn=&quot;Division&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.species
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.species" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="species"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Species&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.family
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.family" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="family"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Family&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.class
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.class" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="class"/>\n\t\t<constructor-arg name="xpath" value="//taxoncl/taxonrv[../taxonrn=&quot;Class&quot;]/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.scientificName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.scientificName" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="fgdc.scientificNameRoot">\n\t\t\t<constructor-arg name="name" value="scientificName"/>\n\t</bean>\n\t\n\t\n'


fgdc.origin
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.origin" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="origin"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/origin/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.placeKey
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.placeKey" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="placeKey"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/keywords/place/placekey/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.pubDate
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.pubDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="pubDate"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/pubdate/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t\t<property name="converter" ref="fgdcDateConverter"/>\n\t</bean>\n\t\n\t\n'


fgdc.purpose
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.purpose" class="org.dataone.cn.indexer.parser.MergeSolrField">\n\t  <constructor-arg name="name" value="purpose"/>\n\t  <constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/descript/purpose/descendant::text()"/>\n\t  <constructor-arg name="delimiter" value=" "/>\n\t  <property name="multivalue" value="false"/>\n\t  <property name="dedupe" value="false"/>\n\t</bean>\n\n\t\n'


fgdc.title
~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/title/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\n\t\n'


fgdc.web_url
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.web_url" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="webUrl"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/onlink/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.fileID
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t<constructor-arg name="name" value="fileID"/>\n\t</bean>\n\t\n\t\n'


fgdc.fullText
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.fullText" class="org.dataone.cn.indexer.parser.AggregateSolrField">\n\t\t<property name="name" value="text"/>\n\t\t<property name="solrFields">\n\t   \t\t<list>\n\t       \t\t<ref bean="fgdc.text"/>\n\t      \t</list>\n\t  \t</property>\n\t</bean>\n\n'


fgdc.presentationCat
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.presentationCat" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="presentationCat"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/geoform/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.author
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.author" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="author"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/origin/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\n\t\n'


fgdc.authorSurName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/origin[1]/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\n\t\n'


fgdc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/origin[1]/text()"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.investigator
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/citation/citeinfo/origin/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.site
~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.site" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="site"/>\n\t\t<constructor-arg name="xpath" value="/*[local-name() = \'metadata\']/idinfo/spdom/descgeog/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


fgdc.attributeName
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeName"/>\n\t\t<constructor-arg name="xpath" value="//attr/attrlabl/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.attributeLabel
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeLabel" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeLabel"/>\n\t\t<constructor-arg name="xpath" value="//attr/attalias/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.attributeDescription
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeDescription" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeDescription"/>\n\t\t<constructor-arg name="xpath" value="//attr/attrdef/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


fgdc.attributeUnit
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeUnit" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="attributeUnit"/>\n\t\t<constructor-arg name="xpath" value="//attr/attrdomv//attrunit/text() | //attr//attrdomv//edomv/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="false"/>\n\t</bean>\n\n\t\n'


fgdc.attributeText
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.attributeText" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="fgdc.attributeTextRoot">\n\t\t\t<constructor-arg name="name" value="attribute"/>\n\t</bean>\n\t\n\t\n'


fgdc.geohash1
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_1"/>\n\t\t<property name="converter" ref="geohashConverter_1"/>\n\t</bean>\n\t\n\t\n'


fgdc.geohash2
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_2"/>\n\t\t<property name="converter" ref="geohashConverter_2"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash3
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_3"/>\n\t\t<property name="converter" ref="geohashConverter_3"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash4
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_4"/>\n\t\t<property name="converter" ref="geohashConverter_4"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash5
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_5"/>\n\t\t<property name="converter" ref="geohashConverter_5"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash6
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_6"/>\n\t\t<property name="converter" ref="geohashConverter_6"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash7
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_7"/>\n\t\t<property name="converter" ref="geohashConverter_7"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash8
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_8"/>\n\t\t<property name="converter" ref="geohashConverter_8"/>\n\t</bean>\n\t\n\t\t\n'


fgdc.geohash9
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="fgdc.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="false" p:root-ref="fgdc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_9"/>\n\t\t<property name="converter" ref="geohashConverter_9"/>\n\t</bean>\n\n\t\n'


