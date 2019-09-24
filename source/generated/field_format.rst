

Field x FormatId Cross Reference
================================

.. list-table::
   :header-rows: 1
   :widths: 1 5

   * - Index
     - FormatId
   * - 1
     - eml://ecoinformatics.org/eml-2.0.0
   * - 2
     - eml://ecoinformatics.org/eml-2.0.1
   * - 3
     - eml://ecoinformatics.org/eml-2.1.0
   * - 4
     - eml://ecoinformatics.org/eml-2.1.1
   * - 5
     - https://eml.ecoinformatics.org/eml-2.2.0
   * - 6
     - http://www.openarchives.org/ore/terms
   * - 7
     - FGDC-STD-001-1998
   * - 8
     - FGDC-STD-001.1-1999
   * - 9
     - FGDC-STD-001.2-1999
   * - 10
     - http://www.esri.com/metadata/esriprof80.dtd
   * - 11
     - http://purl.org/ornl/schema/mercury/terms/v1.0
   * - 12
     - http://purl.org/dryad/terms/
   * - 13
     - http://datadryad.org/profile/v3.1
   * - 14
     - http://dublincore.org/schemas/xmls/qdc/2008/02/11/qualifieddc.xsd
   * - 15
     - http://ns.dataone.org/metadata/schema/onedcx/v1.0
   * - 16
     - http://datacite.org/schema/kernel-3.1
   * - 17
     - http://datacite.org/schema/kernel-3.0
   * - 18
     - http://www.w3.org/TR/rdf-syntax-grammar
   * - 19
     - http://docs.annotatorjs.org/en/v1.2.x/annotation-format.html
   * - 20
     - http://www.isotc211.org/2005/gmd
   * - 21
     - http://www.isotc211.org/2005/gmd-noaa
   * - 22
     - http://www.isotc211.org/2005/gmd-pangaea
   * - 23
     - http://www.openarchives.org/OAI/2.0/oai_dc/
   


The following table indicates which formatIds have processing rules defined to set index field values when processing
metadata. In the table, an "S" means the property is set from system metadata, an "X" means there is a rule defined
to set the value, and blank indicates no rules are setting the field value (though Solr copy fields are not considered
here).

.. csv-table:: FormatId x Solr Field
   :header: Field \ FormatId,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"

   LTERSite, , , , , , , , , , , , , , , , , , , , , , , 
   abstract,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   attribute,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   attributeDescription,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   attributeLabel,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   attributeName,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   attributeUnit,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   author,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   authorGivenName,X,X,X,X,X, , , , , , ,X,X, , ,X,X, , , , , , 
   authorGivenNameSort,X,X,X,X,X, , , , , , ,X,X, , ,X,X, , , , , , 
   authorLastName,X,X,X,X,X, , , , , , , , , , ,X,X, , , , , , 
   authorSurName,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   authorSurNameSort,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   authoritativeMN,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   awardNumber, , , , ,X, , , , , , , , , , , , , , , , , , 
   awardTitle, , , , ,X, , , , , , , , , , , , , , , , , , 
   beginDate,X,X,X,X,X, ,X,X,X,X,X, , ,X,X,X,X, , ,X,X,X, 
   blockedReplicationMN,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   changePermission,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   checksum,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   checksumAlgorithm,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   class,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   contactOrganization,X,X,X,X,X, ,X,X,X,X,X, , ,X,X,X,X, , ,X,X,X,X
   contactOrganizationText, , , , , , , , , , , , , , , , , , , , , , , 
   dataUrl, , , , , , , , , , , , , , , , , , , , , , , 
   datasource,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   dateModified,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   datePublished, , , , , , , , , , , , , , , , , , , , , , , 
   dateUploaded,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   decade, , , , , , , , , , , , , , , , , , , , , , , 
   documents, , , , , , , , , , , , , , , , , , , , , , , 
   eastBoundCoord,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   edition, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   endDate,X,X,X,X,X, ,X,X,X,X,X, , ,X,X,X,X, , ,X,X,X, 
   family,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   fileID,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   fileName,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   formatId,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   formatType,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   funderIdentifier, , , , ,X, , , , , , , , , , , , , , , , , , 
   funderName, , , , ,X, , , , , , , , , , , , , , , , , , 
   funding, , , , ,X, , , , , , , , , , , , , , , , , , 
   fundingText, , , , , , , , , , , , , , , , , , , , , , , 
   gcmdKeyword, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   genus,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   geoform, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   geohash_1,X,X,X,X,X, ,X,X,X,X,X, , ,X,X, , , , ,X,X,X, 
   geohash_2,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_3,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_4,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_5,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_6,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_7,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_8,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   geohash_9,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   id,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   identifier, , , , , , , , , , , , , , , , , , , , , , , 
   investigator,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   investigatorText, , , , , , , , , , , , , , , , , , , , , , , 
   isDocumentedBy, , , , , , , , , , , , , , , , , , , , , , , 
   isPublic,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   isService,X,X,X,X,X, , , , , , , , , , , , , , ,X,X,X, 
   isSpatial, , , , , , , , , , , , , , , , , , , , , , , 
   keyConcept, , , , , , , , , , , , , , , , , , , , , , , 
   keywords,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   keywordsText, , , , , , , , , , , , , , , , , , , , , , , 
   kingdom,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   mediaType,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   mediaTypeProperty,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   namedLocation, , , , , , , , , , , , , , , , , , , , , , , 
   noBoundingBox, , , , , , , , , , , , , , , , , , , , , , , 
   northBoundCoord,X,X,X,X,X, ,X,X,X,X,X, , ,X,X, , , , ,X,X,X, 
   numberReplicas,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   obsoletedBy,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   obsoletes,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   ogcUrl, , , , , , , , , , , , , , , , , , , , , , , 
   order,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   origin,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   originText, , , , , , , , , , , , , , , , , , , , , , , 
   originator, , , , , , , , , , , , , , , , , , , , , , ,X
   originatorText, , , , , , , , , , , , , , , , , , , , , , , 
   parameter, , , , , , , , , , , , , , , , , , , , , , , 
   parameterText, , , , , , , , , , , , , , , , , , , , , , , 
   phylum,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   placeKey, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   preferredReplicationMN,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   presentationCat, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   project,X,X,X,X,X, , , , , , , , , , , , , , , , , , 
   projectText, , , , , , , , , , , , , , , , , , , , , , , 
   prov_generated, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_generatedByExecution, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_generatedByProgram, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_generatedByUser, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_hasDerivations, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_hasSources, , , , , , , , , , , , , , , , , , , , , , , 
   prov_instanceOfClass, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_used, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_usedByExecution, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_usedByProgram, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_usedByUser, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_wasDerivedFrom, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_wasExecutedByExecution, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_wasExecutedByUser, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   prov_wasInformedBy, , , , , ,X, , , , , , , , , , , ,X, , , , , 
   pubDate,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   purpose, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   readPermission,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   relatedOrganizations, , , , , , , , , , , , , , , , , , , , , , , 
   replicaMN,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   replicaVerifiedDate,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   replicationAllowed,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   resourceMap, , , , , , , , , , , , , , , , , , , , , , , 
   rightsHolder,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   scientificName,X,X,X,X,X, ,X,X,X,X,X,X,X, , , , , , , , , , 
   sem_annotated_by, , , , , , , , , , , , , , , , , , , , , , , 
   sem_annotates, , , , , , , , , , , , , , , , , , , , , , , 
   sem_annotation, , , , ,X, , , , , , , , , , , , , ,X, , , , 
   sem_comment, , , , , , , , , , , , , , , , , , , , , , , 
   sensor, , , , , , , , , , , , , , , , , , , , , , , 
   sensorText, , , , , , , , , , , , , , , , , , , , , , , 
   seriesId,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   serviceCoupling, , , , , , , , , , , , , , , , , , , ,X,X,X, 
   serviceDescription,X,X,X,X,X, , , , , , , , , , , , , , ,X,X,X, 
   serviceEndpoint,X,X,X,X,X, , , , , , , , , , , , , , ,X,X,X,X
   serviceInput, , , , , , , , , , , , , , , , , , , ,X,X,X, 
   serviceOutput, , , , , , , , , , , , , , , , , , , ,X,X,X, 
   serviceTitle,X,X,X,X,X, , , , , , , , , , , , , , ,X,X,X, 
   serviceType, , , , , , , , , , , , , , , , , , , ,X,X,X, 
   site,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , , , , , 
   siteText, , , , , , , , , , , , , , , , , , , , , , , 
   size,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   source, , , , , , , , , , , , , , , , , , , , , , , 
   sourceText, , , , , , , , , , , , , , , , , , , , , , , 
   southBoundCoord,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   species,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , , , , , 
   submitter,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   term, , , , , , , , , , , , , , , , , , , , , , , 
   termText, , , , , , , , , , , , , , , , , , , , , , , 
   text,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   title,X,X,X,X,X, ,X,X,X,X,X,X,X,X,X,X,X, , ,X,X,X,X
   titlestr, , , , , , , , , , , , , , , , , , , , , , , 
   topic, , , , , , , , , , , , , , , , , , , , , , , 
   topicText, , , , , , , , , , , , , , , , , , , , , , , 
   updateDate, , , , , , , , , , , , , , , , , , , , , , , 
   webUrl, , , , , , ,X,X,X,X,X, , , , , , , , , , , , 
   westBoundCoord,X,X,X,X,X, ,X,X,X,X,X, , , , , , , , ,X,X,X, 
   writePermission,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S
   

