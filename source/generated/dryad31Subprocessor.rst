dryad31Subprocessor
===================

Format IDs Processed
--------------------


  * http://datadryad.org/profile/v3.1



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - abstract (dryad.abstract, SolrField)
    - False
    - False
    - ::

        //dcterms:description[1]/text()



  * - author (dryad.author, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - authorSurName (dryad.authorSurName, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - authorSurNameSort (dryad.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - authorGivenName (dryad.authorGivenName, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - authorGivenNameSort (dryad.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - investigator (dryad.investigator, SolrField)
    - True
    - True
    - ::

        //dcterms:creator/text()



  * - keywords (dryad.keywords, SolrField)
    - True
    - False
    - ::

        //dcterms:subject/text()



  * - origin (dryad.origin, SolrField)
    - True
    - True
    - ::

        //dcterms:creator/text()



  * - pubDate (dryad.pubDate, SolrField)
    - False
    - False
    - ::

        //dcterms:dateSubmitted/text()



  * - site (dryad.site, SolrField)
    - True
    - False
    - ::

        //dcterms:spatial/text()



  * - title (dryad.title, SolrField)
    - False
    - False
    - ::

        //dcterms:title[1]/text()



  * - scientificName (dryad.scientificName, SolrField)
    - True
    - False
    - ::

        //dwc:scientificName/text()



  * - fileID (dryad.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - text (dryad.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


