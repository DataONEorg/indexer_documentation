Provenance
==========

Describes parser configuration for: prov20150115RdfXmlSubprocessor

Format IDs Processed
--------------------

This parser processes the following DataONE format IDs:


  * | RDF/XML
    | formatId: ``http://www.w3.org/TR/rdf-syntax-grammar``

  * | Object Reuse and Exchange Vocabulary
    | formatId: ``http://www.openarchives.org/ore/terms``


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

  * - :attr:`Index.prov_wasDerivedFrom`
    - False
    - False
    - ::

        

                SELECT (str(?pidValue) as ?pid) (str(?wasDerivedFromValue) as ?prov_wasDerivedFrom)
                FROM <$GRAPH_NAME>
                WHERE { 
                        
                    ?derived_data       prov:wasDerivedFrom ?primary_data .
                    ?derived_data       dcterms:identifier  ?pidValue . 
                    ?primary_data       dcterms:identifier  ?wasDerivedFromValue .
                        
                    } 
                 
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.wasDerivedFrom`_


  * - :attr:`Index.prov_wasInformedBy`
    - False
    - False
    - ::

        

                SELECT (str(?pidValue) as ?pid) (str(?wasInformedByValue) as ?prov_wasInformedBy)
                FROM <$GRAPH_NAME>
                WHERE { 
                        
                    ?activity               prov:wasInformedBy  ?previousActivity .
                    ?activity               dcterms:identifier  ?pidValue . 
                    ?previousActivity       dcterms:identifier  ?wasInformedByValue .
                        
                    } 
                 
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.wasInformedBy`_


  * - :attr:`Index.prov_used`
    - False
    - False
    - ::

        

                SELECT (str(?pidValue) as ?pid) (str(?usedValue) as ?prov_used)
                FROM <$GRAPH_NAME>
                WHERE { 
                        
                    ?activity       prov:used                 ?data .
                    ?activity       prov:qualifiedAssociation ?association .
                    ?association    prov:hadPlan              ?program .
                    ?program        dcterms:identifier        ?pidValue . 
                    ?data           dcterms:identifier        ?usedValue .
                        
                    } 
                 
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.used`_


  * - :attr:`Index.prov_generated`
    - False
    - False
    - ::

        

                SELECT (str(?pidValue) as ?pid) (str(?generatedValue) as ?prov_generated)
                FROM <$GRAPH_NAME>
                WHERE { 
                        
                    ?result         prov:wasGeneratedBy       ?activity .
                    ?activity       prov:qualifiedAssociation ?association .
                    ?association    prov:hadPlan              ?program .
                    ?result         dcterms:identifier        ?generatedValue . 
                    ?program        dcterms:identifier        ?pidValue .
                        
                    } 
                 
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.generated`_


  * - :attr:`Index.prov_generatedByProgram`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?programPidValue) as ?prov_generatedByProgram)
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?derived_data prov:wasGeneratedBy ?execution .
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:hadPlan ?program .
                    ?program dcterms:identifier ?programPidValue .
                    ?derived_data dcterms:identifier ?pidValue .
                }
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.generatedByProgram`_


  * - :attr:`Index.prov_generatedByExecution`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?executionPidValue) as ?prov_generatedByExecution)
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?derived_data prov:wasGeneratedBy ?execution .
                    ?execution dcterms:identifier ?executionPidValue .
                    ?derived_data dcterms:identifier ?pidValue .
                }
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.generatedByExecution`_


  * - :attr:`Index.prov_generatedByUser`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) ?prov_generatedByUser
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?derived_data prov:wasGeneratedBy ?execution .
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:agent ?prov_generatedByUser .
                    ?derived_data dcterms:identifier ?pidValue .
                }
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.generatedByUser`_


  * - :attr:`Index.prov_usedByProgram`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?programPidValue) as ?prov_usedByProgram)
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?execution prov:used ?primary_data .
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:hadPlan ?program .
                    ?program dcterms:identifier ?programPidValue .
                    ?primary_data dcterms:identifier ?pidValue .
                }                
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.usedByProgram`_


  * - :attr:`Index.prov_usedByExecution`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?executionIdValue) as ?prov_usedByExecution)
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?execution prov:used ?primary_data .
                    ?primary_data dcterms:identifier ?pidValue .
                    ?execution dcterms:identifier ?executionIdValue .
                }
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.usedByExecution`_


  * - :attr:`Index.prov_usedByUser`
    - False
    - False
    - ::

        

                SELECT (str(?pidValue) as ?pid) ?prov_usedByUser
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?execution prov:used ?primary_data .
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:agent ?prov_usedByUser .
                    ?primary_data dcterms:identifier ?pidValue .
                }                
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.usedByUser`_


  * - :attr:`Index.prov_wasExecutedByExecution`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?executionIdValue) as ?prov_wasExecutedByExecution)
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:hadPlan ?program .
                    ?execution dcterms:identifier ?executionIdValue .
                    ?program dcterms:identifier ?pidValue .
                }                
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.wasExecutedByExecution`_


  * - :attr:`Index.prov_wasExecutedByUser`
    - False
    - False
    - ::

        
                                
                SELECT (str(?pidValue) as ?pid) ?prov_wasExecutedByUser
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?execution prov:qualifiedAssociation ?association .
                    ?association prov:hadPlan ?program .
                    ?association prov:agent ?prov_wasExecutedByUser .
                    ?program dcterms:identifier ?pidValue .
                }                
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.wasExecutedByUser`_


  * - :attr:`Index.prov_instanceOfClass`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) ?prov_instanceOfClass
                FROM <$GRAPH_NAME>
                WHERE {
                
                    ?subject rdf:type ?prov_instanceOfClass .
                    ?subject dcterms:identifier ?pidValue .
                }                
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.instanceOfClass`_


  * - :attr:`Index.prov_hasDerivations`
    - False
    - False
    - ::

        
                
                SELECT (str(?pidValue) as ?pid) (str(?derivedDataPidValue) as ?prov_hasDerivations)
                FROM <$GRAPH_NAME>
                WHERE {
                    ?derived_data prov:wasDerivedFrom ?source_data .
                    ?source_data dcterms:identifier ?pidValue .
                    ?derived_data dcterms:identifier ?derivedDataPidValue .
                }
                
            

      | Processor: `SparqlField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/annotation/SparqlField.java>`_
      | Configuration: `prov20150115.hasDerivations`_



Bean Configurations
-------------------


prov20150115.wasDerivedFrom
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.wasDerivedFrom" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_wasDerivedFrom"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n\n                SELECT (str(?pidValue) as ?pid) (str(?wasDerivedFromValue) as ?prov_wasDerivedFrom)\n                FROM <$GRAPH_NAME>\n                WHERE { \n                        \n                    ?derived_data       prov:wasDerivedFrom ?primary_data .\n                    ?derived_data       dcterms:identifier  ?pidValue . \n                    ?primary_data       dcterms:identifier  ?wasDerivedFromValue .\n                        \n                    } \n                 ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n    \n    \n'


prov20150115.wasInformedBy
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.wasInformedBy" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_wasInformedBy"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n\n                SELECT (str(?pidValue) as ?pid) (str(?wasInformedByValue) as ?prov_wasInformedBy)\n                FROM <$GRAPH_NAME>\n                WHERE { \n                        \n                    ?activity               prov:wasInformedBy  ?previousActivity .\n                    ?activity               dcterms:identifier  ?pidValue . \n                    ?previousActivity       dcterms:identifier  ?wasInformedByValue .\n                        \n                    } \n                 ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n    \n    \n'


prov20150115.used
~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.used" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_used"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n\n                SELECT (str(?pidValue) as ?pid) (str(?usedValue) as ?prov_used)\n                FROM <$GRAPH_NAME>\n                WHERE { \n                        \n                    ?activity       prov:used                 ?data .\n                    ?activity       prov:qualifiedAssociation ?association .\n                    ?association    prov:hadPlan              ?program .\n                    ?program        dcterms:identifier        ?pidValue . \n                    ?data           dcterms:identifier        ?usedValue .\n                        \n                    } \n                 ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n    \n    \n'


prov20150115.generated
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.generated" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_generated"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n\n                SELECT (str(?pidValue) as ?pid) (str(?generatedValue) as ?prov_generated)\n                FROM <$GRAPH_NAME>\n                WHERE { \n                        \n                    ?result         prov:wasGeneratedBy       ?activity .\n                    ?activity       prov:qualifiedAssociation ?association .\n                    ?association    prov:hadPlan              ?program .\n                    ?result         dcterms:identifier        ?generatedValue . \n                    ?program        dcterms:identifier        ?pidValue .\n                        \n                    } \n                 ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.generatedByProgram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.generatedByProgram" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_generatedByProgram"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?programPidValue) as ?prov_generatedByProgram)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?derived_data prov:wasGeneratedBy ?execution .\n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:hadPlan ?program .\n                    ?program dcterms:identifier ?programPidValue .\n                    ?derived_data dcterms:identifier ?pidValue .\n                }\n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.generatedByExecution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.generatedByExecution" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_generatedByExecution"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?executionPidValue) as ?prov_generatedByExecution)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?derived_data prov:wasGeneratedBy ?execution .\n                    ?execution dcterms:identifier ?executionPidValue .\n                    ?derived_data dcterms:identifier ?pidValue .\n                }\n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.generatedByUser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.generatedByUser" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_generatedByUser"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) ?prov_generatedByUser\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?derived_data prov:wasGeneratedBy ?execution .\n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:agent ?prov_generatedByUser .\n                    ?derived_data dcterms:identifier ?pidValue .\n                }\n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.usedByProgram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.usedByProgram" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_usedByProgram"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?programPidValue) as ?prov_usedByProgram)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?execution prov:used ?primary_data .\n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:hadPlan ?program .\n                    ?program dcterms:identifier ?programPidValue .\n                    ?primary_data dcterms:identifier ?pidValue .\n                }                \n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.usedByExecution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.usedByExecution" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_usedByExecution"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?executionIdValue) as ?prov_usedByExecution)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?execution prov:used ?primary_data .\n                    ?primary_data dcterms:identifier ?pidValue .\n                    ?execution dcterms:identifier ?executionIdValue .\n                }\n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.usedByUser
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.usedByUser" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_usedByUser"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n\n                SELECT (str(?pidValue) as ?pid) ?prov_usedByUser\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?execution prov:used ?primary_data .\n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:agent ?prov_usedByUser .\n                    ?primary_data dcterms:identifier ?pidValue .\n                }                \n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.wasExecutedByExecution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.wasExecutedByExecution" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_wasExecutedByExecution"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?executionIdValue) as ?prov_wasExecutedByExecution)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:hadPlan ?program .\n                    ?execution dcterms:identifier ?executionIdValue .\n                    ?program dcterms:identifier ?pidValue .\n                }                \n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.wasExecutedByUser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.wasExecutedByUser" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_wasExecutedByUser"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                                \n                SELECT (str(?pidValue) as ?pid) ?prov_wasExecutedByUser\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?execution prov:qualifiedAssociation ?association .\n                    ?association prov:hadPlan ?program .\n                    ?association prov:agent ?prov_wasExecutedByUser .\n                    ?program dcterms:identifier ?pidValue .\n                }                \n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


prov20150115.instanceOfClass
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.instanceOfClass" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_instanceOfClass"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                \n                SELECT (str(?pidValue) as ?pid) ?prov_instanceOfClass\n                FROM <$GRAPH_NAME>\n                WHERE {\n                \n                    ?subject rdf:type ?prov_instanceOfClass .\n                    ?subject dcterms:identifier ?pidValue .\n                }                \n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n    \n\n'


prov20150115.hasDerivations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="prov20150115.hasDerivations" class="org.dataone.cn.indexer.annotation.SparqlField">\n        <constructor-arg name="name" value="prov_hasDerivations"/>\n        <constructor-arg name="query">\n            <value>\n                <![CDATA[\n                PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n                PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#> \n                PREFIX owl:     <http://www.w3.org/2002/07/owl#> \n                PREFIX prov:    <http://www.w3.org/ns/prov#> \n                PREFIX provone: <http://purl.dataone.org/provone/2015/01/15/ontology#>\n                PREFIX ore:     <http://www.openarchives.org/ore/terms/> \n                PREFIX dcterms: <http://purl.org/dc/terms/>\n                PREFIX cito:    <http://purl.org/spar/cito/>\n                \n                SELECT (str(?pidValue) as ?pid) (str(?derivedDataPidValue) as ?prov_hasDerivations)\n                FROM <$GRAPH_NAME>\n                WHERE {\n                    ?derived_data prov:wasDerivedFrom ?source_data .\n                    ?source_data dcterms:identifier ?pidValue .\n                    ?derived_data dcterms:identifier ?derivedDataPidValue .\n                }\n                ]]>\n            </value>\n        </constructor-arg>\n    </bean>\n\n    \n'


