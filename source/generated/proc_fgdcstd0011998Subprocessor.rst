fgdcstd0011998Subprocessor
==========================

Format IDs Processed
--------------------


  * FGDC-STD-001-1998



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * -  (fgdc.abstract, MergeSolrField)
    - 
    - 
    - 


  * - :attr:`Index.beginDate` (fgdc.beginDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/begdate/text()



  * - :attr:`Index.contactOrganization` (fgdc.contactOrganization, SolrField)
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/distinfo/distrib/cntinfo/
        cntperp/cntorg/text() | /*[local-name() = 
        'metadata']/distinfo/distrib/cntinfo/cntorgp/cntorg/
        text()



  * - :attr:`Index.eastBoundCoord` (fgdc.eastBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/eastbc/
        text()



  * - :attr:`Index.westBoundCoord` (fgdc.westBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/westbc/
        text()



  * - :attr:`Index.northBoundCoord` (fgdc.northBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/northbc/
        text()



  * - :attr:`Index.southBoundCoord` (fgdc.southBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/southbc/
        text()



  * - :attr:`Index.edition` (fgdc.edition, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citeinfo/edition/text()



  * - :attr:`Index.endDate` (fgdc.endDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/enddate/text()



  * - :attr:`Index.gcmdKeyword` (fgdc.gcmdKeyword, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme[themekt=
        'GCMD Science Keywords']/themekey/text()



  * - :attr:`Index.keywords` (fgdc.keywords, SolrField)
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme/
        themekey/text() | /*[local-name() = 'metadata']/
        idinfo/keywords/place/placekey/text()



  * - :attr:`Index.geoform` (fgdc.geoform, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()



  * - :attr:`Index.genus` (fgdc.genus, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Genus"]/text()



  * - :attr:`Index.kingdom` (fgdc.kingdom, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Kingdom"]/text()



  * - :attr:`Index.order` (fgdc.order, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Order"]/text()



  * - :attr:`Index.phylum` (fgdc.phylum, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Phylum"]/text() | //taxoncl/
        taxonrv[../taxonrn="Division"]/text()



  * - :attr:`Index.species` (fgdc.species, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Species"]/text()



  * - :attr:`Index.family` (fgdc.family, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Family"]/text()



  * - :attr:`Index.class` (fgdc.class, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Class"]/text()



  * - :attr:`Index.scientificName` (fgdc.scientificName, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.origin` (fgdc.origin, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - :attr:`Index.placeKey` (fgdc.placeKey, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/place/
        placekey/text()



  * - :attr:`Index.pubDate` (fgdc.pubDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        pubdate/text()



  * -  (fgdc.purpose, MergeSolrField)
    - 
    - 
    - 


  * - :attr:`Index.title` (fgdc.title, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        title/text()



  * - :attr:`Index.webUrl` (fgdc.web_url, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        onlink/text()



  * - :attr:`Index.fileID` (fgdc.fileID, ResolveSolrField)
    - 
    - 
    - 


  * -  (fgdc.fullText, AggregateSolrField)
    - 
    - 
    - 


  * - :attr:`Index.presentationCat` (fgdc.presentationCat, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()



  * - :attr:`Index.author` (fgdc.author, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - :attr:`Index.authorSurName` (fgdc.authorSurName, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()



  * - :attr:`Index.authorSurNameSort` (fgdc.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()



  * - :attr:`Index.investigator` (fgdc.investigator, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - :attr:`Index.site` (fgdc.site, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/descgeog/text()



  * - :attr:`Index.attributeName` (fgdc.attributeName, SolrField)
    - True
    - False
    - ::

        //attr/attrlabl/text()



  * - :attr:`Index.attributeLabel` (fgdc.attributeLabel, SolrField)
    - True
    - False
    - ::

        //attr/attalias/text()



  * - :attr:`Index.attributeDescription` (fgdc.attributeDescription, SolrField)
    - True
    - False
    - ::

        //attr/attrdef/text()



  * - :attr:`Index.attributeUnit` (fgdc.attributeUnit, SolrField)
    - True
    - False
    - ::

        //attr/attrdomv//attrunit/text() | //attr//attrdomv//edomv/
        text()



  * - :attr:`Index.attribute` (fgdc.attributeText, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_1` (fgdc.geohash1, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_2` (fgdc.geohash2, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_3` (fgdc.geohash3, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_4` (fgdc.geohash4, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_5` (fgdc.geohash5, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_6` (fgdc.geohash6, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_7` (fgdc.geohash7, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_8` (fgdc.geohash8, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.geohash_9` (fgdc.geohash9, CommonRootSolrField)
    - False
    - False
    - ::

        


