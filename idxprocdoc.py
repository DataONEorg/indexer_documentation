"""
Index_processor bean to rst generator.

"""

import logging
import argparse
import os
import codecs
import yaml
import re
from urllib.request import urlopen
from lxml import etree
from jinja2 import Environment, PackageLoader
from pprint import pprint

NAMESPACES = {
    "b": "http://www.springframework.org/schema/beans",
    "c": "http://www.springframework.org/schema/context",
    "p": "http://www.springframework.org/schema/p",
}

# Provides information about subprocessors, indexed by subprocessor bean id, contains: {name, description}
SUBPROCESSOR_INFO = {}

SOLR_DESCRIPTIONS = {}  # Dictionary of solr field - description

FORMAT_IDS = {}  # dictionary of formatid:{description, type}


def loadIndexFieldDescriptions(fn_src):
    global SOLR_DESCRIPTIONS
    logging.info("Loading field descriptions from %s", fn_src)
    with codecs.open(fn_src, encoding="utf-8") as f:
        entries = f.readlines()
        for entry in entries:
            a, b = entry.split("=", 1)
            SOLR_DESCRIPTIONS[a] = b
        # SOLR_DESCRIPTIONS = yaml.load(f)


def loadSubprocessorDescriptions(fn_src):
    global SUBPROCESSOR_INFO
    logging.info("Loading subprocessor descriptions from %s", fn_src)
    with codecs.open(fn_src, encoding="utf-8") as f:
        SUBPROCESSOR_INFO = yaml.load(f)


def loadFormatIds(url="https://cn.dataone.org/cn/v2/formats/"):
    global FORMAT_IDS
    logging.info("Loading format IDs from %s", url)
    formats = etree.parse(urlopen(url))
    for format in formats.xpath("//objectFormat"):
        formatid = format.xpath("formatId")[0].text
        descr = format.xpath("formatName")[0].text
        ftype = format.xpath("formatType")[0].text
        FORMAT_IDS[formatid] = {"description": descr, "type": ftype}


def strToBool(s):
    s = s.lower().strip()
    if s == "0":
        return False
    if s in ["yes", "true", "ok", "yep", "1"]:
        return True
    return False


def xpstrval(ele, xp, default=""):
    try:
        res = ele.xpath(xp, namespaces=NAMESPACES)[0]
        return res
    except IndexError as e:
        logging.debug(e)
    return default


def xpboolval(ele, xp, default=False):
    try:
        res = ele.xpath(xp, namespaces=NAMESPACES)[0]
        return strToBool(res)
    except IndexError as e:
        logging.debug(e)
    return default


def getAttrib(ele, name, default=None):
    try:
        return ele.attrib[name]
    except KeyError:
        pass
    return default


def U1(s):
    return "=" * len(s)


def U2(s):
    return "-" * len(s)


def U3(s):
    return "~" * len(s)


def wrapXPath(original, width=80, ind1=0, ind2=0, prefix=""):
    """ word wrapping function.
      string: the string to wrap
      width: the column number to wrap at
      prefix: prefix each line with this string (goes before any indentation)
      ind1: number of characters to indent the first line
      ind2: number of characters to indent the rest of the lines
  """
    xp = original
    wrap_chars = ["/", " ", ")", "]", "|", "[", "="]
    xp = prefix + ind1 * " " + xp
    newstring = ""
    while len(xp) > width:
        # find position of nearest whitespace char to the left of "width"
        marker = width - 1
        while not xp[marker] in wrap_chars:
            marker = marker - 1
            if marker < 5:
                return original
        # remove line from original string and add it to the new string
        newline = xp[0 : marker + 1] + "\n"
        newstring = newstring + newline
        xp = prefix + ind2 * " " + xp[marker + 1 :]
    return newstring + xp


def classnameLink(cname):
    if cname is None or cname == "":
        return ""
    parts = cname.split(".")
    res = parts[-1]
    url = "https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/java/"
    url += "/".join(parts) + ".java"
    return "`{0} <{1}>`_".format(res, url)


def solrFieldDescription(field):
    try:
        res = SOLR_DESCRIPTIONS[field]
        if res is None:
            return ""
        return res
    except:
        pass
    return ""


def svnRepoLink(target):
    return (
        "https://repository.dataone.org/software/cicore/trunk/cn/d1_cn_index_processor/src/main/"
        + target
    )


# =======================================================================================================================
class B_Bean(object):
    def __init__(self):
        self._L = logging.getLogger(self.__class__.__name__)
        self.p = {"bid": "", "cname": "", "xml": ""}

    def load(self, ele, container):
        """
    Load the properties of this bean
    :param ele:
    :return:
    """
        self.p["cname"] = getAttrib(ele, "class", "")
        self.p["bid"] = getAttrib(ele, "id", "")
        self.p["xml"] = etree.tostring(ele, pretty_print=True).decode()

    def __repr__(self):
        lines = ["{0}:".format(self.__class__.__name__)]
        for k in self.p:
            lines.append("  {0} : {1}".format(k, self.p[k]))
        return "\n".join(lines)

    def toText(self, resolver=None, indent=0):
        return str(self)


# --
class B_BeanXPath(B_Bean):
    def __init__(self):
        super(B_BeanXPath, self).__init__()
        self.p["xpath"] = ""

    def load(self, ele, container):
        super(B_BeanXPath, self).load(ele, container)
        self.p["xpath"] = ele.xpath(
            "b:constructor-arg[@name='xpath']/@value", namespaces=NAMESPACES
        )


# --
class B_SolrField(B_BeanXPath):
    def __init__(self):
        super(B_SolrField, self).__init__()
        self.p["field_name"] = []
        self.p["converter"] = ""
        self.p["xpath"] = ""
        self.p["multivalue"] = False
        self.p["dedupe"] = False

    def load(self, ele, container):
        super(B_SolrField, self).load(ele, container)
        self.p["field_name"] = [xpstrval(ele, "b:constructor-arg[@name='name']/@value")]
        self.p["multivalue"] = xpboolval(ele, "b:property[@name='multivalue']/@value")
        self.p["dedupe"] = xpboolval(ele, "b:property[@name='dedupe']/@value")
        self.p["converter"] = xpstrval(ele, "b:property[@name='converter']/@ref")
        self.p["xpath"] = xpstrval(ele, "b:constructor-arg[@name='xpath']/@value")
        if self.p["bid"] == "":
            # If there's no ID, then it is an anonymous bean contained by some parent
            # query is something like "../../.."
            pele = ele.xpath("../../..")
            if len(pele) > 0:
                self.p["bid"] = "{0}.{1}".format(
                    pele[0].attrib["id"], self.p["field_name"][0]
                )

    def toText(self, resolver=None, indent=0):
        res = repr(self)
        if resolver is None:
            return res
        if self.p["converter"] != "":
            bean = resolver.getBean(self.p["converter"])
            if not bean is None:
                res += "\n"
                res += bean.toText(resolver=resolver, indent=indent + 2)
        return res


# --
class B_RootElement(B_Bean):
    def load(self, ele, container):
        super(B_RootElement, self).load(ele, container)


# --
class B_LeafElement(B_Bean):
    def load(self, ele, container):
        super(B_LeafElement, self).load(ele, container)


# --
class B_CommonRootSolrField(B_Bean):
    def load(self, ele, container):
        super(B_CommonRootSolrField, self).load(ele, container)
        self.p["root-ref"] = xpstrval(ele, "./@p:root-ref")
        self.p["field_name"] = [xpstrval(ele, "b:constructor-arg[@name='name']/@value")]
        self.p["multivalue"] = xpboolval(ele, "b:property[@name='multivalue']/@value")
        self.p["converter"] = xpstrval(ele, "b:property[@name='converter']/@ref")
        if self.p["bid"] == "":
            # If there's no ID, then it is an anonymous bean contained by some parent
            # query is something like "../../.."
            pele = ele.xpath("../../..")
            if len(pele) > 0:
                self.p["bid"] = "{0}.{1}".format(
                    pele[0].attrib["id"], self.p["field_name"][0]
                )


# --
class B_ResolveSolrField(B_Bean):
    """
  "https://" + ROUTER_HOST_NAME + "/cn/v1/resolve/";
  """

    def __init__(self):
        super(B_ResolveSolrField, self).__init__()

    def load(self, ele, container):
        super(B_ResolveSolrField, self).load(ele, container)
        self.p["field_name"] = ["fileID"]
        if self.p["bid"] == "":
            # If there's no ID, then it is an anonymous bean contained by some parent
            # query is something like "../../.."
            pele = ele.xpath("../../..")
            if len(pele) > 0:
                self.p["bid"] = "{0}.{1}".format(
                    pele[0].attrib["id"], self.p["field_name"][0]
                )


# --
class B_MergeSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_MergeSolrField, self).load(ele, container)


# --
class B_FullTextSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_FullTextSolrField, self).load(ele, container)


# --
class B_AggregateSolrField(B_Bean):
    def load(self, ele, container):
        super(B_AggregateSolrField, self).load(ele, container)
        self.p["field_name"] = [xpstrval(ele, "b:property[@name='name']/@value")]


# --
class B_DublinCoreSpatialBoxBoundingCoordinatesSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_DublinCoreSpatialBoxBoundingCoordinatesSolrField, self).load(
            ele, container
        )
        self.p["field_name"] = [
            "northBoundCoord",
            "southBoundCoord",
            "eastBoundCoord",
            "westBoundCoord",
        ]


# --
class B_DublinCoreSpatialBoxGeohashSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_DublinCoreSpatialBoxGeohashSolrField, self).load(ele, container)
        self.p["field_name"] = [
            "geohash_1",
            "geohash_2",
            "geohash_3",
            "geohash_4",
            "geohash_5",
            "geohash_6",
            "geohash_7",
            "geohash_8",
            "geohash_9",
        ]


# --
class B_DataCiteSpatialBoxBoundingCoordinatesSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_DataCiteSpatialBoxBoundingCoordinatesSolrField, self).load(
            ele, container
        )


# --
class B_DataCiteSpatialBoxGeohashSolrField(B_SolrField):
    def load(self, ele, container):
        super(B_DataCiteSpatialBoxGeohashSolrField, self).load(ele, container)


# --
class B_SolrIndexService(B_Bean):
    def __init__(self):
        super(B_SolrIndexService, self).__init__()
        self.p["subprocessors"] = []
        self.p["systemMetadataProcessor"] = ""

    def load(self, ele, container):
        super(B_SolrIndexService, self).load(ele, container)
        self.p["systemMetadataProcessor"] = xpstrval(
            ele, "b:property[@name='systemMetadataProcessor']/@ref"
        )
        bids = ele.xpath(
            "b:property[@name='subprocessors']/b:list/b:ref", namespaces=NAMESPACES
        )
        self.p["subprocessors"] = []
        for bid in bids:
            self.p["subprocessors"].append(bid.attrib["bean"])

    def toText(self, resolver=None, indent=0):
        res = repr(self)
        if resolver is None:
            return res
        for bid in self.p["beans"]:
            bean = resolver.getBean(bid)
            res += "\n"
            if not bean is None:
                res += bean.toText(resolver=resolver, indent=indent + 2)
            else:
                res += "ERROR: could not resolve '{0}'".format(bid)
        return res


# --
class B_BaseXPathDocumentSubprocessor(B_Bean):
    def __init__(self):
        super(B_BaseXPathDocumentSubprocessor, self).__init__()
        self.p["namespaces"] = ""
        self.p["fieldList"] = []

    def load(self, ele, container):
        super(B_BaseXPathDocumentSubprocessor, self).load(ele, container)
        # Bean ID for XMLNameSpace Config
        self.p["namespaces"] = xpstrval(
            ele, "b:property[@name='xmlNamespaceConfig']/@ref"
        )
        # List of fields processed by this processor
        fields = ele.xpath(
            "b:property[@name='fieldList']/b:list/b:bean", namespaces=NAMESPACES
        )
        for field in fields:
            res = container.beanLoaderFactory(field)
            self._L.debug("BID = %s", str(res.p["bid"]))
            self.p["fieldList"].append(res.p["bid"])

    def toText(self, resolver=None, indent=0):
        res = repr(self)
        if resolver is None:
            return res
        fields = resolver.getBean(self.p["field_list"])
        if fields is None:
            return res
        res += "\n"
        res += fields.toText(resolver=resolver, indent=indent + 2)
        for subproc in self.p["subprocessors"]:
            bean = resolver.getBean(subproc)
            if not bean is None:
                res += "\n"
                res += bean.toText(resolver=resolver, indent=indent + 2)
        return res


# --
class B_XPathDocumentParser(B_BaseXPathDocumentSubprocessor):
    pass


# --
class B_ScienceMetadataDocumentSubprocessor(B_Bean):
    def __init__(self):
        super(B_ScienceMetadataDocumentSubprocessor, self).__init__()
        self.p["matchDocuments"] = []
        self.p["fields"] = []

    def load(self, ele, container):
        super(B_ScienceMetadataDocumentSubprocessor, self).load(ele, container)
        self.p["matchDocuments"] = []
        matchdocs = ele.xpath(
            "b:property[@name='matchDocuments']/b:list/b:value", namespaces=NAMESPACES
        )
        for matchdoc in matchdocs:
            self.p["matchDocuments"].append(matchdoc.text)
        self.p["fields"] = []
        fields = ele.xpath(
            "b:property[@name='fieldList']/b:list/b:ref", namespaces=NAMESPACES
        )
        for field in fields:
            self.p["fields"].append(field.attrib["bean"])
        # Fields defined directly in subprocessor config
        beans = ele.xpath(
            "b:property[@name='fieldList']/b:list/b:bean", namespaces=NAMESPACES
        )
        counter = 0
        for bean in beans:
            bid = bean.attrib.get("id", f"{self.p['bid']}.bean{counter}")
            bean.attrib["id"] = bid
            # bean is defined in the subprocessor, need to add it to the list of beans
            logging.info("Loading bean: %s", str(bean))
            instance = container.beanLoaderFactory(bean)
            self.p["fields"].append(bid)
            counter += 1

    def toText(self, resolver=None, indent=0):
        res = repr(self)
        if resolver is None:
            return res
        for field in self.p["fields"]:
            bean = resolver.getBean(field)
            if not bean is None:
                res += "\n"
                res += bean.toText(resolver=resolver, indent=indent + 2)
        return res


# --
class B_ResourceMapSubprocessor(B_ScienceMetadataDocumentSubprocessor):
    def __init__(self):
        super(B_ResourceMapSubprocessor, self).__init__()

    def load(self, ele, container):
        super(B_ResourceMapSubprocessor, self).load(ele, container)


# --
class B_XMLNamespace(B_Bean):
    def __init__(self):
        super(B_XMLNamespace, self).__init__()

    def load(self, ele, container):
        super(B_XMLNamespace, self).load(ele, container)
        self.p["namespace"] = xpstrval(
            ele, "b:constructor-arg[@name='namespace']/@value", ""
        )
        self.p["prefix"] = xpstrval(ele, "b:constructor-arg[@name='prefix']/@value", "")


# --
class B_XMLNamespaceConfig(B_Bean):
    def __init__(self):
        super(B_XMLNamespaceConfig, self).__init__()

    def load(self, ele, container):
        super(B_XMLNamespaceConfig, self).load(ele, container)
        self.p["namespaces"] = []
        namespaces = ele.xpath(
            "b:constructor-arg[@name='namespaceList']/b:list/b:bean",
            namespaces=NAMESPACES,
        )
        for ns in namespaces:
            # cname = ns.attrib["class"]
            entry = container.beanLoaderFactory(ns)
            self.p["namespaces"].append(entry)


# --
class B_BaseDocumentDeleteSubprocessor(B_Bean):
    pass


# --
class B_AnnotatorSubprocessor(B_ScienceMetadataDocumentSubprocessor):
    pass


# --
class B_BaseReprocessSubprocessor(B_Bean):
    pass


# --
class B_SparqlField(B_Bean):
    def __init__(self):
        super(B_SparqlField, self).__init__()
        self.p["field_name"] = []
        self.p["converter"] = ""
        self.p["query"] = ""
        self.p["multivalue"] = False
        self.p["dedupe"] = False

    def load(self, ele, container):
        super(B_SparqlField, self).load(ele, container)
        self.p["field_name"] = [xpstrval(ele, "b:constructor-arg[@name='name']/@value")]
        self.p["multivalue"] = xpboolval(ele, "b:property[@name='multivalue']/@value")
        self.p["dedupe"] = xpboolval(ele, "b:property[@name='dedupe']/@value")
        self.p["converter"] = xpstrval(ele, "b:property[@name='converter']/@ref")
        query = ele.xpath(
            "b:constructor-arg[@name='query']/b:value", namespaces=NAMESPACES
        )
        if len(query) > 0:
            self.p["query"] = query[0].text
        if self.p["bid"] == "":
            # If there's no ID, then it is an anonymous bean contained by some parent
            # query is something like "../../.."
            pele = ele.xpath("../../..")
            if len(pele) > 0:
                self.p["bid"] = "{0}.{1}".format(
                    pele[0].attrib["id"], self.p["field_name"][0]
                )


# --
class B_RdfXmlSubprocessor(B_ScienceMetadataDocumentSubprocessor):
    pass


#  def __init__(self):
#    super(B_RdfXmlSubprocessor, self).__init__()
#    self.p['matchDocuments'] = []
#    self.p['fields'] = []


# --
class B_EmlAnnotationSubprocessor(B_ScienceMetadataDocumentSubprocessor):
    pass


# --
class B_TemporalPeriodSolrField(B_SolrField):
    def __init__(self):
        super(B_TemporalPeriodSolrField, self).__init__()
        self.p["field_name"] = ["beginDate", "endDate"]

    def load(self, ele, container):
        super(B_TemporalPeriodSolrField, self).load(ele, container)
        self.p["field_name"] = ["beginDate", "endDate"]


# --
class B_SolrDateConverter(B_Bean):
    pass


# --
class B_FgdcDateConverter(B_Bean):
    pass


# --
class B_SolrLatitudeConverter(B_Bean):
    pass


# --
class B_SolrLongitudeConverter(B_Bean):
    pass


# --
class B_BooleanMatchConverter(B_Bean):
    pass


# --
class B_FormatIdToFormatTypeConverter(B_Bean):
    pass


# --
class B_GeohashConverter(B_Bean):
    def load(self, ele, container):
        super(B_GeohashConverter, self).load(ele, container)
        self.p["length"] = xpstrval(ele, "b:property[@name='length']/@value", "")


# --
class B_MemberNodeServiceRegistrationTypeConverter(B_Bean):
    pass


# --
class B_MemberNodeServiceRegistrationTypeDocumentService(B_Bean):
    pass


# --
class B_OntologyModelService(B_Bean):
    pass


# --
class B_HashMap(B_Bean):
    pass


# =======================================================================================================================


class IndexProcessorDocument(object):
    def __init__(self):
        self._L = logging.getLogger(self.__class__.__name__)


# =======================================================================================================================


class IndexProcessorDocuments(object):
    def __init__(self):
        self._L = logging.getLogger(self.__class__.__name__)
        self.documents = {}
        self.beans = []
        self.solr_fields = []
        self.solr_dynfields = []
        self.parsers = []

    def getBean(self, bid):
        for b in self.beans:
            if b.p["bid"] == bid:
                return b
        return None

    def getClassInstances(self, class_name):
        res = []
        for bean in self.beans:
            if bean.p["cname"] == class_name:
                res.append(bean)
            else:
                self._L.debug("No bean for class name: %s", class_name)
        return res

    def beanLoaderFactory(self, bean):
        cname = bean.attrib["class"]
        class_name = "B_{0}".format(cname.split(".")[-1])
        self._L.debug("Loading: %s", class_name)
        try:
            instance = globals()[class_name]()
            instance.load(bean, self)
            self.beans.append(instance)
            return instance
        except KeyError as e:
            pass

        self._L.error("Unknown class name: %s", class_name)
        raise ValueError("No handler for class: {0}".format(cname))
        return None

    def load(self, fname):
        """
    Load beans from xml document fname.

    :param fname:
    :return:
    """
        parser = etree.XMLParser(strip_cdata=False)
        doc = etree.parse(fname, parser=parser)
        beans = doc.xpath("//b:bean", namespaces=NAMESPACES)
        for bean in beans:
            b = self.beanLoaderFactory(bean)
            # self.beans.append( b )

    def loadBeans(self, context_path):
        # Load the various bean definitions
        context_doc = os.path.join(context_path, "index-context-file-includes.xml")
        context = etree.parse(context_doc)
        documents = context.xpath("//b:import", namespaces=NAMESPACES)
        for document in documents:
            fname = os.path.basename(document.attrib["resource"])
            if not fname.startswith("classpath:"):
                self._L.info("Loading bean: %s", fname)
                self.load(os.path.join(context_path, fname))

    def loadConverters(self, context_path):
        converter_context_doc = os.path.join(context_path, "index-parser-context.xml")
        converter_context = etree.parse(converter_context_doc)
        converters = converter_context.xpath(
            "//b:bean[contains(@class,'indexer.convert')]", namespaces=NAMESPACES
        )
        for converter in converters:
            b = self.beanLoaderFactory(converter)
            if not b is None:
                self.beans.append(b)

    def loadParsers(self, context_path):
        parser_context_doc = os.path.join(context_path, "index-parser-context.xml")
        parser_context = etree.parse(parser_context_doc)
        documents = parser_context.xpath(
            "//b:bean[@id='solrIndexService']", namespaces=NAMESPACES
        )
        for document in documents:
            doc_parser = self.beanLoaderFactory(document)
            # print(f"*** {doc_parser}")
            self.parsers.append(doc_parser)
        # now the namespaces
        documents = parser_context.xpath(
            "//b:bean[@id='xmlNamespaceConfig']", namespaces=NAMESPACES
        )
        for document in documents:
            nsc = self.beanLoaderFactory(document)
            # print(f"**** {nsc}")
            self.beans.append(nsc)

    def loadSolrSchemaFields(self, context_path):
        doc = os.path.join(context_path, "index-solr-schema.xml")
        doctree = etree.parse(doc)
        fields = doctree.xpath("//field")
        self.solr_fields = []
        for field in fields:
            f = {
                "name": getAttrib(field, "name", ""),
                "type": getAttrib(field, "type", ""),
                "indexed": strToBool(getAttrib(field, "indexed", "false")),
                "stored": strToBool(getAttrib(field, "stored", "false")),
                "multiValued": strToBool(getAttrib(field, "multiValued", "false")),
            }
            self.solr_fields.append(f)
        fields = doctree.xpath("//dynamicField")
        for field in fields:
            f = {
                "name": getAttrib(field, "name", ""),
                "type": getAttrib(field, "type", ""),
                "indexed": strToBool(getAttrib(field, "indexed", "false")),
                "stored": strToBool(getAttrib(field, "stored", "false")),
                "multiValued": strToBool(getAttrib(field, "multiValued", "false")),
            }
            self.solr_dynfields.append(f)

    def loadContext(self, context_path):
        self.loadSolrSchemaFields(context_path)
        self.loadBeans(context_path)
        self.loadConverters(context_path)
        self.loadParsers(context_path)

    def j_attrList(self, names, module="Index", delim=", "):
        res = []
        for name in names:
            if name != "":
                # todo: Need to do some funky escaping for RST links to work here
                # for k in self.solr_dynfields:
                #  if name.endswith(k['name'][1:]):
                #    res.append(":attr:`{0}.{1}`".format(module, k['name']))
                #    return delim.join(res)
                res.append(":attr:`{0}.{1}`".format(module, name))
        return delim.join(res)

    def j_getConverterInfo(self, bid):
        self._L.debug("looking up converter: %s" % bid)
        bean = self.getBean(bid)
        if bean is None:
            return ""
        return bean.p["cname"]

    def j_describeFormatId(self, formatid):
        formatid = formatid.strip()
        try:
            return FORMAT_IDS[formatid]["description"]
        except KeyError as e:
            self._L.error("Unknown format ID: %s", formatid)
        return "Unknown"

    def j_subprocessorName(self, subproc_id):
        res = subproc_id
        try:
            res = SUBPROCESSOR_INFO[subproc_id]["name"]
        except KeyError as e:
            self._L.warn("No description available for subprocessor: %s", subproc_id)
        return res + "\n" + "=" * len(res)

    def j_sparqlTrim(self, sparql):
        """
    Trim the name spaces from the provided sparql query.
    :param sparql:
    :return: trimmed text
    """
        rg = re.compile("\n(\s*)SELECT")
        selpos = rg.search(sparql)
        if selpos is not None:
            return sparql[selpos.start() :]
        return sparql

    def _crossrefMatrix(self):
        """
      Generate a cross reference matrix of field x formatId

      row names = solr fields
      col names = formatIds
      values = 0 | 1

      Returns: {rnames:[], cnames:[], rc:[r:[]]}

      """
        # get list of formatIds
        # for each subprocessor
        #  get list of fields used
        #  for each field used
        #    set formatId column
        res = {"colmeta": [], "rowmeta": [], "rc": []}
        # get list of solr fields
        res["rowmeta"] = sorted(self.solr_fields, key=lambda k: k["name"].lower())

        return res


    def getFormatIds(self):
        """
        Get a list of formatIds and their processor

        Returns: list of dict {formatid:subProcessor}
        """
        res = {}
        for subproc in self.parsers[0].p["subprocessors"]:
            subproc_instance = self.getBean(subproc)
            try:
                for formatId in subproc_instance.p["matchDocuments"]:
                    try:
                        res[formatId].append(subproc)
                    except KeyError as e:
                        res[formatId] = [subproc, ]
            except KeyError as e:
                self._L.info("No formatIds for subprocessor: %s", subproc)
        return res


    def getfieldList(self):
        """
        Get list of all fields in solr index

        Returns:

        """
        res = []
        ignored_fields = ["_root_", "_version_", ]
        fields = sorted( self.solr_fields, key=lambda k: k["name"].lower() )
        for field in fields:
            if not field["name"] in ignored_fields:
                res.append(field["name"])
        return sorted(list(set(res)))


    def getSysMetaFields(self):
        """
        Return the list of fields handled by system metadata processor
        Returns:

        """
        res = []
        sysm_proc = self.getBean(self.parsers[0].p["systemMetadataProcessor"])
        for field in sysm_proc.p["fieldList"]:
          fb = self.getBean(field)
          field_name = str(fb.p["field_name"][0])
          res.append(field_name)
        return res


    def getFields(self, formatId):
        """
        Given a formatId, return a list of fields handled by the processor.

        Args:
          formatId: fields to gather

        Returns:

        """
        res = []
        the_subproc_instances = []
        for subproc in self.parsers[0].p["subprocessors"]:
            subproc_instance = self.getBean(subproc)
            try:
                for fid in subproc_instance.p["matchDocuments"]:
                    if fid == formatId:
                        the_subproc_instances.append(subproc_instance)
            except KeyError as e:
                self._L.info("No formatIds for subprocessor: %s", subproc)
        for subproc_instance in the_subproc_instances:
            # Retrieve fields from subprocessor
            #pprint(the_subproc_instance)
            if "fields" in subproc_instance.p:
                for field in subproc_instance.p["fields"]:
                    bf = self.getBean(field)
                    field_name = str(bf.p["field_name"][0])
                    res.append(field_name)
        return list(set(res))


    def toText(self, dest_folder=None):
        if not os.path.exists(dest_folder):
            self._L.info("Creating folder for generated content: %s", dest_folder)
            os.makedirs(dest_folder)
        env = Environment(loader=PackageLoader("idxprocdoc", "templates"))
        env.filters["U1"] = U1
        env.filters["U2"] = U2
        env.filters["U3"] = U3
        env.filters["wrapXPath"] = wrapXPath
        env.filters["classnameLink"] = classnameLink
        env.filters["attrList"] = self.j_attrList
        env.filters["solrFieldDescription"] = solrFieldDescription
        env.filters["svnRepoLink"] = svnRepoLink
        env.filters["getConverterInfo"] = self.j_getConverterInfo
        env.filters["describeFormatId"] = self.j_describeFormatId
        env.filters["subprocessorName"] = self.j_subprocessorName
        env.filters["sparqlTrim"] = self.j_sparqlTrim

        tnames = [
            "solr_schema.rst",
            "namespaces.rst",
            "parsers.rst",
            "subprocessor.rst",
            "system_metadata.rst",
            "fid_field_cross.rst",
        ]
        templates = {}
        for tname in tnames:
            templates[tname] = {
                "template": env.get_template(tname),
                "dest": os.path.join(dest_folder, tname),
            }

        with codecs.open(
            templates["solr_schema.rst"]["dest"], mode="wb", encoding="utf-8"
        ) as f_dest:
            sorted_solr_fields = sorted(
                self.solr_fields, key=lambda k: k["name"].lower()
            )
            sorted_dyn_fields = sorted(
                self.solr_dynfields, key=lambda k: k["name"].lower()
            )
            f_dest.write(
                templates["solr_schema.rst"]["template"].render(
                    resolver=self,
                    fields=sorted_solr_fields,
                    dynfields=sorted_dyn_fields,
                )
            )
        with codecs.open(
            templates["namespaces.rst"]["dest"], mode="wb", encoding="utf-8"
        ) as f_dest:
            namespaces = self.getClassInstances(
                "org.dataone.cn.indexer.XMLNamespaceConfig"
            )
            f_dest.write(
                templates["namespaces.rst"]["template"].render(
                    esolver=self, namespaces=namespaces
                )
            )

        t_name = "parsers.rst"
        t_parsers = env.get_template(t_name)
        fn_dest = os.path.join(dest_folder, t_name)
        with codecs.open(fn_dest, mode="wb", encoding="utf-8") as f_dest:
            parsers = self.getClassInstances(
                "org.dataone.cn.indexer.parser.ScienceMetadataDocumentSubprocessor"
            )
        self._L.info("Number of parsers loaded = %d", len(self.parsers))
        for parser in self.parsers:
            sysm_proc = self.getBean(parser.p["systemMetadataProcessor"])
            fields = {}
            for field in sysm_proc.p["fieldList"]:
                fields[field] = self.getBean(field)
                field_name = str(fields[field].p["field_name"][0])

            dest = os.path.join(dest_folder, "system_metadata.rst")
            with codecs.open(dest, mode="wb", encoding="utf-8") as f_dest:
                f_dest.write(
                    templates["system_metadata.rst"]["template"].render(
                        resolver=self, sp=sysm_proc, fields=fields
                    )
                )
            for subproc in parser.p["subprocessors"]:
                logging.info("Generating text for subprocessor: %s", subproc)
                subproc_instance = self.getBean(subproc)
                fid_idx = []
                # _column = [False]*len(field_format_matrix["rowmeta"])
                fields = {}
                # _column = [False]*len(field_format_matrix["rowmeta"])
                if "fields" in subproc_instance.p:
                    for field in subproc_instance.p["fields"]:
                        fields[field] = self.getBean(field)
                        field_name = str(fields[field].p["field_name"][0])
                    dest = os.path.join(dest_folder, "proc_" + subproc + ".rst")
                    with codecs.open(dest, mode="wb", encoding="utf-8") as f_dest:
                        f_dest.write(
                            templates["subprocessor.rst"]["template"].render(
                                resolver=self, sp=subproc_instance, fields=fields
                            )
                        )

        field_format_matrix = {"colmeta": [], "rowmeta": [], "rc": []}
        field_format_matrix["rowmeta"] = self.getfieldList()
        sysmeta_fields = self.getSysMetaFields()

        fid_fields = {}
        #Get list of processors for formatIds
        #columns = [{formatId:[processor, ...], }
        columns = self.getFormatIds()
        for c in columns.keys():
            field_format_matrix["colmeta"].append(c)
            fid_fields[c] = self.getFields(c)
        #Fill matrix with values, 0 if not processed, 1 if handled
        for field in field_format_matrix["rowmeta"]:
            row = []
            for c in range(0, len(field_format_matrix["colmeta"])):
                v = " "
                if field in sysmeta_fields:
                    v = "X"
                else:
                    # lookup field for each format Id
                    formatId = field_format_matrix["colmeta"][c]
                    if field in fid_fields[formatId]:
                        v = "X"
                row.append(v)
            field_format_matrix["rc"].append(row)
        # generate the CSV
        header = ["Field", ]
        c = 1
        for hv in field_format_matrix["colmeta"]:
            header.append(f'"{c}"')
            c += 1
        csv_header = ",".join(header)
        csv_rows = []
        for i in range(0, len(field_format_matrix["rowmeta"])):
            r = [field_format_matrix["rowmeta"][i], ]
            for j in range(0, len(field_format_matrix["rc"][i])):
                v = field_format_matrix["rc"][i][j]
                r.append(str(v))
            csv_rows.append(",".join(r))
        dest = os.path.join(dest_folder, "field_format.rst")
        with codecs.open(dest, mode="wb", encoding="utf-8") as f_dest:
            f_dest.write(
                templates["fid_field_cross.rst"]["template"].render(
                    resolver=self, csvheader=csv_header, csvrows=csv_rows
                )
            )

        # print(str(field_format_matrix))


# =======================================================================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Generate Solr index mapping documents."
    )
    parser.add_argument(
        "-l",
        "--log_level",
        action="count",
        default=1,
        help="Set logging level, multiples for more detailed.",
    )
    parser.add_argument(
        "-s",
        "--source",
        default=".",
        help="Folder from which to read bean definition files",
    )
    parser.add_argument(
        "-d", "--dest", default=".", help="Folder that will contain generate docs"
    )
    parser.add_argument(
        "-f",
        "--solrdescr",
        default="dataone-cn-solr/usr/share/dataone-cn-solr/debian/queryFieldDescriptions.properties",
        help="YAML file of solr field: description",
    )
    parser.add_argument(
        "-pf",
        "--subprocdescr",
        default="subprocessor_descriptions.yaml",
        help="YAML file of subprocessor descriptions",
    )
    parser.add_argument(
        "-b",
        "--formatsurl",
        default="https://cn.dataone.org/cn/v2/formats/",
        help="Location to retrieve format list",
    )

    args = parser.parse_args()
    # Setup logging verbosity
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, args.log_level)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")
    loadIndexFieldDescriptions(args.solrdescr)
    loadSubprocessorDescriptions(args.subprocdescr)
    loadFormatIds(args.formatsurl)
    beans = IndexProcessorDocuments()
    beans.loadContext(args.source)

    beans.toText(dest_folder=args.dest)


if __name__ == "__main__":
    main()
