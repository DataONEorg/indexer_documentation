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
      | Notes: SolrField which configures the resolve url for the document being processed.
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

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.author" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="author"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
	</bean>

	



datacite.author_lname
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.author_lname" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorLastName"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>
	
	



datacite.authorSurName
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>
	
	



datacite.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>	
	
	



datacite.authorGivenName
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenName"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
		<property name="substringAfter" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>
	
	



datacite.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenNameSort"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:creators/datacite:creator[1]/datacite:creatorName[1]/text())[1]"/>
		<property name="substringAfter" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>	
	
	



datacite.abstract
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.abstract" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="abstract"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:descriptions/datacite:description[@descriptionType='Abstract'][1]/text())[1]"/>
		<property name="multivalue" value="false"/>
	  	<property name="dedupe" value="false"/>
	</bean>
	
	



datacite.title
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:titles/datacite:title[1]/text())[1]"/>
	</bean>

	



datacite.pubDate
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:publicationYear[1]/text())[1]"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
	



datacite.keywords
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="/datacite:resource/datacite:subjects/datacite:subject/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>

	



datacite.beginDate
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.beginDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="beginDate"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:dates/datacite:date[@dateType='Collected'][1]/text())[1]"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value="/"/>
		<property name="converter" ref="dateConverter"/>
	</bean>	
	
	



datacite.endDate
~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.endDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="endDate"/>
		<constructor-arg name="xpath" value="(/datacite:resource/datacite:dates/datacite:date[@dateType='Collected'][1]/text())[1]"/>
		<property name="substringAfter" value="true"/>
		<property name="splitOnString" value="/"/>
		<property name="converter" ref="dateConverter"/>
	</bean>

	



datacite.origin
~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.origin" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="origin"/>
		<constructor-arg name="xpath" value="/datacite:resource/datacite:creators/datacite:creator/datacite:creatorName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



datacite.investigator
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="/datacite:resource/datacite:creators/datacite:creator/datacite:creatorName/text() | /datacite:resource/datacite:contributors/datacite:contributor[@contributorType='DataCollector']/datacite:contributorName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



datacite.contactOrganization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.contactOrganization" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="contactOrganization"/>
		<constructor-arg name="xpath" value="/datacite:resource/datacite:contributors/datacite:contributor[@contributorType='HostingInstitution']/datacite:contributorName/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



datacite.site
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.site" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="site"/>
		<constructor-arg name="xpath" value="/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPlace/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	



datacite.boxSpatialBoundCoordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.boxSpatialBoundCoordinates" class="org.dataone.cn.indexer.parser.DataCiteSpatialBoxBoundingCoordinatesSolrField">
		<property name="pointXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPoint[1]/text())[1]"/>
		<property name="boxXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationBox[1]/text())[1]"/>
	</bean>

	



datacite.boxSpatialGeohash
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.boxSpatialGeohash" class="org.dataone.cn.indexer.parser.DataCiteSpatialBoxGeohashSolrField">
		<property name="pointXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationPoint[1]/text())[1]"/>
		<property name="boxXPath" value="(/datacite:resource/datacite:geoLocations/datacite:geoLocation/datacite:geoLocationBox[1]/text())[1]"/>
	</bean>

	



datacite.fileID
~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>
	
	



datacite.fullText
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="datacite.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">
		<constructor-arg name="name" value="text"/>
		<constructor-arg name="xpath" value="//*/text()"/>
		<property name="combineNodes" value="true"/>
	</bean>		




