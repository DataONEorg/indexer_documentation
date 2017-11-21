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
    - 
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

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="id"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/identifier/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.seriesId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="seriesId"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/seriesId/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.fileName
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="fileName"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/fileName/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.mediaType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="mediaType"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/mediaType/@name"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.mediaTypeProperty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.CommonRootSolrField" p:multivalue="true" p:root-ref="mediaTypePropertyListRoot">\n\t\t\t\t\t\t<constructor-arg name="name" value="mediaTypeProperty"/>\n\t\t\t\t</bean>\t\t\t\t\n\t\t\t\t\n'



systemMetadata200Subprocessor.formatId
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="formatId"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/formatId/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.formatType
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="formatType"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/formatId/text()"/>\n\t\t\t\t\t<property name="converter" ref="formatIdToFormatTypeConverter"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="size"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/size/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.checksum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="checksum"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/checksum/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.submitter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="submitter"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/submitter/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.checksumAlgorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="checksumAlgorithm"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/checksum/@algorithm"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.rightsHolder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="rightsHolder"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/rightsHolder/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.replicationAllowed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="replicationAllowed"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/@replicationAllowed"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.numberReplicas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="numberReplicas"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/@numberReplicas"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.preferredReplicationMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="preferredReplicationMN"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/preferredMemberNode/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.blockedReplicationMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="blockedReplicationMN"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replicationPolicy/blockedMemberNode/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.obsoletes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="obsoletes"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/obsoletes/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.obsoletedBy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="obsoletedBy"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/obsoletedBy/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.dateUploaded
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="dateUploaded"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/dateUploaded/text()"/>\n\t\t\t\t\t<property name="converter" ref="dateConverter"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.dateModified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="dateModified"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/dateSysMetadataModified/text()"/>\n\t\t\t\t\t<property name="converter" ref="dateConverter"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.datasource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="datasource"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/originMemberNode/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.authoritativeMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="authoritativeMN"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/authoritativeMemberNode/text()"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.replicaMN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="replicaMN"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replica/replicaMemberNode/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.replicaVerifiedDate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="replicaVerifiedDate"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/replica/replicaVerified/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t\t<property name="converter" ref="dateConverter"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.readPermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="readPermission"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= \'read\']/subject/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t\t<property name="dedupe" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.writePermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="writePermission"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= \'write\']/subject/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t\t<property name="dedupe" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.changePermission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="changePermission"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="/d200:systemMetadata/accessPolicy/allow[permission= \'changePermission\']/subject/text()"/>\n\t\t\t\t\t<property name="multivalue" value="true"/>\n\t\t\t\t\t<property name="dedupe" value="true"/>\n\t\t\t\t</bean>\n\t\t\t\t\n'



systemMetadata200Subprocessor.isPublic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.SolrField">\n\t\t\t\t\t<constructor-arg name="name" value="isPublic"/>\n\t\t\t\t\t<constructor-arg name="xpath" value="(//accessPolicy/allow[permission= \'read\']/subject[text()=\'public\']/text() | //accessPolicy/allow[permission= \'write\']/subject[text()=\'public\']/text() | //accessPolicy/allow[permission= \'changePermission\']/subject[text()=\'public\']/text() | //rightsHolder[text()=\'public\']/text())[1]"/>\n\t\t\t\t\t<property name="converter" ref="booleanPublicConverter"/>\n\t\t\t\t</bean>\n\t\t        \n'



systemMetadata200Subprocessor.fileID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

   b'<bean xmlns="http://www.springframework.org/schema/beans" xmlns:p="http://www.springframework.org/schema/p" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" class="org.dataone.cn.indexer.parser.ResolveSolrField">\n\t\t\t\t\t<constructor-arg name="name" value="dataUrl"/>\n\t\t        </bean>\n\t\t\t\n'



