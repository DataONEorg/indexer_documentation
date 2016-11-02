
.. module:: Index

.. currentmodule:: Index

Solr Index Fields
=================

A list of the fields defined in the solr search index used by the Coordinating Nodes.

These fields are populated by the index processor using values drawn from
:class:`API:Types.SystemMetadata`, :term:`Science Metadata`, and :term:`Resource Map`
documents.

.. note:: For Editors

   Definitions are drawn from the `solr configuration file`_ and descriptions for each
   field are contained in a separate `YAML formatted text file`_. After editing
   descriptions, the document source must be regenerated and committed to GitHub for
   the public facing documentation to be updated.

Static Fields
-------------

.. list-table::
   :header-rows: 1
   :widths: 3, 2, 1, 1, 1, 10

   * - Field
     - Type
     - MV
     - Store
     - Index
     - Description
   * - .. attribute:: _root_
     - string
     - False
     - False
     - True
     - 
   * - .. attribute:: _version_
     - long
     - False
     - True
     - True
     - 
   * - .. attribute:: abstract
     - text_general
     - False
     - True
     - True
     - The full text of the abstract as provided in the science metadata document.

   * - .. attribute:: attribute
     - text_general
     - True
     - True
     - True
     - Multi-valued field containing the text from attributeName, attributeLabel, attributeDescription, attributeUnit fields into a single searchable text field.

   * - .. attribute:: attributeDescription
     - text_general
     - True
     - True
     - True
     - Multi-valued field containing the attribute descriptive text.

   * - .. attribute:: attributeLabel
     - string
     - True
     - True
     - True
     - Multi-valued field containing secondary attribute name information.

   * - .. attribute:: attributeName
     - string
     - True
     - True
     - True
     - Multi-valued field containing the main attribute name information.

   * - .. attribute:: attributeUnit
     - string
     - True
     - True
     - True
     - Multi-valued field containing the attribute unit information.

   * - .. attribute:: author
     - string
     - False
     - True
     - True
     - Principle Investigator (PI) / Author as listed in the metadata document. 

   * - .. attribute:: authorGivenName
     - string
     - False
     - True
     - True
     - The given name of the primary author/PI.

   * - .. attribute:: authorGivenNameSort
     - alphaOnlySort
     - False
     - True
     - True
     - The given name of the primary author/PI case normalized for sorting. 

   * - .. attribute:: authoritativeMN
     - string
     - False
     - True
     - True
     - The node Id of the authoritative Member Node for the object.

   * - .. attribute:: authorLastName
     - string
     - True
     - True
     - True
     - The LAST name(s) of the author(s)

   * - .. attribute:: authorSurName
     - string
     - False
     - True
     - True
     - The sur name of the primary author/PI.

   * - .. attribute:: authorSurNameSort
     - alphaOnlySort
     - False
     - True
     - True
     - The sur name of the primary author/PI case normalized for sorting. 

   * - .. attribute:: beginDate
     - tdate
     - False
     - True
     - True
     - The starting date of the temporal range of the content described by the metadata document.

   * - .. attribute:: blockedReplicationMN
     - string
     - True
     - True
     - False
     - A multi-valued field that contains the node Ids of member nodes that are blocked from holding replicas of this object.

   * - .. attribute:: changePermission
     - string
     - True
     - True
     - True
     - List of subjects (groups and individuals) that have change permission on PID.

   * - .. attribute:: checksum
     - string
     - False
     - True
     - False
     - The checksum for the object

   * - .. attribute:: checksumAlgorithm
     - string
     - False
     - True
     - False
     - Algorithm used for generating the object checksum

   * - .. attribute:: class
     - string
     - True
     - True
     - True
     - Taxonomic class name(s)

   * - .. attribute:: contactOrganization
     - string
     - True
     - True
     - True
     - Name of the organization to contact for more information about the dataset

   * - .. attribute:: contactOrganizationText
     - text_general
     - True
     - False
     - True
     - Copy from contactOrganization

   * - .. attribute:: datasource
     - string
     - False
     - True
     - True
     - The node Id of the member node that originally contributed the content.

   * - .. attribute:: dataUrl
     - string
     - False
     - True
     - False
     - The URL that can be used to resolve the location of the object given its PID.

   * - .. attribute:: dateModified
     - tdate
     - False
     - True
     - True
     - The date and time when the object system metadata was last updated.

   * - .. attribute:: datePublished
     - tdate
     - False
     - True
     - True
     - Publication date for the dataset (this may or may not be coincident with when the content is added to DataONE).

   * - .. attribute:: dateUploaded
     - tdate
     - False
     - True
     - True
     - The date and time when the object was uploaded to the Member Node.

   * - .. attribute:: decade
     - string
     - False
     - True
     - True
     - The latest decade that is covered by the dataset, expressed in the form "1999-2009"

   * - .. attribute:: documents
     - string
     - True
     - True
     - True
     - Lists all PIDs that this object describes. Obtained by parsing all resource maps in which this object is referenced. Not set for data or resource map objects.

   * - .. attribute:: eastBoundCoord
     - tfloat
     - False
     - True
     - True
     - Eastern most longitude of the spatial extent, in decimal degrees, WGS84

   * - .. attribute:: edition
     - text_general
     - False
     - True
     - True
     - The version or edition number of the item described.

   * - .. attribute:: endDate
     - tdate
     - False
     - True
     - True
     - The ending date of the temporal range of the content described by the metadata document.

   * - .. attribute:: family
     - string
     - True
     - True
     - True
     - Taxonomic family name(s)

   * - .. attribute:: fileID
     - string
     - False
     - True
     - True
     - Contains the `CNRead.resolve` URL for the object ONLY if the object is a science metadata object.

   * - .. attribute:: fileName
     - string
     - False
     - True
     - True
     - The file name for the object, specified in system metadata field with the same name.

   * - .. attribute:: formatId
     - string
     - False
     - True
     - True
     - The format identifier indicating the type of content this record refers to.

   * - .. attribute:: formatType
     - string
     - False
     - True
     - True
     - The format type of the record - DATA, METADATA, RESOURCE.

   * - .. attribute:: gcmdKeyword
     - text_general
     - True
     - True
     - True
     - Keywords drawn from the GCMD controlled vocabulary

   * - .. attribute:: genus
     - string
     - True
     - True
     - True
     - Taxonomic genus name(s)

   * - .. attribute:: geoform
     - string
     - False
     - True
     - True
     - The name of the general form in which the item's geospatial data is presented

   * - .. attribute:: geohash_1
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_2
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_3
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_4
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_5
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_6
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_7
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_8
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: geohash_9
     - text_general
     - True
     - True
     - True
     - An encoded string that represents the geographic coordinates of the centroid of a spatial extent. This can be used for searching and plotting.

   * - .. attribute:: id
     - string
     - False
     - True
     - True
     - The identifier of the object being indexed.

   * - .. attribute:: identifier
     - text_general
     - False
     - True
     - True
     - Copy id

   * - .. attribute:: investigator
     - string
     - True
     - True
     - True
     - Name of the investigator(s) responsible for developing the dataset and associated content.

   * - .. attribute:: investigatorText
     - text_general
     - True
     - False
     - True
     - Copy from investigator.

   * - .. attribute:: isDocumentedBy
     - string
     - True
     - True
     - True
     - Lists all PIDs that describe this object. Obtained by parsing all resource maps in which this object is referenced.

   * - .. attribute:: isPublic
     - boolean
     - False
     - True
     - True
     - Set to True if the DataONE `public user` is present in the list of subjects with readPermission on PID.

   * - .. attribute:: isService
     - boolean
     - False
     - True
     - True
     - Set to true if document is a member node service description document.  Use to filter search results for to exclude or include member node services.

   * - .. attribute:: isSpatial
     - string
     - False
     - True
     - True
     - Set to "Y" for records that contain spatial information

   * - .. attribute:: keyConcept
     - string
     - True
     - True
     - True
     - Terms drawn from a controlled vocabulary of concepts that are applicable to the content described by the metadata document.

   * - .. attribute:: keywords
     - string
     - True
     - True
     - True
     - Keywords recorded in the science metadata document. These may be controlled by the generator of the metadata or by the metadata standard of the document, but are effectively uncontrolled within the  DataONE context.

   * - .. attribute:: keywordsText
     - text_general
     - True
     - False
     - True
     - Copy from keywords

   * - .. attribute:: kingdom
     - string
     - True
     - True
     - True
     - Taxonomic kingdom(s)

   * - .. attribute:: LTERSite
     - string
     - False
     - True
     - True
     - Data provider organization  identifier, for sources within the LTER network.

   * - .. attribute:: mediaType
     - string
     - False
     - True
     - True
     - The name attribute of the media type element in system metadata.  Indicates media type of the object.

   * - .. attribute:: mediaTypeProperty
     - string
     - True
     - True
     - True
     - A list of properties describing the media type in system metadata.  The value is a concatenation of the property elements name attribute and the value of the property element.

   * - .. attribute:: namedLocation
     - string
     - True
     - True
     - True
     - The name of the location(s) relevant to the content described by the metadata document.

   * - .. attribute:: noBoundingBox
     - string
     - False
     - True
     - True
     - Set to "Y" if there is no bounding box information available (i.e., the east, west, north, south most coordinates)

   * - .. attribute:: northBoundCoord
     - tfloat
     - False
     - True
     - True
     - Northern most latitude of the spatial extent, in decimal degrees, WGS84

   * - .. attribute:: numberReplicas
     - int
     - False
     - True
     - False
     - Requested number of replicas for the object

   * - .. attribute:: obsoletedBy
     - string
     - False
     - True
     - True
     - If set, indicates the object that replaces this record.

   * - .. attribute:: obsoletes
     - string
     - False
     - True
     - True
     - If set, indicates the object that this record obsoletes.

   * - .. attribute:: ogcUrl
     - text_general
     - False
     - True
     - False
     - URL for Open Geospatial Web service if available.

   * - .. attribute:: order
     - string
     - True
     - True
     - True
     - Taxonomic order name(s)

   * - .. attribute:: origin
     - string
     - True
     - True
     - True
     - Investigator or Investigator organization name.

   * - .. attribute:: originator
     - string
     - True
     - True
     - True
     - Investigator or Investigator organization name. Derived by normalizing origin.

   * - .. attribute:: originatorText
     - text_general
     - True
     - False
     - True
     - 
   * - .. attribute:: originText
     - text_general
     - True
     - False
     - True
     - Copy from origin

   * - .. attribute:: parameter
     - string
     - True
     - True
     - True
     - A characteristic, or variable, that is measured or derived as part of data-collection activities.

   * - .. attribute:: parameterText
     - text_general
     - True
     - False
     - True
     - Copy from parameter

   * - .. attribute:: phylum
     - string
     - True
     - True
     - True
     - Taxonomic phylum (or division) name(s)

   * - .. attribute:: placeKey
     - text_general
     - True
     - True
     - True
     - A place name keyword, assigned by the metadata creator. It is one keyword from the thesaurus named in <placekt>

   * - .. attribute:: preferredReplicationMN
     - string
     - True
     - True
     - False
     - A list of member node identifiers that are preferred replication targets for this object.

   * - .. attribute:: presentationCat
     - string
     - False
     - True
     - True
     - Type of data being preserved (maps, text, etc.)

   * - .. attribute:: project
     - string
     - False
     - True
     - True
     - The authorized name of a research effort for which data is collected. This name is often reduced to a convenient abbreviation or acronym. All investigators involved in a project should use a common, agreed-upon name.

   * - .. attribute:: projectText
     - text_general
     - False
     - False
     - True
     - Copy from project

   * - .. attribute:: prov_generated
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of data objects that this program  generated based on the PROV wasGeneratedBy, qualifiedAssociation, and hadPlan properties.

   * - .. attribute:: prov_generatedByExecution
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the executions that this data object was generated by based on the PROV wasGeneratedBy property.

   * - .. attribute:: prov_generatedByProgram
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the programs that this data object was generated by based on the PROV wasGeneratedBy, qualifiedAssociation, and hadPlan properties.

   * - .. attribute:: prov_generatedByUser
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the users that this data object was generated by based on the PROV wasGeneratedBy, qualifiedAssociation, and agent properties.

   * - .. attribute:: prov_hasDerivations
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the data objects that were derivations of the source data object described by this metadata object, based on the PROV wasDerivedBy property.

   * - .. attribute:: prov_hasSources
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the data objects that were sources to the derived data object described by this metadata object, based on the PROV wasDerivedBy property.

   * - .. attribute:: prov_instanceOfClass
     - string
     - True
     - True
     - True
     -  A multi-valued field containing the identifiers of the semantic classes that this object is an instance of, based on the PROV, ProvONE, and other ontologies.

   * - .. attribute:: prov_used
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of data objects that this program used based on the PROV used, qualifiedAssociation, and hadPlan properties.

   * - .. attribute:: prov_usedByExecution
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the executions that used this data object based on the PROV used property.

   * - .. attribute:: prov_usedByProgram
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the programs that used this data object based on the PROV used, qualifiedAssociation, and hadPlan properties.

   * - .. attribute:: prov_usedByUser
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the users that used this data object based on the PROV used, qualifiedAssociation, and agent properties.

   * - .. attribute:: prov_wasDerivedFrom
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of data objects that this data object was derived from based on the PROV wasDerivedBy property.

   * - .. attribute:: prov_wasExecutedByExecution
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the executions that used this program based on the PROV qualifiedAssociation, and hadPlan properties.

   * - .. attribute:: prov_wasExecutedByUser
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of the users that executed this program based on the PROV qualifiedAssociation, hadPlan, and agent properties.

   * - .. attribute:: prov_wasInformedBy
     - string
     - True
     - True
     - True
     - A multi-valued field containing the identifiers of executions that this execution was informed by based on the PROV wasInformedBy property.

   * - .. attribute:: pubDate
     - tdate
     - False
     - True
     - True
     - Publication date for the dataset (this may or may not be coincident with when the content is added to DataONE).

   * - .. attribute:: purpose
     - text_general
     - False
     - True
     - True
     - The "Purpose" describes the "why" aspects of the data set (For example, why was the data set created?).

   * - .. attribute:: readPermission
     - string
     - True
     - True
     - True
     - List of subjects (groups and individuals) that have read permission on PID.

   * - .. attribute:: relatedOrganizations
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: replicaMN
     - string
     - True
     - True
     - True
     - One or more node Ids holding copies of the object.

   * - .. attribute:: replicationAllowed
     - boolean
     - False
     - True
     - False
     - True if this object can be replicated.

   * - .. attribute:: replicaVerifiedDate
     - tdate
     - True
     - True
     - False
     - 
   * - .. attribute:: resourceMap
     - string
     - True
     - True
     - True
     - List of resource map PIDs that reference this PID.

   * - .. attribute:: rightsHolder
     - string
     - False
     - True
     - True
     - The `Subject` that acts as the rights holder for the object. 

   * - .. attribute:: scientificName
     - string
     - True
     - True
     - True
     - Taxonomic scientific name(s) at the most precise level available for the organisms of relevance to the dataset

   * - .. attribute:: sem_annotated_by
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: sem_annotates
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: sem_annotation
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: sem_comment
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: sensor
     - string
     - True
     - True
     - True
     - Also called "instrument." A device that is used for collecting data for a data set. 

   * - .. attribute:: sensorText
     - text_general
     - True
     - False
     - True
     - Copy from sensor.

   * - .. attribute:: seriesId
     - string
     - False
     - True
     - True
     - The seriesId is an optional, unique Unicode string that identifies an object revision chain.

   * - .. attribute:: serviceCoupling
     - string
     - False
     - True
     - True
     - Either 'tight', 'mixed', or 'loose'.  Tight coupled service work only on the data described by this metadata document.  Loose coupling means service works on any data.  Mixed coupling means service works on data described by this metadata document but may work on other data.

   * - .. attribute:: serviceDescription
     - text_general
     - False
     - True
     - True
     - A human readable description of the member node service to assist discovery and to evaluate applicability.

   * - .. attribute:: serviceEndpoint
     - string
     - True
     - True
     - True
     - A URL that indicates how to access the member node service.

   * - .. attribute:: serviceInput
     - string
     - True
     - True
     - True
     - Aspect of the service that accepts a digital entity.  Either a list of DataONE formatIds Urls or pid RESOLVE Urls that the member node service operates on.  A pid RESOLVE url indicates a 'tight' coupled service - while a list of formatIds indicates a loose coupled service.

   * - .. attribute:: serviceOutput
     - string
     - True
     - True
     - True
     - Aspect of the service that provides a digital entity resulting from operation of the service.  A listing of DataONE formatId which this member node service produces.

   * - .. attribute:: serviceTitle
     - text_general
     - False
     - True
     - True
     - A brief, human readable descriptive title for the member node service.

   * - .. attribute:: serviceType
     - string
     - True
     - True
     - True
     - The type of service being provided by the member node.

   * - .. attribute:: site
     - string
     - True
     - True
     - True
     - The name or description of the physical location where the data were collected

   * - .. attribute:: siteText
     - text_general
     - True
     - False
     - True
     - Copy from site.

   * - .. attribute:: size
     - tlong
     - False
     - True
     - True
     - The size of the object, in bytes.

   * - .. attribute:: source
     - string
     - True
     - True
     - True
     - Also called "platform." The mechanism used to support the sensor or instrument that gathers data

   * - .. attribute:: sourceText
     - text_general
     - True
     - False
     - True
     - Copy from source.

   * - .. attribute:: southBoundCoord
     - tfloat
     - False
     - True
     - True
     - Southern most latitude of the spatial extent, in decimal degrees, WGS84

   * - .. attribute:: species
     - string
     - True
     - True
     - True
     - Taxonomic species name(s)

   * - .. attribute:: submitter
     - string
     - False
     - True
     - True
     - The `Subject` name of the original submitter of the content to DataONE.

   * - .. attribute:: term
     - string
     - True
     - True
     - True
     - A secondary subject area within which parameters can be categorized. Approved terms include "agricultural chemicals" and "atmospheric chemistry," among many others. When entering a term in the LandVal Metadata Editor, users should select a standard expression from the pick list for terms if at all possible. 

   * - .. attribute:: termText
     - text_general
     - True
     - False
     - True
     - Copy from term.

   * - .. attribute:: text
     - text_en_splitting
     - False
     - True
     - True
     - Full text of the metadata record, used to support full text searches

   * - .. attribute:: title
     - text_general
     - False
     - True
     - True
     - Title of the dataset as recorded in the science metadata.

   * - .. attribute:: titlestr
     - string
     - False
     - False
     - True
     - Copy from title.

   * - .. attribute:: topic
     - string
     - True
     - True
     - True
     - The most general subject area within which a parameter is categorized. Approved topics include "agriculture," "atmosphere," and "hydrosphere," among others.

   * - .. attribute:: topicText
     - text_general
     - True
     - False
     - True
     - Copy from topic.

   * - .. attribute:: updateDate
     - tdate
     - False
     - True
     - True
     - Copy from dateuploaded.

   * - .. attribute:: webUrl
     - string
     - True
     - True
     - False
     - Link to the investigator's  web-site.

   * - .. attribute:: westBoundCoord
     - tfloat
     - False
     - True
     - True
     - Western most longitude of the spatial extent, in decimal degrees, WGS84

   * - .. attribute:: writePermission
     - string
     - True
     - True
     - True
     - List of subjects (groups and individuals) that have write permission on PID.



Dynamic Fields
--------------

.. list-table::
   :header-rows: 1
   :widths: 3, 2, 1, 1, 1, 10

   * - Field
     - Type
     - MV
     - Store
     - Index
     - Description
   * - .. attribute:: *_b
     - boolean
     - False
     - True
     - True
     - 
   * - .. attribute:: *_bm
     - boolean
     - True
     - True
     - True
     - 
   * - .. attribute:: *_bs
     - boolean
     - True
     - True
     - True
     - 
   * - .. attribute:: *_c
     - currency
     - False
     - True
     - True
     - 
   * - .. attribute:: *_coordinate
     - tdouble
     - False
     - False
     - True
     - 
   * - .. attribute:: *_d
     - double
     - False
     - True
     - True
     - 
   * - .. attribute:: *_dm
     - tdouble
     - True
     - True
     - True
     - 
   * - .. attribute:: *_ds
     - double
     - True
     - True
     - True
     - 
   * - .. attribute:: *_dt
     - date
     - False
     - True
     - True
     - 
   * - .. attribute:: *_dtm
     - tdate
     - True
     - True
     - True
     - 
   * - .. attribute:: *_dts
     - date
     - True
     - True
     - True
     - 
   * - .. attribute:: *_en
     - text_en
     - True
     - True
     - True
     - 
   * - .. attribute:: *_f
     - float
     - False
     - True
     - True
     - 
   * - .. attribute:: *_fm
     - tfloat
     - True
     - True
     - True
     - 
   * - .. attribute:: *_fs
     - float
     - True
     - True
     - True
     - 
   * - .. attribute:: *_i
     - int
     - False
     - True
     - True
     - 
   * - .. attribute:: *_im
     - tint
     - True
     - True
     - True
     - 
   * - .. attribute:: *_is
     - int
     - True
     - True
     - True
     - 
   * - .. attribute:: *_l
     - long
     - False
     - True
     - True
     - 
   * - .. attribute:: *_lm
     - tlong
     - True
     - True
     - True
     - 
   * - .. attribute:: *_ls
     - long
     - True
     - True
     - True
     - 
   * - .. attribute:: *_p
     - location
     - False
     - True
     - True
     - 
   * - .. attribute:: *_s
     - string
     - False
     - True
     - True
     - 
   * - .. attribute:: *_sm
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: *_ss
     - string
     - True
     - True
     - True
     - 
   * - .. attribute:: *_t
     - text_general
     - False
     - True
     - True
     - 
   * - .. attribute:: *_td
     - tdouble
     - False
     - True
     - True
     - 
   * - .. attribute:: *_tdt
     - tdate
     - False
     - True
     - True
     - 
   * - .. attribute:: *_tf
     - tfloat
     - False
     - True
     - True
     - 
   * - .. attribute:: *_ti
     - tint
     - False
     - True
     - True
     - 
   * - .. attribute:: *_tl
     - tlong
     - False
     - True
     - True
     - 
   * - .. attribute:: *_tm
     - text_general
     - True
     - True
     - True
     - 
   * - .. attribute:: *_txt
     - text_general
     - True
     - True
     - True
     - 
   * - .. attribute:: attr_*
     - text_general
     - True
     - True
     - True
     - 
   * - .. attribute:: ignored_*
     - ignored
     - True
     - False
     - False
     - 
   * - .. attribute:: random_*
     - random
     - False
     - False
     - False
     - 


.. _solr configuration file: https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/resources/index-solr-schema.xml
.. _YAML formatted text file: https://github.com/DataONEorg/indexer_documentation/blob/master/solr_field_descriptions.yaml