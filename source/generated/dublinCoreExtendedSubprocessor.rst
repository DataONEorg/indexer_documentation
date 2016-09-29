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

  * - :attr:`Index.abstract` (dc.abstract, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'abstract'][1]/text()



  * - :attr:`Index.author` (dc.author, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - :attr:`Index.authorSurName` (dc.authorSurName, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - :attr:`Index.authorSurNameSort` (dc.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'creator'][1]/text()



  * - :attr:`Index.contactOrganization` (dc.contactOrganization, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - :attr:`Index.investigator` (dc.investigator, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - :attr:`Index.origin` (dc.origin, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'creator']/text()



  * - :attr:`Index.pubDate` (dc.pubDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'dateSubmitted']/text()



  * - :attr:`Index.title` (dc.title, SolrField)
    - False
    - False
    - ::

        (//*[local-name() = 'title'][1]/text())[1]



  * - :attr:`Index.keywords` (dc.keywords, SolrField)
    - True
    - False
    - ::

        //*[local-name() = 'subject']/text()



  * - :attr:`Index.beginDate` (dc.beginDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()



  * - :attr:`Index.endDate` (dc.endDate, SolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][not(@xsi:type=
        'dcterms:Period') and not(@xsi:type='dc:Period') 
        and not(@xsi:type='Period')]/text()



  * - :attr:`Index.beginDate`,:attr:`Index.endDate` (dc.datePeriod, TemporalPeriodSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'temporal'][@xsi:type='dcterms:Period' 
        or @xsi:type='dc:Period' or @xsi:type='Period']/
        text()



  * - :attr:`Index.site` (dc.site, SolrField)
    - True
    - True
    - ::

        //*[local-name() = 'spatial'][not(@xsi:type = 'dcterms:Box')
         and not(@xsi:type = 'dc:Box') and not(@xsi:type = 
        'Box')]/text()



  * - :attr:`Index.northBoundCoord`,:attr:`Index.southBoundCoord`,:attr:`Index.eastBoundCoord`,:attr:`Index.westBoundCoord` (dc.boxSpatialBoundCoordinates, DublinCoreSpatialBoxBoundingCoordinatesSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]



  * - :attr:`Index.geohash_1`,:attr:`Index.geohash_2`,:attr:`Index.geohash_3`,:attr:`Index.geohash_4`,:attr:`Index.geohash_5`,:attr:`Index.geohash_6`,:attr:`Index.geohash_7`,:attr:`Index.geohash_8`,:attr:`Index.geohash_9` (dc.boxSpatialGeohash, DublinCoreSpatialBoxGeohashSolrField)
    - False
    - False
    - ::

        //*[local-name() = 'spatial'][@xsi:type='dcterms:Box' or 
        @xsi:type='dc:Box' or @xsi:type='Box'][1]/text()[1]



  * - :attr:`Index.fileID` (dc.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - :attr:`Index.text` (dc.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


