ISO TC-211
==========

Describes parser configuration for: isotc211Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Geographic MetaData (GMD) Extensible Markup Language
    | formatId: ``http://www.isotc211.org/2005/gmd``


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

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:abstract/gco:CharacterString/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.abstract`_


  * - :attr:`Index.author`
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.author`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.authorSurNameSort`_


  * - :attr:`Index.contactOrganization`
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:organisationName/
        gco:CharacterString/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.contactOrganization`_


  * - :attr:`Index.origin`
    - True
    - True
    - ::

        //gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode/text() = 
        "owner" or gmd:role/gmd:CI_RoleCode/text() = 
        "originator" or gmd:role/gmd:CI_RoleCode/text() = 
        "principalInvestigator" or gmd:role/gmd:CI_RoleCode/
        text() = "author"]/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty[(gmd:role/gmd:CI_RoleCode/
        text() = "owner" or gmd:role/gmd:CI_RoleCode/text() 
        = "originator" or gmd:role/gmd:CI_RoleCode/text() = 
        "principalInvestigator" or gmd:role/gmd:CI_RoleCode/
        text() = "author") and (not(gmd:individualName) or 
        gmd:individualName[@gco:nilReason = "missing"])]/
        gmd:organisationName/gco:CharacterString/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.origin`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        //gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.investigator`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        (//gmd:dateStamp/gco:Date/text() | //gmd:dateStamp/
        gco:DateTime/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.beginDate`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:temporalElement/
        gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 
        'TimePeriod']/*[local-name() = 'beginPosition']/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.beginDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.endDate`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:temporalElement/
        gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 
        'TimePeriod']/*[local-name() = 'endPosition']/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.endDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:citation/gmd:CI_Citation/gmd:title/
        gco:CharacterString/text() | //
        gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:citation/gmd:CI_Citation/gmd:title/gmx:Anchor/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.title`_


  * - :attr:`Index.keywords`
    - True
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/
        gmx:Anchor/text() | //gmd:identificationInfo/
        gmd:MD_DataIdentification/gmd:descriptiveKeywords/
        gmd:MD_Keywords/gmd:keyword/gco:CharacterString/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.keywords`_


  * - :attr:`Index.eastBoundCoord`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/
        gco:Decimal/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.eastBoundCoord`_


  * - :attr:`Index.westBoundCoord`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/
        gco:Decimal/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.westBoundCoord`_


  * - :attr:`Index.southBoundCoord`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/
        gco:Decimal/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.southBoundCoord`_


  * - :attr:`Index.northBoundCoord`
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/
        gco:Decimal/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.northBoundCoord`_


  * - :attr:`Index.geohash_9`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash9`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_1`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash1`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_2`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash2`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_3`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash3`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_4`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash4`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_5`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash5`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_6`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash6`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_7`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash7`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.geohash_8`
    - False
    - 
    - 
      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `isotc.geohash8`_
      | Converter: `GeohashConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/GeohashConverter.java>`_


  * - :attr:`Index.isService`
    - False
    - False
    - ::

        boolean(//srv:SV_ServiceIdentification or //
        gmd:distributionInfo/gmd:MD_Distribution)

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.isService`_


  * - :attr:`Index.serviceCoupling`
    - False
    - False
    - ::

        concat( substring('loose', 1 div boolean( //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue = 'loose')),     
           substring('tight', 1 div boolean( //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue = 'tight')),     
           substring('tight', 1 div boolean( //
        gmd:distributionInfo/gmd:MD_Distribution and not(//
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue))),        
        substring('',  1 div boolean( not(   //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue)                 
         and not(   //gmd:distributionInfo/
        gmd:MD_Distribution))))

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceCoupling`_


  * - :attr:`Index.serviceTitle`
    - False
    - False
    - ::

        (//srv:SV_ServiceIdentification/gmd:citation/
        gmd:CI_Citation/gmd:title/gco:CharacterString | //
        gmd:distributionInfo/gmd:MD_Distribution/
        gmd:distributor/gmd:MD_Distributor/
        gmd:distributorTransferOptions/
        gmd:MD_DigitalTransferOptions/gmd:onLine/
        gmd:CI_OnlineResource/gmd:name/gco:CharacterString)/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceTitle`_


  * - :attr:`Index.serviceDescription`
    - False
    - False
    - ::

        (//srv:SV_ServiceIdentification/gmd:abstract/
        gco:CharacterString | //gmd:distributionInfo/
        gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        gmd:MD_DigitalTransferOptions/gmd:onLine/
        gmd:CI_OnlineResource/gmd:description/
        gco:CharacterString)/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceDescription`_


  * - :attr:`Index.serviceType`
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:serviceType/
        gco:LocalName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceType`_
      | Converter: `MemberNodeServiceRegistrationTypeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/MemberNodeServiceRegistrationTypeConverter.java>`_


  * - :attr:`Index.serviceEndpoint`
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:containsOperations/
        srv:SV_OperationMetadata/srv:connectPoint/
        gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceEndpoint`_


  * - :attr:`Index.serviceInput`
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:operatesOn/@xlink:href

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceInput`_


  * - :attr:`Index.serviceOutput`
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/gmd:resourceFormat/
        @xlink:href

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.serviceOutput`_


  * - :attr:`Index.serviceType`
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        gmd:MD_DigitalTransferOptions/gmd:onLine/
        gmd:CI_OnlineResource/gmd:protocol/
        gco:CharacterString/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.distribServiceType`_
      | Converter: `MemberNodeServiceRegistrationTypeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/MemberNodeServiceRegistrationTypeConverter.java>`_


  * - :attr:`Index.serviceEndpoint`
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        gmd:MD_DigitalTransferOptions/gmd:onLine/
        gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text() | /
        /gmd:distributionInfo/gmd:MD_Distribution/
        gmd:transferOptions/gmd:MD_DigitalTransferOptions/
        gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/
        gmd:URL/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.distribServiceEndpoint`_


  * - :attr:`Index.serviceInput`
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        @xlink:href

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.distribServiceInput`_


  * - :attr:`Index.serviceOutput`
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorFormat/
        gmd:MD_Format/gmd:version/gco:CharacterString/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `isotc.distribServiceOutput`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `isotc.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `isotc.fullText`_



Bean Configurations
-------------------


isotc.abstract
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.abstract" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="abstract"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString/text()"/>
	</bean>
	
	



isotc.author
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.author" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="author"/>
		<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>
	</bean>

	



isotc.authorSurName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>
		<property name="multivalue" value="false"/>
	</bean>

	



isotc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>
		<property name="multivalue" value="false"/>
	</bean>
	
	



isotc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="contactOrganization"/>
		<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString/text())[1]"/>
	</bean>
	
	



isotc.origin
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.origin" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="origin"/>
		<constructor-arg name="xpath" value="//gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode/text() = &quot;owner&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;originator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;principalInvestigator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;author&quot;]/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty[(gmd:role/gmd:CI_RoleCode/text() = &quot;owner&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;originator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;principalInvestigator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;author&quot;) and (not(gmd:individualName) or gmd:individualName[@gco:nilReason = &quot;missing&quot;])]/gmd:organisationName/gco:CharacterString/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



isotc.investigator
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



isotc.pubDate
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="(//gmd:dateStamp/gco:Date/text() | //gmd:dateStamp/gco:DateTime/text())[1]"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
	



isotc.beginDate
~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.beginDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="beginDate"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 'TimePeriod']/*[local-name() = 'beginPosition']/text()"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
	



isotc.endDate
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.endDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="endDate"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 'TimePeriod']/*[local-name() = 'endPosition']/text()"/>
		<property name="converter" ref="dateConverter"/>
	</bean>	

	



isotc.title
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString/text() | //gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gmx:Anchor/text()"/>
	</bean>		
	
	



isotc.keywords
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/gmx:Anchor/text() | //gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/gco:CharacterString/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	



isotc.eastBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="eastBoundCoord"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal/text()"/>
	</bean>	
	
	



isotc.westBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="westBoundCoord"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal/text()"/>
	</bean>
	
	



isotc.southBoundCoord
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="southBoundCoord"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal/text()"/>
	</bean>
	
	



isotc.northBoundCoord
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="northBoundCoord"/>
		<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal/text()"/>
	</bean>

	



isotc.geohash9
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_9"/>
		<property name="converter" ref="geohashConverter_9"/>
	</bean>
		
	



isotc.geohash1
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_1"/>
		<property name="converter" ref="geohashConverter_1"/>
	</bean>

	



isotc.geohash2
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_2"/>
		<property name="converter" ref="geohashConverter_2"/>
	</bean>
	
	



isotc.geohash3
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_3"/>
		<property name="converter" ref="geohashConverter_3"/>
	</bean>
	
	



isotc.geohash4
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_4"/>
		<property name="converter" ref="geohashConverter_4"/>
	</bean>

	



isotc.geohash5
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_5"/>
		<property name="converter" ref="geohashConverter_5"/>
	</bean>
	
	



isotc.geohash6
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_6"/>
		<property name="converter" ref="geohashConverter_6"/>
	</bean>
	
	



isotc.geohash7
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_7"/>
		<property name="converter" ref="geohashConverter_7"/>
	</bean>	

	



isotc.geohash8
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">
		<constructor-arg name="name" value="geohash_8"/>
		<property name="converter" ref="geohashConverter_8"/>
	</bean>

	



isotc.isService
~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.isService" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="isService"/>
		<constructor-arg name="xpath" value="boolean(//srv:SV_ServiceIdentification or //gmd:distributionInfo/gmd:MD_Distribution)"/>
	</bean>
	
	



isotc.serviceCoupling
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceCoupling" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceCoupling"/>
		<constructor-arg name="xpath" value="concat( substring('loose', 1 div boolean( //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue = 'loose')),        substring('tight', 1 div boolean( //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue = 'tight')),        substring('tight', 1 div boolean( //gmd:distributionInfo/gmd:MD_Distribution and not(//srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue))),        substring('',  1 div boolean( not(   //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue)                  and not(   //gmd:distributionInfo/gmd:MD_Distribution))))"/>
	</bean>
	
	



isotc.serviceTitle
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceTitle" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceTitle"/>
		<constructor-arg name="xpath" value="(//srv:SV_ServiceIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString | //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString)/text()"/>
		<property name="combineNodes" value="true"/>
		<property name="combineDelimiter" value=":"/>
	</bean>
	
	



isotc.serviceDescription
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceDescription" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceDescription"/>
		<constructor-arg name="xpath" value="(//srv:SV_ServiceIdentification/gmd:abstract/gco:CharacterString | //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:description/gco:CharacterString)/text()"/>
		<property name="combineNodes" value="true"/>
		<property name="combineDelimiter" value=":"/>
	</bean>	
	
	



isotc.serviceType
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceType" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceType"/>
		<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:serviceType/gco:LocalName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="converter" ref="serviceTypesConverter"/>
	</bean>
	
	



isotc.serviceEndpoint
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceEndpoint"/>
		<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:containsOperations/srv:SV_OperationMetadata/srv:connectPoint/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()"/>
		<property name="multivalue" value="true"/>
	</bean>	

	



isotc.serviceInput
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceInput" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceInput"/>
		<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:operatesOn/@xlink:href"/>
		<property name="multivalue" value="true"/>
	</bean>	

	



isotc.serviceOutput
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceOutput" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceOutput"/>
		<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/gmd:resourceFormat/@xlink:href"/>
		<property name="multivalue" value="true"/>
	</bean>	
	
	



isotc.distribServiceType
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceType" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceType"/>
		<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:protocol/gco:CharacterString/text()"/>
		<property name="multivalue" value="true"/>
		<property name="converter" ref="serviceTypesConverter"/>
	</bean>
	
	



isotc.distribServiceEndpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceEndpoint"/>
		<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text() | //gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()"/>
		<property name="multivalue" value="true"/>
	</bean>	

	



isotc.distribServiceInput
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceInput" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceInput"/>
		<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/@xlink:href"/>
		<property name="multivalue" value="true"/>
	</bean>

	



isotc.distribServiceOutput
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceOutput" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="serviceOutput"/>
		<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorFormat/gmd:MD_Format/gmd:version/gco:CharacterString/text()"/>
		<property name="multivalue" value="true"/>
	</bean>	
	




isotc.fileID
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>

	



isotc.fullText
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">
		<constructor-arg name="name" value="text"/>
		<constructor-arg name="xpath" value="//*/text()"/>
		<property name="combineNodes" value="true"/>
	</bean>
	
	



