fgdcEsri80Subprocessor
======================

Format IDs Processed
--------------------


  * http://www.esri.com/metadata/esriprof80.dtd



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


  * - beginDate (fgdc.beginDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/begdate/text()



  * - contactOrganization (fgdc.contactOrganization, SolrField)
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/distinfo/distrib/cntinfo/
        cntperp/cntorg/text() | /*[local-name() = 
        'metadata']/distinfo/distrib/cntinfo/cntorgp/cntorg/
        text()



  * - eastBoundCoord (fgdc.eastBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/eastbc/
        text()



  * - westBoundCoord (fgdc.westBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/westbc/
        text()



  * - northBoundCoord (fgdc.northBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/northbc/
        text()



  * - southBoundCoord (fgdc.southBoundCoord, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/bounding/southbc/
        text()



  * - edition (fgdc.edition, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citeinfo/edition/text()



  * - endDate (fgdc.endDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/timeperd/timeinfo/
        rngdates/enddate/text()



  * - gcmdKeyword (fgdc.gcmdKeyword, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme[themekt=
        'GCMD Science Keywords']/themekey/text()



  * - keywords (fgdc.keywords, SolrField)
    - True
    - True
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/theme/
        themekey/text() | /*[local-name() = 'metadata']/
        idinfo/keywords/place/placekey/text()



  * - geoform (fgdc.geoform, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()



  * - genus (fgdc.genus, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Genus"]/text()



  * - kingdom (fgdc.kingdom, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Kingdom"]/text()



  * - order (fgdc.order, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Order"]/text()



  * - phylum (fgdc.phylum, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Phylum"]/text() | //taxoncl/
        taxonrv[../taxonrn="Division"]/text()



  * - species (fgdc.species, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Species"]/text()



  * - family (fgdc.family, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Family"]/text()



  * - class (fgdc.class, SolrField)
    - True
    - False
    - ::

        //taxoncl/taxonrv[../taxonrn="Class"]/text()



  * - origin (fgdc.origin, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - scientificName (fgdc.scientificName, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - placeKey (fgdc.placeKey, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/keywords/place/
        placekey/text()



  * - pubDate (fgdc.pubDate, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        pubdate/text()



  * -  (fgdc.purpose, MergeSolrField)
    - 
    - 
    - 


  * - title (fgdc.title, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        title/text()



  * - webUrl (fgdc.web_url, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        onlink/text()



  * - fileID (fgdc.fileID, ResolveSolrField)
    - 
    - 
    - 


  * -  (fgdc.fullText, AggregateSolrField)
    - 
    - 
    - 


  * - presentationCat (fgdc.presentationCat, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        geoform/text()



  * - author (fgdc.author, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - authorSurName (fgdc.authorSurName, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()



  * - authorSurNameSort (fgdc.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin[1]/text()



  * - investigator (fgdc.investigator, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/citation/citeinfo/
        origin/text()



  * - site (fgdc.site, SolrField)
    - True
    - False
    - ::

        /*[local-name() = 'metadata']/idinfo/spdom/descgeog/text()



  * - attributeName (fgdc.attributeName, SolrField)
    - True
    - False
    - ::

        //attr/attrlabl/text()



  * - attributeLabel (fgdc.attributeLabel, SolrField)
    - True
    - False
    - ::

        //attr/attalias/text()



  * - attributeDescription (fgdc.attributeDescription, SolrField)
    - True
    - False
    - ::

        //attr/attrdef/text()



  * - attributeUnit (fgdc.attributeUnit, SolrField)
    - True
    - False
    - ::

        //attr/attrdomv//attrunit/text() | //attr//attrdomv//edomv/
        text()



  * - attribute (fgdc.attributeText, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_1 (fgdc.geohash1, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_2 (fgdc.geohash2, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_3 (fgdc.geohash3, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_4 (fgdc.geohash4, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_5 (fgdc.geohash5, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_6 (fgdc.geohash6, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_7 (fgdc.geohash7, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_8 (fgdc.geohash8, CommonRootSolrField)
    - False
    - False
    - ::

        



  * - geohash_9 (fgdc.geohash9, CommonRootSolrField)
    - False
    - False
    - ::

        


