eml200Subprocessor
==================

Format IDs Processed
--------------------


  * eml://ecoinformatics.org/eml-2.0.0



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * -  (eml.abstract, MergeSolrField)
    - 
    - 
    - 


  * - :attr:`Index.keywords` (eml.keywords, SolrField)
    - True
    - True
    - ::

        //dataset/keywordSet/keyword/text()



  * - :attr:`Index.title` (eml.title, SolrField)
    - False
    - False
    - ::

        //dataset/title/text()



  * - :attr:`Index.project` (eml.project, SolrField)
    - False
    - False
    - ::

        //dataset/project/title/text()



  * - :attr:`Index.southBoundCoord` (eml.southBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        southBoundingCoordinate/text()



  * - :attr:`Index.northBoundCoord` (eml.northBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        northBoundingCoordinate/text()



  * - :attr:`Index.westBoundCoord` (eml.westBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        westBoundingCoordinate/text()



  * - :attr:`Index.eastBoundCoord` (eml.eastBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        eastBoundingCoordinate/text()



  * - :attr:`Index.site` (eml.site, SolrField)
    - True
    - False
    - ::

        //dataset/coverage/geographicCoverage/geographicDescription/
        text()



  * - :attr:`Index.beginDate` (eml.beginDate, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/beginDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()



  * - :attr:`Index.endDate` (eml.endDate, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/endDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()



  * - :attr:`Index.pubDate` (eml.pubDate, SolrField)
    - False
    - False
    - ::

        //dataset/pubDate/text()



  * - :attr:`Index.author` (eml.author, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.authorLastName` (eml.author_lname, SolrField)
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()



  * - :attr:`Index.authorGivenName` (eml.authorGivenName, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()



  * - :attr:`Index.authorSurName` (eml.authorSurName, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()



  * - :attr:`Index.authorGivenNameSort` (eml.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()



  * - :attr:`Index.authorSurNameSort` (eml.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()



  * - :attr:`Index.investigator` (eml.investigator, SolrField)
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()



  * - :attr:`Index.origin` (eml.origin, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.contactOrganization` (eml.contactOrganization, SolrField)
    - True
    - True
    - ::

        //dataset/creator/organizationName/text()



  * - :attr:`Index.genus` (eml.genus, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Genus"]/text()



  * - :attr:`Index.species` (eml.species, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Species"]/text()



  * - :attr:`Index.kingdom` (eml.kingdom, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Kingdom"]/text()



  * - :attr:`Index.order` (eml.order, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Order"]/text()



  * - :attr:`Index.phylum` (eml.phylum, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Phylum"]/text() | //taxonomicClassification/
        taxonRankValue[../taxonRankName="Division"]/text()



  * - :attr:`Index.family` (eml.family, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Family"]/text()



  * - :attr:`Index.class` (eml.class, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Class"]/text()



  * - :attr:`Index.scientificName` (eml.scientificName, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.attributeName` (eml.attributeName, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeName/text()



  * - :attr:`Index.attributeLabel` (eml.attributeLabel, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeLabel/text()



  * - :attr:`Index.attributeDescription` (eml.attributeDescription, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeDefinition/
        text()



  * - :attr:`Index.attributeUnit` (eml.attributeUnit, SolrField)
    - True
    - False
    - ::

        //dataTable//standardUnit/text() | //dataTable//customUnit/
        text()



  * - :attr:`Index.attribute` (eml.attributeText, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.fileID` (eml.fileID, ResolveSolrField)
    - 
    - 
    - 


  * -  (eml.fullText, AggregateSolrField)
    - 
    - 
    - 


  * - :attr:`Index.geohash_1` (eml.geohash1, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_2` (eml.geohash2, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_3` (eml.geohash3, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_4` (eml.geohash4, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_5` (eml.geohash5, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_6` (eml.geohash6, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_7` (eml.geohash7, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_8` (eml.geohash8, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_9` (eml.geohash9, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.isService` (eml.isService, SolrField)
    - False
    - False
    - ::

        boolean(//software/implementation/distribution/online/url)



  * - :attr:`Index.serviceTitle` (eml.serviceTitle, SolrField)
    - False
    - False
    - ::

        //software/title//text()[normalize-space()]



  * - :attr:`Index.serviceDescription` (eml.serviceDescription, SolrField)
    - False
    - False
    - ::

        //software/abstract//text()[normalize-space()]



  * - :attr:`Index.serviceEndpoint` (eml.serviceEndpoint, SolrField)
    - True
    - False
    - ::

        //software/implementation/distribution/online/url/text()


