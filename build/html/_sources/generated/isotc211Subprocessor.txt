isotc211Subprocessor
====================

Format IDs Processed
--------------------


  * http://www.isotc211.org/2005/gmd



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - abstract (isotc.abstract, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:abstract/gco:CharacterString/text()



  * - author (isotc.author, SolrField)
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]



  * - authorSurName (isotc.authorSurName, SolrField)
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]



  * - authorSurNameSort (isotc.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text())[1]



  * - contactOrganization (isotc.contactOrganization, SolrField)
    - False
    - False
    - ::

        (//gmd:CI_ResponsibleParty/gmd:organisationName/
        gco:CharacterString/text())[1]



  * - origin (isotc.origin, SolrField)
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



  * - investigator (isotc.investigator, SolrField)
    - True
    - True
    - ::

        //gmd:CI_ResponsibleParty/gmd:individualName/
        gco:CharacterString/text() | //
        gmd:CI_ResponsibleParty/gmd:individualName/
        gmx:Anchor/text()



  * - pubDate (isotc.pubDate, SolrField)
    - False
    - False
    - ::

        (//gmd:dateStamp/gco:Date/text() | //gmd:dateStamp/
        gco:DateTime/text())[1]



  * - beginDate (isotc.beginDate, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:temporalElement/
        gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 
        'TimePeriod']/*[local-name() = 'beginPosition']/
        text()



  * - endDate (isotc.endDate, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:temporalElement/
        gmd:EX_TemporalExtent/gmd:extent/*[local-name() = 
        'TimePeriod']/*[local-name() = 'endPosition']/text()



  * - title (isotc.title, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:citation/gmd:CI_Citation/gmd:title/
        gco:CharacterString/text() | //
        gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:citation/gmd:CI_Citation/gmd:title/gmx:Anchor/
        text()



  * - keywords (isotc.keywords, SolrField)
    - True
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:descriptiveKeywords/gmd:MD_Keywords/gmd:keyword/
        gmx:Anchor/text() | //gmd:identificationInfo/
        gmd:MD_DataIdentification/gmd:descriptiveKeywords/
        gmd:MD_Keywords/gmd:keyword/gco:CharacterString/
        text()



  * - eastBoundCoord (isotc.eastBoundCoord, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:eastBoundLongitude/
        gco:Decimal/text()



  * - westBoundCoord (isotc.westBoundCoord, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:westBoundLongitude/
        gco:Decimal/text()



  * - southBoundCoord (isotc.southBoundCoord, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:southBoundLatitude/
        gco:Decimal/text()



  * - northBoundCoord (isotc.northBoundCoord, SolrField)
    - False
    - False
    - ::

        //gmd:identificationInfo/gmd:MD_DataIdentification/
        gmd:extent/gmd:EX_Extent/gmd:geographicElement/
        gmd:EX_GeographicBoundingBox/gmd:northBoundLatitude/
        gco:Decimal/text()



  * - geohash_9 (isotc.geohash9, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_1 (isotc.geohash1, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_2 (isotc.geohash2, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_3 (isotc.geohash3, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_4 (isotc.geohash4, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_5 (isotc.geohash5, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_6 (isotc.geohash6, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_7 (isotc.geohash7, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_8 (isotc.geohash8, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - isService (isotc.isService, SolrField)
    - False
    - False
    - ::

        boolean(//srv:SV_ServiceIdentification or //
        gmd:distributionInfo/gmd:MD_Distribution)



  * - serviceCoupling (isotc.serviceCoupling, SolrField)
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



  * - serviceTitle (isotc.serviceTitle, SolrField)
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



  * - serviceDescription (isotc.serviceDescription, SolrField)
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



  * - serviceType (isotc.serviceType, SolrField)
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:serviceType/
        gco:LocalName/text()



  * - serviceEndpoint (isotc.serviceEndpoint, SolrField)
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:containsOperations/
        srv:SV_OperationMetadata/srv:connectPoint/
        gmd:CI_OnlineResource/gmd:linkage/gmd:URL/text()



  * - serviceInput (isotc.serviceInput, SolrField)
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/srv:operatesOn/@xlink:href



  * - serviceOutput (isotc.serviceOutput, SolrField)
    - True
    - False
    - ::

        //srv:SV_ServiceIdentification/gmd:resourceFormat/
        @xlink:href



  * - serviceType (isotc.distribServiceType, SolrField)
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        gmd:MD_DigitalTransferOptions/gmd:onLine/
        gmd:CI_OnlineResource/gmd:protocol/
        gco:CharacterString/text()



  * - serviceEndpoint (isotc.distribServiceEndpoint, SolrField)
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



  * - serviceInput (isotc.distribServiceInput, SolrField)
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorTransferOptions/
        @xlink:href



  * - serviceOutput (isotc.distribServiceOutput, SolrField)
    - True
    - False
    - ::

        //gmd:distributionInfo/gmd:MD_Distribution/gmd:distributor/
        gmd:MD_Distributor/gmd:distributorFormat/
        gmd:MD_Format/gmd:version/gco:CharacterString/text()



  * - fileID (isotc.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - text (isotc.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


