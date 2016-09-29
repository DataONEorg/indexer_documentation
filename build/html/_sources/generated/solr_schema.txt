Solr Fields Defined
===================

A list of the fields defined in the solr search index used by the Coordinating Nodes.

.. list-table::
   :header-rows: 1

   * - Field
     - Type
     - MV
     - Store
     - Index
   * - _version_
     - long
     - False
     - True
     - True
   * - _root_
     - string
     - False
     - False
     - True
   * - id
     - string
     - False
     - True
     - True
   * - seriesId
     - string
     - False
     - True
     - True
   * - fileName
     - string
     - False
     - True
     - True
   * - mediaType
     - string
     - False
     - True
     - True
   * - mediaTypeProperty
     - string
     - True
     - True
     - True
   * - formatId
     - string
     - False
     - True
     - True
   * - formatType
     - string
     - False
     - True
     - True
   * - size
     - tlong
     - False
     - True
     - True
   * - checksum
     - string
     - False
     - True
     - False
   * - checksumAlgorithm
     - string
     - False
     - True
     - False
   * - dateUploaded
     - tdate
     - False
     - True
     - True
   * - dateModified
     - tdate
     - False
     - True
     - True
   * - submitter
     - string
     - False
     - True
     - True
   * - rightsHolder
     - string
     - False
     - True
     - True
   * - authoritativeMN
     - string
     - False
     - True
     - True
   * - replicationAllowed
     - boolean
     - False
     - True
     - False
   * - numberReplicas
     - int
     - False
     - True
     - False
   * - preferredReplicationMN
     - string
     - True
     - True
     - False
   * - blockedReplicationMN
     - string
     - True
     - True
     - False
   * - replicaMN
     - string
     - True
     - True
     - True
   * - replicaVerifiedDate
     - tdate
     - True
     - True
     - False
   * - datasource
     - string
     - False
     - True
     - True
   * - obsoletes
     - string
     - False
     - True
     - True
   * - obsoletedBy
     - string
     - False
     - True
     - True
   * - resourceMap
     - string
     - True
     - True
     - True
   * - documents
     - string
     - True
     - True
     - True
   * - isDocumentedBy
     - string
     - True
     - True
     - True
   * - readPermission
     - string
     - True
     - True
     - True
   * - writePermission
     - string
     - True
     - True
     - True
   * - changePermission
     - string
     - True
     - True
     - True
   * - isPublic
     - boolean
     - False
     - True
     - True
   * - author
     - string
     - False
     - True
     - True
   * - authorSurName
     - string
     - False
     - True
     - True
   * - authorGivenName
     - string
     - False
     - True
     - True
   * - authorSurNameSort
     - alphaOnlySort
     - False
     - True
     - True
   * - authorGivenNameSort
     - alphaOnlySort
     - False
     - True
     - True
   * - authorLastName
     - string
     - True
     - True
     - True
   * - abstract
     - text_general
     - False
     - True
     - True
   * - keywords
     - string
     - True
     - True
     - True
   * - keyConcept
     - string
     - True
     - True
     - True
   * - southBoundCoord
     - tfloat
     - False
     - True
     - True
   * - northBoundCoord
     - tfloat
     - False
     - True
     - True
   * - westBoundCoord
     - tfloat
     - False
     - True
     - True
   * - eastBoundCoord
     - tfloat
     - False
     - True
     - True
   * - namedLocation
     - string
     - True
     - True
     - True
   * - beginDate
     - tdate
     - False
     - True
     - True
   * - endDate
     - tdate
     - False
     - True
     - True
   * - title
     - text_general
     - False
     - True
     - True
   * - scientificName
     - string
     - True
     - True
     - True
   * - relatedOrganizations
     - string
     - True
     - True
     - True
   * - datePublished
     - tdate
     - False
     - True
     - True
   * - pubDate
     - tdate
     - False
     - True
     - True
   * - investigator
     - string
     - True
     - True
     - True
   * - investigatorText
     - text_general
     - True
     - False
     - True
   * - ogcUrl
     - text_general
     - False
     - True
     - False
   * - identifier
     - text_general
     - False
     - True
     - True
   * - LTERSite
     - string
     - False
     - True
     - True
   * - origin
     - string
     - True
     - True
     - True
   * - originText
     - text_general
     - True
     - False
     - True
   * - titlestr
     - string
     - False
     - False
     - True
   * - geoform
     - string
     - False
     - True
     - True
   * - presentationCat
     - string
     - False
     - True
     - True
   * - purpose
     - text_general
     - False
     - True
     - True
   * - updateDate
     - tdate
     - False
     - True
     - True
   * - edition
     - text_general
     - False
     - True
     - True
   * - dataUrl
     - string
     - False
     - True
     - False
   * - originator
     - string
     - True
     - True
     - True
   * - originatorText
     - text_general
     - True
     - False
     - True
   * - family
     - string
     - True
     - True
     - True
   * - species
     - string
     - True
     - True
     - True
   * - genus
     - string
     - True
     - True
     - True
   * - kingdom
     - string
     - True
     - True
     - True
   * - phylum
     - string
     - True
     - True
     - True
   * - order
     - string
     - True
     - True
     - True
   * - class
     - string
     - True
     - True
     - True
   * - attributeName
     - string
     - True
     - True
     - True
   * - attributeLabel
     - string
     - True
     - True
     - True
   * - attributeDescription
     - text_general
     - True
     - True
     - True
   * - attributeUnit
     - string
     - True
     - True
     - True
   * - attribute
     - text_general
     - True
     - True
     - True
   * - webUrl
     - string
     - True
     - True
     - False
   * - contactOrganization
     - string
     - True
     - True
     - True
   * - contactOrganizationText
     - text_general
     - True
     - False
     - True
   * - keywordsText
     - text_general
     - True
     - False
     - True
   * - placeKey
     - text_general
     - True
     - True
     - True
   * - noBoundingBox
     - string
     - False
     - True
     - True
   * - isSpatial
     - string
     - False
     - True
     - True
   * - decade
     - string
     - False
     - True
     - True
   * - gcmdKeyword
     - text_general
     - True
     - True
     - True
   * - project
     - string
     - False
     - True
     - True
   * - projectText
     - text_general
     - False
     - False
     - True
   * - site
     - string
     - True
     - True
     - True
   * - siteText
     - text_general
     - True
     - False
     - True
   * - parameter
     - string
     - True
     - True
     - True
   * - parameterText
     - text_general
     - True
     - False
     - True
   * - sensor
     - string
     - True
     - True
     - True
   * - sensorText
     - text_general
     - True
     - False
     - True
   * - source
     - string
     - True
     - True
     - True
   * - sourceText
     - text_general
     - True
     - False
     - True
   * - term
     - string
     - True
     - True
     - True
   * - termText
     - text_general
     - True
     - False
     - True
   * - topic
     - string
     - True
     - True
     - True
   * - topicText
     - text_general
     - True
     - False
     - True
   * - fileID
     - string
     - False
     - True
     - True
   * - text
     - text_en_splitting
     - False
     - True
     - True
   * - geohash_1
     - text_general
     - True
     - True
     - True
   * - geohash_2
     - text_general
     - True
     - True
     - True
   * - geohash_3
     - text_general
     - True
     - True
     - True
   * - geohash_4
     - text_general
     - True
     - True
     - True
   * - geohash_5
     - text_general
     - True
     - True
     - True
   * - geohash_6
     - text_general
     - True
     - True
     - True
   * - geohash_7
     - text_general
     - True
     - True
     - True
   * - geohash_8
     - text_general
     - True
     - True
     - True
   * - geohash_9
     - text_general
     - True
     - True
     - True
   * - prov_wasDerivedFrom
     - string
     - True
     - True
     - True
   * - prov_wasInformedBy
     - string
     - True
     - True
     - True
   * - prov_used
     - string
     - True
     - True
     - True
   * - prov_generated
     - string
     - True
     - True
     - True
   * - prov_generatedByProgram
     - string
     - True
     - True
     - True
   * - prov_generatedByExecution
     - string
     - True
     - True
     - True
   * - prov_generatedByUser
     - string
     - True
     - True
     - True
   * - prov_usedByProgram
     - string
     - True
     - True
     - True
   * - prov_usedByExecution
     - string
     - True
     - True
     - True
   * - prov_usedByUser
     - string
     - True
     - True
     - True
   * - prov_wasExecutedByExecution
     - string
     - True
     - True
     - True
   * - prov_wasExecutedByUser
     - string
     - True
     - True
     - True
   * - prov_hasSources
     - string
     - True
     - True
     - True
   * - prov_hasDerivations
     - string
     - True
     - True
     - True
   * - prov_instanceOfClass
     - string
     - True
     - True
     - True
   * - sem_annotation
     - string
     - True
     - True
     - True
   * - sem_annotated_by
     - string
     - True
     - True
     - True
   * - sem_annotates
     - string
     - True
     - True
     - True
   * - sem_comment
     - string
     - True
     - True
     - True
   * - isService
     - boolean
     - False
     - True
     - True
   * - serviceCoupling
     - string
     - False
     - True
     - True
   * - serviceTitle
     - text_general
     - False
     - True
     - True
   * - serviceDescription
     - text_general
     - False
     - True
     - True
   * - serviceType
     - string
     - True
     - True
     - True
   * - serviceEndpoint
     - string
     - True
     - True
     - True
   * - serviceInput
     - string
     - True
     - True
     - True
   * - serviceOutput
     - string
     - True
     - True
     - True

