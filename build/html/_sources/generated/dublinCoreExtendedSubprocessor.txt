dublinCoreExtendedSubprocessor
==============================

Format IDs Processed
--------------------


  * http://ns.dataone.org/metadata/schema/onedcx/v1.0



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - abstract (dc.abstract, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'abstract'][1]/text()



  * - author (dc.author, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - authorSurName (dc.authorSurName, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - authorSurNameSort (dc.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - contactOrganization (dc.contactOrganization, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - investigator (dc.investigator, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - origin (dc.origin, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - pubDate (dc.pubDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'dateSubmitted']/text()



  * - title (dc.title, SolrField)
    - False
    - False
    - ::

        (//*[local-name() = 'title'][1]/text())[1]



  * - keywords (dc.keywords, SolrField)
    - True
    - False
    - ::

        //*[local-name() = 'subject']/text()



  * - beginDate (dc.beginDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()



  * - endDate (dc.endDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()



  * - beginDate, endDate (dc.datePeriod, TemporalPeriodSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][@xsi:type='dcterms:Period' 
        or @xsi:type='dc:Period' or @xsi:type='Period']/
        text()



  * - site (dc.site, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'spatial'][not(@xsi:type = 'dcterms:Box')
         and not(@xsi:type = 'dc:Box') and not(@xsi:type = 
        'Box')]/text()



  * - northBoundCoord, southBoundCoord, eastBoundCoord, westBoundCoord (dc.boxSpatialBoundCoordinates, DublinCoreSpatialBoxBoundingCoordinatesSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]



  * - geohash_1, geohash_2, geohash_3, geohash_4, geohash_5, geohash_6, geohash_7, geohash_8, geohash_9 (dc.boxSpatialGeohash, DublinCoreSpatialBoxGeohashSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]



  * - fileID (dc.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - text (dc.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


