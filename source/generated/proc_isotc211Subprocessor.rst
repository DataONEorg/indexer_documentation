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

        if (//gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/
        gmd:date/gmd:CI_Date/gmd:date[
        following-sibling::gmd:dateType/gmd:CI_DateTypeCode/
        text() = 'publication']/gco:Date/text())            
             then //gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[
        following-sibling::gmd:dateType/gmd:CI_DateTypeCode/
        text() = 'publication']/gco:Date/text()           
        else if (//gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[
        following-sibling::gmd:dateType/gmd:CI_DateTypeCode/
        text() = 'publication']/gco:DateTime/text())        
                 then //gmd:identificationInfo/*/
        gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/
        gmd:date[following-sibling::gmd:dateType/
        gmd:CI_DateTypeCode/text() = 'publication']/
        gco:DateTime/text()            else if (//
        gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/
        gco:Date[1]/text())                 then //
        gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/
        gco:Date[1]/text()           else if (//
        gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/
        gco:DateTime[1]/text())                 then //
        gmd:identificationInfo/*/gmd:citation/
        gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/
        gco:DateTime[1]/text()           else ()

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

        concat( substring('loose', 1 div number(boolean( //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue = 'loose'))),    
            substring('tight', 1 div number(boolean( //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue = 'tight'))),    
            substring('tight', 1 div number(boolean( //
        gmd:distributionInfo/gmd:MD_Distribution and not(//
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue)))),        
        substring('',  1 div number(boolean( not(   //
        srv:SV_ServiceIdentification/srv:couplingType/
        srv:SV_CouplingType/@codeListValue)                 
         and not(   //gmd:distributionInfo/
        gmd:MD_Distribution)))))

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

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.abstract" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="abstract"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:abstract/gco:CharacterString/text()"/>\n\t</bean>\n\t\n\t\n'


isotc.author
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.author" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="author"/>\n\t\t<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>\n\t</bean>\n\n\t\n'


isotc.authorSurName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\n\t\n'


isotc.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text())[1]"/>\n\t\t<property name="multivalue" value="false"/>\n\t</bean>\n\t\n\t\n'


isotc.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="contactOrganization"/>\n\t\t<constructor-arg name="xpath" value="(//gmd:CI_ResponsibleParty/gmd:organisationName/gco:CharacterString/text())[1]"/>\n\t</bean>\n\t\n\t\n'


isotc.origin
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.origin" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="origin"/>\n\t\t<constructor-arg name="xpath" value="//gmd:CI_ResponsibleParty[gmd:role/gmd:CI_RoleCode/text() = &quot;owner&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;originator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;principalInvestigator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;author&quot;]/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty[(gmd:role/gmd:CI_RoleCode/text() = &quot;owner&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;originator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;principalInvestigator&quot; or gmd:role/gmd:CI_RoleCode/text() = &quot;author&quot;) and (not(gmd:individualName) or gmd:individualName[@gco:nilReason = &quot;missing&quot;])]/gmd:organisationName/gco:CharacterString/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


isotc.investigator
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="//gmd:CI_ResponsibleParty/gmd:individualName/gco:CharacterString/text() | //gmd:CI_ResponsibleParty/gmd:individualName/gmx:Anchor/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


isotc.pubDate
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.pubDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="pubDate"/>\n\t\t<constructor-arg name="xpath" value="if (//gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[following-sibling::gmd:dateType/gmd:CI_DateTypeCode/text() = \'publication\']/gco:Date/text())                 then //gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[following-sibling::gmd:dateType/gmd:CI_DateTypeCode/text() = \'publication\']/gco:Date/text()           else if (//gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[following-sibling::gmd:dateType/gmd:CI_DateTypeCode/text() = \'publication\']/gco:DateTime/text())                 then //gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date[following-sibling::gmd:dateType/gmd:CI_DateTypeCode/text() = \'publication\']/gco:DateTime/text()            else if (//gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date[1]/text())                 then //gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:Date[1]/text()           else if (//gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime[1]/text())                 then //gmd:identificationInfo/*/gmd:citation/gmd:CI_Citation/gmd:date/gmd:CI_Date/gmd:date/gco:DateTime[1]/text()           else ()"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\t\n\t\n'


isotc.beginDate
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.beginDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="beginDate"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/*[local-name() = \'TimePeriod\']/*[local-name() = \'beginPosition\']/text()"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\t\n\t\n'


isotc.endDate
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.endDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="endDate"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:temporalElement/gmd:EX_TemporalExtent/gmd:extent/*[local-name() = \'TimePeriod\']/*[local-name() = \'endPosition\']/text()"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\t\n\n\t\n'


isotc.title
~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString/text() | //gmd:identificationInfo/gmd:MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gmx:Anchor/text()"/>\n\t</bean>\t\t\n\t\n\t\n'


isotc.keywords
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/gmx:Anchor/text() | //gmd:identificationInfo/gmd:MD_DataIdentification/gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/gco:CharacterString/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\t\n\t\n'


isotc.eastBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.eastBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="eastBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/gco:Decimal/text()"/>\n\t</bean>\t\n\t\n\t\n'


isotc.westBoundCoord
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.westBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="westBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/gco:Decimal/text()"/>\n\t</bean>\n\t\n\t\n'


isotc.southBoundCoord
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.southBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="southBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/gco:Decimal/text()"/>\n\t</bean>\n\t\n\t\n'


isotc.northBoundCoord
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.northBoundCoord" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="northBoundCoord"/>\n\t\t<constructor-arg name="xpath" value="//gmd:identificationInfo/gmd:MD_DataIdentification/gmd:extent/gmd:EX_Extent/gmd:geographicElement/gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/gco:Decimal/text()"/>\n\t</bean>\n\n\t\n'


isotc.geohash9
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash9" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_9"/>\n\t\t<property name="converter" ref="geohashConverter_9"/>\n\t</bean>\n\t\t\n\t\n'


isotc.geohash1
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash1" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_1"/>\n\t\t<property name="converter" ref="geohashConverter_1"/>\n\t</bean>\n\n\t\n'


isotc.geohash2
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash2" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_2"/>\n\t\t<property name="converter" ref="geohashConverter_2"/>\n\t</bean>\n\t\n\t\n'


isotc.geohash3
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash3" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_3"/>\n\t\t<property name="converter" ref="geohashConverter_3"/>\n\t</bean>\n\t\n\t\n'


isotc.geohash4
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash4" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_4"/>\n\t\t<property name="converter" ref="geohashConverter_4"/>\n\t</bean>\n\n\t\n'


isotc.geohash5
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash5" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_5"/>\n\t\t<property name="converter" ref="geohashConverter_5"/>\n\t</bean>\n\t\n\t\n'


isotc.geohash6
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash6" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_6"/>\n\t\t<property name="converter" ref="geohashConverter_6"/>\n\t</bean>\n\t\n\t\n'


isotc.geohash7
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash7" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_7"/>\n\t\t<property name="converter" ref="geohashConverter_7"/>\n\t</bean>\t\n\n\t\n'


isotc.geohash8
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.geohash8" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="isotc.geohashRoot">\n\t\t<constructor-arg name="name" value="geohash_8"/>\n\t\t<property name="converter" ref="geohashConverter_8"/>\n\t</bean>\n\n\t\n'


isotc.isService
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.isService" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="isService"/>\n\t\t<constructor-arg name="xpath" value="boolean(//srv:SV_ServiceIdentification or //gmd:distributionInfo/gmd:MD_Distribution)"/>\n\t</bean>\n\t\n\t\n'


isotc.serviceCoupling
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceCoupling" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceCoupling"/>\n\t\t<constructor-arg name="xpath" value="concat( substring(\'loose\', 1 div number(boolean( //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue = \'loose\'))),        substring(\'tight\', 1 div number(boolean( //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue = \'tight\'))),        substring(\'tight\', 1 div number(boolean( //gmd:distributionInfo/gmd:MD_Distribution and not(//srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue)))),        substring(\'\',  1 div number(boolean( not(   //srv:SV_ServiceIdentification/srv:couplingType/srv:SV_CouplingType/@codeListValue)                  and not(   //gmd:distributionInfo/gmd:MD_Distribution)))))"/>\n\t</bean>\n\t\n\t\n'


isotc.serviceTitle
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceTitle" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceTitle"/>\n\t\t<constructor-arg name="xpath" value="(//srv:SV_ServiceIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gco:CharacterString | //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:name/gco:CharacterString)/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t\t<property name="combineDelimiter" value=":"/>\n\t</bean>\n\t\n\t\n'


isotc.serviceDescription
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceDescription" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceDescription"/>\n\t\t<constructor-arg name="xpath" value="(//srv:SV_ServiceIdentification/gmd:abstract/gco:CharacterString | //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:description/gco:CharacterString)/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t\t<property name="combineDelimiter" value=":"/>\n\t</bean>\t\n\t\n\t\n'


isotc.serviceType
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceType" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceType"/>\n\t\t<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:serviceType/gco:LocalName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="converter" ref="serviceTypesConverter"/>\n\t</bean>\n\t\n\t\n'


isotc.serviceEndpoint
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceEndpoint"/>\n\t\t<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:containsOperations/srv:SV_OperationMetadata/srv:connectPoint/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\n\t\n'


isotc.serviceInput
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceInput" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceInput"/>\n\t\t<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/srv:operatesOn/@xlink:href"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\n\t\n'


isotc.serviceOutput
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.serviceOutput" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceOutput"/>\n\t\t<constructor-arg name="xpath" value="//srv:SV_ServiceIdentification/gmd:resourceFormat/@xlink:href"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\t\n\t\n'


isotc.distribServiceType
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceType" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceType"/>\n\t\t<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:protocol/gco:CharacterString/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="converter" ref="serviceTypesConverter"/>\n\t</bean>\n\t\n\t\n'


isotc.distribServiceEndpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceEndpoint" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceEndpoint"/>\n\t\t<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text() | //gmd:distributionInfo/gmd:MD_Distribution/gmd:transferOptions/gmd:MD_DigitalTransferOptions/gmd:onLine/gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\n\t\n'


isotc.distribServiceInput
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceInput" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceInput"/>\n\t\t<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorTransferOptions/@xlink:href"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\n\n\t\n'


isotc.distribServiceOutput
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.distribServiceOutput" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="serviceOutput"/>\n\t\t<constructor-arg name="xpath" value="//gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/gmd:MD_Distributor/gmd:distributorFormat/gmd:MD_Format/gmd:version/gco:CharacterString/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t</bean>\t\n\t\n\n'


isotc.fileID
~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t<constructor-arg name="name" value="fileID"/>\n\t</bean>\n\n\t\n'


isotc.fullText
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="isotc.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">\n\t\t<constructor-arg name="name" value="text"/>\n\t\t<constructor-arg name="xpath" value="//*/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t</bean>\n\t\n\t\n'


