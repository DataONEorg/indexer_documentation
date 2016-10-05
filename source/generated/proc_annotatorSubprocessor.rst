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

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">
		<constructor-arg name="name" value="sem_annotation"/>
		<constructor-arg name="query">
			<value>
				<![CDATA[
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
				PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
				PREFIX owl: <http://www.w3.org/2002/07/owl#> 
				
				SELECT ?sem_annotation
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation .
				 	} 
				 ]]>
			</value>
		</constructor-arg>
		<!--property name="multivalue" value="false" /-->
	</bean>
	
	



annotation.bioportal.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.bioportal.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">
		<constructor-arg name="name" value="sem_annotation_bioportal_sm"/>
		<constructor-arg name="query">
			<value>
				<![CDATA[
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
				PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
				PREFIX owl: <http://www.w3.org/2002/07/owl#> 
				
				SELECT ?sem_annotation_bioportal_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_bioportal_sm .
				 	} 
				 ]]>
			</value>
		</constructor-arg>
	</bean>
	



annotation.esor.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.esor.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">
		<constructor-arg name="name" value="sem_annotation_esor_sm"/>
		<constructor-arg name="query">
			<value>
				<![CDATA[
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
				PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
				PREFIX owl: <http://www.w3.org/2002/07/owl#> 
				
				SELECT ?sem_annotation_esor_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_esor_sm .
				 	} 
				 ]]>
			</value>
		</constructor-arg>
	</bean>
	



annotation.cosine.expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:p="http://www.springframework.org/schema/p" id="annotation.cosine.expansion" class="org.dataone.cn.indexer.annotation.SparqlField">
		<constructor-arg name="name" value="sem_annotation_cosine_sm"/>
		<constructor-arg name="query">
			<value>
				<![CDATA[
				PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
				PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
				PREFIX owl: <http://www.w3.org/2002/07/owl#> 
				
				SELECT ?sem_annotation_cosine_sm
				WHERE { 
						<$CONCEPT_URI> rdfs:subClassOf+ ?sem_annotation_cosine_sm .
				 	} 
				 ]]>
			</value>
		</constructor-arg>
	</bean>





