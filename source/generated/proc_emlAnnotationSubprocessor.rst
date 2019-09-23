Ecological Markup Language Annotations
======================================

Describes parser configuration for: emlAnnotationSubprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | Ecological Metadata Language, version 2.2.0
    | formatId: ``https://eml.ecoinformatics.org/eml-2.2.0``


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

  * - :attr:`Index.sem_annotation`
    - False
    - False
    - ::

        //annotation/valueURI/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `emlAnnotationSubprocessor.bean0`_



Bean Configurations
-------------------


emlAnnotationSubprocessor.bean0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" class="org.dataone.cn.indexer.parser.SolrField" id="emlAnnotationSubprocessor.bean0">
					<constructor-arg name="name" value="sem_annotation"/>
					<constructor-arg name="xpath" value="//annotation/valueURI/text()"/>
					<constructor-arg name="multivalue" value="true"/>
				</bean>
			



