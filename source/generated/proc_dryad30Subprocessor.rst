dryad30Subprocessor
===================

Format IDs Processed
--------------------


  * http://purl.org/dryad/terms/



Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - :attr:`Index.abstract` (dryad.abstract, SolrField)
    - False
    - False
    - ::

        //dcterms:description[1]/text()



  * - :attr:`Index.author` (dryad.author, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - :attr:`Index.authorSurName` (dryad.authorSurName, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - :attr:`Index.authorSurNameSort` (dryad.authorSurNameSort, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - :attr:`Index.authorGivenName` (dryad.authorGivenName, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - :attr:`Index.authorGivenNameSort` (dryad.authorGivenNameSort, SolrField)
    - False
    - False
    - ::

        //dcterms:creator[1]/text()



  * - :attr:`Index.investigator` (dryad.investigator, SolrField)
    - True
    - True
    - ::

        //dcterms:creator/text()



  * - :attr:`Index.keywords` (dryad.keywords, SolrField)
    - True
    - False
    - ::

        //dcterms:subject/text()



  * - :attr:`Index.origin` (dryad.origin, SolrField)
    - True
    - True
    - ::

        //dcterms:creator/text()



  * - :attr:`Index.pubDate` (dryad.pubDate, SolrField)
    - False
    - False
    - ::

        //dcterms:dateSubmitted/text()



  * - :attr:`Index.site` (dryad.site, SolrField)
    - True
    - False
    - ::

        //dcterms:spatial/text()



  * - :attr:`Index.title` (dryad.title, SolrField)
    - False
    - False
    - ::

        //dcterms:title[1]/text()



  * - :attr:`Index.scientificName` (dryad.scientificName, SolrField)
    - True
    - False
    - ::

        //dwc:scientificName/text()



  * - :attr:`Index.fileID` (dryad.fileID, ResolveSolrField)
    - 
    - 
    - 


  * - :attr:`Index.text` (dryad.fullText, FullTextSolrField)
    - False
    - False
    - ::

        //*/text()


