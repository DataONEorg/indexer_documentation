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

  * - author (datacite.author, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - authorLastName (datacite.author_lname, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - authorSurName (datacite.authorSurName, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - authorSurNameSort (datacite.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - authorGivenName (datacite.authorGivenName, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - authorGivenNameSort (datacite.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]



  * - abstract (datacite.abstract, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:descriptions/
        datacite:description[@descriptionType='Abstract'][1]
        /text())[1]



  * - title (datacite.title, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:titles/datacite:title[1]/text()
        )[1]



  * - pubDate (datacite.pubDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:publicationYear[1]/text())[1]



  * - keywords (datacite.keywords, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:subjects/datacite:subject/text()



  * - beginDate (datacite.beginDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]



  * - endDate (datacite.endDate, SolrField)
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]



  * - origin (datacite.origin, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text()



  * - investigator (datacite.investigator, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text() | /datacite:resource/
        datacite:contributors/datacite:contributor[
        @contributorType='DataCollector']/
        datacite:contributorName/text()



  * - contactOrganization (datacite.contactOrganization, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:contributors/
        datacite:contributor[@contributorType=
        'HostingInstitution']/datacite:contributorName/
        text()



  * - site (datacite.site, SolrField)
    - True
    - True
    - ::

        /datacite:resource/datacite:geoLocations/
        datacite:geoLocation/datacite:geoLocationPlace/
        text()



  * -  (datacite.boxSpatialBoundCoordinates, DataCiteSpatialBoxBoundingCoordinatesSolrField)
    - False
    - False
    - ::

        



  * -  (datacite.boxSpatialGeohash, DataCiteSpatialBoxGeohashSolrField)
    - False
    - False
    - ::

        



  * - fileID (datacite.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - text (datacite.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


