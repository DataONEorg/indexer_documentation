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

  * - :attr:`Index.abstract`
    - False
    - False
    - ::

        //dcterms:description[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.abstract`_


  * - :attr:`Index.author`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.author`_


  * - :attr:`Index.authorSurName`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorSurName`_


  * - :attr:`Index.authorSurNameSort`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorSurNameSort`_


  * - :attr:`Index.authorGivenName`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorGivenName`_


  * - :attr:`Index.authorGivenNameSort`
    - False
    - False
    - ::

        //dcterms:creator[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.authorGivenNameSort`_


  * - :attr:`Index.investigator`
    - True
    - True
    - ::

        //dcterms:creator/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.investigator`_


  * - :attr:`Index.keywords`
    - True
    - False
    - ::

        //dcterms:subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.keywords`_


  * - :attr:`Index.origin`
    - True
    - True
    - ::

        //dcterms:creator/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.origin`_


  * - :attr:`Index.pubDate`
    - False
    - False
    - ::

        //dcterms:dateSubmitted/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.pubDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.site`
    - True
    - False
    - ::

        //dcterms:spatial/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.site`_


  * - :attr:`Index.title`
    - False
    - False
    - ::

        //dcterms:title[1]/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.title`_


  * - :attr:`Index.scientificName`
    - True
    - False
    - ::

        //dwc:scientificName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `dryad.scientificName`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `dryad.fileID`_
      | Converter: 


  * - :attr:`Index.text`
    - False
    - False
    - ::

        //*/text()

      | Processor: `FullTextSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/FullTextSolrField.java>`_
      | Configuration: `dryad.fullText`_



Bean Configurations
-------------------


dryad.abstract
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.abstract" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="abstract"/>
		<constructor-arg name="xpath" value="//dcterms:description[1]/text()"/>
	</bean>

	




dryad.author
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.author" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="author"/>
		<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>
	</bean>
	
	




dryad.authorSurName
~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorSurName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurName"/>
		<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>
	
	




dryad.authorSurNameSort
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorSurNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorSurNameSort"/>
		<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>
		<property name="substringBefore" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>	
	
	




dryad.authorGivenName
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorGivenName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenName"/>
		<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>
		<property name="substringAfter" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>
	
	




dryad.authorGivenNameSort
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.authorGivenNameSort" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="authorGivenNameSort"/>
		<constructor-arg name="xpath" value="//dcterms:creator[1]/text()"/>
		<property name="substringAfter" value="true"/>
		<property name="splitOnString" value=","/>
	</bean>	
	
	




dryad.investigator
~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.investigator" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="investigator"/>
		<constructor-arg name="xpath" value="//dcterms:creator/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	




dryad.keywords
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.keywords" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="keywords"/>
		<constructor-arg name="xpath" value="//dcterms:subject/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
	
	




dryad.origin
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.origin" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="origin"/>
		<constructor-arg name="xpath" value="//dcterms:creator/text()"/>
		<property name="multivalue" value="true"/>
		<property name="dedupe" value="true"/>
	</bean>
	
	




dryad.pubDate
~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.pubDate" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="pubDate"/>
		<constructor-arg name="xpath" value="//dcterms:dateSubmitted/text()"/>
		<property name="converter" ref="dateConverter"/>
	</bean>
	
 	




dryad.site
~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.site" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="site"/>
		<constructor-arg name="xpath" value="//dcterms:spatial/text()"/>
		<property name="multivalue" value="true"/>
	</bean>
		
	




dryad.title
~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.title" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="title"/>
		<constructor-arg name="xpath" value="//dcterms:title[1]/text()"/>
	</bean>
 
 	




dryad.scientificName
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.scientificName" class="org.dataone.cn.indexer.parser.SolrField">
		<constructor-arg name="name" value="scientificName"/>
		<constructor-arg name="xpath" value="//dwc:scientificName/text()"/>
		<property name="multivalue" value="true"/>
	</bean>

	




dryad.fileID
~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.fileID" class="org.dataone.cn.indexer.parser.ResolveSolrField">
		<constructor-arg name="name" value="fileID"/>
	</bean>
	
	




dryad.fullText
~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="dryad.fullText" class="org.dataone.cn.indexer.parser.FullTextSolrField">
		<constructor-arg name="name" value="text"/>
		<constructor-arg name="xpath" value="//*/text()"/>
		<property name="combineNodes" value="true"/>
	</bean>
	





