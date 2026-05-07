# Auto generated from cve.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-07T15:00:52
# Schema: cve
#
# id: https://w3id.org/lmodel/cve
# description: Common Vulnerabilities and Exposures (CVE™) Program - LinkML Schema.
#   Provides complete semantic coverage of the CVE Record Format v5 JSON Schema, including published and rejected records, all container types, CVSS 4.0/3.1/3.0/2.0 scoring, CPE applicability, taxonomy mappings, credits, and timeline entries.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Datetime, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDateTime

metamodel_version = "1.7.0"
version = "5.2.0"

# Namespaces
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/vulnerability-core/')
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
CWE = CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
KEV_CATALOG = CurieNamespace('kev_catalog', 'https://w3id.org/lmodel/kev-catalog/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NVD = CurieNamespace('nvd', 'https://w3id.org/lmodel/nist-nvd/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CVE


# Types
class UuidType(str):
    """ A version 4 (random) universally unique identifier (UUID) as defined by RFC 4122 section 4.1.3. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UuidType"
    type_model_uri = CVE.UuidType


class Timestamp(str):
    """ Date/time format based on RFC3339 and ISO ISO8601, with an optional timezone in the format 'yyyy-MM-ddTHH:mm:ss[+-]ZH:ZM'. If timezone offset is not given, GMT (+00:00) is assumed. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "Timestamp"
    type_model_uri = CVE.Timestamp


class Datestamp(str):
    """ Date format based on RFC3339 and ISO ISO8601 (date only, no time component). """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "Datestamp"
    type_model_uri = CVE.Datestamp


class VersionString(str):
    """ A single version of a product, as expressed in its own version numbering scheme. May include wildcards such as '*' and version range notation. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "VersionString"
    type_model_uri = CVE.VersionString


class LanguageTag(str):
    """ BCP 47 language code, language-region. The default value is 'en' (English). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "LanguageTag"
    type_model_uri = CVE.LanguageTag


class CpeNameType(str):
    """ Common Platform Enumeration (CPE) Name in either 2.2 or 2.3 format. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CpeNameType"
    type_model_uri = CVE.CpeNameType


class CpeName23Type(str):
    """ Common Platform Enumeration (CPE) Name in 2.3 format only. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CpeName23Type"
    type_model_uri = CVE.CpeName23Type


class CveId(str):
    """ A CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CveId"
    type_model_uri = CVE.CveId


class IsoDate(str):
    """ A calendar date in ISO 8601 format (YYYY-MM-DD). """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "IsoDate"
    type_model_uri = CVE.IsoDate


# Class references
class VulnerabilityCveId(extended_str):
    pass


class CVERecordCveId(VulnerabilityCveId):
    pass


Any = Any

class CveMetadata(YAMLRoot):
    """
    Abstract base for CVE Record metadata. Represents either a Published or Rejected record's metadata. All fields are
    controlled by CVE Services.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetadata"]
    class_class_curie: ClassVar[str] = "cve:CveMetadata"
    class_name: ClassVar[str] = "CveMetadata"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetadata


@dataclass(repr=False)
class CveMetadataPublished(CveMetadata):
    """
    Metadata for a CVE Record in the PUBLISHED state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetadataPublished"]
    class_class_curie: ClassVar[str] = "cve:CveMetadataPublished"
    class_name: ClassVar[str] = "CveMetadataPublished"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetadataPublished

    record_cve_id: str = None
    assigner_org_id: str = None
    published_state: Union[str, "RecordState"] = None
    assigner_short_name: Optional[str] = None
    serial: Optional[int] = None
    date_updated: Optional[str] = None
    date_reserved: Optional[str] = None
    requester_user_id: Optional[str] = None
    date_published: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.record_cve_id):
            self.MissingRequiredField("record_cve_id")
        if not isinstance(self.record_cve_id, str):
            self.record_cve_id = str(self.record_cve_id)

        if self._is_empty(self.assigner_org_id):
            self.MissingRequiredField("assigner_org_id")
        if not isinstance(self.assigner_org_id, str):
            self.assigner_org_id = str(self.assigner_org_id)

        if self._is_empty(self.published_state):
            self.MissingRequiredField("published_state")
        if not isinstance(self.published_state, RecordState):
            self.published_state = RecordState(self.published_state)

        if self.assigner_short_name is not None and not isinstance(self.assigner_short_name, str):
            self.assigner_short_name = str(self.assigner_short_name)

        if self.serial is not None and not isinstance(self.serial, int):
            self.serial = int(self.serial)

        if self.date_updated is not None and not isinstance(self.date_updated, str):
            self.date_updated = str(self.date_updated)

        if self.date_reserved is not None and not isinstance(self.date_reserved, str):
            self.date_reserved = str(self.date_reserved)

        if self.requester_user_id is not None and not isinstance(self.requester_user_id, str):
            self.requester_user_id = str(self.requester_user_id)

        if self.date_published is not None and not isinstance(self.date_published, str):
            self.date_published = str(self.date_published)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveMetadataRejected(CveMetadata):
    """
    Metadata for a CVE Record in the REJECTED state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetadataRejected"]
    class_class_curie: ClassVar[str] = "cve:CveMetadataRejected"
    class_name: ClassVar[str] = "CveMetadataRejected"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetadataRejected

    record_cve_id: str = None
    assigner_org_id: str = None
    rejected_state: Union[str, "RecordState"] = None
    assigner_short_name: Optional[str] = None
    serial: Optional[int] = None
    date_updated: Optional[str] = None
    date_reserved: Optional[str] = None
    date_published: Optional[str] = None
    date_rejected: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.record_cve_id):
            self.MissingRequiredField("record_cve_id")
        if not isinstance(self.record_cve_id, str):
            self.record_cve_id = str(self.record_cve_id)

        if self._is_empty(self.assigner_org_id):
            self.MissingRequiredField("assigner_org_id")
        if not isinstance(self.assigner_org_id, str):
            self.assigner_org_id = str(self.assigner_org_id)

        if self._is_empty(self.rejected_state):
            self.MissingRequiredField("rejected_state")
        if not isinstance(self.rejected_state, RecordState):
            self.rejected_state = RecordState(self.rejected_state)

        if self.assigner_short_name is not None and not isinstance(self.assigner_short_name, str):
            self.assigner_short_name = str(self.assigner_short_name)

        if self.serial is not None and not isinstance(self.serial, int):
            self.serial = int(self.serial)

        if self.date_updated is not None and not isinstance(self.date_updated, str):
            self.date_updated = str(self.date_updated)

        if self.date_reserved is not None and not isinstance(self.date_reserved, str):
            self.date_reserved = str(self.date_reserved)

        if self.date_published is not None and not isinstance(self.date_published, str):
            self.date_published = str(self.date_published)

        if self.date_rejected is not None and not isinstance(self.date_rejected, str):
            self.date_rejected = str(self.date_rejected)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Containers(YAMLRoot):
    """
    A set of structures (called containers) used to store vulnerability information related to a specific CVE ID. At
    minimum a 'cna' container is required.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["Containers"]
    class_class_curie: ClassVar[str] = "cve:Containers"
    class_name: ClassVar[str] = "Containers"
    class_model_uri: ClassVar[URIRef] = CVE.Containers

    cna: Union[dict, "CnaContainer"] = None
    adp: Optional[Union[Union[dict, "AdpContainer"], list[Union[dict, "AdpContainer"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cna):
            self.MissingRequiredField("cna")
        if not isinstance(self.cna, CnaContainer):
            self.cna = CnaContainer()

        if not isinstance(self.adp, list):
            self.adp = [self.adp] if self.adp is not None else []
        self.adp = [v if isinstance(v, AdpContainer) else AdpContainer(**as_dict(v)) for v in self.adp]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProviderMetadata(YAMLRoot):
    """
    Details related to the information container provider (CNA or ADP).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["ProviderMetadata"]
    class_class_curie: ClassVar[str] = "cve:ProviderMetadata"
    class_name: ClassVar[str] = "ProviderMetadata"
    class_model_uri: ClassVar[URIRef] = CVE.ProviderMetadata

    org_id: str = None
    short_name: Optional[str] = None
    date_updated: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.org_id):
            self.MissingRequiredField("org_id")
        if not isinstance(self.org_id, str):
            self.org_id = str(self.org_id)

        if self.short_name is not None and not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self.date_updated is not None and not isinstance(self.date_updated, str):
            self.date_updated = str(self.date_updated)

        super().__post_init__(**kwargs)


class CnaContainer(YAMLRoot):
    """
    Abstract base for CNA containers (published and rejected).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CnaContainer"]
    class_class_curie: ClassVar[str] = "cve:CnaContainer"
    class_name: ClassVar[str] = "CnaContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CnaContainer


@dataclass(repr=False)
class CnaPublishedContainer(CnaContainer):
    """
    An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a published CVE ID.
    There can only be one CNA container per CVE record since there can only be one assigning CNA.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CnaPublishedContainer"]
    class_class_curie: ClassVar[str] = "cve:CnaPublishedContainer"
    class_name: ClassVar[str] = "CnaPublishedContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CnaPublishedContainer

    provider_metadata: Union[dict, ProviderMetadata] = None
    descriptions: Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]] = None
    affected: Union[Union[dict, "AffectedProduct"], list[Union[dict, "AffectedProduct"]]] = None
    cve_references: Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]] = None
    date_assigned: Optional[str] = None
    date_public: Optional[str] = None
    title: Optional[str] = None
    cpe_applicability: Optional[Union[Union[dict, "CpeApplicabilityElement"], list[Union[dict, "CpeApplicabilityElement"]]]] = empty_list()
    problem_types: Optional[Union[Union[dict, "ProblemType"], list[Union[dict, "ProblemType"]]]] = empty_list()
    impacts: Optional[Union[Union[dict, "ImpactEntry"], list[Union[dict, "ImpactEntry"]]]] = empty_list()
    metrics: Optional[Union[Union[dict, "MetricEntry"], list[Union[dict, "MetricEntry"]]]] = empty_list()
    configurations_text: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    workarounds: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    solutions: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    exploits: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    timeline: Optional[Union[Union[dict, "TimelineEntry"], list[Union[dict, "TimelineEntry"]]]] = empty_list()
    credits: Optional[Union[Union[dict, "CreditEntry"], list[Union[dict, "CreditEntry"]]]] = empty_list()
    cna_source: Optional[Union[dict, "SourceInformation"]] = None
    cna_tags: Optional[Union[str, list[str]]] = empty_list()
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.provider_metadata):
            self.MissingRequiredField("provider_metadata")
        if not isinstance(self.provider_metadata, ProviderMetadata):
            self.provider_metadata = ProviderMetadata(**as_dict(self.provider_metadata))

        if self._is_empty(self.descriptions):
            self.MissingRequiredField("descriptions")
        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        if self._is_empty(self.affected):
            self.MissingRequiredField("affected")
        if not isinstance(self.affected, list):
            self.affected = [self.affected] if self.affected is not None else []
        self.affected = [v if isinstance(v, AffectedProduct) else AffectedProduct(**as_dict(v)) for v in self.affected]

        if self._is_empty(self.cve_references):
            self.MissingRequiredField("cve_references")
        self._normalize_inlined_as_list(slot_name="cve_references", slot_type=CveReference, key_name="url", keyed=False)

        if self.date_assigned is not None and not isinstance(self.date_assigned, str):
            self.date_assigned = str(self.date_assigned)

        if self.date_public is not None and not isinstance(self.date_public, str):
            self.date_public = str(self.date_public)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.cpe_applicability, list):
            self.cpe_applicability = [self.cpe_applicability] if self.cpe_applicability is not None else []
        self.cpe_applicability = [v if isinstance(v, CpeApplicabilityElement) else CpeApplicabilityElement(**as_dict(v)) for v in self.cpe_applicability]

        if not isinstance(self.problem_types, list):
            self.problem_types = [self.problem_types] if self.problem_types is not None else []
        self.problem_types = [v if isinstance(v, ProblemType) else ProblemType(**as_dict(v)) for v in self.problem_types]

        if not isinstance(self.impacts, list):
            self.impacts = [self.impacts] if self.impacts is not None else []
        self.impacts = [v if isinstance(v, ImpactEntry) else ImpactEntry(**as_dict(v)) for v in self.impacts]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, MetricEntry) else MetricEntry(**as_dict(v)) for v in self.metrics]

        self._normalize_inlined_as_list(slot_name="configurations_text", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="workarounds", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="solutions", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="exploits", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="timeline", slot_type=TimelineEntry, key_name="event_time", keyed=False)

        self._normalize_inlined_as_list(slot_name="credits", slot_type=CreditEntry, key_name="lang", keyed=False)

        if self.cna_source is not None and not isinstance(self.cna_source, SourceInformation):
            self.cna_source = SourceInformation(**as_dict(self.cna_source))

        if not isinstance(self.cna_tags, list):
            self.cna_tags = [self.cna_tags] if self.cna_tags is not None else []
        self.cna_tags = [v if isinstance(v, str) else str(v) for v in self.cna_tags]

        self._normalize_inlined_as_list(slot_name="taxonomy_mappings", slot_type=TaxonomyMapping, key_name="taxonomy_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CnaRejectedContainer(CnaContainer):
    """
    An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a rejected CVE ID.
    There can only be one CNA container per CVE record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CnaRejectedContainer"]
    class_class_curie: ClassVar[str] = "cve:CnaRejectedContainer"
    class_name: ClassVar[str] = "CnaRejectedContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CnaRejectedContainer

    provider_metadata: Union[dict, ProviderMetadata] = None
    rejected_reasons: Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]] = None
    replaced_by: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.provider_metadata):
            self.MissingRequiredField("provider_metadata")
        if not isinstance(self.provider_metadata, ProviderMetadata):
            self.provider_metadata = ProviderMetadata(**as_dict(self.provider_metadata))

        if self._is_empty(self.rejected_reasons):
            self.MissingRequiredField("rejected_reasons")
        self._normalize_inlined_as_list(slot_name="rejected_reasons", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        if not isinstance(self.replaced_by, list):
            self.replaced_by = [self.replaced_by] if self.replaced_by is not None else []
        self.replaced_by = [v if isinstance(v, str) else str(v) for v in self.replaced_by]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AdpContainer(YAMLRoot):
    """
    An object containing vulnerability information provided by an Authorized Data Publisher (ADP). Multiple ADPs can
    provide containers for a single CVE ID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["AdpContainer"]
    class_class_curie: ClassVar[str] = "cve:AdpContainer"
    class_name: ClassVar[str] = "AdpContainer"
    class_model_uri: ClassVar[URIRef] = CVE.AdpContainer

    provider_metadata: Union[dict, ProviderMetadata] = None
    date_public: Optional[str] = None
    title: Optional[str] = None
    descriptions: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    affected: Optional[Union[Union[dict, "AffectedProduct"], list[Union[dict, "AffectedProduct"]]]] = empty_list()
    cpe_applicability: Optional[Union[Union[dict, "CpeApplicabilityElement"], list[Union[dict, "CpeApplicabilityElement"]]]] = empty_list()
    problem_types: Optional[Union[Union[dict, "ProblemType"], list[Union[dict, "ProblemType"]]]] = empty_list()
    cve_references: Optional[Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]]] = empty_list()
    impacts: Optional[Union[Union[dict, "ImpactEntry"], list[Union[dict, "ImpactEntry"]]]] = empty_list()
    metrics: Optional[Union[Union[dict, "MetricEntry"], list[Union[dict, "MetricEntry"]]]] = empty_list()
    configurations_text: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    workarounds: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    solutions: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    exploits: Optional[Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]]] = empty_list()
    timeline: Optional[Union[Union[dict, "TimelineEntry"], list[Union[dict, "TimelineEntry"]]]] = empty_list()
    credits: Optional[Union[Union[dict, "CreditEntry"], list[Union[dict, "CreditEntry"]]]] = empty_list()
    cna_source: Optional[Union[dict, "SourceInformation"]] = None
    adp_tags: Optional[Union[str, list[str]]] = empty_list()
    taxonomy_mappings: Optional[Union[Union[dict, "TaxonomyMapping"], list[Union[dict, "TaxonomyMapping"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.provider_metadata):
            self.MissingRequiredField("provider_metadata")
        if not isinstance(self.provider_metadata, ProviderMetadata):
            self.provider_metadata = ProviderMetadata(**as_dict(self.provider_metadata))

        if self.date_public is not None and not isinstance(self.date_public, str):
            self.date_public = str(self.date_public)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        if not isinstance(self.affected, list):
            self.affected = [self.affected] if self.affected is not None else []
        self.affected = [v if isinstance(v, AffectedProduct) else AffectedProduct(**as_dict(v)) for v in self.affected]

        if not isinstance(self.cpe_applicability, list):
            self.cpe_applicability = [self.cpe_applicability] if self.cpe_applicability is not None else []
        self.cpe_applicability = [v if isinstance(v, CpeApplicabilityElement) else CpeApplicabilityElement(**as_dict(v)) for v in self.cpe_applicability]

        if not isinstance(self.problem_types, list):
            self.problem_types = [self.problem_types] if self.problem_types is not None else []
        self.problem_types = [v if isinstance(v, ProblemType) else ProblemType(**as_dict(v)) for v in self.problem_types]

        self._normalize_inlined_as_list(slot_name="cve_references", slot_type=CveReference, key_name="url", keyed=False)

        if not isinstance(self.impacts, list):
            self.impacts = [self.impacts] if self.impacts is not None else []
        self.impacts = [v if isinstance(v, ImpactEntry) else ImpactEntry(**as_dict(v)) for v in self.impacts]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, MetricEntry) else MetricEntry(**as_dict(v)) for v in self.metrics]

        self._normalize_inlined_as_list(slot_name="configurations_text", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="workarounds", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="solutions", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="exploits", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="timeline", slot_type=TimelineEntry, key_name="event_time", keyed=False)

        self._normalize_inlined_as_list(slot_name="credits", slot_type=CreditEntry, key_name="lang", keyed=False)

        if self.cna_source is not None and not isinstance(self.cna_source, SourceInformation):
            self.cna_source = SourceInformation(**as_dict(self.cna_source))

        if not isinstance(self.adp_tags, list):
            self.adp_tags = [self.adp_tags] if self.adp_tags is not None else []
        self.adp_tags = [v if isinstance(v, str) else str(v) for v in self.adp_tags]

        self._normalize_inlined_as_list(slot_name="taxonomy_mappings", slot_type=TaxonomyMapping, key_name="taxonomy_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProgramRoutine(YAMLRoot):
    """
    An affected source code function, method, subroutine, or procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["ProgramRoutine"]
    class_class_curie: ClassVar[str] = "cve:ProgramRoutine"
    class_name: ClassVar[str] = "ProgramRoutine"
    class_model_uri: ClassVar[URIRef] = CVE.ProgramRoutine

    routine_name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.routine_name):
            self.MissingRequiredField("routine_name")
        if not isinstance(self.routine_name, str):
            self.routine_name = str(self.routine_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VersionEntry(YAMLRoot):
    """
    A single version or a range of versions of a product with associated vulnerability status. An entry with only
    version and status is a point version; an entry with versionType and a less-than limit describes a range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["VersionEntry"]
    class_class_curie: ClassVar[str] = "cve:VersionEntry"
    class_name: ClassVar[str] = "VersionEntry"
    class_model_uri: ClassVar[URIRef] = CVE.VersionEntry

    version_value: str = None
    version_status: Union[str, "VersionStatus"] = None
    version_type: Optional[str] = None
    less_than: Optional[str] = None
    less_than_or_equal: Optional[str] = None
    version_changes: Optional[Union[Union[dict, "VersionChange"], list[Union[dict, "VersionChange"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version_value):
            self.MissingRequiredField("version_value")
        if not isinstance(self.version_value, str):
            self.version_value = str(self.version_value)

        if self._is_empty(self.version_status):
            self.MissingRequiredField("version_status")
        if not isinstance(self.version_status, VersionStatus):
            self.version_status = VersionStatus(self.version_status)

        if self.version_type is not None and not isinstance(self.version_type, str):
            self.version_type = str(self.version_type)

        if self.less_than is not None and not isinstance(self.less_than, str):
            self.less_than = str(self.less_than)

        if self.less_than_or_equal is not None and not isinstance(self.less_than_or_equal, str):
            self.less_than_or_equal = str(self.less_than_or_equal)

        self._normalize_inlined_as_list(slot_name="version_changes", slot_type=VersionChange, key_name="change_at", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VersionChange(YAMLRoot):
    """
    A status change that takes place at a specific point within a version range.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["VersionChange"]
    class_class_curie: ClassVar[str] = "cve:VersionChange"
    class_name: ClassVar[str] = "VersionChange"
    class_model_uri: ClassVar[URIRef] = CVE.VersionChange

    change_at: str = None
    change_status: Union[str, "VersionStatus"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.change_at):
            self.MissingRequiredField("change_at")
        if not isinstance(self.change_at, str):
            self.change_at = str(self.change_at)

        if self._is_empty(self.change_status):
            self.MissingRequiredField("change_status")
        if not isinstance(self.change_status, VersionStatus):
            self.change_status = VersionStatus(self.change_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiLangDescription(YAMLRoot):
    """
    Text in a particular language with optional alternate markup or formatted representation (e.g., Markdown) or
    embedded media. Used for vulnerability descriptions, rejected reasons, configurations, workarounds, solutions, and
    exploits.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["MultiLangDescription"]
    class_class_curie: ClassVar[str] = "cve:MultiLangDescription"
    class_name: ClassVar[str] = "MultiLangDescription"
    class_model_uri: ClassVar[URIRef] = CVE.MultiLangDescription

    description_value: str = None
    lang: str = "en"
    supporting_media: Optional[Union[Union[dict, "SupportingMedia"], list[Union[dict, "SupportingMedia"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.description_value):
            self.MissingRequiredField("description_value")
        if not isinstance(self.description_value, str):
            self.description_value = str(self.description_value)

        self._normalize_inlined_as_list(slot_name="supporting_media", slot_type=SupportingMedia, key_name="media_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportingMedia(YAMLRoot):
    """
    Supporting media data for a description such as markdown, diagrams, etc. Similar to RFC 2397, each media object
    has a media type, data value, and an optional base64 flag.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["SupportingMedia"]
    class_class_curie: ClassVar[str] = "cve:SupportingMedia"
    class_name: ClassVar[str] = "SupportingMedia"
    class_model_uri: ClassVar[URIRef] = CVE.SupportingMedia

    media_type: str = None
    media_value: str = None
    base64_encoded: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.media_type):
            self.MissingRequiredField("media_type")
        if not isinstance(self.media_type, str):
            self.media_type = str(self.media_type)

        if self._is_empty(self.media_value):
            self.MissingRequiredField("media_value")
        if not isinstance(self.media_value, str):
            self.media_value = str(self.media_value)

        if self.base64_encoded is not None and not isinstance(self.base64_encoded, Bool):
            self.base64_encoded = Bool(self.base64_encoded)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProblemType(YAMLRoot):
    """
    Problem type information (e.g., CWE identifier). Wraps one or more problem type descriptions. The CNA requirement
    is [PROBLEMTYPE].
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["ProblemType"]
    class_class_curie: ClassVar[str] = "cve:ProblemType"
    class_name: ClassVar[str] = "ProblemType"
    class_model_uri: ClassVar[URIRef] = CVE.ProblemType

    problem_type_descriptions: Union[Union[dict, "ProblemTypeDescription"], list[Union[dict, "ProblemTypeDescription"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.problem_type_descriptions):
            self.MissingRequiredField("problem_type_descriptions")
        self._normalize_inlined_as_list(slot_name="problem_type_descriptions", slot_type=ProblemTypeDescription, key_name="lang", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProblemTypeDescription(YAMLRoot):
    """
    Individual problem type description entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["ProblemTypeDescription"]
    class_class_curie: ClassVar[str] = "cve:ProblemTypeDescription"
    class_name: ClassVar[str] = "ProblemTypeDescription"
    class_model_uri: ClassVar[URIRef] = CVE.ProblemTypeDescription

    problem_description: str = None
    lang: str = "en"
    cwe_id: Optional[str] = None
    problem_source_type: Optional[str] = None
    problem_references: Optional[Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.problem_description):
            self.MissingRequiredField("problem_description")
        if not isinstance(self.problem_description, str):
            self.problem_description = str(self.problem_description)

        if self.cwe_id is not None and not isinstance(self.cwe_id, str):
            self.cwe_id = str(self.cwe_id)

        if self.problem_source_type is not None and not isinstance(self.problem_source_type, str):
            self.problem_source_type = str(self.problem_source_type)

        self._normalize_inlined_as_list(slot_name="problem_references", slot_type=CveReference, key_name="url", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImpactEntry(YAMLRoot):
    """
    An impact entry linking an optional CAPEC attack pattern ID to one or more prose descriptions of the impact
    scenario.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["ImpactEntry"]
    class_class_curie: ClassVar[str] = "cve:ImpactEntry"
    class_name: ClassVar[str] = "ImpactEntry"
    class_model_uri: ClassVar[URIRef] = CVE.ImpactEntry

    impact_descriptions: Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]] = None
    capec_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.impact_descriptions):
            self.MissingRequiredField("impact_descriptions")
        self._normalize_inlined_as_list(slot_name="impact_descriptions", slot_type=MultiLangDescription, key_name="lang", keyed=False)

        if self.capec_id is not None and not isinstance(self.capec_id, str):
            self.capec_id = str(self.capec_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetricEntry(YAMLRoot):
    """
    A metric entry containing scoring data in one of the CVSS formats (v4.0, v3.x, v2.0) or a custom format, with
    optional applicability scenarios. At least one of cvss_v4_0, cvss_v3, cvss_v2_0, or other_metric is required. CVSS
    3.0 and 3.1 are both represented by CvssV3 (distinguished by the cvss3_version slot).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["MetricEntry"]
    class_class_curie: ClassVar[str] = "cve:MetricEntry"
    class_name: ClassVar[str] = "MetricEntry"
    class_model_uri: ClassVar[URIRef] = CVE.MetricEntry

    metric_format: Optional[str] = None
    metric_scenarios: Optional[Union[Union[dict, "MetricScenario"], list[Union[dict, "MetricScenario"]]]] = empty_list()
    cvss_v4_0: Optional[Union[dict, "CvssV40"]] = None
    cvss_v3: Optional[Union[dict, "CvssV3"]] = None
    cvss_v2_0: Optional[Union[dict, "CvssV20"]] = None
    other_metric: Optional[Union[dict, "OtherMetric"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.metric_format is not None and not isinstance(self.metric_format, str):
            self.metric_format = str(self.metric_format)

        self._normalize_inlined_as_list(slot_name="metric_scenarios", slot_type=MetricScenario, key_name="lang", keyed=False)

        if self.cvss_v4_0 is not None and not isinstance(self.cvss_v4_0, CvssV40):
            self.cvss_v4_0 = CvssV40(**as_dict(self.cvss_v4_0))

        if self.cvss_v3 is not None and not isinstance(self.cvss_v3, CvssV3):
            self.cvss_v3 = CvssV3(**as_dict(self.cvss_v3))

        if self.cvss_v2_0 is not None and not isinstance(self.cvss_v2_0, CvssV20):
            self.cvss_v2_0 = CvssV20(**as_dict(self.cvss_v2_0))

        if self.other_metric is not None and not isinstance(self.other_metric, OtherMetric):
            self.other_metric = OtherMetric(**as_dict(self.other_metric))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MetricScenario(YAMLRoot):
    """
    A scenario description indicating the context in which a metric applies. If no specific scenario is given, GENERAL
    is used as the default.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["MetricScenario"]
    class_class_curie: ClassVar[str] = "cve:MetricScenario"
    class_name: ClassVar[str] = "MetricScenario"
    class_model_uri: ClassVar[URIRef] = CVE.MetricScenario

    lang: str = "en"
    scenario_value: str = "GENERAL"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.scenario_value):
            self.MissingRequiredField("scenario_value")
        if not isinstance(self.scenario_value, str):
            self.scenario_value = str(self.scenario_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV40(YAMLRoot):
    """
    CVSS version 4.0 scoring object. Requires version, vectorString, baseScore, and baseSeverity. All other fields are
    optional.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV40"]
    class_class_curie: ClassVar[str] = "cve:CvssV40"
    class_name: ClassVar[str] = "CvssV4_0"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV40

    cvss4_version: str = None
    cvss4_vector_string: str = None
    cvss4_base_score: float = None
    cvss4_base_severity: Union[str, "Cvss4Severity"] = None
    cvss4_attack_vector: Optional[Union[str, "Cvss4AttackVector"]] = None
    cvss4_attack_complexity: Optional[Union[str, "Cvss4AttackComplexity"]] = None
    cvss4_attack_requirements: Optional[Union[str, "Cvss4AttackRequirements"]] = None
    cvss4_privileges_required: Optional[Union[str, "Cvss4PrivilegesRequired"]] = None
    cvss4_user_interaction: Optional[Union[str, "Cvss4UserInteraction"]] = None
    cvss4_vuln_confidentiality_impact: Optional[Union[str, "Cvss4VulnCia"]] = None
    cvss4_vuln_integrity_impact: Optional[Union[str, "Cvss4VulnCia"]] = None
    cvss4_vuln_availability_impact: Optional[Union[str, "Cvss4VulnCia"]] = None
    cvss4_sub_confidentiality_impact: Optional[Union[str, "Cvss4SubCia"]] = None
    cvss4_sub_integrity_impact: Optional[Union[str, "Cvss4SubCia"]] = None
    cvss4_sub_availability_impact: Optional[Union[str, "Cvss4SubCia"]] = None
    cvss4_exploit_maturity: Optional[Union[str, "Cvss4ExploitMaturity"]] = None
    cvss4_confidentiality_requirement: Optional[Union[str, "Cvss4CiaRequirement"]] = None
    cvss4_integrity_requirement: Optional[Union[str, "Cvss4CiaRequirement"]] = None
    cvss4_availability_requirement: Optional[Union[str, "Cvss4CiaRequirement"]] = None
    cvss4_modified_attack_vector: Optional[Union[str, "Cvss4ModifiedAttackVector"]] = None
    cvss4_modified_attack_complexity: Optional[Union[str, "Cvss4ModifiedAttackComplexity"]] = None
    cvss4_modified_attack_requirements: Optional[Union[str, "Cvss4ModifiedAttackRequirements"]] = None
    cvss4_modified_privileges_required: Optional[Union[str, "Cvss4ModifiedPrivilegesRequired"]] = None
    cvss4_modified_user_interaction: Optional[Union[str, "Cvss4ModifiedUserInteraction"]] = None
    cvss4_modified_vuln_confidentiality_impact: Optional[Union[str, "Cvss4ModifiedVulnCia"]] = None
    cvss4_modified_vuln_integrity_impact: Optional[Union[str, "Cvss4ModifiedVulnCia"]] = None
    cvss4_modified_vuln_availability_impact: Optional[Union[str, "Cvss4ModifiedVulnCia"]] = None
    cvss4_modified_sub_confidentiality_impact: Optional[Union[str, "Cvss4ModifiedSubC"]] = None
    cvss4_modified_sub_integrity_impact: Optional[Union[str, "Cvss4ModifiedSubIa"]] = None
    cvss4_modified_sub_availability_impact: Optional[Union[str, "Cvss4ModifiedSubIa"]] = None
    cvss4_safety: Optional[Union[str, "Cvss4Safety"]] = None
    cvss4_automatable: Optional[Union[str, "Cvss4Automatable"]] = None
    cvss4_recovery: Optional[Union[str, "Cvss4Recovery"]] = None
    cvss4_value_density: Optional[Union[str, "Cvss4ValueDensity"]] = None
    cvss4_vulnerability_response_effort: Optional[Union[str, "Cvss4VulnerabilityResponseEffort"]] = None
    cvss4_provider_urgency: Optional[Union[str, "Cvss4ProviderUrgency"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cvss4_version):
            self.MissingRequiredField("cvss4_version")
        if not isinstance(self.cvss4_version, str):
            self.cvss4_version = str(self.cvss4_version)

        if self._is_empty(self.cvss4_vector_string):
            self.MissingRequiredField("cvss4_vector_string")
        if not isinstance(self.cvss4_vector_string, str):
            self.cvss4_vector_string = str(self.cvss4_vector_string)

        if self._is_empty(self.cvss4_base_score):
            self.MissingRequiredField("cvss4_base_score")
        if not isinstance(self.cvss4_base_score, float):
            self.cvss4_base_score = float(self.cvss4_base_score)

        if self._is_empty(self.cvss4_base_severity):
            self.MissingRequiredField("cvss4_base_severity")
        if not isinstance(self.cvss4_base_severity, Cvss4Severity):
            self.cvss4_base_severity = Cvss4Severity(self.cvss4_base_severity)

        if self.cvss4_attack_vector is not None and not isinstance(self.cvss4_attack_vector, Cvss4AttackVector):
            self.cvss4_attack_vector = Cvss4AttackVector(self.cvss4_attack_vector)

        if self.cvss4_attack_complexity is not None and not isinstance(self.cvss4_attack_complexity, Cvss4AttackComplexity):
            self.cvss4_attack_complexity = Cvss4AttackComplexity(self.cvss4_attack_complexity)

        if self.cvss4_attack_requirements is not None and not isinstance(self.cvss4_attack_requirements, Cvss4AttackRequirements):
            self.cvss4_attack_requirements = Cvss4AttackRequirements(self.cvss4_attack_requirements)

        if self.cvss4_privileges_required is not None and not isinstance(self.cvss4_privileges_required, Cvss4PrivilegesRequired):
            self.cvss4_privileges_required = Cvss4PrivilegesRequired(self.cvss4_privileges_required)

        if self.cvss4_user_interaction is not None and not isinstance(self.cvss4_user_interaction, Cvss4UserInteraction):
            self.cvss4_user_interaction = Cvss4UserInteraction(self.cvss4_user_interaction)

        if self.cvss4_vuln_confidentiality_impact is not None and not isinstance(self.cvss4_vuln_confidentiality_impact, Cvss4VulnCia):
            self.cvss4_vuln_confidentiality_impact = Cvss4VulnCia(self.cvss4_vuln_confidentiality_impact)

        if self.cvss4_vuln_integrity_impact is not None and not isinstance(self.cvss4_vuln_integrity_impact, Cvss4VulnCia):
            self.cvss4_vuln_integrity_impact = Cvss4VulnCia(self.cvss4_vuln_integrity_impact)

        if self.cvss4_vuln_availability_impact is not None and not isinstance(self.cvss4_vuln_availability_impact, Cvss4VulnCia):
            self.cvss4_vuln_availability_impact = Cvss4VulnCia(self.cvss4_vuln_availability_impact)

        if self.cvss4_sub_confidentiality_impact is not None and not isinstance(self.cvss4_sub_confidentiality_impact, Cvss4SubCia):
            self.cvss4_sub_confidentiality_impact = Cvss4SubCia(self.cvss4_sub_confidentiality_impact)

        if self.cvss4_sub_integrity_impact is not None and not isinstance(self.cvss4_sub_integrity_impact, Cvss4SubCia):
            self.cvss4_sub_integrity_impact = Cvss4SubCia(self.cvss4_sub_integrity_impact)

        if self.cvss4_sub_availability_impact is not None and not isinstance(self.cvss4_sub_availability_impact, Cvss4SubCia):
            self.cvss4_sub_availability_impact = Cvss4SubCia(self.cvss4_sub_availability_impact)

        if self.cvss4_exploit_maturity is not None and not isinstance(self.cvss4_exploit_maturity, Cvss4ExploitMaturity):
            self.cvss4_exploit_maturity = Cvss4ExploitMaturity(self.cvss4_exploit_maturity)

        if self.cvss4_confidentiality_requirement is not None and not isinstance(self.cvss4_confidentiality_requirement, Cvss4CiaRequirement):
            self.cvss4_confidentiality_requirement = Cvss4CiaRequirement(self.cvss4_confidentiality_requirement)

        if self.cvss4_integrity_requirement is not None and not isinstance(self.cvss4_integrity_requirement, Cvss4CiaRequirement):
            self.cvss4_integrity_requirement = Cvss4CiaRequirement(self.cvss4_integrity_requirement)

        if self.cvss4_availability_requirement is not None and not isinstance(self.cvss4_availability_requirement, Cvss4CiaRequirement):
            self.cvss4_availability_requirement = Cvss4CiaRequirement(self.cvss4_availability_requirement)

        if self.cvss4_modified_attack_vector is not None and not isinstance(self.cvss4_modified_attack_vector, Cvss4ModifiedAttackVector):
            self.cvss4_modified_attack_vector = Cvss4ModifiedAttackVector(self.cvss4_modified_attack_vector)

        if self.cvss4_modified_attack_complexity is not None and not isinstance(self.cvss4_modified_attack_complexity, Cvss4ModifiedAttackComplexity):
            self.cvss4_modified_attack_complexity = Cvss4ModifiedAttackComplexity(self.cvss4_modified_attack_complexity)

        if self.cvss4_modified_attack_requirements is not None and not isinstance(self.cvss4_modified_attack_requirements, Cvss4ModifiedAttackRequirements):
            self.cvss4_modified_attack_requirements = Cvss4ModifiedAttackRequirements(self.cvss4_modified_attack_requirements)

        if self.cvss4_modified_privileges_required is not None and not isinstance(self.cvss4_modified_privileges_required, Cvss4ModifiedPrivilegesRequired):
            self.cvss4_modified_privileges_required = Cvss4ModifiedPrivilegesRequired(self.cvss4_modified_privileges_required)

        if self.cvss4_modified_user_interaction is not None and not isinstance(self.cvss4_modified_user_interaction, Cvss4ModifiedUserInteraction):
            self.cvss4_modified_user_interaction = Cvss4ModifiedUserInteraction(self.cvss4_modified_user_interaction)

        if self.cvss4_modified_vuln_confidentiality_impact is not None and not isinstance(self.cvss4_modified_vuln_confidentiality_impact, Cvss4ModifiedVulnCia):
            self.cvss4_modified_vuln_confidentiality_impact = Cvss4ModifiedVulnCia(self.cvss4_modified_vuln_confidentiality_impact)

        if self.cvss4_modified_vuln_integrity_impact is not None and not isinstance(self.cvss4_modified_vuln_integrity_impact, Cvss4ModifiedVulnCia):
            self.cvss4_modified_vuln_integrity_impact = Cvss4ModifiedVulnCia(self.cvss4_modified_vuln_integrity_impact)

        if self.cvss4_modified_vuln_availability_impact is not None and not isinstance(self.cvss4_modified_vuln_availability_impact, Cvss4ModifiedVulnCia):
            self.cvss4_modified_vuln_availability_impact = Cvss4ModifiedVulnCia(self.cvss4_modified_vuln_availability_impact)

        if self.cvss4_modified_sub_confidentiality_impact is not None and not isinstance(self.cvss4_modified_sub_confidentiality_impact, Cvss4ModifiedSubC):
            self.cvss4_modified_sub_confidentiality_impact = Cvss4ModifiedSubC(self.cvss4_modified_sub_confidentiality_impact)

        if self.cvss4_modified_sub_integrity_impact is not None and not isinstance(self.cvss4_modified_sub_integrity_impact, Cvss4ModifiedSubIa):
            self.cvss4_modified_sub_integrity_impact = Cvss4ModifiedSubIa(self.cvss4_modified_sub_integrity_impact)

        if self.cvss4_modified_sub_availability_impact is not None and not isinstance(self.cvss4_modified_sub_availability_impact, Cvss4ModifiedSubIa):
            self.cvss4_modified_sub_availability_impact = Cvss4ModifiedSubIa(self.cvss4_modified_sub_availability_impact)

        if self.cvss4_safety is not None and not isinstance(self.cvss4_safety, Cvss4Safety):
            self.cvss4_safety = Cvss4Safety(self.cvss4_safety)

        if self.cvss4_automatable is not None and not isinstance(self.cvss4_automatable, Cvss4Automatable):
            self.cvss4_automatable = Cvss4Automatable(self.cvss4_automatable)

        if self.cvss4_recovery is not None and not isinstance(self.cvss4_recovery, Cvss4Recovery):
            self.cvss4_recovery = Cvss4Recovery(self.cvss4_recovery)

        if self.cvss4_value_density is not None and not isinstance(self.cvss4_value_density, Cvss4ValueDensity):
            self.cvss4_value_density = Cvss4ValueDensity(self.cvss4_value_density)

        if self.cvss4_vulnerability_response_effort is not None and not isinstance(self.cvss4_vulnerability_response_effort, Cvss4VulnerabilityResponseEffort):
            self.cvss4_vulnerability_response_effort = Cvss4VulnerabilityResponseEffort(self.cvss4_vulnerability_response_effort)

        if self.cvss4_provider_urgency is not None and not isinstance(self.cvss4_provider_urgency, Cvss4ProviderUrgency):
            self.cvss4_provider_urgency = Cvss4ProviderUrgency(self.cvss4_provider_urgency)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV3(YAMLRoot):
    """
    CVSS version 3.x scoring object covering both CVSS 3.0 and CVSS 3.1. The two versions share an identical metric
    model; the 3.1 spec was a clarification, not a structural change. The cvss3_version slot distinguishes between
    them. Requires version ('3.0' or '3.1'), vectorString, baseScore, and baseSeverity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV3"]
    class_class_curie: ClassVar[str] = "cve:CvssV3"
    class_name: ClassVar[str] = "CvssV3"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV3

    cvss3_version: Union[str, "CvssV3Version"] = None
    cvss3_vector_string: str = None
    cvss3_base_score: float = None
    cvss3_base_severity: Union[str, "Cvss3Severity"] = None
    cvss3_attack_vector: Optional[Union[str, "Cvss3AttackVector"]] = None
    cvss3_attack_complexity: Optional[Union[str, "Cvss3AttackComplexity"]] = None
    cvss3_privileges_required: Optional[Union[str, "Cvss3PrivilegesRequired"]] = None
    cvss3_user_interaction: Optional[Union[str, "Cvss3UserInteraction"]] = None
    cvss3_scope: Optional[Union[str, "Cvss3Scope"]] = None
    cvss3_confidentiality_impact: Optional[Union[str, "Cvss3Cia"]] = None
    cvss3_integrity_impact: Optional[Union[str, "Cvss3Cia"]] = None
    cvss3_availability_impact: Optional[Union[str, "Cvss3Cia"]] = None
    cvss3_exploit_code_maturity: Optional[Union[str, "Cvss3ExploitCodeMaturity"]] = None
    cvss3_remediation_level: Optional[Union[str, "Cvss3RemediationLevel"]] = None
    cvss3_report_confidence: Optional[Union[str, "Cvss3Confidence"]] = None
    cvss3_temporal_score: Optional[float] = None
    cvss3_temporal_severity: Optional[Union[str, "Cvss3Severity"]] = None
    cvss3_confidentiality_requirement: Optional[Union[str, "Cvss3CiaRequirement"]] = None
    cvss3_integrity_requirement: Optional[Union[str, "Cvss3CiaRequirement"]] = None
    cvss3_availability_requirement: Optional[Union[str, "Cvss3CiaRequirement"]] = None
    cvss3_modified_attack_vector: Optional[Union[str, "Cvss3ModifiedAttackVector"]] = None
    cvss3_modified_attack_complexity: Optional[Union[str, "Cvss3ModifiedAttackComplexity"]] = None
    cvss3_modified_privileges_required: Optional[Union[str, "Cvss3ModifiedPrivilegesRequired"]] = None
    cvss3_modified_user_interaction: Optional[Union[str, "Cvss3ModifiedUserInteraction"]] = None
    cvss3_modified_scope: Optional[Union[str, "Cvss3ModifiedScope"]] = None
    cvss3_modified_confidentiality_impact: Optional[Union[str, "Cvss3ModifiedCia"]] = None
    cvss3_modified_integrity_impact: Optional[Union[str, "Cvss3ModifiedCia"]] = None
    cvss3_modified_availability_impact: Optional[Union[str, "Cvss3ModifiedCia"]] = None
    cvss3_environmental_score: Optional[float] = None
    cvss3_environmental_severity: Optional[Union[str, "Cvss3Severity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cvss3_version):
            self.MissingRequiredField("cvss3_version")
        if not isinstance(self.cvss3_version, CvssV3Version):
            self.cvss3_version = CvssV3Version(self.cvss3_version)

        if self._is_empty(self.cvss3_vector_string):
            self.MissingRequiredField("cvss3_vector_string")
        if not isinstance(self.cvss3_vector_string, str):
            self.cvss3_vector_string = str(self.cvss3_vector_string)

        if self._is_empty(self.cvss3_base_score):
            self.MissingRequiredField("cvss3_base_score")
        if not isinstance(self.cvss3_base_score, float):
            self.cvss3_base_score = float(self.cvss3_base_score)

        if self._is_empty(self.cvss3_base_severity):
            self.MissingRequiredField("cvss3_base_severity")
        if not isinstance(self.cvss3_base_severity, Cvss3Severity):
            self.cvss3_base_severity = Cvss3Severity(self.cvss3_base_severity)

        if self.cvss3_attack_vector is not None and not isinstance(self.cvss3_attack_vector, Cvss3AttackVector):
            self.cvss3_attack_vector = Cvss3AttackVector(self.cvss3_attack_vector)

        if self.cvss3_attack_complexity is not None and not isinstance(self.cvss3_attack_complexity, Cvss3AttackComplexity):
            self.cvss3_attack_complexity = Cvss3AttackComplexity(self.cvss3_attack_complexity)

        if self.cvss3_privileges_required is not None and not isinstance(self.cvss3_privileges_required, Cvss3PrivilegesRequired):
            self.cvss3_privileges_required = Cvss3PrivilegesRequired(self.cvss3_privileges_required)

        if self.cvss3_user_interaction is not None and not isinstance(self.cvss3_user_interaction, Cvss3UserInteraction):
            self.cvss3_user_interaction = Cvss3UserInteraction(self.cvss3_user_interaction)

        if self.cvss3_scope is not None and not isinstance(self.cvss3_scope, Cvss3Scope):
            self.cvss3_scope = Cvss3Scope(self.cvss3_scope)

        if self.cvss3_confidentiality_impact is not None and not isinstance(self.cvss3_confidentiality_impact, Cvss3Cia):
            self.cvss3_confidentiality_impact = Cvss3Cia(self.cvss3_confidentiality_impact)

        if self.cvss3_integrity_impact is not None and not isinstance(self.cvss3_integrity_impact, Cvss3Cia):
            self.cvss3_integrity_impact = Cvss3Cia(self.cvss3_integrity_impact)

        if self.cvss3_availability_impact is not None and not isinstance(self.cvss3_availability_impact, Cvss3Cia):
            self.cvss3_availability_impact = Cvss3Cia(self.cvss3_availability_impact)

        if self.cvss3_exploit_code_maturity is not None and not isinstance(self.cvss3_exploit_code_maturity, Cvss3ExploitCodeMaturity):
            self.cvss3_exploit_code_maturity = Cvss3ExploitCodeMaturity(self.cvss3_exploit_code_maturity)

        if self.cvss3_remediation_level is not None and not isinstance(self.cvss3_remediation_level, Cvss3RemediationLevel):
            self.cvss3_remediation_level = Cvss3RemediationLevel(self.cvss3_remediation_level)

        if self.cvss3_report_confidence is not None and not isinstance(self.cvss3_report_confidence, Cvss3Confidence):
            self.cvss3_report_confidence = Cvss3Confidence(self.cvss3_report_confidence)

        if self.cvss3_temporal_score is not None and not isinstance(self.cvss3_temporal_score, float):
            self.cvss3_temporal_score = float(self.cvss3_temporal_score)

        if self.cvss3_temporal_severity is not None and not isinstance(self.cvss3_temporal_severity, Cvss3Severity):
            self.cvss3_temporal_severity = Cvss3Severity(self.cvss3_temporal_severity)

        if self.cvss3_confidentiality_requirement is not None and not isinstance(self.cvss3_confidentiality_requirement, Cvss3CiaRequirement):
            self.cvss3_confidentiality_requirement = Cvss3CiaRequirement(self.cvss3_confidentiality_requirement)

        if self.cvss3_integrity_requirement is not None and not isinstance(self.cvss3_integrity_requirement, Cvss3CiaRequirement):
            self.cvss3_integrity_requirement = Cvss3CiaRequirement(self.cvss3_integrity_requirement)

        if self.cvss3_availability_requirement is not None and not isinstance(self.cvss3_availability_requirement, Cvss3CiaRequirement):
            self.cvss3_availability_requirement = Cvss3CiaRequirement(self.cvss3_availability_requirement)

        if self.cvss3_modified_attack_vector is not None and not isinstance(self.cvss3_modified_attack_vector, Cvss3ModifiedAttackVector):
            self.cvss3_modified_attack_vector = Cvss3ModifiedAttackVector(self.cvss3_modified_attack_vector)

        if self.cvss3_modified_attack_complexity is not None and not isinstance(self.cvss3_modified_attack_complexity, Cvss3ModifiedAttackComplexity):
            self.cvss3_modified_attack_complexity = Cvss3ModifiedAttackComplexity(self.cvss3_modified_attack_complexity)

        if self.cvss3_modified_privileges_required is not None and not isinstance(self.cvss3_modified_privileges_required, Cvss3ModifiedPrivilegesRequired):
            self.cvss3_modified_privileges_required = Cvss3ModifiedPrivilegesRequired(self.cvss3_modified_privileges_required)

        if self.cvss3_modified_user_interaction is not None and not isinstance(self.cvss3_modified_user_interaction, Cvss3ModifiedUserInteraction):
            self.cvss3_modified_user_interaction = Cvss3ModifiedUserInteraction(self.cvss3_modified_user_interaction)

        if self.cvss3_modified_scope is not None and not isinstance(self.cvss3_modified_scope, Cvss3ModifiedScope):
            self.cvss3_modified_scope = Cvss3ModifiedScope(self.cvss3_modified_scope)

        if self.cvss3_modified_confidentiality_impact is not None and not isinstance(self.cvss3_modified_confidentiality_impact, Cvss3ModifiedCia):
            self.cvss3_modified_confidentiality_impact = Cvss3ModifiedCia(self.cvss3_modified_confidentiality_impact)

        if self.cvss3_modified_integrity_impact is not None and not isinstance(self.cvss3_modified_integrity_impact, Cvss3ModifiedCia):
            self.cvss3_modified_integrity_impact = Cvss3ModifiedCia(self.cvss3_modified_integrity_impact)

        if self.cvss3_modified_availability_impact is not None and not isinstance(self.cvss3_modified_availability_impact, Cvss3ModifiedCia):
            self.cvss3_modified_availability_impact = Cvss3ModifiedCia(self.cvss3_modified_availability_impact)

        if self.cvss3_environmental_score is not None and not isinstance(self.cvss3_environmental_score, float):
            self.cvss3_environmental_score = float(self.cvss3_environmental_score)

        if self.cvss3_environmental_severity is not None and not isinstance(self.cvss3_environmental_severity, Cvss3Severity):
            self.cvss3_environmental_severity = Cvss3Severity(self.cvss3_environmental_severity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV20(YAMLRoot):
    """
    CVSS version 2.0 scoring object. Requires version ('2.0'), vectorString, and baseScore.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV20"]
    class_class_curie: ClassVar[str] = "cve:CvssV20"
    class_name: ClassVar[str] = "CvssV2_0"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV20

    cvss2_vector_string: str = None
    cvss2_base_score: float = None
    cvss2_version: str = "2.0"
    cvss2_access_vector: Optional[Union[str, "Cvss2AccessVector"]] = None
    cvss2_access_complexity: Optional[Union[str, "Cvss2AccessComplexity"]] = None
    cvss2_authentication: Optional[Union[str, "Cvss2Authentication"]] = None
    cvss2_confidentiality_impact: Optional[Union[str, "Cvss2Cia"]] = None
    cvss2_integrity_impact: Optional[Union[str, "Cvss2Cia"]] = None
    cvss2_availability_impact: Optional[Union[str, "Cvss2Cia"]] = None
    cvss2_exploitability: Optional[Union[str, "Cvss2Exploitability"]] = None
    cvss2_remediation_level: Optional[Union[str, "Cvss2RemediationLevel"]] = None
    cvss2_report_confidence: Optional[Union[str, "Cvss2ReportConfidence"]] = None
    cvss2_temporal_score: Optional[float] = None
    cvss2_collateral_damage_potential: Optional[Union[str, "Cvss2CollateralDamagePotential"]] = None
    cvss2_target_distribution: Optional[Union[str, "Cvss2TargetDistribution"]] = None
    cvss2_confidentiality_requirement: Optional[Union[str, "Cvss2CiaRequirement"]] = None
    cvss2_integrity_requirement: Optional[Union[str, "Cvss2CiaRequirement"]] = None
    cvss2_availability_requirement: Optional[Union[str, "Cvss2CiaRequirement"]] = None
    cvss2_environmental_score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cvss2_version):
            self.MissingRequiredField("cvss2_version")
        if not isinstance(self.cvss2_version, str):
            self.cvss2_version = str(self.cvss2_version)

        if self._is_empty(self.cvss2_vector_string):
            self.MissingRequiredField("cvss2_vector_string")
        if not isinstance(self.cvss2_vector_string, str):
            self.cvss2_vector_string = str(self.cvss2_vector_string)

        if self._is_empty(self.cvss2_base_score):
            self.MissingRequiredField("cvss2_base_score")
        if not isinstance(self.cvss2_base_score, float):
            self.cvss2_base_score = float(self.cvss2_base_score)

        if self.cvss2_access_vector is not None and not isinstance(self.cvss2_access_vector, Cvss2AccessVector):
            self.cvss2_access_vector = Cvss2AccessVector(self.cvss2_access_vector)

        if self.cvss2_access_complexity is not None and not isinstance(self.cvss2_access_complexity, Cvss2AccessComplexity):
            self.cvss2_access_complexity = Cvss2AccessComplexity(self.cvss2_access_complexity)

        if self.cvss2_authentication is not None and not isinstance(self.cvss2_authentication, Cvss2Authentication):
            self.cvss2_authentication = Cvss2Authentication(self.cvss2_authentication)

        if self.cvss2_confidentiality_impact is not None and not isinstance(self.cvss2_confidentiality_impact, Cvss2Cia):
            self.cvss2_confidentiality_impact = Cvss2Cia(self.cvss2_confidentiality_impact)

        if self.cvss2_integrity_impact is not None and not isinstance(self.cvss2_integrity_impact, Cvss2Cia):
            self.cvss2_integrity_impact = Cvss2Cia(self.cvss2_integrity_impact)

        if self.cvss2_availability_impact is not None and not isinstance(self.cvss2_availability_impact, Cvss2Cia):
            self.cvss2_availability_impact = Cvss2Cia(self.cvss2_availability_impact)

        if self.cvss2_exploitability is not None and not isinstance(self.cvss2_exploitability, Cvss2Exploitability):
            self.cvss2_exploitability = Cvss2Exploitability(self.cvss2_exploitability)

        if self.cvss2_remediation_level is not None and not isinstance(self.cvss2_remediation_level, Cvss2RemediationLevel):
            self.cvss2_remediation_level = Cvss2RemediationLevel(self.cvss2_remediation_level)

        if self.cvss2_report_confidence is not None and not isinstance(self.cvss2_report_confidence, Cvss2ReportConfidence):
            self.cvss2_report_confidence = Cvss2ReportConfidence(self.cvss2_report_confidence)

        if self.cvss2_temporal_score is not None and not isinstance(self.cvss2_temporal_score, float):
            self.cvss2_temporal_score = float(self.cvss2_temporal_score)

        if self.cvss2_collateral_damage_potential is not None and not isinstance(self.cvss2_collateral_damage_potential, Cvss2CollateralDamagePotential):
            self.cvss2_collateral_damage_potential = Cvss2CollateralDamagePotential(self.cvss2_collateral_damage_potential)

        if self.cvss2_target_distribution is not None and not isinstance(self.cvss2_target_distribution, Cvss2TargetDistribution):
            self.cvss2_target_distribution = Cvss2TargetDistribution(self.cvss2_target_distribution)

        if self.cvss2_confidentiality_requirement is not None and not isinstance(self.cvss2_confidentiality_requirement, Cvss2CiaRequirement):
            self.cvss2_confidentiality_requirement = Cvss2CiaRequirement(self.cvss2_confidentiality_requirement)

        if self.cvss2_integrity_requirement is not None and not isinstance(self.cvss2_integrity_requirement, Cvss2CiaRequirement):
            self.cvss2_integrity_requirement = Cvss2CiaRequirement(self.cvss2_integrity_requirement)

        if self.cvss2_availability_requirement is not None and not isinstance(self.cvss2_availability_requirement, Cvss2CiaRequirement):
            self.cvss2_availability_requirement = Cvss2CiaRequirement(self.cvss2_availability_requirement)

        if self.cvss2_environmental_score is not None and not isinstance(self.cvss2_environmental_score, float):
            self.cvss2_environmental_score = float(self.cvss2_environmental_score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OtherMetric(YAMLRoot):
    """
    A non-standard impact description in a custom format. May be a prose description or an arbitrary JSON-compatible
    object.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["OtherMetric"]
    class_class_curie: ClassVar[str] = "cve:OtherMetric"
    class_name: ClassVar[str] = "OtherMetric"
    class_model_uri: ClassVar[URIRef] = CVE.OtherMetric

    other_metric_type: str = None
    other_metric_content: Union[dict, Any] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.other_metric_type):
            self.MissingRequiredField("other_metric_type")
        if not isinstance(self.other_metric_type, str):
            self.other_metric_type = str(self.other_metric_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimelineEntry(YAMLRoot):
    """
    A timeline event recording a significant event about the vulnerability or changes to the CVE Record. Requires
    time, lang, and value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["TimelineEntry"]
    class_class_curie: ClassVar[str] = "cve:TimelineEntry"
    class_name: ClassVar[str] = "TimelineEntry"
    class_model_uri: ClassVar[URIRef] = CVE.TimelineEntry

    event_time: str = None
    event_value: str = None
    lang: str = "en"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.event_time):
            self.MissingRequiredField("event_time")
        if not isinstance(self.event_time, str):
            self.event_time = str(self.event_time)

        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.event_value):
            self.MissingRequiredField("event_value")
        if not isinstance(self.event_value, str):
            self.event_value = str(self.event_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CreditEntry(YAMLRoot):
    """
    A credit acknowledging a specific person, organization, or tool for work related to the research, discovery,
    remediation, or coordination of the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CreditEntry"]
    class_class_curie: ClassVar[str] = "cve:CreditEntry"
    class_name: ClassVar[str] = "CreditEntry"
    class_model_uri: ClassVar[URIRef] = CVE.CreditEntry

    credit_value: str = None
    lang: str = "en"
    credit_user: Optional[str] = None
    credit_type: Optional[Union[str, "CreditType"]] = 'finder'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.credit_value):
            self.MissingRequiredField("credit_value")
        if not isinstance(self.credit_value, str):
            self.credit_value = str(self.credit_value)

        if self.credit_user is not None and not isinstance(self.credit_user, str):
            self.credit_user = str(self.credit_user)

        if self.credit_type is not None and not isinstance(self.credit_type, CreditType):
            self.credit_type = getattr(CreditType, self.credit_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceInformation(YAMLRoot):
    """
    Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. This is
    an open object — at least one property must be present.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["SourceInformation"]
    class_class_curie: ClassVar[str] = "cve:SourceInformation"
    class_name: ClassVar[str] = "SourceInformation"
    class_model_uri: ClassVar[URIRef] = CVE.SourceInformation

    source_defects: Optional[Union[str, list[str]]] = empty_list()
    source_advisory: Optional[str] = None
    source_discovery: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.source_defects, list):
            self.source_defects = [self.source_defects] if self.source_defects is not None else []
        self.source_defects = [v if isinstance(v, str) else str(v) for v in self.source_defects]

        if self.source_advisory is not None and not isinstance(self.source_advisory, str):
            self.source_advisory = str(self.source_advisory)

        if self.source_discovery is not None and not isinstance(self.source_discovery, str):
            self.source_discovery = str(self.source_discovery)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomyMapping(YAMLRoot):
    """
    A taxonomy mapping identifying the taxonomy by name and version, along with a list of relations relevant to the
    CVE (e.g., ATT&CK, D3FEND, CWE).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["TaxonomyMapping"]
    class_class_curie: ClassVar[str] = "cve:TaxonomyMapping"
    class_name: ClassVar[str] = "TaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CVE.TaxonomyMapping

    taxonomy_name: str = None
    taxonomy_relations: Union[Union[dict, "TaxonomyRelation"], list[Union[dict, "TaxonomyRelation"]]] = None
    taxonomy_version: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomy_name):
            self.MissingRequiredField("taxonomy_name")
        if not isinstance(self.taxonomy_name, str):
            self.taxonomy_name = str(self.taxonomy_name)

        if self._is_empty(self.taxonomy_relations):
            self.MissingRequiredField("taxonomy_relations")
        self._normalize_inlined_as_list(slot_name="taxonomy_relations", slot_type=TaxonomyRelation, key_name="taxonomy_id", keyed=False)

        if self.taxonomy_version is not None and not isinstance(self.taxonomy_version, str):
            self.taxonomy_version = str(self.taxonomy_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TaxonomyRelation(YAMLRoot):
    """
    A relationship between a taxonomy item and a CVE or another taxonomy item. Provides subject (taxonomyId),
    predicate (relationshipName), and object (relationshipValue).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["TaxonomyRelation"]
    class_class_curie: ClassVar[str] = "cve:TaxonomyRelation"
    class_name: ClassVar[str] = "TaxonomyRelation"
    class_model_uri: ClassVar[URIRef] = CVE.TaxonomyRelation

    taxonomy_id: str = None
    relationship_name: str = None
    relationship_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomy_id):
            self.MissingRequiredField("taxonomy_id")
        if not isinstance(self.taxonomy_id, str):
            self.taxonomy_id = str(self.taxonomy_id)

        if self._is_empty(self.relationship_name):
            self.MissingRequiredField("relationship_name")
        if not isinstance(self.relationship_name, str):
            self.relationship_name = str(self.relationship_name)

        if self._is_empty(self.relationship_value):
            self.MissingRequiredField("relationship_value")
        if not isinstance(self.relationship_value, str):
            self.relationship_value = str(self.relationship_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CpeApplicabilityElement(YAMLRoot):
    """
    Affected products defined using an implementation of the CPE Applicability Language. An operator property allows
    AND or OR logic between CPEs or combinations of CPEs.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CpeApplicabilityElement"]
    class_class_curie: ClassVar[str] = "cve:CpeApplicabilityElement"
    class_name: ClassVar[str] = "CpeApplicabilityElement"
    class_model_uri: ClassVar[URIRef] = CVE.CpeApplicabilityElement

    cpe_nodes: Union[Union[dict, "CpeNode"], list[Union[dict, "CpeNode"]]] = None
    cpe_operator: Optional[Union[str, "CpeOperator"]] = None
    cpe_negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpe_nodes):
            self.MissingRequiredField("cpe_nodes")
        self._normalize_inlined_as_list(slot_name="cpe_nodes", slot_type=CpeNode, key_name="cpe_operator", keyed=False)

        if self.cpe_operator is not None and not isinstance(self.cpe_operator, CpeOperator):
            self.cpe_operator = CpeOperator(self.cpe_operator)

        if self.cpe_negate is not None and not isinstance(self.cpe_negate, Bool):
            self.cpe_negate = Bool(self.cpe_negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CpeNode(YAMLRoot):
    """
    Defines a CPE configuration node in an applicability statement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CpeNode"]
    class_class_curie: ClassVar[str] = "cve:CpeNode"
    class_name: ClassVar[str] = "CpeNode"
    class_model_uri: ClassVar[URIRef] = CVE.CpeNode

    cpe_operator: Union[str, "CpeOperator"] = None
    cpe_match_criteria: Union[Union[dict, "CpeMatch"], list[Union[dict, "CpeMatch"]]] = None
    cpe_negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpe_operator):
            self.MissingRequiredField("cpe_operator")
        if not isinstance(self.cpe_operator, CpeOperator):
            self.cpe_operator = CpeOperator(self.cpe_operator)

        if self._is_empty(self.cpe_match_criteria):
            self.MissingRequiredField("cpe_match_criteria")
        self._normalize_inlined_as_list(slot_name="cpe_match_criteria", slot_type=CpeMatch, key_name="cpe_vulnerable", keyed=False)

        if self.cpe_negate is not None and not isinstance(self.cpe_negate, Bool):
            self.cpe_negate = Bool(self.cpe_negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CpeMatch(YAMLRoot):
    """
    CPE match string or range within a CPE applicability node.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CpeMatch"]
    class_class_curie: ClassVar[str] = "cve:CpeMatch"
    class_name: ClassVar[str] = "CpeMatch"
    class_model_uri: ClassVar[URIRef] = CVE.CpeMatch

    cpe_vulnerable: Union[bool, Bool] = None
    cpe_criteria: str = None
    match_criteria_id: Optional[str] = None
    version_start_excluding: Optional[str] = None
    version_start_including: Optional[str] = None
    version_end_excluding: Optional[str] = None
    version_end_including: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpe_vulnerable):
            self.MissingRequiredField("cpe_vulnerable")
        if not isinstance(self.cpe_vulnerable, Bool):
            self.cpe_vulnerable = Bool(self.cpe_vulnerable)

        if self._is_empty(self.cpe_criteria):
            self.MissingRequiredField("cpe_criteria")
        if not isinstance(self.cpe_criteria, str):
            self.cpe_criteria = str(self.cpe_criteria)

        if self.match_criteria_id is not None and not isinstance(self.match_criteria_id, str):
            self.match_criteria_id = str(self.match_criteria_id)

        if self.version_start_excluding is not None and not isinstance(self.version_start_excluding, str):
            self.version_start_excluding = str(self.version_start_excluding)

        if self.version_start_including is not None and not isinstance(self.version_start_including, str):
            self.version_start_including = str(self.version_start_including)

        if self.version_end_excluding is not None and not isinstance(self.version_end_excluding, str):
            self.version_end_excluding = str(self.version_end_excluding)

        if self.version_end_including is not None and not isinstance(self.version_end_including, str):
            self.version_end_including = str(self.version_end_including)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vulnerability(YAMLRoot):
    """
    Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Vulnerability"]
    class_class_curie: ClassVar[str] = "core:Vulnerability"
    class_name: ClassVar[str] = "Vulnerability"
    class_model_uri: ClassVar[URIRef] = CVE.Vulnerability

    cve_id: Union[str, VulnerabilityCveId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    published_date: Optional[Union[str, XSDDateTime]] = None
    last_modified_date: Optional[Union[str, XSDDateTime]] = None
    products: Optional[Union[Union[dict, "Product"], list[Union[dict, "Product"]]]] = empty_list()
    weaknesses: Optional[Union[Union[dict, "Weakness"], list[Union[dict, "Weakness"]]]] = empty_list()
    references: Optional[Union[Union[dict, "Reference"], list[Union[dict, "Reference"]]]] = empty_list()
    impact: Optional[Union[dict, "Impact"]] = None
    status: Optional[Union[str, "VulnerabilityStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cve_id):
            self.MissingRequiredField("cve_id")
        if not isinstance(self.cve_id, VulnerabilityCveId):
            self.cve_id = VulnerabilityCveId(self.cve_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.published_date is not None and not isinstance(self.published_date, XSDDateTime):
            self.published_date = XSDDateTime(self.published_date)

        if self.last_modified_date is not None and not isinstance(self.last_modified_date, XSDDateTime):
            self.last_modified_date = XSDDateTime(self.last_modified_date)

        if not isinstance(self.products, list):
            self.products = [self.products] if self.products is not None else []
        self.products = [v if isinstance(v, Product) else Product(**as_dict(v)) for v in self.products]

        if not isinstance(self.weaknesses, list):
            self.weaknesses = [self.weaknesses] if self.weaknesses is not None else []
        self.weaknesses = [v if isinstance(v, Weakness) else Weakness(**as_dict(v)) for v in self.weaknesses]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, Reference) else Reference(**as_dict(v)) for v in self.references]

        if self.impact is not None and not isinstance(self.impact, Impact):
            self.impact = Impact(**as_dict(self.impact))

        if self.status is not None and not isinstance(self.status, VulnerabilityStatus):
            self.status = VulnerabilityStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVERecord(Vulnerability):
    """
    Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™
    Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected
    records.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CVERecord"]
    class_class_curie: ClassVar[str] = "cve:CVERecord"
    class_name: ClassVar[str] = "CVERecord"
    class_model_uri: ClassVar[URIRef] = CVE.CVERecord

    cve_id: Union[str, CVERecordCveId] = None
    cve_metadata: Union[dict, CveMetadata] = None
    containers: Union[dict, Containers] = None
    data_type: Optional[Union[str, "DataType"]] = 'CVE_RECORD'
    data_version: Optional[str] = "5.2.0"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cve_id):
            self.MissingRequiredField("cve_id")
        if not isinstance(self.cve_id, CVERecordCveId):
            self.cve_id = CVERecordCveId(self.cve_id)

        if self._is_empty(self.cve_metadata):
            self.MissingRequiredField("cve_metadata")
        if not isinstance(self.cve_metadata, CveMetadata):
            self.cve_metadata = CveMetadata()

        if self._is_empty(self.containers):
            self.MissingRequiredField("containers")
        if not isinstance(self.containers, Containers):
            self.containers = Containers(**as_dict(self.containers))

        if self.data_type is not None and not isinstance(self.data_type, DataType):
            self.data_type = getattr(DataType, self.data_type)

        if self.data_version is not None and not isinstance(self.data_version, str):
            self.data_version = str(self.data_version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Product(YAMLRoot):
    """
    Software or hardware entity affected by the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Product"]
    class_class_curie: ClassVar[str] = "core:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = CVE.Product

    vendor: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platforms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.platforms, list):
            self.platforms = [self.platforms] if self.platforms is not None else []
        self.platforms = [v if isinstance(v, str) else str(v) for v in self.platforms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AffectedProduct(Product):
    """
    Information about the set of products and services affected by a vulnerability. At least one of (vendor + product)
    or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["AffectedProduct"]
    class_class_curie: ClassVar[str] = "cve:AffectedProduct"
    class_name: ClassVar[str] = "AffectedProduct"
    class_model_uri: ClassVar[URIRef] = CVE.AffectedProduct

    collection_url: Optional[Union[str, URI]] = None
    package_name: Optional[str] = None
    cpes: Optional[Union[str, list[str]]] = empty_list()
    modules: Optional[Union[str, list[str]]] = empty_list()
    program_files: Optional[Union[str, list[str]]] = empty_list()
    program_routines: Optional[Union[Union[dict, ProgramRoutine], list[Union[dict, ProgramRoutine]]]] = empty_list()
    repo: Optional[Union[str, URI]] = None
    default_status: Optional[Union[str, "VersionStatus"]] = None
    versions: Optional[Union[Union[dict, VersionEntry], list[Union[dict, VersionEntry]]]] = empty_list()
    package_url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.collection_url is not None and not isinstance(self.collection_url, URI):
            self.collection_url = URI(self.collection_url)

        if self.package_name is not None and not isinstance(self.package_name, str):
            self.package_name = str(self.package_name)

        if not isinstance(self.cpes, list):
            self.cpes = [self.cpes] if self.cpes is not None else []
        self.cpes = [v if isinstance(v, str) else str(v) for v in self.cpes]

        if not isinstance(self.modules, list):
            self.modules = [self.modules] if self.modules is not None else []
        self.modules = [v if isinstance(v, str) else str(v) for v in self.modules]

        if not isinstance(self.program_files, list):
            self.program_files = [self.program_files] if self.program_files is not None else []
        self.program_files = [v if isinstance(v, str) else str(v) for v in self.program_files]

        self._normalize_inlined_as_list(slot_name="program_routines", slot_type=ProgramRoutine, key_name="routine_name", keyed=False)

        if self.repo is not None and not isinstance(self.repo, URI):
            self.repo = URI(self.repo)

        if self.default_status is not None and not isinstance(self.default_status, VersionStatus):
            self.default_status = VersionStatus(self.default_status)

        self._normalize_inlined_as_list(slot_name="versions", slot_type=VersionEntry, key_name="version_value", keyed=False)

        if self.package_url is not None and not isinstance(self.package_url, URI):
            self.package_url = URI(self.package_url)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    External reference such as an advisory or article.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Reference"]
    class_class_curie: ClassVar[str] = "core:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = CVE.Reference

    url: Optional[Union[str, URI]] = None
    name: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveReference(Reference):
    """
    An external reference associated with a CVE Record. Extends the core Reference with optional descriptive tags
    characterizing the resource.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveReference"]
    class_class_curie: ClassVar[str] = "cve:CveReference"
    class_name: ClassVar[str] = "CveReference"
    class_model_uri: ClassVar[URIRef] = CVE.CveReference

    url: Union[str, URI] = None
    reference_tags: Optional[Union[Union[str, "ReferenceTag"], list[Union[str, "ReferenceTag"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if not isinstance(self.reference_tags, list):
            self.reference_tags = [self.reference_tags] if self.reference_tags is not None else []
        self.reference_tags = [v if isinstance(v, ReferenceTag) else ReferenceTag(v) for v in self.reference_tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Weakness(YAMLRoot):
    """
    Weakness classification from CWE or a similar taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Weakness"]
    class_class_curie: ClassVar[str] = "core:Weakness"
    class_name: ClassVar[str] = "Weakness"
    class_model_uri: ClassVar[URIRef] = CVE.Weakness

    cwe_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cwe_id is not None and not isinstance(self.cwe_id, str):
            self.cwe_id = str(self.cwe_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Impact(YAMLRoot):
    """
    Assessment of the vulnerability's impact and severity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Impact"]
    class_class_curie: ClassVar[str] = "core:Impact"
    class_name: ClassVar[str] = "Impact"
    class_model_uri: ClassVar[URIRef] = CVE.Impact

    severity: Optional[Union[str, "ImpactSeverity"]] = None
    vector: Optional[str] = None
    score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.severity is not None and not isinstance(self.severity, ImpactSeverity):
            self.severity = ImpactSeverity(self.severity)

        if self.vector is not None and not isinstance(self.vector, str):
            self.vector = str(self.vector)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Configuration(YAMLRoot):
    """
    Logical grouping of CPE match expressions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Configuration"]
    class_class_curie: ClassVar[str] = "core:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = CVE.Configuration

    cpe_uri: Optional[str] = None
    operator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpe_uri is not None and not isinstance(self.cpe_uri, str):
            self.cpe_uri = str(self.cpe_uri)

        if self.operator is not None and not isinstance(self.operator, str):
            self.operator = str(self.operator)

        super().__post_init__(**kwargs)


# Enumerations
class DataType(EnumDefinitionImpl):
    """
    Indicates the type of information represented in a CVE JSON instance.
    """
    CVE_RECORD = PermissibleValue(
        text="CVE_RECORD",
        description="The instance is a CVE Record.")

    _defn = EnumDefinition(
        name="DataType",
        description="Indicates the type of information represented in a CVE JSON instance.",
    )

class RecordState(EnumDefinitionImpl):
    """
    Lifecycle state of a CVE Record (PUBLISHED or REJECTED).
    """
    PUBLISHED = PermissibleValue(
        text="PUBLISHED",
        description="The CVE ID has associated vulnerability data published in the CVE List.")
    REJECTED = PermissibleValue(
        text="REJECTED",
        description="The CVE ID has been rejected and should not be used.")

    _defn = EnumDefinition(
        name="RecordState",
        description="Lifecycle state of a CVE Record (PUBLISHED or REJECTED).",
    )

class VersionStatus(EnumDefinitionImpl):
    """
    The vulnerability status of a given version or range of versions of a product.
    """
    affected = PermissibleValue(
        text="affected",
        description="The version is affected by the vulnerability.")
    unaffected = PermissibleValue(
        text="unaffected",
        description="The version is not affected by the vulnerability.")
    unknown = PermissibleValue(
        text="unknown",
        description="It is unknown or unspecified whether the version is affected.")

    _defn = EnumDefinition(
        name="VersionStatus",
        description="The vulnerability status of a given version or range of versions of a product.",
    )

class ReferenceTag(EnumDefinitionImpl):
    """
    A tag describing the type or nature of the resource referenced by a URL.
    """
    exploit = PermissibleValue(
        text="exploit",
        description="""Reference contains an in-depth description of steps to exploit a vulnerability OR contains legitimate Proof of Concept (PoC) code or an exploit kit.""")
    mitigation = PermissibleValue(
        text="mitigation",
        description="""The reference contains information on steps to mitigate against the vulnerability when a patch cannot be applied or is unavailable, or for EOL product situations.""")
    patch = PermissibleValue(
        text="patch",
        description="The reference contains an update to the software that fixes the vulnerability.")
    product = PermissibleValue(
        text="product",
        description="A reference appropriate for describing a product for the purpose of CPE or SWID.")
    related = PermissibleValue(
        text="related",
        description="A reference that is for a related (but not the same) vulnerability.")
    signature = PermissibleValue(
        text="signature",
        description="""The reference contains a method to detect or prevent the presence or exploitation of the vulnerability.""")

    _defn = EnumDefinition(
        name="ReferenceTag",
        description="A tag describing the type or nature of the resource referenced by a URL.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "broken-link",
            PermissibleValue(
                text="broken-link",
                description="The reference link is returning a 404 error, or the site is no longer online."))
        setattr(cls, "customer-entitlement",
            PermissibleValue(
                text="customer-entitlement",
                description="""Similar to Privileges Required, but specific to references that require non-public or paid access for customers of the particular vendor."""))
        setattr(cls, "government-resource",
            PermissibleValue(
                text="government-resource",
                description="All reference links that are from a government agency or organization."))
        setattr(cls, "issue-tracking",
            PermissibleValue(
                text="issue-tracking",
                description="""The reference is a post from a bug tracking tool such as MantisBT, Bugzilla, JIRA, GitHub Issues, etc."""))
        setattr(cls, "mailing-list",
            PermissibleValue(
                text="mailing-list",
                description="The reference is from a mailing list -- often specific to a product or vendor."))
        setattr(cls, "not-applicable",
            PermissibleValue(
                text="not-applicable",
                description="""The reference link is not applicable to the vulnerability and was likely associated accidentally (should be used sparingly)."""))
        setattr(cls, "permissions-required",
            PermissibleValue(
                text="permissions-required",
                description="The reference link provided is blocked by a logon page."))
        setattr(cls, "media-coverage",
            PermissibleValue(
                text="media-coverage",
                description="""The reference is from a media outlet such as a newspaper, magazine, social media, or weblog. Not intended for individual personal social media accounts."""))
        setattr(cls, "release-notes",
            PermissibleValue(
                text="release-notes",
                description="""The reference is in the format of a vendor or open source project's release notes or change log."""))
        setattr(cls, "technical-description",
            PermissibleValue(
                text="technical-description",
                description="""The reference contains in-depth technical information about a vulnerability and its exploitation process, typically in the form of a presentation or whitepaper."""))
        setattr(cls, "third-party-advisory",
            PermissibleValue(
                text="third-party-advisory",
                description="""Advisory is from an organization that is not the vulnerable product's vendor, publisher, or maintainer."""))
        setattr(cls, "vendor-advisory",
            PermissibleValue(
                text="vendor-advisory",
                description="""Advisory is from the vendor, publisher, or maintainer of the product or the parent organization."""))
        setattr(cls, "vdb-entry",
            PermissibleValue(
                text="vdb-entry",
                description="""VDBs are loosely defined as sites that provide information about this vulnerability, such as advisories, with identifiers."""))

class CNATag(EnumDefinitionImpl):
    """
    Tags provided by a CNA describing the CVE Record.
    """
    disputed = PermissibleValue(
        text="disputed",
        description="""One party disagrees with another party's assertion that a particular issue in software is a vulnerability.""")

    _defn = EnumDefinition(
        name="CNATag",
        description="Tags provided by a CNA describing the CVE Record.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unsupported-when-assigned",
            PermissibleValue(
                text="unsupported-when-assigned",
                description="""When a request for a CVE assignment was received, the product was already end-of-life (EOL) or a product or specific version was deemed not to be supported by the vendor."""))
        setattr(cls, "exclusively-hosted-service",
            PermissibleValue(
                text="exclusively-hosted-service",
                description="""All known software and/or hardware affected by this CVE Record is known to exist only in the affected hosted service."""))

class ADPTag(EnumDefinitionImpl):
    """
    Tags provided by an ADP describing the CVE Record.
    """
    disputed = PermissibleValue(
        text="disputed",
        description="""One party disagrees with another party's assertion that a particular issue in software is a vulnerability.""")

    _defn = EnumDefinition(
        name="ADPTag",
        description="Tags provided by an ADP describing the CVE Record.",
    )

class CreditType(EnumDefinitionImpl):
    """
    Type or role of the entity being credited.
    """
    finder = PermissibleValue(
        text="finder",
        description="Identifies the vulnerability.")
    reporter = PermissibleValue(
        text="reporter",
        description="Notifies the vendor of the vulnerability to a CNA.")
    analyst = PermissibleValue(
        text="analyst",
        description="Validates the vulnerability to ensure accuracy or severity.")
    coordinator = PermissibleValue(
        text="coordinator",
        description="Facilitates the coordinated response process.")
    tool = PermissibleValue(
        text="tool",
        description="Names of tools used in vulnerability discovery or identification.")
    sponsor = PermissibleValue(
        text="sponsor",
        description="Supports the vulnerability identification or remediation activities.")
    other = PermissibleValue(
        text="other",
        description="Other credit type not covered by the above categories.")

    _defn = EnumDefinition(
        name="CreditType",
        description="Type or role of the entity being credited.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "remediation developer",
            PermissibleValue(
                text="remediation developer",
                description="Prepares a code change or other remediation plans."))
        setattr(cls, "remediation reviewer",
            PermissibleValue(
                text="remediation reviewer",
                description="""Reviews vulnerability remediation plans or code changes for effectiveness and completeness."""))
        setattr(cls, "remediation verifier",
            PermissibleValue(
                text="remediation verifier",
                description="Tests and verifies the vulnerability or its remediation."))

class CpeOperator(EnumDefinitionImpl):
    """
    Logical operator used in CPE applicability nodes.
    """
    AND = PermissibleValue(
        text="AND",
        description="All CPE match criteria must be satisfied.")
    OR = PermissibleValue(
        text="OR",
        description="Any one CPE match criterion must be satisfied.")

    _defn = EnumDefinition(
        name="CpeOperator",
        description="Logical operator used in CPE applicability nodes.",
    )

class Cvss4AttackVector(EnumDefinitionImpl):
    """
    CVSS 4.0 attack vector base metric.
    """
    NETWORK = PermissibleValue(text="NETWORK")
    ADJACENT = PermissibleValue(text="ADJACENT")
    LOCAL = PermissibleValue(text="LOCAL")
    PHYSICAL = PermissibleValue(text="PHYSICAL")

    _defn = EnumDefinition(
        name="Cvss4AttackVector",
        description="CVSS 4.0 attack vector base metric.",
    )

class Cvss4AttackComplexity(EnumDefinitionImpl):
    """
    CVSS 4.0 attack complexity base metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")

    _defn = EnumDefinition(
        name="Cvss4AttackComplexity",
        description="CVSS 4.0 attack complexity base metric.",
    )

class Cvss4AttackRequirements(EnumDefinitionImpl):
    """
    CVSS 4.0 attack requirements base metric.
    """
    NONE = PermissibleValue(text="NONE")
    PRESENT = PermissibleValue(text="PRESENT")

    _defn = EnumDefinition(
        name="Cvss4AttackRequirements",
        description="CVSS 4.0 attack requirements base metric.",
    )

class Cvss4PrivilegesRequired(EnumDefinitionImpl):
    """
    CVSS 4.0 privileges required base metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NONE = PermissibleValue(text="NONE")

    _defn = EnumDefinition(
        name="Cvss4PrivilegesRequired",
        description="CVSS 4.0 privileges required base metric.",
    )

class Cvss4UserInteraction(EnumDefinitionImpl):
    """
    CVSS 4.0 user interaction base metric.
    """
    NONE = PermissibleValue(text="NONE")
    PASSIVE = PermissibleValue(text="PASSIVE")
    ACTIVE = PermissibleValue(text="ACTIVE")

    _defn = EnumDefinition(
        name="Cvss4UserInteraction",
        description="CVSS 4.0 user interaction base metric.",
    )

class Cvss4VulnCia(EnumDefinitionImpl):
    """
    CVSS 4.0 vulnerable system confidentiality/integrity/availability impact base metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")

    _defn = EnumDefinition(
        name="Cvss4VulnCia",
        description="CVSS 4.0 vulnerable system confidentiality/integrity/availability impact base metric.",
    )

class Cvss4SubCia(EnumDefinitionImpl):
    """
    CVSS 4.0 subsequent system confidentiality/integrity/availability impact base metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")

    _defn = EnumDefinition(
        name="Cvss4SubCia",
        description="CVSS 4.0 subsequent system confidentiality/integrity/availability impact base metric.",
    )

class Cvss4ExploitMaturity(EnumDefinitionImpl):
    """
    CVSS 4.0 exploit maturity supplemental metric.
    """
    UNREPORTED = PermissibleValue(text="UNREPORTED")
    PROOF_OF_CONCEPT = PermissibleValue(text="PROOF_OF_CONCEPT")
    ATTACKED = PermissibleValue(text="ATTACKED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ExploitMaturity",
        description="CVSS 4.0 exploit maturity supplemental metric.",
    )

class Cvss4CiaRequirement(EnumDefinitionImpl):
    """
    CVSS 4.0 confidentiality/integrity/availability requirement environmental metric.
    """
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4CiaRequirement",
        description="CVSS 4.0 confidentiality/integrity/availability requirement environmental metric.",
    )

class Cvss4Safety(EnumDefinitionImpl):
    """
    CVSS 4.0 safety supplemental metric.
    """
    NEGLIGIBLE = PermissibleValue(text="NEGLIGIBLE")
    PRESENT = PermissibleValue(text="PRESENT")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4Safety",
        description="CVSS 4.0 safety supplemental metric.",
    )

class Cvss4Automatable(EnumDefinitionImpl):
    """
    CVSS 4.0 automatable supplemental metric.
    """
    NO = PermissibleValue(
        text="NO",
        description="The attack cannot be automated.")
    YES = PermissibleValue(
        text="YES",
        description="The attack can be automated.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="Automatable status is not defined.")

    _defn = EnumDefinition(
        name="Cvss4Automatable",
        description="CVSS 4.0 automatable supplemental metric.",
    )

class Cvss4Recovery(EnumDefinitionImpl):
    """
    CVSS 4.0 recovery supplemental metric.
    """
    AUTOMATIC = PermissibleValue(text="AUTOMATIC")
    USER = PermissibleValue(text="USER")
    IRRECOVERABLE = PermissibleValue(text="IRRECOVERABLE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4Recovery",
        description="CVSS 4.0 recovery supplemental metric.",
    )

class Cvss4ValueDensity(EnumDefinitionImpl):
    """
    CVSS 4.0 value density supplemental metric.
    """
    DIFFUSE = PermissibleValue(text="DIFFUSE")
    CONCENTRATED = PermissibleValue(text="CONCENTRATED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ValueDensity",
        description="CVSS 4.0 value density supplemental metric.",
    )

class Cvss4VulnerabilityResponseEffort(EnumDefinitionImpl):
    """
    CVSS 4.0 vulnerability response effort supplemental metric.
    """
    LOW = PermissibleValue(text="LOW")
    MODERATE = PermissibleValue(text="MODERATE")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4VulnerabilityResponseEffort",
        description="CVSS 4.0 vulnerability response effort supplemental metric.",
    )

class Cvss4ProviderUrgency(EnumDefinitionImpl):
    """
    CVSS 4.0 provider urgency supplemental metric.
    """
    CLEAR = PermissibleValue(text="CLEAR")
    GREEN = PermissibleValue(text="GREEN")
    AMBER = PermissibleValue(text="AMBER")
    RED = PermissibleValue(text="RED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ProviderUrgency",
        description="CVSS 4.0 provider urgency supplemental metric.",
    )

class Cvss4Severity(EnumDefinitionImpl):
    """
    CVSS 4.0 qualitative severity rating.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    CRITICAL = PermissibleValue(text="CRITICAL")

    _defn = EnumDefinition(
        name="Cvss4Severity",
        description="CVSS 4.0 qualitative severity rating.",
    )

class Cvss4ModifiedAttackVector(EnumDefinitionImpl):
    """
    CVSS 4.0 modified attack vector environmental metric.
    """
    NETWORK = PermissibleValue(text="NETWORK")
    ADJACENT = PermissibleValue(text="ADJACENT")
    LOCAL = PermissibleValue(text="LOCAL")
    PHYSICAL = PermissibleValue(text="PHYSICAL")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedAttackVector",
        description="CVSS 4.0 modified attack vector environmental metric.",
    )

class Cvss4ModifiedAttackComplexity(EnumDefinitionImpl):
    """
    CVSS 4.0 modified attack complexity environmental metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedAttackComplexity",
        description="CVSS 4.0 modified attack complexity environmental metric.",
    )

class Cvss4ModifiedAttackRequirements(EnumDefinitionImpl):
    """
    CVSS 4.0 modified attack requirements environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    PRESENT = PermissibleValue(text="PRESENT")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedAttackRequirements",
        description="CVSS 4.0 modified attack requirements environmental metric.",
    )

class Cvss4ModifiedPrivilegesRequired(EnumDefinitionImpl):
    """
    CVSS 4.0 modified privileges required environmental metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NONE = PermissibleValue(text="NONE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedPrivilegesRequired",
        description="CVSS 4.0 modified privileges required environmental metric.",
    )

class Cvss4ModifiedUserInteraction(EnumDefinitionImpl):
    """
    CVSS 4.0 modified user interaction environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    PASSIVE = PermissibleValue(text="PASSIVE")
    ACTIVE = PermissibleValue(text="ACTIVE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedUserInteraction",
        description="CVSS 4.0 modified user interaction environmental metric.",
    )

class Cvss4ModifiedVulnCia(EnumDefinitionImpl):
    """
    CVSS 4.0 modified vulnerable system CIA environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedVulnCia",
        description="CVSS 4.0 modified vulnerable system CIA environmental metric.",
    )

class Cvss4ModifiedSubC(EnumDefinitionImpl):
    """
    CVSS 4.0 modified subsequent system confidentiality environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedSubC",
        description="CVSS 4.0 modified subsequent system confidentiality environmental metric.",
    )

class Cvss4ModifiedSubIa(EnumDefinitionImpl):
    """
    CVSS 4.0 modified subsequent system integrity/availability environmental metric (includes SAFETY value).
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")
    SAFETY = PermissibleValue(text="SAFETY")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss4ModifiedSubIa",
        description="""CVSS 4.0 modified subsequent system integrity/availability environmental metric (includes SAFETY value).""",
    )

class CvssV3Version(EnumDefinitionImpl):
    """
    CVSS version 3.x identifier. CVSS 3.0 and 3.1 share an identical metric model; the 3.1 spec was a clarification,
    not a structural change. The consolidated CvssV3 class accepts either via this enum.
    """
    _defn = EnumDefinition(
        name="CvssV3Version",
        description="""CVSS version 3.x identifier. CVSS 3.0 and 3.1 share an identical metric model; the 3.1 spec was a clarification, not a structural change. The consolidated CvssV3 class accepts either via this enum.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3.0",
            PermissibleValue(
                text="3.0",
                description="CVSS version 3.0 (2015-2019)"))
        setattr(cls, "3.1",
            PermissibleValue(
                text="3.1",
                description="CVSS version 3.1 (2019-present)"))

class Cvss3AttackVector(EnumDefinitionImpl):
    """
    CVSS 3.x attack vector base metric.
    """
    NETWORK = PermissibleValue(text="NETWORK")
    ADJACENT_NETWORK = PermissibleValue(text="ADJACENT_NETWORK")
    LOCAL = PermissibleValue(text="LOCAL")
    PHYSICAL = PermissibleValue(text="PHYSICAL")

    _defn = EnumDefinition(
        name="Cvss3AttackVector",
        description="CVSS 3.x attack vector base metric.",
    )

class Cvss3AttackComplexity(EnumDefinitionImpl):
    """
    CVSS 3.x attack complexity base metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")

    _defn = EnumDefinition(
        name="Cvss3AttackComplexity",
        description="CVSS 3.x attack complexity base metric.",
    )

class Cvss3PrivilegesRequired(EnumDefinitionImpl):
    """
    CVSS 3.x privileges required base metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NONE = PermissibleValue(text="NONE")

    _defn = EnumDefinition(
        name="Cvss3PrivilegesRequired",
        description="CVSS 3.x privileges required base metric.",
    )

class Cvss3UserInteraction(EnumDefinitionImpl):
    """
    CVSS 3.x user interaction base metric.
    """
    NONE = PermissibleValue(text="NONE")
    REQUIRED = PermissibleValue(text="REQUIRED")

    _defn = EnumDefinition(
        name="Cvss3UserInteraction",
        description="CVSS 3.x user interaction base metric.",
    )

class Cvss3Scope(EnumDefinitionImpl):
    """
    CVSS 3.x scope base metric.
    """
    UNCHANGED = PermissibleValue(text="UNCHANGED")
    CHANGED = PermissibleValue(text="CHANGED")

    _defn = EnumDefinition(
        name="Cvss3Scope",
        description="CVSS 3.x scope base metric.",
    )

class Cvss3Cia(EnumDefinitionImpl):
    """
    CVSS 3.x confidentiality/integrity/availability impact base metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")

    _defn = EnumDefinition(
        name="Cvss3Cia",
        description="CVSS 3.x confidentiality/integrity/availability impact base metric.",
    )

class Cvss3Severity(EnumDefinitionImpl):
    """
    CVSS 3.x qualitative severity rating.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    CRITICAL = PermissibleValue(text="CRITICAL")

    _defn = EnumDefinition(
        name="Cvss3Severity",
        description="CVSS 3.x qualitative severity rating.",
    )

class Cvss3ExploitCodeMaturity(EnumDefinitionImpl):
    """
    CVSS 3.x exploit code maturity temporal metric.
    """
    UNPROVEN = PermissibleValue(text="UNPROVEN")
    PROOF_OF_CONCEPT = PermissibleValue(text="PROOF_OF_CONCEPT")
    FUNCTIONAL = PermissibleValue(text="FUNCTIONAL")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ExploitCodeMaturity",
        description="CVSS 3.x exploit code maturity temporal metric.",
    )

class Cvss3RemediationLevel(EnumDefinitionImpl):
    """
    CVSS 3.x remediation level temporal metric.
    """
    OFFICIAL_FIX = PermissibleValue(text="OFFICIAL_FIX")
    TEMPORARY_FIX = PermissibleValue(text="TEMPORARY_FIX")
    WORKAROUND = PermissibleValue(text="WORKAROUND")
    UNAVAILABLE = PermissibleValue(text="UNAVAILABLE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3RemediationLevel",
        description="CVSS 3.x remediation level temporal metric.",
    )

class Cvss3Confidence(EnumDefinitionImpl):
    """
    CVSS 3.x report confidence temporal metric.
    """
    UNKNOWN = PermissibleValue(text="UNKNOWN")
    REASONABLE = PermissibleValue(text="REASONABLE")
    CONFIRMED = PermissibleValue(text="CONFIRMED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3Confidence",
        description="CVSS 3.x report confidence temporal metric.",
    )

class Cvss3CiaRequirement(EnumDefinitionImpl):
    """
    CVSS 3.x CIA requirement environmental metric.
    """
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3CiaRequirement",
        description="CVSS 3.x CIA requirement environmental metric.",
    )

class Cvss3ModifiedAttackVector(EnumDefinitionImpl):
    """
    CVSS 3.x modified attack vector environmental metric.
    """
    NETWORK = PermissibleValue(text="NETWORK")
    ADJACENT_NETWORK = PermissibleValue(text="ADJACENT_NETWORK")
    LOCAL = PermissibleValue(text="LOCAL")
    PHYSICAL = PermissibleValue(text="PHYSICAL")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedAttackVector",
        description="CVSS 3.x modified attack vector environmental metric.",
    )

class Cvss3ModifiedAttackComplexity(EnumDefinitionImpl):
    """
    CVSS 3.x modified attack complexity environmental metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedAttackComplexity",
        description="CVSS 3.x modified attack complexity environmental metric.",
    )

class Cvss3ModifiedPrivilegesRequired(EnumDefinitionImpl):
    """
    CVSS 3.x modified privileges required environmental metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    LOW = PermissibleValue(text="LOW")
    NONE = PermissibleValue(text="NONE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedPrivilegesRequired",
        description="CVSS 3.x modified privileges required environmental metric.",
    )

class Cvss3ModifiedUserInteraction(EnumDefinitionImpl):
    """
    CVSS 3.x modified user interaction environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    REQUIRED = PermissibleValue(text="REQUIRED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedUserInteraction",
        description="CVSS 3.x modified user interaction environmental metric.",
    )

class Cvss3ModifiedScope(EnumDefinitionImpl):
    """
    CVSS 3.x modified scope environmental metric.
    """
    UNCHANGED = PermissibleValue(text="UNCHANGED")
    CHANGED = PermissibleValue(text="CHANGED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedScope",
        description="CVSS 3.x modified scope environmental metric.",
    )

class Cvss3ModifiedCia(EnumDefinitionImpl):
    """
    CVSS 3.x modified CIA environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss3ModifiedCia",
        description="CVSS 3.x modified CIA environmental metric.",
    )

class Cvss2AccessVector(EnumDefinitionImpl):
    """
    CVSS 2.0 access vector base metric.
    """
    NETWORK = PermissibleValue(text="NETWORK")
    ADJACENT_NETWORK = PermissibleValue(text="ADJACENT_NETWORK")
    LOCAL = PermissibleValue(text="LOCAL")

    _defn = EnumDefinition(
        name="Cvss2AccessVector",
        description="CVSS 2.0 access vector base metric.",
    )

class Cvss2AccessComplexity(EnumDefinitionImpl):
    """
    CVSS 2.0 access complexity base metric.
    """
    HIGH = PermissibleValue(text="HIGH")
    MEDIUM = PermissibleValue(text="MEDIUM")
    LOW = PermissibleValue(text="LOW")

    _defn = EnumDefinition(
        name="Cvss2AccessComplexity",
        description="CVSS 2.0 access complexity base metric.",
    )

class Cvss2Authentication(EnumDefinitionImpl):
    """
    CVSS 2.0 authentication base metric.
    """
    MULTIPLE = PermissibleValue(text="MULTIPLE")
    SINGLE = PermissibleValue(text="SINGLE")
    NONE = PermissibleValue(text="NONE")

    _defn = EnumDefinition(
        name="Cvss2Authentication",
        description="CVSS 2.0 authentication base metric.",
    )

class Cvss2Cia(EnumDefinitionImpl):
    """
    CVSS 2.0 confidentiality/integrity/availability impact base metric.
    """
    NONE = PermissibleValue(text="NONE")
    PARTIAL = PermissibleValue(text="PARTIAL")
    COMPLETE = PermissibleValue(text="COMPLETE")

    _defn = EnumDefinition(
        name="Cvss2Cia",
        description="CVSS 2.0 confidentiality/integrity/availability impact base metric.",
    )

class Cvss2Exploitability(EnumDefinitionImpl):
    """
    CVSS 2.0 exploitability temporal metric.
    """
    UNPROVEN = PermissibleValue(text="UNPROVEN")
    PROOF_OF_CONCEPT = PermissibleValue(text="PROOF_OF_CONCEPT")
    FUNCTIONAL = PermissibleValue(text="FUNCTIONAL")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2Exploitability",
        description="CVSS 2.0 exploitability temporal metric.",
    )

class Cvss2RemediationLevel(EnumDefinitionImpl):
    """
    CVSS 2.0 remediation level temporal metric.
    """
    OFFICIAL_FIX = PermissibleValue(text="OFFICIAL_FIX")
    TEMPORARY_FIX = PermissibleValue(text="TEMPORARY_FIX")
    WORKAROUND = PermissibleValue(text="WORKAROUND")
    UNAVAILABLE = PermissibleValue(text="UNAVAILABLE")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2RemediationLevel",
        description="CVSS 2.0 remediation level temporal metric.",
    )

class Cvss2ReportConfidence(EnumDefinitionImpl):
    """
    CVSS 2.0 report confidence temporal metric.
    """
    UNCONFIRMED = PermissibleValue(text="UNCONFIRMED")
    UNCORROBORATED = PermissibleValue(text="UNCORROBORATED")
    CONFIRMED = PermissibleValue(text="CONFIRMED")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2ReportConfidence",
        description="CVSS 2.0 report confidence temporal metric.",
    )

class Cvss2CollateralDamagePotential(EnumDefinitionImpl):
    """
    CVSS 2.0 collateral damage potential environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    LOW_MEDIUM = PermissibleValue(text="LOW_MEDIUM")
    MEDIUM_HIGH = PermissibleValue(text="MEDIUM_HIGH")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2CollateralDamagePotential",
        description="CVSS 2.0 collateral damage potential environmental metric.",
    )

class Cvss2TargetDistribution(EnumDefinitionImpl):
    """
    CVSS 2.0 target distribution environmental metric.
    """
    NONE = PermissibleValue(text="NONE")
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2TargetDistribution",
        description="CVSS 2.0 target distribution environmental metric.",
    )

class Cvss2CiaRequirement(EnumDefinitionImpl):
    """
    CVSS 2.0 CIA requirement environmental metric.
    """
    LOW = PermissibleValue(text="LOW")
    MEDIUM = PermissibleValue(text="MEDIUM")
    HIGH = PermissibleValue(text="HIGH")
    NOT_DEFINED = PermissibleValue(text="NOT_DEFINED")

    _defn = EnumDefinition(
        name="Cvss2CiaRequirement",
        description="CVSS 2.0 CIA requirement environmental metric.",
    )

class VulnerabilityStatus(EnumDefinitionImpl):
    """
    Lifecycle state of a vulnerability record.
    """
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Vulnerability is actively maintained and published.")
    REJECTED = PermissibleValue(
        text="REJECTED",
        description="CVE ID was rejected and should not be used.")
    DISPUTED = PermissibleValue(
        text="DISPUTED",
        description="The vulnerability details are disputed by a party.")
    RESERVED = PermissibleValue(
        text="RESERVED",
        description="CVE ID is reserved but details are not yet published.")
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="Entry has been superseded or withdrawn.")

    _defn = EnumDefinition(
        name="VulnerabilityStatus",
        description="Lifecycle state of a vulnerability record.",
    )

class ImpactSeverity(EnumDefinitionImpl):
    """
    CVSS qualitative severity rating.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No measurable impact.")
    LOW = PermissibleValue(
        text="LOW",
        description="Limited impact; exploitation requires specific conditions.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="Moderate impact; partial compromise of security properties.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="High impact; significant compromise of security properties.")
    CRITICAL = PermissibleValue(
        text="CRITICAL",
        description="Critical impact; complete compromise; remote exploitation likely.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Severity has not been assessed or is unavailable.")

    _defn = EnumDefinition(
        name="ImpactSeverity",
        description="CVSS qualitative severity rating.",
    )

# Slots
class slots:
    pass

slots.data_type = Slot(uri=CVE.data_type, name="data_type", curie=CVE.curie('data_type'),
                   model_uri=CVE.data_type, domain=None, range=Optional[Union[str, "DataType"]])

slots.data_version = Slot(uri=CVE.data_version, name="data_version", curie=CVE.curie('data_version'),
                   model_uri=CVE.data_version, domain=None, range=Optional[str],
                   pattern=re.compile(r'^5\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))?$'))

slots.cve_metadata = Slot(uri=CVE.cve_metadata, name="cve_metadata", curie=CVE.curie('cve_metadata'),
                   model_uri=CVE.cve_metadata, domain=None, range=Optional[Union[dict, CveMetadata]])

slots.containers = Slot(uri=CVE.containers, name="containers", curie=CVE.curie('containers'),
                   model_uri=CVE.containers, domain=None, range=Optional[Union[dict, Containers]])

slots.record_cve_id = Slot(uri=CVE.record_cve_id, name="record_cve_id", curie=CVE.curie('record_cve_id'),
                   model_uri=CVE.record_cve_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CVE-[0-9]{4}-[0-9]{4,19}$'))

slots.assigner_org_id = Slot(uri=CVE.assigner_org_id, name="assigner_org_id", curie=CVE.curie('assigner_org_id'),
                   model_uri=CVE.assigner_org_id, domain=None, range=Optional[str])

slots.assigner_short_name = Slot(uri=CVE.assigner_short_name, name="assigner_short_name", curie=CVE.curie('assigner_short_name'),
                   model_uri=CVE.assigner_short_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^.{2,32}$'))

slots.requester_user_id = Slot(uri=CVE.requester_user_id, name="requester_user_id", curie=CVE.curie('requester_user_id'),
                   model_uri=CVE.requester_user_id, domain=None, range=Optional[str])

slots.serial = Slot(uri=CVE.serial, name="serial", curie=CVE.curie('serial'),
                   model_uri=CVE.serial, domain=None, range=Optional[int])

slots.date_reserved = Slot(uri=CVE.date_reserved, name="date_reserved", curie=CVE.curie('date_reserved'),
                   model_uri=CVE.date_reserved, domain=None, range=Optional[str])

slots.date_published = Slot(uri=CVE.date_published, name="date_published", curie=CVE.curie('date_published'),
                   model_uri=CVE.date_published, domain=None, range=Optional[str])

slots.date_updated = Slot(uri=CVE.date_updated, name="date_updated", curie=CVE.curie('date_updated'),
                   model_uri=CVE.date_updated, domain=None, range=Optional[str])

slots.date_rejected = Slot(uri=CVE.date_rejected, name="date_rejected", curie=CVE.curie('date_rejected'),
                   model_uri=CVE.date_rejected, domain=None, range=Optional[str])

slots.published_state = Slot(uri=CVE.published_state, name="published_state", curie=CVE.curie('published_state'),
                   model_uri=CVE.published_state, domain=None, range=Optional[Union[str, "RecordState"]])

slots.rejected_state = Slot(uri=CVE.rejected_state, name="rejected_state", curie=CVE.curie('rejected_state'),
                   model_uri=CVE.rejected_state, domain=None, range=Optional[Union[str, "RecordState"]])

slots.cna = Slot(uri=CVE.cna, name="cna", curie=CVE.curie('cna'),
                   model_uri=CVE.cna, domain=None, range=Optional[Union[dict, CnaContainer]])

slots.adp = Slot(uri=CVE.adp, name="adp", curie=CVE.curie('adp'),
                   model_uri=CVE.adp, domain=None, range=Optional[Union[Union[dict, AdpContainer], list[Union[dict, AdpContainer]]]])

slots.org_id = Slot(uri=CVE.org_id, name="org_id", curie=CVE.curie('org_id'),
                   model_uri=CVE.org_id, domain=None, range=Optional[str])

slots.short_name = Slot(uri=CVE.short_name, name="short_name", curie=CVE.curie('short_name'),
                   model_uri=CVE.short_name, domain=None, range=Optional[str],
                   pattern=re.compile(r'^.{2,32}$'))

slots.provider_metadata = Slot(uri=CVE.provider_metadata, name="provider_metadata", curie=CVE.curie('provider_metadata'),
                   model_uri=CVE.provider_metadata, domain=None, range=Optional[Union[dict, ProviderMetadata]])

slots.date_assigned = Slot(uri=CVE.date_assigned, name="date_assigned", curie=CVE.curie('date_assigned'),
                   model_uri=CVE.date_assigned, domain=None, range=Optional[str])

slots.date_public = Slot(uri=CVE.date_public, name="date_public", curie=CVE.curie('date_public'),
                   model_uri=CVE.date_public, domain=None, range=Optional[str])

slots.descriptions = Slot(uri=CVE.descriptions, name="descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.descriptions, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.affected = Slot(uri=CVE.affected, name="affected", curie=CVE.curie('affected'),
                   model_uri=CVE.affected, domain=None, range=Optional[Union[Union[dict, AffectedProduct], list[Union[dict, AffectedProduct]]]])

slots.cpe_applicability = Slot(uri=CVE.cpe_applicability, name="cpe_applicability", curie=CVE.curie('cpe_applicability'),
                   model_uri=CVE.cpe_applicability, domain=None, range=Optional[Union[Union[dict, CpeApplicabilityElement], list[Union[dict, CpeApplicabilityElement]]]])

slots.problem_types = Slot(uri=CVE.problem_types, name="problem_types", curie=CVE.curie('problem_types'),
                   model_uri=CVE.problem_types, domain=None, range=Optional[Union[Union[dict, ProblemType], list[Union[dict, ProblemType]]]])

slots.cve_references = Slot(uri=CVE.cve_references, name="cve_references", curie=CVE.curie('cve_references'),
                   model_uri=CVE.cve_references, domain=None, range=Optional[Union[Union[dict, CveReference], list[Union[dict, CveReference]]]])

slots.impacts = Slot(uri=CVE.impacts, name="impacts", curie=CVE.curie('impacts'),
                   model_uri=CVE.impacts, domain=None, range=Optional[Union[Union[dict, ImpactEntry], list[Union[dict, ImpactEntry]]]])

slots.metrics = Slot(uri=CVE.metrics, name="metrics", curie=CVE.curie('metrics'),
                   model_uri=CVE.metrics, domain=None, range=Optional[Union[Union[dict, MetricEntry], list[Union[dict, MetricEntry]]]])

slots.configurations_text = Slot(uri=CVE.configurations_text, name="configurations_text", curie=CVE.curie('configurations_text'),
                   model_uri=CVE.configurations_text, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.workarounds = Slot(uri=CVE.workarounds, name="workarounds", curie=CVE.curie('workarounds'),
                   model_uri=CVE.workarounds, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.solutions = Slot(uri=CVE.solutions, name="solutions", curie=CVE.curie('solutions'),
                   model_uri=CVE.solutions, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.exploits = Slot(uri=CVE.exploits, name="exploits", curie=CVE.curie('exploits'),
                   model_uri=CVE.exploits, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.timeline = Slot(uri=CVE.timeline, name="timeline", curie=CVE.curie('timeline'),
                   model_uri=CVE.timeline, domain=None, range=Optional[Union[Union[dict, TimelineEntry], list[Union[dict, TimelineEntry]]]])

slots.credits = Slot(uri=CVE.credits, name="credits", curie=CVE.curie('credits'),
                   model_uri=CVE.credits, domain=None, range=Optional[Union[Union[dict, CreditEntry], list[Union[dict, CreditEntry]]]])

slots.cna_source = Slot(uri=CVE.cna_source, name="cna_source", curie=CVE.curie('cna_source'),
                   model_uri=CVE.cna_source, domain=None, range=Optional[Union[dict, SourceInformation]])

slots.source_defects = Slot(uri=CVE.source_defects, name="source_defects", curie=CVE.curie('source_defects'),
                   model_uri=CVE.source_defects, domain=None, range=Optional[Union[str, list[str]]])

slots.source_advisory = Slot(uri=CVE.source_advisory, name="source_advisory", curie=CVE.curie('source_advisory'),
                   model_uri=CVE.source_advisory, domain=None, range=Optional[str])

slots.source_discovery = Slot(uri=CVE.source_discovery, name="source_discovery", curie=CVE.curie('source_discovery'),
                   model_uri=CVE.source_discovery, domain=None, range=Optional[str])

slots.cna_tags = Slot(uri=CVE.cna_tags, name="cna_tags", curie=CVE.curie('cna_tags'),
                   model_uri=CVE.cna_tags, domain=None, range=Optional[Union[str, list[str]]])

slots.adp_tags = Slot(uri=CVE.adp_tags, name="adp_tags", curie=CVE.curie('adp_tags'),
                   model_uri=CVE.adp_tags, domain=None, range=Optional[Union[str, list[str]]])

slots.taxonomy_mappings = Slot(uri=CVE.taxonomy_mappings, name="taxonomy_mappings", curie=CVE.curie('taxonomy_mappings'),
                   model_uri=CVE.taxonomy_mappings, domain=None, range=Optional[Union[Union[dict, TaxonomyMapping], list[Union[dict, TaxonomyMapping]]]])

slots.rejected_reasons = Slot(uri=CVE.rejected_reasons, name="rejected_reasons", curie=CVE.curie('rejected_reasons'),
                   model_uri=CVE.rejected_reasons, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.replaced_by = Slot(uri=CVE.replaced_by, name="replaced_by", curie=CVE.curie('replaced_by'),
                   model_uri=CVE.replaced_by, domain=None, range=Optional[Union[str, list[str]]])

slots.collection_url = Slot(uri=CVE.collection_url, name="collection_url", curie=CVE.curie('collection_url'),
                   model_uri=CVE.collection_url, domain=None, range=Optional[Union[str, URI]])

slots.package_name = Slot(uri=CVE.package_name, name="package_name", curie=CVE.curie('package_name'),
                   model_uri=CVE.package_name, domain=None, range=Optional[str])

slots.cpes = Slot(uri=CVE.cpes, name="cpes", curie=CVE.curie('cpes'),
                   model_uri=CVE.cpes, domain=None, range=Optional[Union[str, list[str]]])

slots.modules = Slot(uri=CVE.modules, name="modules", curie=CVE.curie('modules'),
                   model_uri=CVE.modules, domain=None, range=Optional[Union[str, list[str]]])

slots.program_files = Slot(uri=CVE.program_files, name="program_files", curie=CVE.curie('program_files'),
                   model_uri=CVE.program_files, domain=None, range=Optional[Union[str, list[str]]])

slots.program_routines = Slot(uri=CVE.program_routines, name="program_routines", curie=CVE.curie('program_routines'),
                   model_uri=CVE.program_routines, domain=None, range=Optional[Union[Union[dict, ProgramRoutine], list[Union[dict, ProgramRoutine]]]])

slots.repo = Slot(uri=CVE.repo, name="repo", curie=CVE.curie('repo'),
                   model_uri=CVE.repo, domain=None, range=Optional[Union[str, URI]])

slots.default_status = Slot(uri=CVE.default_status, name="default_status", curie=CVE.curie('default_status'),
                   model_uri=CVE.default_status, domain=None, range=Optional[Union[str, "VersionStatus"]])

slots.versions = Slot(uri=CVE.versions, name="versions", curie=CVE.curie('versions'),
                   model_uri=CVE.versions, domain=None, range=Optional[Union[Union[dict, VersionEntry], list[Union[dict, VersionEntry]]]])

slots.package_url = Slot(uri=CVE.package_url, name="package_url", curie=CVE.curie('package_url'),
                   model_uri=CVE.package_url, domain=None, range=Optional[Union[str, URI]])

slots.version_value = Slot(uri=CVE.version_value, name="version_value", curie=CVE.curie('version_value'),
                   model_uri=CVE.version_value, domain=None, range=Optional[str])

slots.version_status = Slot(uri=CVE.version_status, name="version_status", curie=CVE.curie('version_status'),
                   model_uri=CVE.version_status, domain=None, range=Optional[Union[str, "VersionStatus"]])

slots.version_type = Slot(uri=CVE.version_type, name="version_type", curie=CVE.curie('version_type'),
                   model_uri=CVE.version_type, domain=None, range=Optional[str])

slots.less_than = Slot(uri=CVE.less_than, name="less_than", curie=CVE.curie('less_than'),
                   model_uri=CVE.less_than, domain=None, range=Optional[str])

slots.less_than_or_equal = Slot(uri=CVE.less_than_or_equal, name="less_than_or_equal", curie=CVE.curie('less_than_or_equal'),
                   model_uri=CVE.less_than_or_equal, domain=None, range=Optional[str])

slots.version_changes = Slot(uri=CVE.version_changes, name="version_changes", curie=CVE.curie('version_changes'),
                   model_uri=CVE.version_changes, domain=None, range=Optional[Union[Union[dict, VersionChange], list[Union[dict, VersionChange]]]])

slots.change_at = Slot(uri=CVE.change_at, name="change_at", curie=CVE.curie('change_at'),
                   model_uri=CVE.change_at, domain=None, range=Optional[str])

slots.change_status = Slot(uri=CVE.change_status, name="change_status", curie=CVE.curie('change_status'),
                   model_uri=CVE.change_status, domain=None, range=Optional[Union[str, "VersionStatus"]])

slots.routine_name = Slot(uri=CVE.routine_name, name="routine_name", curie=CVE.curie('routine_name'),
                   model_uri=CVE.routine_name, domain=None, range=Optional[str])

slots.lang = Slot(uri=CVE.lang, name="lang", curie=CVE.curie('lang'),
                   model_uri=CVE.lang, domain=None, range=Optional[str])

slots.description_value = Slot(uri=CVE.description_value, name="description_value", curie=CVE.curie('description_value'),
                   model_uri=CVE.description_value, domain=None, range=Optional[str])

slots.supporting_media = Slot(uri=CVE.supporting_media, name="supporting_media", curie=CVE.curie('supporting_media'),
                   model_uri=CVE.supporting_media, domain=None, range=Optional[Union[Union[dict, SupportingMedia], list[Union[dict, SupportingMedia]]]])

slots.media_type = Slot(uri=CVE.media_type, name="media_type", curie=CVE.curie('media_type'),
                   model_uri=CVE.media_type, domain=None, range=Optional[str])

slots.base64_encoded = Slot(uri=CVE.base64_encoded, name="base64_encoded", curie=CVE.curie('base64_encoded'),
                   model_uri=CVE.base64_encoded, domain=None, range=Optional[Union[bool, Bool]])

slots.media_value = Slot(uri=CVE.media_value, name="media_value", curie=CVE.curie('media_value'),
                   model_uri=CVE.media_value, domain=None, range=Optional[str])

slots.problem_type_descriptions = Slot(uri=CVE.problem_type_descriptions, name="problem_type_descriptions", curie=CVE.curie('problem_type_descriptions'),
                   model_uri=CVE.problem_type_descriptions, domain=None, range=Optional[Union[Union[dict, ProblemTypeDescription], list[Union[dict, ProblemTypeDescription]]]])

slots.problem_description = Slot(uri=CVE.problem_description, name="problem_description", curie=CVE.curie('problem_description'),
                   model_uri=CVE.problem_description, domain=None, range=Optional[str])

slots.problem_source_type = Slot(uri=CVE.problem_source_type, name="problem_source_type", curie=CVE.curie('problem_source_type'),
                   model_uri=CVE.problem_source_type, domain=None, range=Optional[str])

slots.problem_references = Slot(uri=CVE.problem_references, name="problem_references", curie=CVE.curie('problem_references'),
                   model_uri=CVE.problem_references, domain=None, range=Optional[Union[Union[dict, CveReference], list[Union[dict, CveReference]]]])

slots.reference_tags = Slot(uri=CVE.reference_tags, name="reference_tags", curie=CVE.curie('reference_tags'),
                   model_uri=CVE.reference_tags, domain=None, range=Optional[Union[Union[str, "ReferenceTag"], list[Union[str, "ReferenceTag"]]]])

slots.capec_id = Slot(uri=CVE.capec_id, name="capec_id", curie=CVE.curie('capec_id'),
                   model_uri=CVE.capec_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CAPEC-[1-9][0-9]{0,4}$'))

slots.impact_descriptions = Slot(uri=CVE.impact_descriptions, name="impact_descriptions", curie=CVE.curie('impact_descriptions'),
                   model_uri=CVE.impact_descriptions, domain=None, range=Optional[Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]]])

slots.metric_format = Slot(uri=CVE.metric_format, name="metric_format", curie=CVE.curie('metric_format'),
                   model_uri=CVE.metric_format, domain=None, range=Optional[str])

slots.metric_scenarios = Slot(uri=CVE.metric_scenarios, name="metric_scenarios", curie=CVE.curie('metric_scenarios'),
                   model_uri=CVE.metric_scenarios, domain=None, range=Optional[Union[Union[dict, MetricScenario], list[Union[dict, MetricScenario]]]])

slots.scenario_value = Slot(uri=CVE.scenario_value, name="scenario_value", curie=CVE.curie('scenario_value'),
                   model_uri=CVE.scenario_value, domain=None, range=Optional[str])

slots.cvss_v4_0 = Slot(uri=CVE.cvss_v4_0, name="cvss_v4_0", curie=CVE.curie('cvss_v4_0'),
                   model_uri=CVE.cvss_v4_0, domain=None, range=Optional[Union[dict, CvssV40]])

slots.cvss_v3 = Slot(uri=CVE.cvss_v3, name="cvss_v3", curie=CVE.curie('cvss_v3'),
                   model_uri=CVE.cvss_v3, domain=None, range=Optional[Union[dict, CvssV3]])

slots.cvss_v2_0 = Slot(uri=CVE.cvss_v2_0, name="cvss_v2_0", curie=CVE.curie('cvss_v2_0'),
                   model_uri=CVE.cvss_v2_0, domain=None, range=Optional[Union[dict, CvssV20]])

slots.other_metric = Slot(uri=CVE.other_metric, name="other_metric", curie=CVE.curie('other_metric'),
                   model_uri=CVE.other_metric, domain=None, range=Optional[Union[dict, OtherMetric]])

slots.other_metric_type = Slot(uri=CVE.other_metric_type, name="other_metric_type", curie=CVE.curie('other_metric_type'),
                   model_uri=CVE.other_metric_type, domain=None, range=Optional[str])

slots.other_metric_content = Slot(uri=CVE.other_metric_content, name="other_metric_content", curie=CVE.curie('other_metric_content'),
                   model_uri=CVE.other_metric_content, domain=None, range=Optional[Union[dict, Any]])

slots.cvss4_version = Slot(uri=CVE.cvss4_version, name="cvss4_version", curie=CVE.curie('cvss4_version'),
                   model_uri=CVE.cvss4_version, domain=None, range=Optional[str])

slots.cvss4_vector_string = Slot(uri=CVE.cvss4_vector_string, name="cvss4_vector_string", curie=CVE.curie('cvss4_vector_string'),
                   model_uri=CVE.cvss4_vector_string, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'))

slots.cvss4_base_score = Slot(uri=CVE.cvss4_base_score, name="cvss4_base_score", curie=CVE.curie('cvss4_base_score'),
                   model_uri=CVE.cvss4_base_score, domain=None, range=Optional[float])

slots.cvss4_base_severity = Slot(uri=CVE.cvss4_base_severity, name="cvss4_base_severity", curie=CVE.curie('cvss4_base_severity'),
                   model_uri=CVE.cvss4_base_severity, domain=None, range=Optional[Union[str, "Cvss4Severity"]])

slots.cvss4_attack_vector = Slot(uri=CVE.cvss4_attack_vector, name="cvss4_attack_vector", curie=CVE.curie('cvss4_attack_vector'),
                   model_uri=CVE.cvss4_attack_vector, domain=None, range=Optional[Union[str, "Cvss4AttackVector"]])

slots.cvss4_attack_complexity = Slot(uri=CVE.cvss4_attack_complexity, name="cvss4_attack_complexity", curie=CVE.curie('cvss4_attack_complexity'),
                   model_uri=CVE.cvss4_attack_complexity, domain=None, range=Optional[Union[str, "Cvss4AttackComplexity"]])

slots.cvss4_attack_requirements = Slot(uri=CVE.cvss4_attack_requirements, name="cvss4_attack_requirements", curie=CVE.curie('cvss4_attack_requirements'),
                   model_uri=CVE.cvss4_attack_requirements, domain=None, range=Optional[Union[str, "Cvss4AttackRequirements"]])

slots.cvss4_privileges_required = Slot(uri=CVE.cvss4_privileges_required, name="cvss4_privileges_required", curie=CVE.curie('cvss4_privileges_required'),
                   model_uri=CVE.cvss4_privileges_required, domain=None, range=Optional[Union[str, "Cvss4PrivilegesRequired"]])

slots.cvss4_user_interaction = Slot(uri=CVE.cvss4_user_interaction, name="cvss4_user_interaction", curie=CVE.curie('cvss4_user_interaction'),
                   model_uri=CVE.cvss4_user_interaction, domain=None, range=Optional[Union[str, "Cvss4UserInteraction"]])

slots.cvss4_vuln_confidentiality_impact = Slot(uri=CVE.cvss4_vuln_confidentiality_impact, name="cvss4_vuln_confidentiality_impact", curie=CVE.curie('cvss4_vuln_confidentiality_impact'),
                   model_uri=CVE.cvss4_vuln_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss4VulnCia"]])

slots.cvss4_vuln_integrity_impact = Slot(uri=CVE.cvss4_vuln_integrity_impact, name="cvss4_vuln_integrity_impact", curie=CVE.curie('cvss4_vuln_integrity_impact'),
                   model_uri=CVE.cvss4_vuln_integrity_impact, domain=None, range=Optional[Union[str, "Cvss4VulnCia"]])

slots.cvss4_vuln_availability_impact = Slot(uri=CVE.cvss4_vuln_availability_impact, name="cvss4_vuln_availability_impact", curie=CVE.curie('cvss4_vuln_availability_impact'),
                   model_uri=CVE.cvss4_vuln_availability_impact, domain=None, range=Optional[Union[str, "Cvss4VulnCia"]])

slots.cvss4_sub_confidentiality_impact = Slot(uri=CVE.cvss4_sub_confidentiality_impact, name="cvss4_sub_confidentiality_impact", curie=CVE.curie('cvss4_sub_confidentiality_impact'),
                   model_uri=CVE.cvss4_sub_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss4SubCia"]])

slots.cvss4_sub_integrity_impact = Slot(uri=CVE.cvss4_sub_integrity_impact, name="cvss4_sub_integrity_impact", curie=CVE.curie('cvss4_sub_integrity_impact'),
                   model_uri=CVE.cvss4_sub_integrity_impact, domain=None, range=Optional[Union[str, "Cvss4SubCia"]])

slots.cvss4_sub_availability_impact = Slot(uri=CVE.cvss4_sub_availability_impact, name="cvss4_sub_availability_impact", curie=CVE.curie('cvss4_sub_availability_impact'),
                   model_uri=CVE.cvss4_sub_availability_impact, domain=None, range=Optional[Union[str, "Cvss4SubCia"]])

slots.cvss4_exploit_maturity = Slot(uri=CVE.cvss4_exploit_maturity, name="cvss4_exploit_maturity", curie=CVE.curie('cvss4_exploit_maturity'),
                   model_uri=CVE.cvss4_exploit_maturity, domain=None, range=Optional[Union[str, "Cvss4ExploitMaturity"]])

slots.cvss4_confidentiality_requirement = Slot(uri=CVE.cvss4_confidentiality_requirement, name="cvss4_confidentiality_requirement", curie=CVE.curie('cvss4_confidentiality_requirement'),
                   model_uri=CVE.cvss4_confidentiality_requirement, domain=None, range=Optional[Union[str, "Cvss4CiaRequirement"]])

slots.cvss4_integrity_requirement = Slot(uri=CVE.cvss4_integrity_requirement, name="cvss4_integrity_requirement", curie=CVE.curie('cvss4_integrity_requirement'),
                   model_uri=CVE.cvss4_integrity_requirement, domain=None, range=Optional[Union[str, "Cvss4CiaRequirement"]])

slots.cvss4_availability_requirement = Slot(uri=CVE.cvss4_availability_requirement, name="cvss4_availability_requirement", curie=CVE.curie('cvss4_availability_requirement'),
                   model_uri=CVE.cvss4_availability_requirement, domain=None, range=Optional[Union[str, "Cvss4CiaRequirement"]])

slots.cvss4_modified_attack_vector = Slot(uri=CVE.cvss4_modified_attack_vector, name="cvss4_modified_attack_vector", curie=CVE.curie('cvss4_modified_attack_vector'),
                   model_uri=CVE.cvss4_modified_attack_vector, domain=None, range=Optional[Union[str, "Cvss4ModifiedAttackVector"]])

slots.cvss4_modified_attack_complexity = Slot(uri=CVE.cvss4_modified_attack_complexity, name="cvss4_modified_attack_complexity", curie=CVE.curie('cvss4_modified_attack_complexity'),
                   model_uri=CVE.cvss4_modified_attack_complexity, domain=None, range=Optional[Union[str, "Cvss4ModifiedAttackComplexity"]])

slots.cvss4_modified_attack_requirements = Slot(uri=CVE.cvss4_modified_attack_requirements, name="cvss4_modified_attack_requirements", curie=CVE.curie('cvss4_modified_attack_requirements'),
                   model_uri=CVE.cvss4_modified_attack_requirements, domain=None, range=Optional[Union[str, "Cvss4ModifiedAttackRequirements"]])

slots.cvss4_modified_privileges_required = Slot(uri=CVE.cvss4_modified_privileges_required, name="cvss4_modified_privileges_required", curie=CVE.curie('cvss4_modified_privileges_required'),
                   model_uri=CVE.cvss4_modified_privileges_required, domain=None, range=Optional[Union[str, "Cvss4ModifiedPrivilegesRequired"]])

slots.cvss4_modified_user_interaction = Slot(uri=CVE.cvss4_modified_user_interaction, name="cvss4_modified_user_interaction", curie=CVE.curie('cvss4_modified_user_interaction'),
                   model_uri=CVE.cvss4_modified_user_interaction, domain=None, range=Optional[Union[str, "Cvss4ModifiedUserInteraction"]])

slots.cvss4_modified_vuln_confidentiality_impact = Slot(uri=CVE.cvss4_modified_vuln_confidentiality_impact, name="cvss4_modified_vuln_confidentiality_impact", curie=CVE.curie('cvss4_modified_vuln_confidentiality_impact'),
                   model_uri=CVE.cvss4_modified_vuln_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedVulnCia"]])

slots.cvss4_modified_vuln_integrity_impact = Slot(uri=CVE.cvss4_modified_vuln_integrity_impact, name="cvss4_modified_vuln_integrity_impact", curie=CVE.curie('cvss4_modified_vuln_integrity_impact'),
                   model_uri=CVE.cvss4_modified_vuln_integrity_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedVulnCia"]])

slots.cvss4_modified_vuln_availability_impact = Slot(uri=CVE.cvss4_modified_vuln_availability_impact, name="cvss4_modified_vuln_availability_impact", curie=CVE.curie('cvss4_modified_vuln_availability_impact'),
                   model_uri=CVE.cvss4_modified_vuln_availability_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedVulnCia"]])

slots.cvss4_modified_sub_confidentiality_impact = Slot(uri=CVE.cvss4_modified_sub_confidentiality_impact, name="cvss4_modified_sub_confidentiality_impact", curie=CVE.curie('cvss4_modified_sub_confidentiality_impact'),
                   model_uri=CVE.cvss4_modified_sub_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedSubC"]])

slots.cvss4_modified_sub_integrity_impact = Slot(uri=CVE.cvss4_modified_sub_integrity_impact, name="cvss4_modified_sub_integrity_impact", curie=CVE.curie('cvss4_modified_sub_integrity_impact'),
                   model_uri=CVE.cvss4_modified_sub_integrity_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedSubIa"]])

slots.cvss4_modified_sub_availability_impact = Slot(uri=CVE.cvss4_modified_sub_availability_impact, name="cvss4_modified_sub_availability_impact", curie=CVE.curie('cvss4_modified_sub_availability_impact'),
                   model_uri=CVE.cvss4_modified_sub_availability_impact, domain=None, range=Optional[Union[str, "Cvss4ModifiedSubIa"]])

slots.cvss4_safety = Slot(uri=CVE.cvss4_safety, name="cvss4_safety", curie=CVE.curie('cvss4_safety'),
                   model_uri=CVE.cvss4_safety, domain=None, range=Optional[Union[str, "Cvss4Safety"]])

slots.cvss4_automatable = Slot(uri=CVE.cvss4_automatable, name="cvss4_automatable", curie=CVE.curie('cvss4_automatable'),
                   model_uri=CVE.cvss4_automatable, domain=None, range=Optional[Union[str, "Cvss4Automatable"]])

slots.cvss4_recovery = Slot(uri=CVE.cvss4_recovery, name="cvss4_recovery", curie=CVE.curie('cvss4_recovery'),
                   model_uri=CVE.cvss4_recovery, domain=None, range=Optional[Union[str, "Cvss4Recovery"]])

slots.cvss4_value_density = Slot(uri=CVE.cvss4_value_density, name="cvss4_value_density", curie=CVE.curie('cvss4_value_density'),
                   model_uri=CVE.cvss4_value_density, domain=None, range=Optional[Union[str, "Cvss4ValueDensity"]])

slots.cvss4_vulnerability_response_effort = Slot(uri=CVE.cvss4_vulnerability_response_effort, name="cvss4_vulnerability_response_effort", curie=CVE.curie('cvss4_vulnerability_response_effort'),
                   model_uri=CVE.cvss4_vulnerability_response_effort, domain=None, range=Optional[Union[str, "Cvss4VulnerabilityResponseEffort"]])

slots.cvss4_provider_urgency = Slot(uri=CVE.cvss4_provider_urgency, name="cvss4_provider_urgency", curie=CVE.curie('cvss4_provider_urgency'),
                   model_uri=CVE.cvss4_provider_urgency, domain=None, range=Optional[Union[str, "Cvss4ProviderUrgency"]])

slots.cvss3_version = Slot(uri=CVE.cvss3_version, name="cvss3_version", curie=CVE.curie('cvss3_version'),
                   model_uri=CVE.cvss3_version, domain=None, range=Optional[Union[str, "CvssV3Version"]])

slots.cvss3_vector_string = Slot(uri=CVE.cvss3_vector_string, name="cvss3_vector_string", curie=CVE.curie('cvss3_vector_string'),
                   model_uri=CVE.cvss3_vector_string, domain=None, range=Optional[str])

slots.cvss3_attack_vector = Slot(uri=CVE.cvss3_attack_vector, name="cvss3_attack_vector", curie=CVE.curie('cvss3_attack_vector'),
                   model_uri=CVE.cvss3_attack_vector, domain=None, range=Optional[Union[str, "Cvss3AttackVector"]])

slots.cvss3_attack_complexity = Slot(uri=CVE.cvss3_attack_complexity, name="cvss3_attack_complexity", curie=CVE.curie('cvss3_attack_complexity'),
                   model_uri=CVE.cvss3_attack_complexity, domain=None, range=Optional[Union[str, "Cvss3AttackComplexity"]])

slots.cvss3_privileges_required = Slot(uri=CVE.cvss3_privileges_required, name="cvss3_privileges_required", curie=CVE.curie('cvss3_privileges_required'),
                   model_uri=CVE.cvss3_privileges_required, domain=None, range=Optional[Union[str, "Cvss3PrivilegesRequired"]])

slots.cvss3_user_interaction = Slot(uri=CVE.cvss3_user_interaction, name="cvss3_user_interaction", curie=CVE.curie('cvss3_user_interaction'),
                   model_uri=CVE.cvss3_user_interaction, domain=None, range=Optional[Union[str, "Cvss3UserInteraction"]])

slots.cvss3_scope = Slot(uri=CVE.cvss3_scope, name="cvss3_scope", curie=CVE.curie('cvss3_scope'),
                   model_uri=CVE.cvss3_scope, domain=None, range=Optional[Union[str, "Cvss3Scope"]])

slots.cvss3_confidentiality_impact = Slot(uri=CVE.cvss3_confidentiality_impact, name="cvss3_confidentiality_impact", curie=CVE.curie('cvss3_confidentiality_impact'),
                   model_uri=CVE.cvss3_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss3Cia"]])

slots.cvss3_integrity_impact = Slot(uri=CVE.cvss3_integrity_impact, name="cvss3_integrity_impact", curie=CVE.curie('cvss3_integrity_impact'),
                   model_uri=CVE.cvss3_integrity_impact, domain=None, range=Optional[Union[str, "Cvss3Cia"]])

slots.cvss3_availability_impact = Slot(uri=CVE.cvss3_availability_impact, name="cvss3_availability_impact", curie=CVE.curie('cvss3_availability_impact'),
                   model_uri=CVE.cvss3_availability_impact, domain=None, range=Optional[Union[str, "Cvss3Cia"]])

slots.cvss3_base_score = Slot(uri=CVE.cvss3_base_score, name="cvss3_base_score", curie=CVE.curie('cvss3_base_score'),
                   model_uri=CVE.cvss3_base_score, domain=None, range=Optional[float])

slots.cvss3_base_severity = Slot(uri=CVE.cvss3_base_severity, name="cvss3_base_severity", curie=CVE.curie('cvss3_base_severity'),
                   model_uri=CVE.cvss3_base_severity, domain=None, range=Optional[Union[str, "Cvss3Severity"]])

slots.cvss3_exploit_code_maturity = Slot(uri=CVE.cvss3_exploit_code_maturity, name="cvss3_exploit_code_maturity", curie=CVE.curie('cvss3_exploit_code_maturity'),
                   model_uri=CVE.cvss3_exploit_code_maturity, domain=None, range=Optional[Union[str, "Cvss3ExploitCodeMaturity"]])

slots.cvss3_remediation_level = Slot(uri=CVE.cvss3_remediation_level, name="cvss3_remediation_level", curie=CVE.curie('cvss3_remediation_level'),
                   model_uri=CVE.cvss3_remediation_level, domain=None, range=Optional[Union[str, "Cvss3RemediationLevel"]])

slots.cvss3_report_confidence = Slot(uri=CVE.cvss3_report_confidence, name="cvss3_report_confidence", curie=CVE.curie('cvss3_report_confidence'),
                   model_uri=CVE.cvss3_report_confidence, domain=None, range=Optional[Union[str, "Cvss3Confidence"]])

slots.cvss3_temporal_score = Slot(uri=CVE.cvss3_temporal_score, name="cvss3_temporal_score", curie=CVE.curie('cvss3_temporal_score'),
                   model_uri=CVE.cvss3_temporal_score, domain=None, range=Optional[float])

slots.cvss3_temporal_severity = Slot(uri=CVE.cvss3_temporal_severity, name="cvss3_temporal_severity", curie=CVE.curie('cvss3_temporal_severity'),
                   model_uri=CVE.cvss3_temporal_severity, domain=None, range=Optional[Union[str, "Cvss3Severity"]])

slots.cvss3_confidentiality_requirement = Slot(uri=CVE.cvss3_confidentiality_requirement, name="cvss3_confidentiality_requirement", curie=CVE.curie('cvss3_confidentiality_requirement'),
                   model_uri=CVE.cvss3_confidentiality_requirement, domain=None, range=Optional[Union[str, "Cvss3CiaRequirement"]])

slots.cvss3_integrity_requirement = Slot(uri=CVE.cvss3_integrity_requirement, name="cvss3_integrity_requirement", curie=CVE.curie('cvss3_integrity_requirement'),
                   model_uri=CVE.cvss3_integrity_requirement, domain=None, range=Optional[Union[str, "Cvss3CiaRequirement"]])

slots.cvss3_availability_requirement = Slot(uri=CVE.cvss3_availability_requirement, name="cvss3_availability_requirement", curie=CVE.curie('cvss3_availability_requirement'),
                   model_uri=CVE.cvss3_availability_requirement, domain=None, range=Optional[Union[str, "Cvss3CiaRequirement"]])

slots.cvss3_modified_attack_vector = Slot(uri=CVE.cvss3_modified_attack_vector, name="cvss3_modified_attack_vector", curie=CVE.curie('cvss3_modified_attack_vector'),
                   model_uri=CVE.cvss3_modified_attack_vector, domain=None, range=Optional[Union[str, "Cvss3ModifiedAttackVector"]])

slots.cvss3_modified_attack_complexity = Slot(uri=CVE.cvss3_modified_attack_complexity, name="cvss3_modified_attack_complexity", curie=CVE.curie('cvss3_modified_attack_complexity'),
                   model_uri=CVE.cvss3_modified_attack_complexity, domain=None, range=Optional[Union[str, "Cvss3ModifiedAttackComplexity"]])

slots.cvss3_modified_privileges_required = Slot(uri=CVE.cvss3_modified_privileges_required, name="cvss3_modified_privileges_required", curie=CVE.curie('cvss3_modified_privileges_required'),
                   model_uri=CVE.cvss3_modified_privileges_required, domain=None, range=Optional[Union[str, "Cvss3ModifiedPrivilegesRequired"]])

slots.cvss3_modified_user_interaction = Slot(uri=CVE.cvss3_modified_user_interaction, name="cvss3_modified_user_interaction", curie=CVE.curie('cvss3_modified_user_interaction'),
                   model_uri=CVE.cvss3_modified_user_interaction, domain=None, range=Optional[Union[str, "Cvss3ModifiedUserInteraction"]])

slots.cvss3_modified_scope = Slot(uri=CVE.cvss3_modified_scope, name="cvss3_modified_scope", curie=CVE.curie('cvss3_modified_scope'),
                   model_uri=CVE.cvss3_modified_scope, domain=None, range=Optional[Union[str, "Cvss3ModifiedScope"]])

slots.cvss3_modified_confidentiality_impact = Slot(uri=CVE.cvss3_modified_confidentiality_impact, name="cvss3_modified_confidentiality_impact", curie=CVE.curie('cvss3_modified_confidentiality_impact'),
                   model_uri=CVE.cvss3_modified_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss3ModifiedCia"]])

slots.cvss3_modified_integrity_impact = Slot(uri=CVE.cvss3_modified_integrity_impact, name="cvss3_modified_integrity_impact", curie=CVE.curie('cvss3_modified_integrity_impact'),
                   model_uri=CVE.cvss3_modified_integrity_impact, domain=None, range=Optional[Union[str, "Cvss3ModifiedCia"]])

slots.cvss3_modified_availability_impact = Slot(uri=CVE.cvss3_modified_availability_impact, name="cvss3_modified_availability_impact", curie=CVE.curie('cvss3_modified_availability_impact'),
                   model_uri=CVE.cvss3_modified_availability_impact, domain=None, range=Optional[Union[str, "Cvss3ModifiedCia"]])

slots.cvss3_environmental_score = Slot(uri=CVE.cvss3_environmental_score, name="cvss3_environmental_score", curie=CVE.curie('cvss3_environmental_score'),
                   model_uri=CVE.cvss3_environmental_score, domain=None, range=Optional[float])

slots.cvss3_environmental_severity = Slot(uri=CVE.cvss3_environmental_severity, name="cvss3_environmental_severity", curie=CVE.curie('cvss3_environmental_severity'),
                   model_uri=CVE.cvss3_environmental_severity, domain=None, range=Optional[Union[str, "Cvss3Severity"]])

slots.cvss2_version = Slot(uri=CVE.cvss2_version, name="cvss2_version", curie=CVE.curie('cvss2_version'),
                   model_uri=CVE.cvss2_version, domain=None, range=Optional[str])

slots.cvss2_vector_string = Slot(uri=CVE.cvss2_vector_string, name="cvss2_vector_string", curie=CVE.curie('cvss2_vector_string'),
                   model_uri=CVE.cvss2_vector_string, domain=None, range=Optional[str],
                   pattern=re.compile(r'^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'))

slots.cvss2_access_vector = Slot(uri=CVE.cvss2_access_vector, name="cvss2_access_vector", curie=CVE.curie('cvss2_access_vector'),
                   model_uri=CVE.cvss2_access_vector, domain=None, range=Optional[Union[str, "Cvss2AccessVector"]])

slots.cvss2_access_complexity = Slot(uri=CVE.cvss2_access_complexity, name="cvss2_access_complexity", curie=CVE.curie('cvss2_access_complexity'),
                   model_uri=CVE.cvss2_access_complexity, domain=None, range=Optional[Union[str, "Cvss2AccessComplexity"]])

slots.cvss2_authentication = Slot(uri=CVE.cvss2_authentication, name="cvss2_authentication", curie=CVE.curie('cvss2_authentication'),
                   model_uri=CVE.cvss2_authentication, domain=None, range=Optional[Union[str, "Cvss2Authentication"]])

slots.cvss2_confidentiality_impact = Slot(uri=CVE.cvss2_confidentiality_impact, name="cvss2_confidentiality_impact", curie=CVE.curie('cvss2_confidentiality_impact'),
                   model_uri=CVE.cvss2_confidentiality_impact, domain=None, range=Optional[Union[str, "Cvss2Cia"]])

slots.cvss2_integrity_impact = Slot(uri=CVE.cvss2_integrity_impact, name="cvss2_integrity_impact", curie=CVE.curie('cvss2_integrity_impact'),
                   model_uri=CVE.cvss2_integrity_impact, domain=None, range=Optional[Union[str, "Cvss2Cia"]])

slots.cvss2_availability_impact = Slot(uri=CVE.cvss2_availability_impact, name="cvss2_availability_impact", curie=CVE.curie('cvss2_availability_impact'),
                   model_uri=CVE.cvss2_availability_impact, domain=None, range=Optional[Union[str, "Cvss2Cia"]])

slots.cvss2_base_score = Slot(uri=CVE.cvss2_base_score, name="cvss2_base_score", curie=CVE.curie('cvss2_base_score'),
                   model_uri=CVE.cvss2_base_score, domain=None, range=Optional[float])

slots.cvss2_exploitability = Slot(uri=CVE.cvss2_exploitability, name="cvss2_exploitability", curie=CVE.curie('cvss2_exploitability'),
                   model_uri=CVE.cvss2_exploitability, domain=None, range=Optional[Union[str, "Cvss2Exploitability"]])

slots.cvss2_remediation_level = Slot(uri=CVE.cvss2_remediation_level, name="cvss2_remediation_level", curie=CVE.curie('cvss2_remediation_level'),
                   model_uri=CVE.cvss2_remediation_level, domain=None, range=Optional[Union[str, "Cvss2RemediationLevel"]])

slots.cvss2_report_confidence = Slot(uri=CVE.cvss2_report_confidence, name="cvss2_report_confidence", curie=CVE.curie('cvss2_report_confidence'),
                   model_uri=CVE.cvss2_report_confidence, domain=None, range=Optional[Union[str, "Cvss2ReportConfidence"]])

slots.cvss2_temporal_score = Slot(uri=CVE.cvss2_temporal_score, name="cvss2_temporal_score", curie=CVE.curie('cvss2_temporal_score'),
                   model_uri=CVE.cvss2_temporal_score, domain=None, range=Optional[float])

slots.cvss2_collateral_damage_potential = Slot(uri=CVE.cvss2_collateral_damage_potential, name="cvss2_collateral_damage_potential", curie=CVE.curie('cvss2_collateral_damage_potential'),
                   model_uri=CVE.cvss2_collateral_damage_potential, domain=None, range=Optional[Union[str, "Cvss2CollateralDamagePotential"]])

slots.cvss2_target_distribution = Slot(uri=CVE.cvss2_target_distribution, name="cvss2_target_distribution", curie=CVE.curie('cvss2_target_distribution'),
                   model_uri=CVE.cvss2_target_distribution, domain=None, range=Optional[Union[str, "Cvss2TargetDistribution"]])

slots.cvss2_confidentiality_requirement = Slot(uri=CVE.cvss2_confidentiality_requirement, name="cvss2_confidentiality_requirement", curie=CVE.curie('cvss2_confidentiality_requirement'),
                   model_uri=CVE.cvss2_confidentiality_requirement, domain=None, range=Optional[Union[str, "Cvss2CiaRequirement"]])

slots.cvss2_integrity_requirement = Slot(uri=CVE.cvss2_integrity_requirement, name="cvss2_integrity_requirement", curie=CVE.curie('cvss2_integrity_requirement'),
                   model_uri=CVE.cvss2_integrity_requirement, domain=None, range=Optional[Union[str, "Cvss2CiaRequirement"]])

slots.cvss2_availability_requirement = Slot(uri=CVE.cvss2_availability_requirement, name="cvss2_availability_requirement", curie=CVE.curie('cvss2_availability_requirement'),
                   model_uri=CVE.cvss2_availability_requirement, domain=None, range=Optional[Union[str, "Cvss2CiaRequirement"]])

slots.cvss2_environmental_score = Slot(uri=CVE.cvss2_environmental_score, name="cvss2_environmental_score", curie=CVE.curie('cvss2_environmental_score'),
                   model_uri=CVE.cvss2_environmental_score, domain=None, range=Optional[float])

slots.event_time = Slot(uri=CVE.event_time, name="event_time", curie=CVE.curie('event_time'),
                   model_uri=CVE.event_time, domain=None, range=Optional[str])

slots.event_value = Slot(uri=CVE.event_value, name="event_value", curie=CVE.curie('event_value'),
                   model_uri=CVE.event_value, domain=None, range=Optional[str])

slots.credit_value = Slot(uri=CVE.credit_value, name="credit_value", curie=CVE.curie('credit_value'),
                   model_uri=CVE.credit_value, domain=None, range=Optional[str])

slots.credit_user = Slot(uri=CVE.credit_user, name="credit_user", curie=CVE.curie('credit_user'),
                   model_uri=CVE.credit_user, domain=None, range=Optional[str])

slots.credit_type = Slot(uri=CVE.credit_type, name="credit_type", curie=CVE.curie('credit_type'),
                   model_uri=CVE.credit_type, domain=None, range=Optional[Union[str, "CreditType"]])

slots.taxonomy_name = Slot(uri=CVE.taxonomy_name, name="taxonomy_name", curie=CVE.curie('taxonomy_name'),
                   model_uri=CVE.taxonomy_name, domain=None, range=Optional[str])

slots.taxonomy_version = Slot(uri=CVE.taxonomy_version, name="taxonomy_version", curie=CVE.curie('taxonomy_version'),
                   model_uri=CVE.taxonomy_version, domain=None, range=Optional[str])

slots.taxonomy_relations = Slot(uri=CVE.taxonomy_relations, name="taxonomy_relations", curie=CVE.curie('taxonomy_relations'),
                   model_uri=CVE.taxonomy_relations, domain=None, range=Optional[Union[Union[dict, TaxonomyRelation], list[Union[dict, TaxonomyRelation]]]])

slots.taxonomy_id = Slot(uri=CVE.taxonomy_id, name="taxonomy_id", curie=CVE.curie('taxonomy_id'),
                   model_uri=CVE.taxonomy_id, domain=None, range=Optional[str])

slots.relationship_name = Slot(uri=CVE.relationship_name, name="relationship_name", curie=CVE.curie('relationship_name'),
                   model_uri=CVE.relationship_name, domain=None, range=Optional[str])

slots.relationship_value = Slot(uri=CVE.relationship_value, name="relationship_value", curie=CVE.curie('relationship_value'),
                   model_uri=CVE.relationship_value, domain=None, range=Optional[str])

slots.cpe_operator = Slot(uri=CVE.cpe_operator, name="cpe_operator", curie=CVE.curie('cpe_operator'),
                   model_uri=CVE.cpe_operator, domain=None, range=Optional[Union[str, "CpeOperator"]])

slots.cpe_negate = Slot(uri=CVE.cpe_negate, name="cpe_negate", curie=CVE.curie('cpe_negate'),
                   model_uri=CVE.cpe_negate, domain=None, range=Optional[Union[bool, Bool]])

slots.cpe_nodes = Slot(uri=CVE.cpe_nodes, name="cpe_nodes", curie=CVE.curie('cpe_nodes'),
                   model_uri=CVE.cpe_nodes, domain=None, range=Optional[Union[Union[dict, CpeNode], list[Union[dict, CpeNode]]]])

slots.cpe_match_criteria = Slot(uri=CVE.cpe_match_criteria, name="cpe_match_criteria", curie=CVE.curie('cpe_match_criteria'),
                   model_uri=CVE.cpe_match_criteria, domain=None, range=Optional[Union[Union[dict, CpeMatch], list[Union[dict, CpeMatch]]]])

slots.cpe_vulnerable = Slot(uri=CVE.cpe_vulnerable, name="cpe_vulnerable", curie=CVE.curie('cpe_vulnerable'),
                   model_uri=CVE.cpe_vulnerable, domain=None, range=Optional[Union[bool, Bool]])

slots.cpe_criteria = Slot(uri=CVE.cpe_criteria, name="cpe_criteria", curie=CVE.curie('cpe_criteria'),
                   model_uri=CVE.cpe_criteria, domain=None, range=Optional[str])

slots.match_criteria_id = Slot(uri=CVE.match_criteria_id, name="match_criteria_id", curie=CVE.curie('match_criteria_id'),
                   model_uri=CVE.match_criteria_id, domain=None, range=Optional[str])

slots.version_start_excluding = Slot(uri=CVE.version_start_excluding, name="version_start_excluding", curie=CVE.curie('version_start_excluding'),
                   model_uri=CVE.version_start_excluding, domain=None, range=Optional[str])

slots.version_start_including = Slot(uri=CVE.version_start_including, name="version_start_including", curie=CVE.curie('version_start_including'),
                   model_uri=CVE.version_start_including, domain=None, range=Optional[str])

slots.version_end_excluding = Slot(uri=CVE.version_end_excluding, name="version_end_excluding", curie=CVE.curie('version_end_excluding'),
                   model_uri=CVE.version_end_excluding, domain=None, range=Optional[str])

slots.version_end_including = Slot(uri=CVE.version_end_including, name="version_end_including", curie=CVE.curie('version_end_including'),
                   model_uri=CVE.version_end_including, domain=None, range=Optional[str])

slots.cve_id = Slot(uri=DCT.identifier, name="cve_id", curie=DCT.curie('identifier'),
                   model_uri=CVE.cve_id, domain=None, range=URIRef)

slots.title = Slot(uri=DCT.title, name="title", curie=DCT.curie('title'),
                   model_uri=CVE.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCT.description, name="description", curie=DCT.curie('description'),
                   model_uri=CVE.description, domain=None, range=Optional[str])

slots.published_date = Slot(uri=DCT.created, name="published_date", curie=DCT.curie('created'),
                   model_uri=CVE.published_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.last_modified_date = Slot(uri=DCT.modified, name="last_modified_date", curie=DCT.curie('modified'),
                   model_uri=CVE.last_modified_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.products = Slot(uri=CORE.products, name="products", curie=CORE.curie('products'),
                   model_uri=CVE.products, domain=None, range=Optional[Union[Union[dict, Product], list[Union[dict, Product]]]])

slots.weaknesses = Slot(uri=CORE.weaknesses, name="weaknesses", curie=CORE.curie('weaknesses'),
                   model_uri=CVE.weaknesses, domain=None, range=Optional[Union[Union[dict, Weakness], list[Union[dict, Weakness]]]])

slots.references = Slot(uri=CORE.references, name="references", curie=CORE.curie('references'),
                   model_uri=CVE.references, domain=None, range=Optional[Union[Union[dict, Reference], list[Union[dict, Reference]]]])

slots.impact = Slot(uri=CORE.impact, name="impact", curie=CORE.curie('impact'),
                   model_uri=CVE.impact, domain=None, range=Optional[Union[dict, Impact]])

slots.status = Slot(uri=CORE.status, name="status", curie=CORE.curie('status'),
                   model_uri=CVE.status, domain=None, range=Optional[Union[str, "VulnerabilityStatus"]])

slots.vendor = Slot(uri=SCHEMA.name, name="vendor", curie=SCHEMA.curie('name'),
                   model_uri=CVE.vendor, domain=None, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=CVE.name, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=CVE.version, domain=None, range=Optional[str])

slots.platforms = Slot(uri=CORE.platforms, name="platforms", curie=CORE.curie('platforms'),
                   model_uri=CVE.platforms, domain=None, range=Optional[Union[str, list[str]]])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=CVE.url, domain=None, range=Optional[Union[str, URI]])

slots.source = Slot(uri=DCT.source, name="source", curie=DCT.curie('source'),
                   model_uri=CVE.source, domain=None, range=Optional[str])

slots.cwe_id = Slot(uri=DCT.identifier, name="cwe_id", curie=DCT.curie('identifier'),
                   model_uri=CVE.cwe_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CWE-[1-9][0-9]*$'))

slots.severity = Slot(uri=CORE.severity, name="severity", curie=CORE.curie('severity'),
                   model_uri=CVE.severity, domain=None, range=Optional[Union[str, "ImpactSeverity"]])

slots.vector = Slot(uri=CORE.vector, name="vector", curie=CORE.curie('vector'),
                   model_uri=CVE.vector, domain=None, range=Optional[str])

slots.score = Slot(uri=CORE.score, name="score", curie=CORE.curie('score'),
                   model_uri=CVE.score, domain=None, range=Optional[float])

slots.cpe_uri = Slot(uri=CORE.cpe_uri, name="cpe_uri", curie=CORE.curie('cpe_uri'),
                   model_uri=CVE.cpe_uri, domain=None, range=Optional[str])

slots.operator = Slot(uri=CORE.operator, name="operator", curie=CORE.curie('operator'),
                   model_uri=CVE.operator, domain=None, range=Optional[str])

slots.CVERecord_cve_id = Slot(uri=DCT.identifier, name="CVERecord_cve_id", curie=DCT.curie('identifier'),
                   model_uri=CVE.CVERecord_cve_id, domain=CVERecord, range=Union[str, CVERecordCveId])

slots.CVERecord_cve_metadata = Slot(uri=CVE.cve_metadata, name="CVERecord_cve_metadata", curie=CVE.curie('cve_metadata'),
                   model_uri=CVE.CVERecord_cve_metadata, domain=CVERecord, range=Union[dict, CveMetadata])

slots.CVERecord_containers = Slot(uri=CVE.containers, name="CVERecord_containers", curie=CVE.curie('containers'),
                   model_uri=CVE.CVERecord_containers, domain=CVERecord, range=Union[dict, Containers])

slots.CveMetadataPublished_record_cve_id = Slot(uri=CVE.record_cve_id, name="CveMetadataPublished_record_cve_id", curie=CVE.curie('record_cve_id'),
                   model_uri=CVE.CveMetadataPublished_record_cve_id, domain=CveMetadataPublished, range=str,
                   pattern=re.compile(r'^CVE-[0-9]{4}-[0-9]{4,19}$'))

slots.CveMetadataPublished_assigner_org_id = Slot(uri=CVE.assigner_org_id, name="CveMetadataPublished_assigner_org_id", curie=CVE.curie('assigner_org_id'),
                   model_uri=CVE.CveMetadataPublished_assigner_org_id, domain=CveMetadataPublished, range=str)

slots.CveMetadataPublished_published_state = Slot(uri=CVE.published_state, name="CveMetadataPublished_published_state", curie=CVE.curie('published_state'),
                   model_uri=CVE.CveMetadataPublished_published_state, domain=CveMetadataPublished, range=Union[str, "RecordState"])

slots.CveMetadataRejected_record_cve_id = Slot(uri=CVE.record_cve_id, name="CveMetadataRejected_record_cve_id", curie=CVE.curie('record_cve_id'),
                   model_uri=CVE.CveMetadataRejected_record_cve_id, domain=CveMetadataRejected, range=str,
                   pattern=re.compile(r'^CVE-[0-9]{4}-[0-9]{4,19}$'))

slots.CveMetadataRejected_assigner_org_id = Slot(uri=CVE.assigner_org_id, name="CveMetadataRejected_assigner_org_id", curie=CVE.curie('assigner_org_id'),
                   model_uri=CVE.CveMetadataRejected_assigner_org_id, domain=CveMetadataRejected, range=str)

slots.CveMetadataRejected_rejected_state = Slot(uri=CVE.rejected_state, name="CveMetadataRejected_rejected_state", curie=CVE.curie('rejected_state'),
                   model_uri=CVE.CveMetadataRejected_rejected_state, domain=CveMetadataRejected, range=Union[str, "RecordState"])

slots.Containers_cna = Slot(uri=CVE.cna, name="Containers_cna", curie=CVE.curie('cna'),
                   model_uri=CVE.Containers_cna, domain=Containers, range=Union[dict, "CnaContainer"])

slots.ProviderMetadata_org_id = Slot(uri=CVE.org_id, name="ProviderMetadata_org_id", curie=CVE.curie('org_id'),
                   model_uri=CVE.ProviderMetadata_org_id, domain=ProviderMetadata, range=str)

slots.CnaPublishedContainer_provider_metadata = Slot(uri=CVE.provider_metadata, name="CnaPublishedContainer_provider_metadata", curie=CVE.curie('provider_metadata'),
                   model_uri=CVE.CnaPublishedContainer_provider_metadata, domain=CnaPublishedContainer, range=Union[dict, ProviderMetadata])

slots.CnaPublishedContainer_descriptions = Slot(uri=CVE.descriptions, name="CnaPublishedContainer_descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.CnaPublishedContainer_descriptions, domain=CnaPublishedContainer, range=Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]])

slots.CnaPublishedContainer_affected = Slot(uri=CVE.affected, name="CnaPublishedContainer_affected", curie=CVE.curie('affected'),
                   model_uri=CVE.CnaPublishedContainer_affected, domain=CnaPublishedContainer, range=Union[Union[dict, "AffectedProduct"], list[Union[dict, "AffectedProduct"]]])

slots.CnaPublishedContainer_cve_references = Slot(uri=CVE.cve_references, name="CnaPublishedContainer_cve_references", curie=CVE.curie('cve_references'),
                   model_uri=CVE.CnaPublishedContainer_cve_references, domain=CnaPublishedContainer, range=Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]])

slots.CnaRejectedContainer_provider_metadata = Slot(uri=CVE.provider_metadata, name="CnaRejectedContainer_provider_metadata", curie=CVE.curie('provider_metadata'),
                   model_uri=CVE.CnaRejectedContainer_provider_metadata, domain=CnaRejectedContainer, range=Union[dict, ProviderMetadata])

slots.CnaRejectedContainer_rejected_reasons = Slot(uri=CVE.rejected_reasons, name="CnaRejectedContainer_rejected_reasons", curie=CVE.curie('rejected_reasons'),
                   model_uri=CVE.CnaRejectedContainer_rejected_reasons, domain=CnaRejectedContainer, range=Union[Union[dict, "MultiLangDescription"], list[Union[dict, "MultiLangDescription"]]])

slots.AdpContainer_provider_metadata = Slot(uri=CVE.provider_metadata, name="AdpContainer_provider_metadata", curie=CVE.curie('provider_metadata'),
                   model_uri=CVE.AdpContainer_provider_metadata, domain=AdpContainer, range=Union[dict, ProviderMetadata])

slots.ProgramRoutine_routine_name = Slot(uri=CVE.routine_name, name="ProgramRoutine_routine_name", curie=CVE.curie('routine_name'),
                   model_uri=CVE.ProgramRoutine_routine_name, domain=ProgramRoutine, range=str)

slots.VersionEntry_version_value = Slot(uri=CVE.version_value, name="VersionEntry_version_value", curie=CVE.curie('version_value'),
                   model_uri=CVE.VersionEntry_version_value, domain=VersionEntry, range=str)

slots.VersionEntry_version_status = Slot(uri=CVE.version_status, name="VersionEntry_version_status", curie=CVE.curie('version_status'),
                   model_uri=CVE.VersionEntry_version_status, domain=VersionEntry, range=Union[str, "VersionStatus"])

slots.VersionChange_change_at = Slot(uri=CVE.change_at, name="VersionChange_change_at", curie=CVE.curie('change_at'),
                   model_uri=CVE.VersionChange_change_at, domain=VersionChange, range=str)

slots.VersionChange_change_status = Slot(uri=CVE.change_status, name="VersionChange_change_status", curie=CVE.curie('change_status'),
                   model_uri=CVE.VersionChange_change_status, domain=VersionChange, range=Union[str, "VersionStatus"])

slots.MultiLangDescription_lang = Slot(uri=CVE.lang, name="MultiLangDescription_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.MultiLangDescription_lang, domain=MultiLangDescription, range=str)

slots.MultiLangDescription_description_value = Slot(uri=CVE.description_value, name="MultiLangDescription_description_value", curie=CVE.curie('description_value'),
                   model_uri=CVE.MultiLangDescription_description_value, domain=MultiLangDescription, range=str)

slots.SupportingMedia_media_type = Slot(uri=CVE.media_type, name="SupportingMedia_media_type", curie=CVE.curie('media_type'),
                   model_uri=CVE.SupportingMedia_media_type, domain=SupportingMedia, range=str)

slots.SupportingMedia_media_value = Slot(uri=CVE.media_value, name="SupportingMedia_media_value", curie=CVE.curie('media_value'),
                   model_uri=CVE.SupportingMedia_media_value, domain=SupportingMedia, range=str)

slots.ProblemType_problem_type_descriptions = Slot(uri=CVE.problem_type_descriptions, name="ProblemType_problem_type_descriptions", curie=CVE.curie('problem_type_descriptions'),
                   model_uri=CVE.ProblemType_problem_type_descriptions, domain=ProblemType, range=Union[Union[dict, "ProblemTypeDescription"], list[Union[dict, "ProblemTypeDescription"]]])

slots.ProblemTypeDescription_lang = Slot(uri=CVE.lang, name="ProblemTypeDescription_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.ProblemTypeDescription_lang, domain=ProblemTypeDescription, range=str)

slots.ProblemTypeDescription_problem_description = Slot(uri=CVE.problem_description, name="ProblemTypeDescription_problem_description", curie=CVE.curie('problem_description'),
                   model_uri=CVE.ProblemTypeDescription_problem_description, domain=ProblemTypeDescription, range=str)

slots.ProblemTypeDescription_cwe_id = Slot(uri=DCT.identifier, name="ProblemTypeDescription_cwe_id", curie=DCT.curie('identifier'),
                   model_uri=CVE.ProblemTypeDescription_cwe_id, domain=ProblemTypeDescription, range=Optional[str],
                   pattern=re.compile(r'^CWE-[1-9][0-9]*$'))

slots.CveReference_url = Slot(uri=SCHEMA.url, name="CveReference_url", curie=SCHEMA.curie('url'),
                   model_uri=CVE.CveReference_url, domain=CveReference, range=Union[str, URI])

slots.ImpactEntry_impact_descriptions = Slot(uri=CVE.impact_descriptions, name="ImpactEntry_impact_descriptions", curie=CVE.curie('impact_descriptions'),
                   model_uri=CVE.ImpactEntry_impact_descriptions, domain=ImpactEntry, range=Union[Union[dict, MultiLangDescription], list[Union[dict, MultiLangDescription]]])

slots.MetricScenario_lang = Slot(uri=CVE.lang, name="MetricScenario_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.MetricScenario_lang, domain=MetricScenario, range=str)

slots.MetricScenario_scenario_value = Slot(uri=CVE.scenario_value, name="MetricScenario_scenario_value", curie=CVE.curie('scenario_value'),
                   model_uri=CVE.MetricScenario_scenario_value, domain=MetricScenario, range=str)

slots.CvssV4_0_cvss4_version = Slot(uri=CVE.cvss4_version, name="CvssV4_0_cvss4_version", curie=CVE.curie('cvss4_version'),
                   model_uri=CVE.CvssV4_0_cvss4_version, domain=CvssV40, range=str)

slots.CvssV4_0_cvss4_vector_string = Slot(uri=CVE.cvss4_vector_string, name="CvssV4_0_cvss4_vector_string", curie=CVE.curie('cvss4_vector_string'),
                   model_uri=CVE.CvssV4_0_cvss4_vector_string, domain=CvssV40, range=str,
                   pattern=re.compile(r'^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'))

slots.CvssV4_0_cvss4_base_score = Slot(uri=CVE.cvss4_base_score, name="CvssV4_0_cvss4_base_score", curie=CVE.curie('cvss4_base_score'),
                   model_uri=CVE.CvssV4_0_cvss4_base_score, domain=CvssV40, range=float)

slots.CvssV4_0_cvss4_base_severity = Slot(uri=CVE.cvss4_base_severity, name="CvssV4_0_cvss4_base_severity", curie=CVE.curie('cvss4_base_severity'),
                   model_uri=CVE.CvssV4_0_cvss4_base_severity, domain=CvssV40, range=Union[str, "Cvss4Severity"])

slots.CvssV3_cvss3_version = Slot(uri=CVE.cvss3_version, name="CvssV3_cvss3_version", curie=CVE.curie('cvss3_version'),
                   model_uri=CVE.CvssV3_cvss3_version, domain=CvssV3, range=Union[str, "CvssV3Version"])

slots.CvssV3_cvss3_vector_string = Slot(uri=CVE.cvss3_vector_string, name="CvssV3_cvss3_vector_string", curie=CVE.curie('cvss3_vector_string'),
                   model_uri=CVE.CvssV3_cvss3_vector_string, domain=CvssV3, range=str)

slots.CvssV3_cvss3_base_score = Slot(uri=CVE.cvss3_base_score, name="CvssV3_cvss3_base_score", curie=CVE.curie('cvss3_base_score'),
                   model_uri=CVE.CvssV3_cvss3_base_score, domain=CvssV3, range=float)

slots.CvssV3_cvss3_base_severity = Slot(uri=CVE.cvss3_base_severity, name="CvssV3_cvss3_base_severity", curie=CVE.curie('cvss3_base_severity'),
                   model_uri=CVE.CvssV3_cvss3_base_severity, domain=CvssV3, range=Union[str, "Cvss3Severity"])

slots.CvssV2_0_cvss2_version = Slot(uri=CVE.cvss2_version, name="CvssV2_0_cvss2_version", curie=CVE.curie('cvss2_version'),
                   model_uri=CVE.CvssV2_0_cvss2_version, domain=CvssV20, range=str)

slots.CvssV2_0_cvss2_vector_string = Slot(uri=CVE.cvss2_vector_string, name="CvssV2_0_cvss2_vector_string", curie=CVE.curie('cvss2_vector_string'),
                   model_uri=CVE.CvssV2_0_cvss2_vector_string, domain=CvssV20, range=str,
                   pattern=re.compile(r'^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'))

slots.CvssV2_0_cvss2_base_score = Slot(uri=CVE.cvss2_base_score, name="CvssV2_0_cvss2_base_score", curie=CVE.curie('cvss2_base_score'),
                   model_uri=CVE.CvssV2_0_cvss2_base_score, domain=CvssV20, range=float)

slots.OtherMetric_other_metric_type = Slot(uri=CVE.other_metric_type, name="OtherMetric_other_metric_type", curie=CVE.curie('other_metric_type'),
                   model_uri=CVE.OtherMetric_other_metric_type, domain=OtherMetric, range=str)

slots.OtherMetric_other_metric_content = Slot(uri=CVE.other_metric_content, name="OtherMetric_other_metric_content", curie=CVE.curie('other_metric_content'),
                   model_uri=CVE.OtherMetric_other_metric_content, domain=OtherMetric, range=Union[dict, Any])

slots.TimelineEntry_event_time = Slot(uri=CVE.event_time, name="TimelineEntry_event_time", curie=CVE.curie('event_time'),
                   model_uri=CVE.TimelineEntry_event_time, domain=TimelineEntry, range=str)

slots.TimelineEntry_lang = Slot(uri=CVE.lang, name="TimelineEntry_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.TimelineEntry_lang, domain=TimelineEntry, range=str)

slots.TimelineEntry_event_value = Slot(uri=CVE.event_value, name="TimelineEntry_event_value", curie=CVE.curie('event_value'),
                   model_uri=CVE.TimelineEntry_event_value, domain=TimelineEntry, range=str)

slots.CreditEntry_lang = Slot(uri=CVE.lang, name="CreditEntry_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CreditEntry_lang, domain=CreditEntry, range=str)

slots.CreditEntry_credit_value = Slot(uri=CVE.credit_value, name="CreditEntry_credit_value", curie=CVE.curie('credit_value'),
                   model_uri=CVE.CreditEntry_credit_value, domain=CreditEntry, range=str)

slots.TaxonomyMapping_taxonomy_name = Slot(uri=CVE.taxonomy_name, name="TaxonomyMapping_taxonomy_name", curie=CVE.curie('taxonomy_name'),
                   model_uri=CVE.TaxonomyMapping_taxonomy_name, domain=TaxonomyMapping, range=str)

slots.TaxonomyMapping_taxonomy_relations = Slot(uri=CVE.taxonomy_relations, name="TaxonomyMapping_taxonomy_relations", curie=CVE.curie('taxonomy_relations'),
                   model_uri=CVE.TaxonomyMapping_taxonomy_relations, domain=TaxonomyMapping, range=Union[Union[dict, "TaxonomyRelation"], list[Union[dict, "TaxonomyRelation"]]])

slots.TaxonomyRelation_taxonomy_id = Slot(uri=CVE.taxonomy_id, name="TaxonomyRelation_taxonomy_id", curie=CVE.curie('taxonomy_id'),
                   model_uri=CVE.TaxonomyRelation_taxonomy_id, domain=TaxonomyRelation, range=str)

slots.TaxonomyRelation_relationship_name = Slot(uri=CVE.relationship_name, name="TaxonomyRelation_relationship_name", curie=CVE.curie('relationship_name'),
                   model_uri=CVE.TaxonomyRelation_relationship_name, domain=TaxonomyRelation, range=str)

slots.TaxonomyRelation_relationship_value = Slot(uri=CVE.relationship_value, name="TaxonomyRelation_relationship_value", curie=CVE.curie('relationship_value'),
                   model_uri=CVE.TaxonomyRelation_relationship_value, domain=TaxonomyRelation, range=str)

slots.CpeApplicabilityElement_cpe_nodes = Slot(uri=CVE.cpe_nodes, name="CpeApplicabilityElement_cpe_nodes", curie=CVE.curie('cpe_nodes'),
                   model_uri=CVE.CpeApplicabilityElement_cpe_nodes, domain=CpeApplicabilityElement, range=Union[Union[dict, "CpeNode"], list[Union[dict, "CpeNode"]]])

slots.CpeNode_cpe_operator = Slot(uri=CVE.cpe_operator, name="CpeNode_cpe_operator", curie=CVE.curie('cpe_operator'),
                   model_uri=CVE.CpeNode_cpe_operator, domain=CpeNode, range=Union[str, "CpeOperator"])

slots.CpeNode_cpe_match_criteria = Slot(uri=CVE.cpe_match_criteria, name="CpeNode_cpe_match_criteria", curie=CVE.curie('cpe_match_criteria'),
                   model_uri=CVE.CpeNode_cpe_match_criteria, domain=CpeNode, range=Union[Union[dict, "CpeMatch"], list[Union[dict, "CpeMatch"]]])

slots.CpeMatch_cpe_vulnerable = Slot(uri=CVE.cpe_vulnerable, name="CpeMatch_cpe_vulnerable", curie=CVE.curie('cpe_vulnerable'),
                   model_uri=CVE.CpeMatch_cpe_vulnerable, domain=CpeMatch, range=Union[bool, Bool])

slots.CpeMatch_cpe_criteria = Slot(uri=CVE.cpe_criteria, name="CpeMatch_cpe_criteria", curie=CVE.curie('cpe_criteria'),
                   model_uri=CVE.CpeMatch_cpe_criteria, domain=CpeMatch, range=str)

slots.Vulnerability_cve_id = Slot(uri=DCT.identifier, name="Vulnerability_cve_id", curie=DCT.curie('identifier'),
                   model_uri=CVE.Vulnerability_cve_id, domain=Vulnerability, range=Union[str, VulnerabilityCveId])

slots.Vulnerability_description = Slot(uri=DCT.description, name="Vulnerability_description", curie=DCT.curie('description'),
                   model_uri=CVE.Vulnerability_description, domain=Vulnerability, range=Optional[str])
