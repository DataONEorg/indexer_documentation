Semantic Annotation from JSON
=============================

Describes parser configuration for: annotatorSubprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | AnnotatorJS 1.2.x Annotation model
    | formatId: ``http://docs.annotatorjs.org/en/v1.2.x/annotation-format.html``


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

        
				
				SELECT ?sem_annotation
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation .
				 	} 
				 
			

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `annotation.expansion`_


  * - :attr:`Index.sem_annotation_bioportal_sm`
    - False
    - False
    - ::

        
				
				SELECT ?sem_annotation_bioportal_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_bioportal_sm .
				 	} 
				 
			

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `annotation.bioportal.expansion`_


  * - :attr:`Index.sem_annotation_esor_sm`
    - False
    - False
    - ::

        
				
				SELECT ?sem_annotation_esor_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_esor_sm .
				 	} 
				 
			

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `annotation.esor.expansion`_


  * - :attr:`Index.sem_annotation_cosine_sm`
    - False
    - False
    - ::

        
				
				SELECT ?sem_annotation_cosine_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_cosine_sm .
				 	} 
				 
			

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `annotation.cosine.expansion`_



Bean Configurations
-------------------


annotation.expansion
~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">\n\t\t<constructor-arg name="name" value="sem_annotation"/>\n\t\t<constructor-arg name="query">\n\t\t\t<value>\n\t\t\t\t<![CDATA[\n\t\t\t\tPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\t\t\t\tPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n\t\t\t\tPREFIX owl: <http://www.w3.org/2002/07/owl#> \n\t\t\t\t\n\t\t\t\tSELECT ?sem_annotation\n\t\t\t\tWHERE { \n\t\t\t\t\t\t<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation .\n\t\t\t\t \t} \n\t\t\t\t ]]>\n\t\t\t</value>\n\t\t</constructor-arg>\n\t\t<!--property name="multivalue" value="false" /-->\n\t</bean>\n\t\n\t\n'


annotation.bioportal.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.bioportal.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">\n\t\t<constructor-arg name="name" value="sem_annotation_bioportal_sm"/>\n\t\t<constructor-arg name="query">\n\t\t\t<value>\n\t\t\t\t<![CDATA[\n\t\t\t\tPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\t\t\t\tPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n\t\t\t\tPREFIX owl: <http://www.w3.org/2002/07/owl#> \n\t\t\t\t\n\t\t\t\tSELECT ?sem_annotation_bioportal_sm\n\t\t\t\tWHERE { \n\t\t\t\t\t\t<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_bioportal_sm .\n\t\t\t\t \t} \n\t\t\t\t ]]>\n\t\t\t</value>\n\t\t</constructor-arg>\n\t</bean>\n\t\n'


annotation.esor.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.esor.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">\n\t\t<constructor-arg name="name" value="sem_annotation_esor_sm"/>\n\t\t<constructor-arg name="query">\n\t\t\t<value>\n\t\t\t\t<![CDATA[\n\t\t\t\tPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\t\t\t\tPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n\t\t\t\tPREFIX owl: <http://www.w3.org/2002/07/owl#> \n\t\t\t\t\n\t\t\t\tSELECT ?sem_annotation_esor_sm\n\t\t\t\tWHERE { \n\t\t\t\t\t\t<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_esor_sm .\n\t\t\t\t \t} \n\t\t\t\t ]]>\n\t\t\t</value>\n\t\t</constructor-arg>\n\t</bean>\n\t\n'


annotation.cosine.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.cosine.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">\n\t\t<constructor-arg name="name" value="sem_annotation_cosine_sm"/>\n\t\t<constructor-arg name="query">\n\t\t\t<value>\n\t\t\t\t<![CDATA[\n\t\t\t\tPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n\t\t\t\tPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n\t\t\t\tPREFIX owl: <http://www.w3.org/2002/07/owl#> \n\t\t\t\t\n\t\t\t\tSELECT ?sem_annotation_cosine_sm\n\t\t\t\tWHERE { \n\t\t\t\t\t\t<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_cosine_sm .\n\t\t\t\t \t} \n\t\t\t\t ]]>\n\t\t\t</value>\n\t\t</constructor-arg>\n\t</bean>\n\n\n'


