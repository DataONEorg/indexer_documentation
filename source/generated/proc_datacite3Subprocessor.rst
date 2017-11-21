DataCite 3
==========

Describes parser configuration for: datacite3Subprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | DataCite Metadata Schema version 3.1
    | formatId: ``http://datacite.org/schema/kernel-3.1``

  * | DataCite Metadata Schema version 3.0
    | formatId: ``http://datacite.org/schema/kernel-3.0``


A full list of DataONE format IDs can be found at https://cn.dataone.org/cn/v2/formats/

Fields
------

The following fields in the solr index are populated from values retrieved from this type of metadata document.
Note that these are in addition to the information extracted from :doc:`system_metadata`.

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - Source

  * - :attr:`Index.author`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.author`_


  * - :attr:`Index.authorLastName`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.author_lname`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.authorSurNameSort`_


  * - :attr:`Index.authorGivenName`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.authorGivenName`_


  * - :attr:`Index.authorGivenNameSort`
    - False
    - False
    - ::

        (/datacite:resource/datacite:creators/datacite:creator[1]/
        datacite:creatorName[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.authorGivenNameSort`_


  * - :attr:`Index.abstract`
    - False
    - False
    - ::

        (/datacite:resource/datacite:descriptions/
        datacite:description[@descriptionType='Abstract'][1]
        /text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.abstract`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        (/datacite:resource/datacite:titles/datacite:title[1]/text()
        )[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.title`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        (/datacite:resource/datacite:publicationYear[1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.keywords`
    - True
    - True
    - ::

        /datacite:resource/datacite:subjects/datacite:subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.keywords`_


  * - :attr:`Index.beginDate`
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.beginDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.endDate`
    - False
    - False
    - ::

        (/datacite:resource/datacite:dates/datacite:date[@dateType=
        'Collected'][1]/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.endDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.origin`
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.origin`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        /datacite:resource/datacite:creators/datacite:creator/
        datacite:creatorName/text() | /datacite:resource/
        datacite:contributors/datacite:contributor[
        @contributorType='DataCollector']/
        datacite:contributorName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.investigator`_


  * - :attr:`Index.contactOrganization`
    - True
    - True
    - ::

        /datacite:resource/datacite:contributors/
        datacite:contributor[@contributorType=
        'HostingInstitution']/datacite:contributorName/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.contactOrganization`_


  * - :attr:`Index.site`
    - True
    - True
    - ::

        /datacite:resource/datacite:geoLocations/
        datacite:geoLocation/datacite:geoLocationPlace/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `datacite.site`_


  * - 
    - False
    - False
    - ::

        

      | Processor: `DataCiteSpatialBoxBoundingCoordinatesSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/DataCiteSpatialBoxBoundingCoordinatesSolrField.java>`_
      | Configuration: `datacite.boxSpatialBoundCoordinates`_


  * - 
    - False
    - False
    - ::

        

      | Processor: `DataCiteSpatialBoxGeohashSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/DataCiteSpatialBoxGeohashSolrField.java>`_
      | Configuration: `datacite.boxSpatialGeohash`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `datacite.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `datacite.fullText`_



Bean Configurations
-------------------


datacite.author
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.author" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="author"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t</bean>\n\n\t\n'


datacite.author_lname
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.author_lname" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorLastName"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\n\t\n\t\n'


datacite.authorSurName
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurName"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\n\t\n\t\n'


datacite.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorSurNameSort"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\t\n\t\n\t\n'


datacite.authorGivenName
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenName"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t\t<property name="substringAfter" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\n\t\n\t\n'


datacite.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="authorGivenNameSort"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>\n\t\t<property name="substringAfter" value="true"/>\n\t\t<property name="splitOnString" value=","/>\n\t</bean>\t\n\t\n\t\n'


datacite.abstract
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.abstract" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="abstract"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:descriptions/datacite:description[@descriptionType=\'Abstract\'][1]/text())[1]"/>\n\t\t<property name="multivalue" value="false"/>\n\t  \t<property name="dedupe" value="false"/>\n\t</bean>\n\t\n\t\n'


datacite.title
~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.title" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="title"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:titles/datacite:title[1]/text())[1]"/>\n\t</bean>\n\n\t\n'


datacite.pubDate
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.pubDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="pubDate"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:publicationYear[1]/text())[1]"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\t\n\t\n'


datacite.keywords
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.keywords" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="keywords"/>\n\t\t<constructor-arg name="xpath" value="/datacite:resource/datacite:subjects/datacite:subject/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\n\t\n'


datacite.beginDate
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.beginDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="beginDate"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:dates/datacite:date[@dateType=\'Collected\'][1]/text())[1]"/>\n\t\t<property name="substringBefore" value="true"/>\n\t\t<property name="splitOnString" value="/"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\t\n\t\n\t\n'


datacite.endDate
~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.endDate" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="endDate"/>\n\t\t<constructor-arg name="xpath" value="(/datacite:resource/datacite:dates/datacite:date[@dateType=\'Collected\'][1]/text())[1]"/>\n\t\t<property name="substringAfter" value="true"/>\n\t\t<property name="splitOnString" value="/"/>\n\t\t<property name="converter" ref="dateConverter"/>\n\t</bean>\n\n\t\n'


datacite.origin
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.origin" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="origin"/>\n\t\t<constructor-arg name="xpath" value="/datacite:resource/datacite:creators/datacite:creator/datacite:creatorName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


datacite.investigator
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.investigator" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="investigator"/>\n\t\t<constructor-arg name="xpath" value="/datacite:resource/datacite:creators/datacite:creator/datacite:creatorName/text() | /datacite:resource/datacite:contributors/datacite:contributor[@contributorType=\'DataCollector\']/datacite:contributorName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


datacite.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="contactOrganization"/>\n\t\t<constructor-arg name="xpath" value="/datacite:resource/datacite:contributors/datacite:contributor[@contributorType=\'HostingInstitution\']/datacite:contributorName/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


datacite.site
~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.site" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t<constructor-arg name="name" value="site"/>\n\t\t<constructor-arg name="xpath" value="/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPlace/text()"/>\n\t\t<property name="multivalue" value="true"/>\n\t\t<property name="dedupe" value="true"/>\n\t</bean>\n\t\n\t\n'


datacite.boxSpatialBoundCoordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.boxSpatialBoundCoordinates" class="org.dataone.cn.indexer.parser.DataCiteSpatialBoxBoundingCoordinatesSolrField">\n\t\t<property name="pointXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPoint[1]/text())[1]"/>\n\t\t<property name="boxXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationBox[1]/text())[1]"/>\n\t</bean>\n\n\t\n'


datacite.boxSpatialGeohash
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.boxSpatialGeohash" class="org.dataone.cn.indexer.parser.DataCiteSpatialBoxGeohashSolrField">\n\t\t<property name="pointXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPoint[1]/text())[1]"/>\n\t\t<property name="boxXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationBox[1]/text())[1]"/>\n\t</bean>\n\n\t\n'


datacite.fileID
~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t<constructor-arg name="name" value="fileID"/>\n\t</bean>\n\t\n\t\n'


datacite.fullText
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">\n\t\t<constructor-arg name="name" value="text"/>\n\t\t<constructor-arg name="xpath" value="//*/text()"/>\n\t\t<property name="combineNodes" value="true"/>\n\t</bean>\t\t\n\n'


