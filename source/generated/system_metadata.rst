System Metadata Parser
======================


Fields
------

.. list-table::
  :header-rows: 1
  :widths: 5, 1, 1, 10

  * - Solr Field
    - Multi
    - Dedupe
    - XPath

  * - :attr:`Index.id`
    - False
    - False
    - ::

        /d200:systemMetadata/identifier/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.id`_


  * - :attr:`Index.seriesId`
    - False
    - False
    - ::

        /d200:systemMetadata/seriesId/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.seriesId`_


  * - :attr:`Index.fileName`
    - False
    - False
    - ::

        /d200:systemMetadata/fileName/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.fileName`_


  * - :attr:`Index.mediaType`
    - False
    - False
    - ::

        /d200:systemMetadata/mediaType/@name

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.mediaType`_


  * - :attr:`Index.mediaTypeProperty`
    - False
    - 
    - ::

        /d200:systemMetadata/mediaType/property ->{{[
        mediaTypePropertyName] [mediaTypePropertyValue]}}; 
        mediaTypePropertyName = @name; 
        mediaTypePropertyValue = text()

      | Processor: `CommonRootSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/CommonRootSolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.mediaTypeProperty`_


  * - :attr:`Index.formatId`
    - False
    - False
    - ::

        /d200:systemMetadata/formatId/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.formatId`_


  * - :attr:`Index.formatType`
    - False
    - False
    - ::

        /d200:systemMetadata/formatId/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.formatType`_
      | Converter: `FormatIdToFormatTypeConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/FormatIdToFormatTypeConverter.java>`_


  * - :attr:`Index.size`
    - False
    - False
    - ::

        /d200:systemMetadata/size/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.size`_


  * - :attr:`Index.checksum`
    - False
    - False
    - ::

        /d200:systemMetadata/checksum/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.checksum`_


  * - :attr:`Index.submitter`
    - False
    - False
    - ::

        /d200:systemMetadata/submitter/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.submitter`_


  * - :attr:`Index.checksumAlgorithm`
    - False
    - False
    - ::

        /d200:systemMetadata/checksum/@algorithm

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.checksumAlgorithm`_


  * - :attr:`Index.rightsHolder`
    - False
    - False
    - ::

        /d200:systemMetadata/rightsHolder/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.rightsHolder`_


  * - :attr:`Index.replicationAllowed`
    - False
    - False
    - ::

        /d200:systemMetadata/replicationPolicy/@replicationAllowed

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.replicationAllowed`_


  * - :attr:`Index.numberReplicas`
    - False
    - False
    - ::

        /d200:systemMetadata/replicationPolicy/@numberReplicas

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.numberReplicas`_


  * - :attr:`Index.preferredReplicationMN`
    - True
    - False
    - ::

        /d200:systemMetadata/replicationPolicy/preferredMemberNode/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.preferredReplicationMN`_


  * - :attr:`Index.blockedReplicationMN`
    - True
    - False
    - ::

        /d200:systemMetadata/replicationPolicy/blockedMemberNode/
        text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.blockedReplicationMN`_


  * - :attr:`Index.obsoletes`
    - False
    - False
    - ::

        /d200:systemMetadata/obsoletes/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.obsoletes`_


  * - :attr:`Index.obsoletedBy`
    - False
    - False
    - ::

        /d200:systemMetadata/obsoletedBy/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.obsoletedBy`_


  * - :attr:`Index.dateUploaded`
    - False
    - False
    - ::

        /d200:systemMetadata/dateUploaded/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.dateUploaded`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.dateModified`
    - False
    - False
    - ::

        /d200:systemMetadata/dateSysMetadataModified/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.dateModified`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.datasource`
    - False
    - False
    - ::

        /d200:systemMetadata/originMemberNode/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.datasource`_


  * - :attr:`Index.authoritativeMN`
    - False
    - False
    - ::

        /d200:systemMetadata/authoritativeMemberNode/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.authoritativeMN`_


  * - :attr:`Index.replicaMN`
    - True
    - False
    - ::

        /d200:systemMetadata/replica/replicaMemberNode/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.replicaMN`_


  * - :attr:`Index.replicationStatus`
    - True
    - False
    - ::

        /d200:systemMetadata/replica/replicationStatus/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.replicationStatus`_


  * - :attr:`Index.replicaVerifiedDate`
    - True
    - False
    - ::

        /d200:systemMetadata/replica/replicaVerified/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.replicaVerifiedDate`_
      | Converter: `SolrDateConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/SolrDateConverter.java>`_


  * - :attr:`Index.readPermission`
    - True
    - True
    - ::

        /d200:systemMetadata/accessPolicy/allow[permission= 'read']/
        subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.readPermission`_


  * - :attr:`Index.writePermission`
    - True
    - True
    - ::

        /d200:systemMetadata/accessPolicy/allow[permission= 'write']
        /subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.writePermission`_


  * - :attr:`Index.changePermission`
    - True
    - True
    - ::

        /d200:systemMetadata/accessPolicy/allow[permission= 
        'changePermission']/subject/text()

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.changePermission`_


  * - :attr:`Index.isPublic`
    - False
    - False
    - ::

        (//accessPolicy/allow[permission= 'read']/subject[text()=
        'public']/text() | //accessPolicy/allow[permission= 
        'write']/subject[text()='public']/text() | //
        accessPolicy/allow[permission= 'changePermission']/
        subject[text()='public']/text() | //rightsHolder[
        text()='public']/text())[1]

      | Processor: `SolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/SolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.isPublic`_
      | Converter: `BooleanMatchConverter <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/convert/BooleanMatchConverter.java>`_


  * - :attr:`Index.fileID`
    - 
    - 
    - 
      | Processor: `ResolveSolrField <https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/org/dataone/cn/indexer/parser/ResolveSolrField.java>`_
      | Configuration: `systemMetadata200Subprocessor.fileID`_
      | Converter: 



Bean Configurations
-------------------


systemMetadata200Subprocessor.id
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="id"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/identifier/text()"/>
				</bean>
				




systemMetadata200Subprocessor.seriesId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="seriesId"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/seriesId/text()"/>
				</bean>
				




systemMetadata200Subprocessor.fileName
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="fileName"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/fileName/text()"/>
				</bean>
				




systemMetadata200Subprocessor.mediaType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="mediaType"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/mediaType/@name"/>
				</bean>
				




systemMetadata200Subprocessor.mediaTypeProperty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="mediaTypePropertyListRoot">
						<constructor-arg name="name" value="mediaTypeProperty"/>
				</bean>				
				




systemMetadata200Subprocessor.formatId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="formatId"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/formatId/text()"/>
				</bean>
				




systemMetadata200Subprocessor.formatType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="formatType"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/formatId/text()"/>
					<property name="converter" ref="formatIdToFormatTypeConverter"/>
				</bean>
				




systemMetadata200Subprocessor.size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="size"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/size/text()"/>
				</bean>
				




systemMetadata200Subprocessor.checksum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="checksum"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/checksum/text()"/>
				</bean>
				




systemMetadata200Subprocessor.submitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="submitter"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/submitter/text()"/>
				</bean>
				




systemMetadata200Subprocessor.checksumAlgorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="checksumAlgorithm"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/checksum/@algorithm"/>
				</bean>
				




systemMetadata200Subprocessor.rightsHolder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="rightsHolder"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/rightsHolder/text()"/>
				</bean>
				




systemMetadata200Subprocessor.replicationAllowed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="replicationAllowed"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/@replicationAllowed"/>
				</bean>
				




systemMetadata200Subprocessor.numberReplicas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="numberReplicas"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/@numberReplicas"/>
				</bean>
				




systemMetadata200Subprocessor.preferredReplicationMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="preferredReplicationMN"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/preferredMemberNode/text()"/>
					<property name="multivalue" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.blockedReplicationMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="blockedReplicationMN"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/blockedMemberNode/text()"/>
					<property name="multivalue" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.obsoletes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="obsoletes"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/obsoletes/text()"/>
				</bean>
				




systemMetadata200Subprocessor.obsoletedBy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="obsoletedBy"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/obsoletedBy/text()"/>
				</bean>
				




systemMetadata200Subprocessor.dateUploaded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="dateUploaded"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/dateUploaded/text()"/>
					<property name="converter" ref="dateConverter"/>
				</bean>
				




systemMetadata200Subprocessor.dateModified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="dateModified"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/dateSysMetadataModified/text()"/>
					<property name="converter" ref="dateConverter"/>
				</bean>
				




systemMetadata200Subprocessor.datasource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="datasource"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/originMemberNode/text()"/>
				</bean>
				




systemMetadata200Subprocessor.authoritativeMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="authoritativeMN"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/authoritativeMemberNode/text()"/>
				</bean>
				




systemMetadata200Subprocessor.replicaMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="replicaMN"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replica/replicaMemberNode/text()"/>
					<property name="multivalue" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.replicationStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
                    <constructor-arg name="name" value="replicationStatus"/>
                    <constructor-arg name="xpath" value="/d200:systemMetadata/replica/replicationStatus/text()"/>
                    <property name="multivalue" value="true"/>
                </bean>
				




systemMetadata200Subprocessor.replicaVerifiedDate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="replicaVerifiedDate"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/replica/replicaVerified/text()"/>
					<property name="multivalue" value="true"/>
					<property name="converter" ref="dateConverter"/>
				</bean>
				




systemMetadata200Subprocessor.readPermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="readPermission"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= 'read']/subject/text()"/>
					<property name="multivalue" value="true"/>
					<property name="dedupe" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.writePermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="writePermission"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= 'write']/subject/text()"/>
					<property name="multivalue" value="true"/>
					<property name="dedupe" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.changePermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="changePermission"/>
					<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= 'changePermission']/subject/text()"/>
					<property name="multivalue" value="true"/>
					<property name="dedupe" value="true"/>
				</bean>
				




systemMetadata200Subprocessor.isPublic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">
					<constructor-arg name="name" value="isPublic"/>
					<constructor-arg name="xpath" value="(//accessPolicy/allow[permission= 'read']/subject[text()='public']/text() | //accessPolicy/allow[permission= 'write']/subject[text()='public']/text() | //accessPolicy/allow[permission= 'changePermission']/subject[text()='public']/text() | //rightsHolder[text()='public']/text())[1]"/>
					<property name="converter" ref="booleanPublicConverter"/>
				</bean>
		        




systemMetadata200Subprocessor.fileID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   <bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.ResolveSolrField">
					<constructor-arg name="name" value="dataUrl"/>
		        </bean>
			




