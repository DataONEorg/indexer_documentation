datacite3Subprocessor
=====================

Format IDs Processed
--------------------


  * http://datacite.org/schema/kernel-3.1

  * http://datacite.org/schema/kernel-3.0



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - :attr:`Index.author` (datacite.author, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.authorLastName` (datacite.author_lname, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.authorSurName` (datacite.authorSurName, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.authorSurNameSort` (datacite.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.authorGivenName` (datacite.authorGivenName, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.authorGivenNameSort` (datacite.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - :attr:`Index.abstract` (datacite.abstract, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:descriptions/
        datacite:description[@descriptionType='Abstract'][1]
        /text())[1]



  * - :attr:`Index.title` (datacite.title, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:titles/datacite:title[1]/text()
        )[1]



  * - :attr:`Index.pubDate` (datacite.pubDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:publicationYear[1]/text())[1]



  * - :attr:`Index.keywords` (datacite.keywords, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:subjects/datacite:subject/text()



  * - :attr:`Index.beginDate` (datacite.beginDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]



  * - :attr:`Index.endDate` (datacite.endDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]



  * - :attr:`Index.origin` (datacite.origin, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text()



  * - :attr:`Index.investigator` (datacite.investigator, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text() | /datacite:resource/
        datacite:contributors/datacite:contributor[
        @contributorType='DataCollector']/
        datacite:contributorName/text()



  * - :attr:`Index.contactOrganization` (datacite.contactOrganization, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:contributors/
        datacite:contributor[@contributorType=
        'HostingInstitution']/datacite:contributorName/
        text()



  * - :attr:`Index.site` (datacite.site, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:geoLocations/
        datacite:geoLocation/datacite:geoLocationPlace/
        text()



  * - :attr:`Index.` (datacite.boxSpatialBoundCoordinates, DataCiteSpatialBoxBoundingCoordinatesSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.` (datacite.boxSpatialGeohash, DataCiteSpatialBoxGeohashSolrField)
    - False
    - False
    - ::

        



  * - :attr:`Index.fileID` (datacite.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - :attr:`Index.text` (datacite.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


