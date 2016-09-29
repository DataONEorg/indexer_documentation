eml201Subprocessor
==================

Format IDs Processed
--------------------


  * eml://ecoinformatics.org/eml-2.0.1



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


  * - keywords (eml.keywords, SolrField)
    - True
    - True
    - ::

        //dataset/keywordSet/keyword/text()



  * - title (eml.title, SolrField)
    - False
    - False
    - ::

        //dataset/title/text()



  * - project (eml.project, SolrField)
    - False
    - False
    - ::

        //dataset/project/title/text()



  * - southBoundCoord (eml.southBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        southBoundingCoordinate/text()



  * - northBoundCoord (eml.northBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        northBoundingCoordinate/text()



  * - westBoundCoord (eml.westBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        westBoundingCoordinate/text()



  * - eastBoundCoord (eml.eastBoundCoord, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/geographicCoverage/boundingCoordinates/
        eastBoundingCoordinate/text()



  * - site (eml.site, SolrField)
    - True
    - False
    - ::

        //dataset/coverage/geographicCoverage/geographicDescription/
        text()



  * - beginDate (eml.beginDate, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/beginDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()



  * - endDate (eml.endDate, SolrField)
    - False
    - False
    - ::

        //dataset/coverage/temporalCoverage/rangeOfDates/endDate/
        calendarDate/text() | //dataset/coverage/
        temporalCoverage/singleDateTime/calendarDate/text()



  * - pubDate (eml.pubDate, SolrField)
    - False
    - False
    - ::

        //dataset/pubDate/text()



  * - author (eml.author, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - authorGivenName (eml.authorGivenName, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()



  * - authorSurName (eml.authorSurName, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()



  * - authorGivenNameSort (eml.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/givenName/text()



  * - authorSurNameSort (eml.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //dataset/creator[1]/individualName[1]/surName/text()



  * - authorLastName (eml.author_lname, SolrField)
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()



  * - investigator (eml.investigator, SolrField)
    - True
    - False
    - ::

        //dataset/creator/individualName/surName/text()



  * - origin (eml.origin, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - contactOrganization (eml.contactOrganization, SolrField)
    - True
    - True
    - ::

        //dataset/creator/organizationName/text()



  * - genus (eml.genus, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Genus"]/text()



  * - species (eml.species, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Species"]/text()



  * - kingdom (eml.kingdom, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Kingdom"]/text()



  * - order (eml.order, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Order"]/text()



  * - phylum (eml.phylum, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Phylum"]/text() | //taxonomicClassification/
        taxonRankValue[../taxonRankName="Division"]/text()



  * - family (eml.family, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Family"]/text()



  * - class (eml.class, SolrField)
    - True
    - True
    - ::

        //taxonomicClassification/taxonRankValue[../taxonRankName=
        "Class"]/text()



  * - scientificName (eml.scientificName, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - attributeName (eml.attributeName, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeName/text()



  * - attributeLabel (eml.attributeLabel, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeLabel/text()



  * - attributeDescription (eml.attributeDescription, SolrField)
    - True
    - False
    - ::

        //dataTable/attributeList/attribute/attributeDefinition/
        text()



  * - attributeUnit (eml.attributeUnit, SolrField)
    - True
    - False
    - ::

        //dataTable//standardUnit/text() | //dataTable//customUnit/
        text()



  * - attribute (eml.attributeText, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - fileID (eml.fileID, ResolveSolrField)
    - 
    - 
    - 


  * -  (eml.fullText, AggregateSolrField)
    - 
    - 
    - 


  * - geohash_1 (eml.geohash1, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_2 (eml.geohash2, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_3 (eml.geohash3, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_4 (eml.geohash4, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_5 (eml.geohash5, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_6 (eml.geohash6, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_7 (eml.geohash7, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_8 (eml.geohash8, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_9 (eml.geohash9, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - isService (eml.isService, SolrField)
    - False
    - False
    - ::

        boolean(//software/implementation/distribution/online/url)



  * - serviceTitle (eml.serviceTitle, SolrField)
    - False
    - False
    - ::

        //software/title//text()[normalize-space()]



  * - serviceDescription (eml.serviceDescription, SolrField)
    - False
    - False
    - ::

        //software/abstract//text()[normalize-space()]



  * - serviceEndpoint (eml.serviceEndpoint, SolrField)
    - True
    - False
    - ::

        //software/implementation/distribution/online/url/text()


