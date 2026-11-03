# Auto generated from cve.yaml by pythongen.py version: 0.0.1
# Schema: cve
#
# id: https://w3id.org/lmodel/cve
# description: A LinkML model of the CVE Record Format, in which the CVE Program publishes each vulnerability record, with its CVSS scores. It keeps the format's own keys and values, so a real record validates unchanged.
# license: Apache-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI

metamodel_version = "1.12.0"
version = "5.2.0"

# Namespaces
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEPSES_CVE = CurieNamespace('sepses_cve', 'http://w3id.org/sepses/vocab/ref/cve#')
SEPSES_CVSS = CurieNamespace('sepses_cvss', 'http://w3id.org/sepses/vocab/ref/cvss#')
SPDX_SECURITY = CurieNamespace('spdx_security', 'https://spdx.org/rdf/3.0.1/terms/Security/')
SPDX_SOFTWARE = CurieNamespace('spdx_software', 'https://spdx.org/rdf/3.0.1/terms/Software/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CVE


# Types
class CveUri(Uri):
    """ An address of up to 2048 characters. """
    type_class_uri = XSD["anyURI"]
    type_class_curie = "xsd:anyURI"
    type_name = "cve_uri"
    type_model_uri = CVE.CveUri


class CveUuid(String):
    """ A random (version 4) UUID, as the CVE Program gives its users and organisations. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_uuid"
    type_model_uri = CVE.CveUuid


class CveIdentifier(String):
    """ A CVE identifier, such as CVE-2021-44228. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_identifier"
    type_model_uri = CVE.CveIdentifier


class CveCpe22and23(String):
    """ A Common Platform Enumeration name in the form of version 2.2 or 2.3. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_cpe22and23"
    type_model_uri = CVE.CveCpe22and23


class CveCpe23(String):
    """ A Common Platform Enumeration name in the form of version 2.3. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_cpe23"
    type_model_uri = CVE.CveCpe23


class CveShortName(String):
    """ An organisation's short name of 2 to 32 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_short_name"
    type_model_uri = CVE.CveShortName


class CveDatestamp(String):
    """ A calendar date, such as 2021-12-10. """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "cve_datestamp"
    type_model_uri = CVE.CveDatestamp


class CveTimestamp(String):
    """ A date and time, such as 2021-12-10T10:00:00Z. Without a time zone, it means UTC. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "cve_timestamp"
    type_model_uri = CVE.CveTimestamp


class CveVersion(String):
    """ A product version of 1 to 1024 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_version"
    type_model_uri = CVE.CveVersion


class CveDataVersion(String):
    """ The version of the record format that a record follows, such as 5.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_data_version"
    type_model_uri = CVE.CveDataVersion


class CveLanguage(String):
    """ A language tag, such as en or pt-BR. """
    type_class_uri = XSD["language"]
    type_class_curie = "xsd:language"
    type_name = "cve_language"
    type_model_uri = CVE.CveLanguage


class CveEnglishLanguage(String):
    """ A language tag for English, such as en or en-US. """
    type_class_uri = XSD["language"]
    type_class_curie = "xsd:language"
    type_name = "cve_english_language"
    type_model_uri = CVE.CveEnglishLanguage


class CveTagExtension(String):
    """ A tag of the publisher's own, beginning x_. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_tag_extension"
    type_model_uri = CVE.CveTagExtension


class CveText64(String):
    """ Text of 1 to 64 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_64"
    type_model_uri = CVE.CveText64


class CveText128(String):
    """ Text of 1 to 128 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_128"
    type_model_uri = CVE.CveText128


class CveText256(String):
    """ Text of 1 to 256 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_256"
    type_model_uri = CVE.CveText256


class CveText512(String):
    """ Text of 1 to 512 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_512"
    type_model_uri = CVE.CveText512


class CveText1024(String):
    """ Text of 1 to 1024 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_1024"
    type_model_uri = CVE.CveText1024


class CveTextUpTo1024(String):
    """ Text of at most 1024 characters, which may be empty. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_up_to_1024"
    type_model_uri = CVE.CveTextUpTo1024


class CveText2048(String):
    """ Text of 1 to 2048 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_2048"
    type_model_uri = CVE.CveText2048


class CveText4096(String):
    """ Text of 1 to 4096 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_4096"
    type_model_uri = CVE.CveText4096


class CveText16384(String):
    """ Text of 1 to 16384 characters. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "cve_text_16384"
    type_model_uri = CVE.CveText16384


# Class references



class CveRecordRoot(YAMLRoot):
    """
    Any one CVE record, published or rejected, as a file or an API answer holds it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveRecordRoot"]
    class_class_curie: ClassVar[str] = "cve:CveRecordRoot"
    class_name: ClassVar[str] = "CveRecordRoot"
    class_model_uri: ClassVar[URIRef] = CVE.CveRecordRoot


@dataclass(repr=False)
class CvssSeverityBandsMixin(YAMLRoot):
    """
    The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssSeverityBandsMixin"]
    class_class_curie: ClassVar[str] = "cve:CvssSeverityBandsMixin"
    class_name: ClassVar[str] = "CvssSeverityBandsMixin"
    class_model_uri: ClassVar[URIRef] = CVE.CvssSeverityBandsMixin

    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV20(YAMLRoot):
    """
    A score under CVSS version 2.0, which has no severity bands.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV20"]
    class_class_curie: ClassVar[str] = "cve:CvssV20"
    class_name: ClassVar[str] = "CvssV20"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV20

    version: str = None
    vectorString: str = None
    baseScore: float = None
    confidentialityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    integrityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    availabilityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV2ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    environmentalScore: Optional[float] = None
    accessVector: Optional[Union[str, "CvssV2AccessVector"]] = None
    accessComplexity: Optional[Union[str, "CvssV2AccessComplexity"]] = None
    authentication: Optional[Union[str, "CvssV2Authentication"]] = None
    exploitability: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    collateralDamagePotential: Optional[Union[str, "CvssV2CollateralDamagePotential"]] = None
    targetDistribution: Optional[Union[str, "CvssV2TargetDistribution"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssV2Impact):
            self.confidentialityImpact = CvssV2Impact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssV2Impact):
            self.integrityImpact = CvssV2Impact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssV2Impact):
            self.availabilityImpact = CvssV2Impact(self.availabilityImpact)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV2ReportConfidence):
            self.reportConfidence = CvssV2ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.accessVector is not None and not isinstance(self.accessVector, CvssV2AccessVector):
            self.accessVector = CvssV2AccessVector(self.accessVector)

        if self.accessComplexity is not None and not isinstance(self.accessComplexity, CvssV2AccessComplexity):
            self.accessComplexity = CvssV2AccessComplexity(self.accessComplexity)

        if self.authentication is not None and not isinstance(self.authentication, CvssV2Authentication):
            self.authentication = CvssV2Authentication(self.authentication)

        if self.exploitability is not None and not isinstance(self.exploitability, CvssExploitCodeMaturity):
            self.exploitability = CvssExploitCodeMaturity(self.exploitability)

        if self.collateralDamagePotential is not None and not isinstance(self.collateralDamagePotential, CvssV2CollateralDamagePotential):
            self.collateralDamagePotential = CvssV2CollateralDamagePotential(self.collateralDamagePotential)

        if self.targetDistribution is not None and not isinstance(self.targetDistribution, CvssV2TargetDistribution):
            self.targetDistribution = CvssV2TargetDistribution(self.targetDistribution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV30(YAMLRoot):
    """
    A score under CVSS version 3.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV30"]
    class_class_curie: ClassVar[str] = "cve:CvssV30"
    class_name: ClassVar[str] = "CvssV30"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV30

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV3AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV3UserInteraction"]] = None
    scope: Optional[Union[str, "CvssV3Scope"]] = None
    confidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    integrityImpact: Optional[Union[str, "CvssImpact"]] = None
    availabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitCodeMaturity: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV3ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    temporalSeverity: Optional[Union[str, "CvssSeverity"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    modifiedAttackVector: Optional[Union[str, "CvssV3ModifiedAttackVector"]] = None
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = None
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = None
    modifiedUserInteraction: Optional[Union[str, "CvssV3ModifiedUserInteraction"]] = None
    modifiedScope: Optional[Union[str, "CvssV3ModifiedScope"]] = None
    modifiedConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    environmentalScore: Optional[float] = None
    environmentalSeverity: Optional[Union[str, "CvssSeverity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV3AttackVector):
            self.attackVector = CvssV3AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV3UserInteraction):
            self.userInteraction = CvssV3UserInteraction(self.userInteraction)

        if self.scope is not None and not isinstance(self.scope, CvssV3Scope):
            self.scope = CvssV3Scope(self.scope)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssImpact):
            self.confidentialityImpact = CvssImpact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssImpact):
            self.integrityImpact = CvssImpact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssImpact):
            self.availabilityImpact = CvssImpact(self.availabilityImpact)

        if self.exploitCodeMaturity is not None and not isinstance(self.exploitCodeMaturity, CvssExploitCodeMaturity):
            self.exploitCodeMaturity = CvssExploitCodeMaturity(self.exploitCodeMaturity)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV3ReportConfidence):
            self.reportConfidence = CvssV3ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.temporalSeverity is not None and not isinstance(self.temporalSeverity, CvssSeverity):
            self.temporalSeverity = CvssSeverity(self.temporalSeverity)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV3ModifiedAttackVector):
            self.modifiedAttackVector = CvssV3ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV3ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV3ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.modifiedScope is not None and not isinstance(self.modifiedScope, CvssV3ModifiedScope):
            self.modifiedScope = CvssV3ModifiedScope(self.modifiedScope)

        if self.modifiedConfidentialityImpact is not None and not isinstance(self.modifiedConfidentialityImpact, CvssModifiedImpact):
            self.modifiedConfidentialityImpact = CvssModifiedImpact(self.modifiedConfidentialityImpact)

        if self.modifiedIntegrityImpact is not None and not isinstance(self.modifiedIntegrityImpact, CvssModifiedImpact):
            self.modifiedIntegrityImpact = CvssModifiedImpact(self.modifiedIntegrityImpact)

        if self.modifiedAvailabilityImpact is not None and not isinstance(self.modifiedAvailabilityImpact, CvssModifiedImpact):
            self.modifiedAvailabilityImpact = CvssModifiedImpact(self.modifiedAvailabilityImpact)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.environmentalSeverity is not None and not isinstance(self.environmentalSeverity, CvssSeverity):
            self.environmentalSeverity = CvssSeverity(self.environmentalSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV31(YAMLRoot):
    """
    A score under CVSS version 3.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV31"]
    class_class_curie: ClassVar[str] = "cve:CvssV31"
    class_name: ClassVar[str] = "CvssV31"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV31

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV3AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV3UserInteraction"]] = None
    scope: Optional[Union[str, "CvssV3Scope"]] = None
    confidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    integrityImpact: Optional[Union[str, "CvssImpact"]] = None
    availabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitCodeMaturity: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV3ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    temporalSeverity: Optional[Union[str, "CvssSeverity"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    modifiedAttackVector: Optional[Union[str, "CvssV3ModifiedAttackVector"]] = None
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = None
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = None
    modifiedUserInteraction: Optional[Union[str, "CvssV3ModifiedUserInteraction"]] = None
    modifiedScope: Optional[Union[str, "CvssV3ModifiedScope"]] = None
    modifiedConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    environmentalScore: Optional[float] = None
    environmentalSeverity: Optional[Union[str, "CvssSeverity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV3AttackVector):
            self.attackVector = CvssV3AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV3UserInteraction):
            self.userInteraction = CvssV3UserInteraction(self.userInteraction)

        if self.scope is not None and not isinstance(self.scope, CvssV3Scope):
            self.scope = CvssV3Scope(self.scope)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssImpact):
            self.confidentialityImpact = CvssImpact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssImpact):
            self.integrityImpact = CvssImpact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssImpact):
            self.availabilityImpact = CvssImpact(self.availabilityImpact)

        if self.exploitCodeMaturity is not None and not isinstance(self.exploitCodeMaturity, CvssExploitCodeMaturity):
            self.exploitCodeMaturity = CvssExploitCodeMaturity(self.exploitCodeMaturity)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV3ReportConfidence):
            self.reportConfidence = CvssV3ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.temporalSeverity is not None and not isinstance(self.temporalSeverity, CvssSeverity):
            self.temporalSeverity = CvssSeverity(self.temporalSeverity)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV3ModifiedAttackVector):
            self.modifiedAttackVector = CvssV3ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV3ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV3ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.modifiedScope is not None and not isinstance(self.modifiedScope, CvssV3ModifiedScope):
            self.modifiedScope = CvssV3ModifiedScope(self.modifiedScope)

        if self.modifiedConfidentialityImpact is not None and not isinstance(self.modifiedConfidentialityImpact, CvssModifiedImpact):
            self.modifiedConfidentialityImpact = CvssModifiedImpact(self.modifiedConfidentialityImpact)

        if self.modifiedIntegrityImpact is not None and not isinstance(self.modifiedIntegrityImpact, CvssModifiedImpact):
            self.modifiedIntegrityImpact = CvssModifiedImpact(self.modifiedIntegrityImpact)

        if self.modifiedAvailabilityImpact is not None and not isinstance(self.modifiedAvailabilityImpact, CvssModifiedImpact):
            self.modifiedAvailabilityImpact = CvssModifiedImpact(self.modifiedAvailabilityImpact)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.environmentalSeverity is not None and not isinstance(self.environmentalSeverity, CvssSeverity):
            self.environmentalSeverity = CvssSeverity(self.environmentalSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV40(YAMLRoot):
    """
    A score under CVSS version 4.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV40"]
    class_class_curie: ClassVar[str] = "cve:CvssV40"
    class_name: ClassVar[str] = "CvssV40"
    class_model_uri: ClassVar[URIRef] = CVE.CvssV40

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV4AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV4UserInteraction"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    modifiedAttackVector: Optional[Union[str, "CvssV4ModifiedAttackVector"]] = 'NOT_DEFINED'
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = 'NOT_DEFINED'
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = 'NOT_DEFINED'
    modifiedUserInteraction: Optional[Union[str, "CvssV4ModifiedUserInteraction"]] = 'NOT_DEFINED'
    attackRequirements: Optional[Union[str, "CvssV4AttackRequirements"]] = None
    vulnConfidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    vulnIntegrityImpact: Optional[Union[str, "CvssImpact"]] = None
    vulnAvailabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    subConfidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    subIntegrityImpact: Optional[Union[str, "CvssImpact"]] = None
    subAvailabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitMaturity: Optional[Union[str, "CvssV4ExploitMaturity"]] = 'NOT_DEFINED'
    modifiedAttackRequirements: Optional[Union[str, "CvssV4ModifiedAttackRequirements"]] = 'NOT_DEFINED'
    modifiedVulnConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedVulnIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedVulnAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedSubConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedSubIntegrityImpact: Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]] = 'NOT_DEFINED'
    modifiedSubAvailabilityImpact: Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]] = 'NOT_DEFINED'
    Safety: Optional[Union[str, "CvssV4Safety"]] = 'NOT_DEFINED'
    Automatable: Optional[Union[str, "CvssV4Automatable"]] = 'NOT_DEFINED'
    Recovery: Optional[Union[str, "CvssV4Recovery"]] = 'NOT_DEFINED'
    valueDensity: Optional[Union[str, "CvssV4ValueDensity"]] = 'NOT_DEFINED'
    vulnerabilityResponseEffort: Optional[Union[str, "CvssV4ResponseEffort"]] = 'NOT_DEFINED'
    providerUrgency: Optional[Union[str, "CvssV4ProviderUrgency"]] = 'NOT_DEFINED'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV4AttackVector):
            self.attackVector = CvssV4AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV4UserInteraction):
            self.userInteraction = CvssV4UserInteraction(self.userInteraction)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV4ModifiedAttackVector):
            self.modifiedAttackVector = CvssV4ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV4ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV4ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.attackRequirements is not None and not isinstance(self.attackRequirements, CvssV4AttackRequirements):
            self.attackRequirements = CvssV4AttackRequirements(self.attackRequirements)

        if self.vulnConfidentialityImpact is not None and not isinstance(self.vulnConfidentialityImpact, CvssImpact):
            self.vulnConfidentialityImpact = CvssImpact(self.vulnConfidentialityImpact)

        if self.vulnIntegrityImpact is not None and not isinstance(self.vulnIntegrityImpact, CvssImpact):
            self.vulnIntegrityImpact = CvssImpact(self.vulnIntegrityImpact)

        if self.vulnAvailabilityImpact is not None and not isinstance(self.vulnAvailabilityImpact, CvssImpact):
            self.vulnAvailabilityImpact = CvssImpact(self.vulnAvailabilityImpact)

        if self.subConfidentialityImpact is not None and not isinstance(self.subConfidentialityImpact, CvssImpact):
            self.subConfidentialityImpact = CvssImpact(self.subConfidentialityImpact)

        if self.subIntegrityImpact is not None and not isinstance(self.subIntegrityImpact, CvssImpact):
            self.subIntegrityImpact = CvssImpact(self.subIntegrityImpact)

        if self.subAvailabilityImpact is not None and not isinstance(self.subAvailabilityImpact, CvssImpact):
            self.subAvailabilityImpact = CvssImpact(self.subAvailabilityImpact)

        if self.exploitMaturity is not None and not isinstance(self.exploitMaturity, CvssV4ExploitMaturity):
            self.exploitMaturity = CvssV4ExploitMaturity(self.exploitMaturity)

        if self.modifiedAttackRequirements is not None and not isinstance(self.modifiedAttackRequirements, CvssV4ModifiedAttackRequirements):
            self.modifiedAttackRequirements = CvssV4ModifiedAttackRequirements(self.modifiedAttackRequirements)

        if self.modifiedVulnConfidentialityImpact is not None and not isinstance(self.modifiedVulnConfidentialityImpact, CvssModifiedImpact):
            self.modifiedVulnConfidentialityImpact = CvssModifiedImpact(self.modifiedVulnConfidentialityImpact)

        if self.modifiedVulnIntegrityImpact is not None and not isinstance(self.modifiedVulnIntegrityImpact, CvssModifiedImpact):
            self.modifiedVulnIntegrityImpact = CvssModifiedImpact(self.modifiedVulnIntegrityImpact)

        if self.modifiedVulnAvailabilityImpact is not None and not isinstance(self.modifiedVulnAvailabilityImpact, CvssModifiedImpact):
            self.modifiedVulnAvailabilityImpact = CvssModifiedImpact(self.modifiedVulnAvailabilityImpact)

        if self.modifiedSubConfidentialityImpact is not None and not isinstance(self.modifiedSubConfidentialityImpact, CvssModifiedImpact):
            self.modifiedSubConfidentialityImpact = CvssModifiedImpact(self.modifiedSubConfidentialityImpact)

        if self.modifiedSubIntegrityImpact is not None and not isinstance(self.modifiedSubIntegrityImpact, CvssV4ModifiedSubsequentImpact):
            self.modifiedSubIntegrityImpact = CvssV4ModifiedSubsequentImpact(self.modifiedSubIntegrityImpact)

        if self.modifiedSubAvailabilityImpact is not None and not isinstance(self.modifiedSubAvailabilityImpact, CvssV4ModifiedSubsequentImpact):
            self.modifiedSubAvailabilityImpact = CvssV4ModifiedSubsequentImpact(self.modifiedSubAvailabilityImpact)

        if self.Safety is not None and not isinstance(self.Safety, CvssV4Safety):
            self.Safety = CvssV4Safety(self.Safety)

        if self.Automatable is not None and not isinstance(self.Automatable, CvssV4Automatable):
            self.Automatable = CvssV4Automatable(self.Automatable)

        if self.Recovery is not None and not isinstance(self.Recovery, CvssV4Recovery):
            self.Recovery = CvssV4Recovery(self.Recovery)

        if self.valueDensity is not None and not isinstance(self.valueDensity, CvssV4ValueDensity):
            self.valueDensity = CvssV4ValueDensity(self.valueDensity)

        if self.vulnerabilityResponseEffort is not None and not isinstance(self.vulnerabilityResponseEffort, CvssV4ResponseEffort):
            self.vulnerabilityResponseEffort = CvssV4ResponseEffort(self.vulnerabilityResponseEffort)

        if self.providerUrgency is not None and not isinstance(self.providerUrgency, CvssV4ProviderUrgency):
            self.providerUrgency = CvssV4ProviderUrgency(self.providerUrgency)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveRecord(YAMLRoot):
    """
    A record of one vulnerability under one CVE identifier, in the CVE Program's format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveRecord"]
    class_class_curie: ClassVar[str] = "cve:CveRecord"
    class_name: ClassVar[str] = "CveRecord"
    class_model_uri: ClassVar[URIRef] = CVE.CveRecord

    cveMetadata: Union[dict, "CveRecordMetadata"] = None
    containers: Union[dict, "CveContainers"] = None
    dataType: Union[str, "CveDataType"] = None
    dataVersion: Union[str, CveDataVersion] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cveMetadata):
            self.MissingRequiredField("cveMetadata")
        if not isinstance(self.cveMetadata, CveRecordMetadata):
            self.cveMetadata = CveRecordMetadata(**as_dict(self.cveMetadata))

        if self._is_empty(self.containers):
            self.MissingRequiredField("containers")
        if not isinstance(self.containers, CveContainers):
            self.containers = CveContainers(**as_dict(self.containers))

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, CveDataType):
            self.dataType = CveDataType(self.dataType)

        if self._is_empty(self.dataVersion):
            self.MissingRequiredField("dataVersion")
        if not isinstance(self.dataVersion, CveDataVersion):
            self.dataVersion = CveDataVersion(self.dataVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvePublishedRecord(CveRecord):
    """
    A record whose assigning organisation has filled it in and made it public.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvePublishedRecord"]
    class_class_curie: ClassVar[str] = "cve:CvePublishedRecord"
    class_name: ClassVar[str] = "CvePublishedRecord"
    class_model_uri: ClassVar[URIRef] = CVE.CvePublishedRecord

    dataType: Union[str, "CveDataType"] = None
    dataVersion: Union[str, CveDataVersion] = None
    cveMetadata: Union[dict, "CveMetadataPublished"] = None
    containers: Union[dict, "CvePublishedContainers"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cveMetadata):
            self.MissingRequiredField("cveMetadata")
        if not isinstance(self.cveMetadata, CveMetadataPublished):
            self.cveMetadata = CveMetadataPublished(**as_dict(self.cveMetadata))

        if self._is_empty(self.containers):
            self.MissingRequiredField("containers")
        if not isinstance(self.containers, CvePublishedContainers):
            self.containers = CvePublishedContainers(**as_dict(self.containers))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveRejectedRecord(CveRecord):
    """
    A record that should no longer be used, kept so that people can see it is invalid.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveRejectedRecord"]
    class_class_curie: ClassVar[str] = "cve:CveRejectedRecord"
    class_name: ClassVar[str] = "CveRejectedRecord"
    class_model_uri: ClassVar[URIRef] = CVE.CveRejectedRecord

    dataType: Union[str, "CveDataType"] = None
    dataVersion: Union[str, CveDataVersion] = None
    cveMetadata: Union[dict, "CveMetadataRejected"] = None
    containers: Union[dict, "CveRejectedContainers"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cveMetadata):
            self.MissingRequiredField("cveMetadata")
        if not isinstance(self.cveMetadata, CveMetadataRejected):
            self.cveMetadata = CveMetadataRejected(**as_dict(self.cveMetadata))

        if self._is_empty(self.containers):
            self.MissingRequiredField("containers")
        if not isinstance(self.containers, CveRejectedContainers):
            self.containers = CveRejectedContainers(**as_dict(self.containers))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveRecordMetadata(YAMLRoot):
    """
    The facts about a record itself, as distinct from the vulnerability it describes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveRecordMetadata"]
    class_class_curie: ClassVar[str] = "cve:CveRecordMetadata"
    class_name: ClassVar[str] = "CveRecordMetadata"
    class_model_uri: ClassVar[URIRef] = CVE.CveRecordMetadata

    state: Union[str, "CveRecordState"] = None
    cveId: Union[str, CveIdentifier] = None
    assignerOrgId: Union[str, CveUuid] = None
    dateUpdated: Optional[Union[str, CveTimestamp]] = None
    assignerShortName: Optional[Union[str, CveShortName]] = None
    serial: Optional[int] = None
    dateReserved: Optional[Union[str, CveTimestamp]] = None
    datePublished: Optional[Union[str, CveTimestamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, CveRecordState):
            self.state = CveRecordState(self.state)

        if self._is_empty(self.cveId):
            self.MissingRequiredField("cveId")
        if not isinstance(self.cveId, CveIdentifier):
            self.cveId = CveIdentifier(self.cveId)

        if self._is_empty(self.assignerOrgId):
            self.MissingRequiredField("assignerOrgId")
        if not isinstance(self.assignerOrgId, CveUuid):
            self.assignerOrgId = CveUuid(self.assignerOrgId)

        if self.dateUpdated is not None and not isinstance(self.dateUpdated, CveTimestamp):
            self.dateUpdated = CveTimestamp(self.dateUpdated)

        if self.assignerShortName is not None and not isinstance(self.assignerShortName, CveShortName):
            self.assignerShortName = CveShortName(self.assignerShortName)

        if self.serial is not None and not isinstance(self.serial, int):
            self.serial = int(self.serial)

        if self.dateReserved is not None and not isinstance(self.dateReserved, CveTimestamp):
            self.dateReserved = CveTimestamp(self.dateReserved)

        if self.datePublished is not None and not isinstance(self.datePublished, CveTimestamp):
            self.datePublished = CveTimestamp(self.datePublished)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveMetadataPublished(CveRecordMetadata):
    """
    The metadata of a published record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetadataPublished"]
    class_class_curie: ClassVar[str] = "cve:CveMetadataPublished"
    class_name: ClassVar[str] = "CveMetadataPublished"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetadataPublished

    cveId: Union[str, CveIdentifier] = None
    assignerOrgId: Union[str, CveUuid] = None
    state: Union[str, "CvePublishedState"] = None
    requesterUserId: Optional[Union[str, CveUuid]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, CvePublishedState):
            self.state = CvePublishedState(self.state)

        if self.requesterUserId is not None and not isinstance(self.requesterUserId, CveUuid):
            self.requesterUserId = CveUuid(self.requesterUserId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveMetadataRejected(CveRecordMetadata):
    """
    The metadata of a rejected record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetadataRejected"]
    class_class_curie: ClassVar[str] = "cve:CveMetadataRejected"
    class_name: ClassVar[str] = "CveMetadataRejected"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetadataRejected

    cveId: Union[str, CveIdentifier] = None
    assignerOrgId: Union[str, CveUuid] = None
    state: Union[str, "CveRejectedState"] = None
    dateRejected: Optional[Union[str, CveTimestamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state):
            self.MissingRequiredField("state")
        if not isinstance(self.state, CveRejectedState):
            self.state = CveRejectedState(self.state)

        if self.dateRejected is not None and not isinstance(self.dateRejected, CveTimestamp):
            self.dateRejected = CveTimestamp(self.dateRejected)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveContainers(YAMLRoot):
    """
    The sets of vulnerability information in a record, one per providing organisation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveContainers"]
    class_class_curie: ClassVar[str] = "cve:CveContainers"
    class_name: ClassVar[str] = "CveContainers"
    class_model_uri: ClassVar[URIRef] = CVE.CveContainers

    cna: Union[dict, "CveCnaContainer"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cna):
            self.MissingRequiredField("cna")
        if not isinstance(self.cna, CveCnaContainer):
            self.cna = CveCnaContainer(**as_dict(self.cna))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvePublishedContainers(CveContainers):
    """
    The containers of a published record, the assigning organisation's and any others'.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvePublishedContainers"]
    class_class_curie: ClassVar[str] = "cve:CvePublishedContainers"
    class_name: ClassVar[str] = "CvePublishedContainers"
    class_model_uri: ClassVar[URIRef] = CVE.CvePublishedContainers

    cna: Union[dict, "CveCnaPublishedContainer"] = None
    adp: Optional[Union[Union[dict, "CveAdpContainer"], list[Union[dict, "CveAdpContainer"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cna):
            self.MissingRequiredField("cna")
        if not isinstance(self.cna, CveCnaPublishedContainer):
            self.cna = CveCnaPublishedContainer(**as_dict(self.cna))

        if not isinstance(self.adp, list):
            self.adp = [self.adp] if self.adp is not None else []
        self.adp = [v if isinstance(v, CveAdpContainer) else CveAdpContainer(**as_dict(v)) for v in self.adp]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveRejectedContainers(CveContainers):
    """
    The container of a rejected record, which only the assigning organisation provides.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveRejectedContainers"]
    class_class_curie: ClassVar[str] = "cve:CveRejectedContainers"
    class_name: ClassVar[str] = "CveRejectedContainers"
    class_model_uri: ClassVar[URIRef] = CVE.CveRejectedContainers

    cna: Union[dict, "CveCnaRejectedContainer"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cna):
            self.MissingRequiredField("cna")
        if not isinstance(self.cna, CveCnaRejectedContainer):
            self.cna = CveCnaRejectedContainer(**as_dict(self.cna))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProviderMetadata(YAMLRoot):
    """
    Who provided a container, and when it was last updated.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProviderMetadata"]
    class_class_curie: ClassVar[str] = "cve:CveProviderMetadata"
    class_name: ClassVar[str] = "CveProviderMetadata"
    class_model_uri: ClassVar[URIRef] = CVE.CveProviderMetadata

    orgId: Union[str, CveUuid] = None
    dateUpdated: Optional[Union[str, CveTimestamp]] = None
    shortName: Optional[Union[str, CveShortName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.orgId):
            self.MissingRequiredField("orgId")
        if not isinstance(self.orgId, CveUuid):
            self.orgId = CveUuid(self.orgId)

        if self.dateUpdated is not None and not isinstance(self.dateUpdated, CveTimestamp):
            self.dateUpdated = CveTimestamp(self.dateUpdated)

        if self.shortName is not None and not isinstance(self.shortName, CveShortName):
            self.shortName = CveShortName(self.shortName)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCnaContainer(YAMLRoot):
    """
    The container from the CVE Numbering Authority that assigned the identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCnaContainer"]
    class_class_curie: ClassVar[str] = "cve:CveCnaContainer"
    class_name: ClassVar[str] = "CveCnaContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CveCnaContainer

    providerMetadata: Union[dict, CveProviderMetadata] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.providerMetadata):
            self.MissingRequiredField("providerMetadata")
        if not isinstance(self.providerMetadata, CveProviderMetadata):
            self.providerMetadata = CveProviderMetadata(**as_dict(self.providerMetadata))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCnaPublishedContainer(CveCnaContainer):
    """
    The assigning authority's account of a published vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCnaPublishedContainer"]
    class_class_curie: ClassVar[str] = "cve:CveCnaPublishedContainer"
    class_name: ClassVar[str] = "CveCnaPublishedContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CveCnaPublishedContainer

    providerMetadata: Union[dict, CveProviderMetadata] = None
    descriptions: Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]] = None
    affected: Union[Union[dict, "CveProduct"], list[Union[dict, "CveProduct"]]] = None
    references: Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]] = None
    datePublic: Optional[Union[str, CveTimestamp]] = None
    title: Optional[Union[str, CveText256]] = None
    cpeApplicability: Optional[Union[Union[dict, "CveCpeApplicabilityElement"], list[Union[dict, "CveCpeApplicabilityElement"]]]] = empty_list()
    problemTypes: Optional[Union[Union[dict, "CveProblemType"], list[Union[dict, "CveProblemType"]]]] = empty_list()
    impacts: Optional[Union[Union[dict, "CveImpact"], list[Union[dict, "CveImpact"]]]] = empty_list()
    metrics: Optional[Union[Union[dict, "CveMetric"], list[Union[dict, "CveMetric"]]]] = empty_list()
    configurations: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    workarounds: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    solutions: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    exploits: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    timeline: Optional[Union[Union[dict, "CveTimelineEvent"], list[Union[dict, "CveTimelineEvent"]]]] = empty_list()
    credits: Optional[Union[Union[dict, "CveCredit"], list[Union[dict, "CveCredit"]]]] = empty_list()
    source: Optional[Union[dict, "CveSource"]] = None
    tags: Optional[Union[str, list[str]]] = empty_list()
    taxonomyMappings: Optional[Union[Union[dict, "CveTaxonomyMapping"], list[Union[dict, "CveTaxonomyMapping"]]]] = empty_list()
    dateAssigned: Optional[Union[str, CveTimestamp]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.descriptions):
            self.MissingRequiredField("descriptions")
        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=CveDescription, key_name="lang", keyed=False)

        if self._is_empty(self.affected):
            self.MissingRequiredField("affected")
        if not isinstance(self.affected, list):
            self.affected = [self.affected] if self.affected is not None else []
        self.affected = [v if isinstance(v, CveProduct) else CveProduct(**as_dict(v)) for v in self.affected]

        if self._is_empty(self.references):
            self.MissingRequiredField("references")
        self._normalize_inlined_as_list(slot_name="references", slot_type=CveReference, key_name="url", keyed=False)

        if self.datePublic is not None and not isinstance(self.datePublic, CveTimestamp):
            self.datePublic = CveTimestamp(self.datePublic)

        if self.title is not None and not isinstance(self.title, CveText256):
            self.title = CveText256(self.title)

        if not isinstance(self.cpeApplicability, list):
            self.cpeApplicability = [self.cpeApplicability] if self.cpeApplicability is not None else []
        self.cpeApplicability = [v if isinstance(v, CveCpeApplicabilityElement) else CveCpeApplicabilityElement(**as_dict(v)) for v in self.cpeApplicability]

        if not isinstance(self.problemTypes, list):
            self.problemTypes = [self.problemTypes] if self.problemTypes is not None else []
        self.problemTypes = [v if isinstance(v, CveProblemType) else CveProblemType(**as_dict(v)) for v in self.problemTypes]

        if not isinstance(self.impacts, list):
            self.impacts = [self.impacts] if self.impacts is not None else []
        self.impacts = [v if isinstance(v, CveImpact) else CveImpact(**as_dict(v)) for v in self.impacts]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, CveMetric) else CveMetric(**as_dict(v)) for v in self.metrics]

        self._normalize_inlined_as_list(slot_name="configurations", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="workarounds", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="solutions", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="exploits", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="timeline", slot_type=CveTimelineEvent, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="credits", slot_type=CveCredit, key_name="lang", keyed=False)

        if self.source is not None and not isinstance(self.source, CveSource):
            self.source = CveSource()

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        self._normalize_inlined_as_list(slot_name="taxonomyMappings", slot_type=CveTaxonomyMapping, key_name="taxonomyName", keyed=False)

        if self.dateAssigned is not None and not isinstance(self.dateAssigned, CveTimestamp):
            self.dateAssigned = CveTimestamp(self.dateAssigned)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCnaRejectedContainer(CveCnaContainer):
    """
    The assigning authority's account of why a record was rejected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCnaRejectedContainer"]
    class_class_curie: ClassVar[str] = "cve:CveCnaRejectedContainer"
    class_name: ClassVar[str] = "CveCnaRejectedContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CveCnaRejectedContainer

    providerMetadata: Union[dict, CveProviderMetadata] = None
    rejectedReasons: Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]] = None
    replacedBy: Optional[Union[Union[str, CveIdentifier], list[Union[str, CveIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rejectedReasons):
            self.MissingRequiredField("rejectedReasons")
        self._normalize_inlined_as_list(slot_name="rejectedReasons", slot_type=CveDescription, key_name="lang", keyed=False)

        if not isinstance(self.replacedBy, list):
            self.replacedBy = [self.replacedBy] if self.replacedBy is not None else []
        self.replacedBy = [v if isinstance(v, CveIdentifier) else CveIdentifier(v) for v in self.replacedBy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveAdpContainer(YAMLRoot):
    """
    What an Authorized Data Publisher adds to a record beside the assigning authority's account.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveAdpContainer"]
    class_class_curie: ClassVar[str] = "cve:CveAdpContainer"
    class_name: ClassVar[str] = "CveAdpContainer"
    class_model_uri: ClassVar[URIRef] = CVE.CveAdpContainer

    providerMetadata: Union[dict, CveProviderMetadata] = None
    datePublic: Optional[Union[str, CveTimestamp]] = None
    title: Optional[Union[str, CveText256]] = None
    descriptions: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    affected: Optional[Union[Union[dict, "CveProduct"], list[Union[dict, "CveProduct"]]]] = empty_list()
    cpeApplicability: Optional[Union[Union[dict, "CveCpeApplicabilityElement"], list[Union[dict, "CveCpeApplicabilityElement"]]]] = empty_list()
    problemTypes: Optional[Union[Union[dict, "CveProblemType"], list[Union[dict, "CveProblemType"]]]] = empty_list()
    references: Optional[Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]]] = empty_list()
    impacts: Optional[Union[Union[dict, "CveImpact"], list[Union[dict, "CveImpact"]]]] = empty_list()
    metrics: Optional[Union[Union[dict, "CveMetric"], list[Union[dict, "CveMetric"]]]] = empty_list()
    configurations: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    workarounds: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    solutions: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    exploits: Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]] = empty_list()
    timeline: Optional[Union[Union[dict, "CveTimelineEvent"], list[Union[dict, "CveTimelineEvent"]]]] = empty_list()
    credits: Optional[Union[Union[dict, "CveCredit"], list[Union[dict, "CveCredit"]]]] = empty_list()
    source: Optional[Union[dict, "CveSource"]] = None
    tags: Optional[Union[str, list[str]]] = empty_list()
    taxonomyMappings: Optional[Union[Union[dict, "CveTaxonomyMapping"], list[Union[dict, "CveTaxonomyMapping"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.providerMetadata):
            self.MissingRequiredField("providerMetadata")
        if not isinstance(self.providerMetadata, CveProviderMetadata):
            self.providerMetadata = CveProviderMetadata(**as_dict(self.providerMetadata))

        if self.datePublic is not None and not isinstance(self.datePublic, CveTimestamp):
            self.datePublic = CveTimestamp(self.datePublic)

        if self.title is not None and not isinstance(self.title, CveText256):
            self.title = CveText256(self.title)

        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=CveDescription, key_name="lang", keyed=False)

        if not isinstance(self.affected, list):
            self.affected = [self.affected] if self.affected is not None else []
        self.affected = [v if isinstance(v, CveProduct) else CveProduct(**as_dict(v)) for v in self.affected]

        if not isinstance(self.cpeApplicability, list):
            self.cpeApplicability = [self.cpeApplicability] if self.cpeApplicability is not None else []
        self.cpeApplicability = [v if isinstance(v, CveCpeApplicabilityElement) else CveCpeApplicabilityElement(**as_dict(v)) for v in self.cpeApplicability]

        if not isinstance(self.problemTypes, list):
            self.problemTypes = [self.problemTypes] if self.problemTypes is not None else []
        self.problemTypes = [v if isinstance(v, CveProblemType) else CveProblemType(**as_dict(v)) for v in self.problemTypes]

        self._normalize_inlined_as_list(slot_name="references", slot_type=CveReference, key_name="url", keyed=False)

        if not isinstance(self.impacts, list):
            self.impacts = [self.impacts] if self.impacts is not None else []
        self.impacts = [v if isinstance(v, CveImpact) else CveImpact(**as_dict(v)) for v in self.impacts]

        if not isinstance(self.metrics, list):
            self.metrics = [self.metrics] if self.metrics is not None else []
        self.metrics = [v if isinstance(v, CveMetric) else CveMetric(**as_dict(v)) for v in self.metrics]

        self._normalize_inlined_as_list(slot_name="configurations", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="workarounds", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="solutions", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="exploits", slot_type=CveDescription, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="timeline", slot_type=CveTimelineEvent, key_name="lang", keyed=False)

        self._normalize_inlined_as_list(slot_name="credits", slot_type=CveCredit, key_name="lang", keyed=False)

        if self.source is not None and not isinstance(self.source, CveSource):
            self.source = CveSource()

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        self._normalize_inlined_as_list(slot_name="taxonomyMappings", slot_type=CveTaxonomyMapping, key_name="taxonomyName", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProduct(YAMLRoot):
    """
    One affected product or package, and which of its versions are affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProduct"]
    class_class_curie: ClassVar[str] = "cve:CveProduct"
    class_name: ClassVar[str] = "CveProduct"
    class_model_uri: ClassVar[URIRef] = CVE.CveProduct

    vendor: Optional[Union[str, CveText512]] = None
    product: Optional[Union[str, CveText2048]] = None
    collectionURL: Optional[Union[str, CveUri]] = None
    packageName: Optional[Union[str, CveText2048]] = None
    packageURL: Optional[Union[str, CveUri]] = None
    cpes: Optional[Union[Union[str, CveCpe22and23], list[Union[str, CveCpe22and23]]]] = empty_list()
    modules: Optional[Union[Union[str, CveText4096], list[Union[str, CveText4096]]]] = empty_list()
    programFiles: Optional[Union[Union[str, CveText1024], list[Union[str, CveText1024]]]] = empty_list()
    programRoutines: Optional[Union[Union[dict, "CveProgramRoutine"], list[Union[dict, "CveProgramRoutine"]]]] = empty_list()
    platforms: Optional[Union[Union[str, CveTextUpTo1024], list[Union[str, CveTextUpTo1024]]]] = empty_list()
    repo: Optional[Union[str, CveUri]] = None
    defaultStatus: Optional[Union[str, "CveVersionStatus"]] = None
    versions: Optional[Union[Union[dict, "CveProductVersion"], list[Union[dict, "CveProductVersion"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vendor is not None and not isinstance(self.vendor, CveText512):
            self.vendor = CveText512(self.vendor)

        if self.product is not None and not isinstance(self.product, CveText2048):
            self.product = CveText2048(self.product)

        if self.collectionURL is not None and not isinstance(self.collectionURL, CveUri):
            self.collectionURL = CveUri(self.collectionURL)

        if self.packageName is not None and not isinstance(self.packageName, CveText2048):
            self.packageName = CveText2048(self.packageName)

        if self.packageURL is not None and not isinstance(self.packageURL, CveUri):
            self.packageURL = CveUri(self.packageURL)

        if not isinstance(self.cpes, list):
            self.cpes = [self.cpes] if self.cpes is not None else []
        self.cpes = [v if isinstance(v, CveCpe22and23) else CveCpe22and23(v) for v in self.cpes]

        if not isinstance(self.modules, list):
            self.modules = [self.modules] if self.modules is not None else []
        self.modules = [v if isinstance(v, CveText4096) else CveText4096(v) for v in self.modules]

        if not isinstance(self.programFiles, list):
            self.programFiles = [self.programFiles] if self.programFiles is not None else []
        self.programFiles = [v if isinstance(v, CveText1024) else CveText1024(v) for v in self.programFiles]

        self._normalize_inlined_as_list(slot_name="programRoutines", slot_type=CveProgramRoutine, key_name="name", keyed=False)

        if not isinstance(self.platforms, list):
            self.platforms = [self.platforms] if self.platforms is not None else []
        self.platforms = [v if isinstance(v, CveTextUpTo1024) else CveTextUpTo1024(v) for v in self.platforms]

        if self.repo is not None and not isinstance(self.repo, CveUri):
            self.repo = CveUri(self.repo)

        if self.defaultStatus is not None and not isinstance(self.defaultStatus, CveVersionStatus):
            self.defaultStatus = CveVersionStatus(self.defaultStatus)

        self._normalize_inlined_as_list(slot_name="versions", slot_type=CveProductVersion, key_name="version", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProgramRoutine(YAMLRoot):
    """
    One affected function, method or similar routine in the source.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProgramRoutine"]
    class_class_curie: ClassVar[str] = "cve:CveProgramRoutine"
    class_name: ClassVar[str] = "CveProgramRoutine"
    class_model_uri: ClassVar[URIRef] = CVE.CveProgramRoutine

    name: Union[str, CveText4096] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CveText4096):
            self.name = CveText4096(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProductVersion(YAMLRoot):
    """
    A single version or a stretch of versions, and whether it is affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProductVersion"]
    class_class_curie: ClassVar[str] = "cve:CveProductVersion"
    class_name: ClassVar[str] = "CveProductVersion"
    class_model_uri: ClassVar[URIRef] = CVE.CveProductVersion

    version: Union[str, CveVersion] = None
    status: Union[str, "CveVersionStatus"] = None
    versionType: Optional[Union[str, CveText128]] = None
    lessThan: Optional[Union[str, CveVersion]] = None
    lessThanOrEqual: Optional[Union[str, CveVersion]] = None
    changes: Optional[Union[Union[dict, "CveVersionChange"], list[Union[dict, "CveVersionChange"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, CveVersion):
            self.version = CveVersion(self.version)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, CveVersionStatus):
            self.status = CveVersionStatus(self.status)

        if self.versionType is not None and not isinstance(self.versionType, CveText128):
            self.versionType = CveText128(self.versionType)

        if self.lessThan is not None and not isinstance(self.lessThan, CveVersion):
            self.lessThan = CveVersion(self.lessThan)

        if self.lessThanOrEqual is not None and not isinstance(self.lessThanOrEqual, CveVersion):
            self.lessThanOrEqual = CveVersion(self.lessThanOrEqual)

        self._normalize_inlined_as_list(slot_name="changes", slot_type=CveVersionChange, key_name="at", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveVersionChange(YAMLRoot):
    """
    A point in a range of versions from which the status changes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveVersionChange"]
    class_class_curie: ClassVar[str] = "cve:CveVersionChange"
    class_name: ClassVar[str] = "CveVersionChange"
    class_model_uri: ClassVar[URIRef] = CVE.CveVersionChange

    at: Union[str, CveVersion] = None
    status: Union[str, "CveVersionStatus"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.at):
            self.MissingRequiredField("at")
        if not isinstance(self.at, CveVersion):
            self.at = CveVersion(self.at)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, CveVersionStatus):
            self.status = CveVersionStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCpeApplicabilityElement(YAMLRoot):
    """
    A statement in the CPE Applicability Language of which platforms are affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCpeApplicabilityElement"]
    class_class_curie: ClassVar[str] = "cve:CveCpeApplicabilityElement"
    class_name: ClassVar[str] = "CveCpeApplicabilityElement"
    class_model_uri: ClassVar[URIRef] = CVE.CveCpeApplicabilityElement

    nodes: Union[Union[dict, "CveCpeNode"], list[Union[dict, "CveCpeNode"]]] = None
    operator: Optional[Union[str, "CveCpeOperator"]] = None
    negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=CveCpeNode, key_name="operator", keyed=False)

        if self.operator is not None and not isinstance(self.operator, CveCpeOperator):
            self.operator = CveCpeOperator(self.operator)

        if self.negate is not None and not isinstance(self.negate, Bool):
            self.negate = Bool(self.negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCpeNode(YAMLRoot):
    """
    A group of CPE matches, combined by an operator.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCpeNode"]
    class_class_curie: ClassVar[str] = "cve:CveCpeNode"
    class_name: ClassVar[str] = "CveCpeNode"
    class_model_uri: ClassVar[URIRef] = CVE.CveCpeNode

    operator: Union[str, "CveCpeOperator"] = None
    cpeMatch: Union[Union[dict, "CveCpeMatch"], list[Union[dict, "CveCpeMatch"]]] = None
    negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.operator):
            self.MissingRequiredField("operator")
        if not isinstance(self.operator, CveCpeOperator):
            self.operator = CveCpeOperator(self.operator)

        if self._is_empty(self.cpeMatch):
            self.MissingRequiredField("cpeMatch")
        self._normalize_inlined_as_list(slot_name="cpeMatch", slot_type=CveCpeMatch, key_name="vulnerable", keyed=False)

        if self.negate is not None and not isinstance(self.negate, Bool):
            self.negate = Bool(self.negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCpeMatch(YAMLRoot):
    """
    One CPE name, optionally bounded by versions, and whether it is vulnerable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCpeMatch"]
    class_class_curie: ClassVar[str] = "cve:CveCpeMatch"
    class_name: ClassVar[str] = "CveCpeMatch"
    class_model_uri: ClassVar[URIRef] = CVE.CveCpeMatch

    vulnerable: Union[bool, Bool] = None
    criteria: Union[str, CveCpe23] = None
    matchCriteriaId: Optional[Union[str, CveUuid]] = None
    versionStartExcluding: Optional[Union[str, CveVersion]] = None
    versionStartIncluding: Optional[Union[str, CveVersion]] = None
    versionEndExcluding: Optional[Union[str, CveVersion]] = None
    versionEndIncluding: Optional[Union[str, CveVersion]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vulnerable):
            self.MissingRequiredField("vulnerable")
        if not isinstance(self.vulnerable, Bool):
            self.vulnerable = Bool(self.vulnerable)

        if self._is_empty(self.criteria):
            self.MissingRequiredField("criteria")
        if not isinstance(self.criteria, CveCpe23):
            self.criteria = CveCpe23(self.criteria)

        if self.matchCriteriaId is not None and not isinstance(self.matchCriteriaId, CveUuid):
            self.matchCriteriaId = CveUuid(self.matchCriteriaId)

        if self.versionStartExcluding is not None and not isinstance(self.versionStartExcluding, CveVersion):
            self.versionStartExcluding = CveVersion(self.versionStartExcluding)

        if self.versionStartIncluding is not None and not isinstance(self.versionStartIncluding, CveVersion):
            self.versionStartIncluding = CveVersion(self.versionStartIncluding)

        if self.versionEndExcluding is not None and not isinstance(self.versionEndExcluding, CveVersion):
            self.versionEndExcluding = CveVersion(self.versionEndExcluding)

        if self.versionEndIncluding is not None and not isinstance(self.versionEndIncluding, CveVersion):
            self.versionEndIncluding = CveVersion(self.versionEndIncluding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveDescription(YAMLRoot):
    """
    A piece of text in one language, with any media that support it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveDescription"]
    class_class_curie: ClassVar[str] = "cve:CveDescription"
    class_name: ClassVar[str] = "CveDescription"
    class_model_uri: ClassVar[URIRef] = CVE.CveDescription

    lang: Union[str, CveLanguage] = None
    value: Union[str, CveText4096] = None
    supportingMedia: Optional[Union[Union[dict, "CveSupportingMedia"], list[Union[dict, "CveSupportingMedia"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, CveLanguage):
            self.lang = CveLanguage(self.lang)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CveText4096):
            self.value = CveText4096(self.value)

        self._normalize_inlined_as_list(slot_name="supportingMedia", slot_type=CveSupportingMedia, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveSupportingMedia(YAMLRoot):
    """
    A richer form of a description, as a media type and its content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveSupportingMedia"]
    class_class_curie: ClassVar[str] = "cve:CveSupportingMedia"
    class_name: ClassVar[str] = "CveSupportingMedia"
    class_model_uri: ClassVar[URIRef] = CVE.CveSupportingMedia

    type: Union[str, CveText256] = None
    value: Union[str, CveText16384] = None
    base64: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, CveText256):
            self.type = CveText256(self.type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CveText16384):
            self.value = CveText16384(self.value)

        if self.base64 is not None and not isinstance(self.base64, Bool):
            self.base64 = Bool(self.base64)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProblemType(YAMLRoot):
    """
    One kind of problem the vulnerability is, in one or more languages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProblemType"]
    class_class_curie: ClassVar[str] = "cve:CveProblemType"
    class_name: ClassVar[str] = "CveProblemType"
    class_model_uri: ClassVar[URIRef] = CVE.CveProblemType

    descriptions: Union[Union[dict, "CveProblemTypeDescription"], list[Union[dict, "CveProblemTypeDescription"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.descriptions):
            self.MissingRequiredField("descriptions")
        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=CveProblemTypeDescription, key_name="lang", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveProblemTypeDescription(YAMLRoot):
    """
    A problem type described in one language, often by a weakness identifier and its title.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveProblemTypeDescription"]
    class_class_curie: ClassVar[str] = "cve:CveProblemTypeDescription"
    class_name: ClassVar[str] = "CveProblemTypeDescription"
    class_model_uri: ClassVar[URIRef] = CVE.CveProblemTypeDescription

    lang: Union[str, CveLanguage] = None
    description: Union[str, CveText4096] = None
    type: Optional[Union[str, CveText128]] = None
    references: Optional[Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]]] = empty_list()
    cweId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, CveLanguage):
            self.lang = CveLanguage(self.lang)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, CveText4096):
            self.description = CveText4096(self.description)

        if self.type is not None and not isinstance(self.type, CveText128):
            self.type = CveText128(self.type)

        self._normalize_inlined_as_list(slot_name="references", slot_type=CveReference, key_name="url", keyed=False)

        if self.cweId is not None and not isinstance(self.cweId, str):
            self.cweId = str(self.cweId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveReference(YAMLRoot):
    """
    A link to something about the vulnerability, such as an advisory or a patch.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveReference"]
    class_class_curie: ClassVar[str] = "cve:CveReference"
    class_name: ClassVar[str] = "CveReference"
    class_model_uri: ClassVar[URIRef] = CVE.CveReference

    url: Union[str, CveUri] = None
    name: Optional[Union[str, CveText512]] = None
    tags: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, CveUri):
            self.url = CveUri(self.url)

        if self.name is not None and not isinstance(self.name, CveText512):
            self.name = CveText512(self.name)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveImpact(YAMLRoot):
    """
    A consequence of the vulnerability, in words.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveImpact"]
    class_class_curie: ClassVar[str] = "cve:CveImpact"
    class_name: ClassVar[str] = "CveImpact"
    class_model_uri: ClassVar[URIRef] = CVE.CveImpact

    descriptions: Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]] = None
    capecId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.descriptions):
            self.MissingRequiredField("descriptions")
        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=CveDescription, key_name="lang", keyed=False)

        if self.capecId is not None and not isinstance(self.capecId, str):
            self.capecId = str(self.capecId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveMetric(YAMLRoot):
    """
    One scoring of the vulnerability, in a CVSS version or another format, and where it applies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetric"]
    class_class_curie: ClassVar[str] = "cve:CveMetric"
    class_name: ClassVar[str] = "CveMetric"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetric

    format: Optional[Union[str, CveText64]] = None
    scenarios: Optional[Union[Union[dict, "CveMetricScenario"], list[Union[dict, "CveMetricScenario"]]]] = empty_list()
    cvssV4_0: Optional[Union[dict, CvssV40]] = None
    cvssV3_1: Optional[Union[dict, CvssV31]] = None
    cvssV3_0: Optional[Union[dict, CvssV30]] = None
    cvssV2_0: Optional[Union[dict, CvssV20]] = None
    other: Optional[Union[dict, "CveOtherMetric"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.format is not None and not isinstance(self.format, CveText64):
            self.format = CveText64(self.format)

        self._normalize_inlined_as_list(slot_name="scenarios", slot_type=CveMetricScenario, key_name="lang", keyed=False)

        if self.cvssV4_0 is not None and not isinstance(self.cvssV4_0, CvssV40):
            self.cvssV4_0 = CvssV40(**as_dict(self.cvssV4_0))

        if self.cvssV3_1 is not None and not isinstance(self.cvssV3_1, CvssV31):
            self.cvssV3_1 = CvssV31(**as_dict(self.cvssV3_1))

        if self.cvssV3_0 is not None and not isinstance(self.cvssV3_0, CvssV30):
            self.cvssV3_0 = CvssV30(**as_dict(self.cvssV3_0))

        if self.cvssV2_0 is not None and not isinstance(self.cvssV2_0, CvssV20):
            self.cvssV2_0 = CvssV20(**as_dict(self.cvssV2_0))

        if self.other is not None and not isinstance(self.other, CveOtherMetric):
            self.other = CveOtherMetric(**as_dict(self.other))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveMetricScenario(YAMLRoot):
    """
    A situation a scoring applies to, in one language.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveMetricScenario"]
    class_class_curie: ClassVar[str] = "cve:CveMetricScenario"
    class_name: ClassVar[str] = "CveMetricScenario"
    class_model_uri: ClassVar[URIRef] = CVE.CveMetricScenario

    lang: Union[str, CveLanguage] = None
    value: Union[str, CveText4096] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, CveLanguage):
            self.lang = CveLanguage(self.lang)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CveText4096):
            self.value = CveText4096(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveOtherMetric(YAMLRoot):
    """
    A score or impact statement in a format the record format does not name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveOtherMetric"]
    class_class_curie: ClassVar[str] = "cve:CveOtherMetric"
    class_name: ClassVar[str] = "CveOtherMetric"
    class_model_uri: ClassVar[URIRef] = CVE.CveOtherMetric

    type: Union[str, CveText128] = None
    content: Union[dict, "CveOtherMetricContent"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, CveText128):
            self.type = CveText128(self.type)

        if self._is_empty(self.content):
            self.MissingRequiredField("content")
        if not isinstance(self.content, CveOtherMetricContent):
            self.content = CveOtherMetricContent()

        super().__post_init__(**kwargs)


class CveOtherMetricContent(YAMLRoot):
    """
    The free-form object inside a metric of another format.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveOtherMetricContent"]
    class_class_curie: ClassVar[str] = "cve:CveOtherMetricContent"
    class_name: ClassVar[str] = "CveOtherMetricContent"
    class_model_uri: ClassVar[URIRef] = CVE.CveOtherMetricContent


@dataclass(repr=False)
class CveTimelineEvent(YAMLRoot):
    """
    One dated event in the vulnerability's history.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveTimelineEvent"]
    class_class_curie: ClassVar[str] = "cve:CveTimelineEvent"
    class_name: ClassVar[str] = "CveTimelineEvent"
    class_model_uri: ClassVar[URIRef] = CVE.CveTimelineEvent

    lang: Union[str, CveLanguage] = None
    value: Union[str, CveText4096] = None
    time: Union[str, CveTimestamp] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, CveLanguage):
            self.lang = CveLanguage(self.lang)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CveText4096):
            self.value = CveText4096(self.value)

        if self._is_empty(self.time):
            self.MissingRequiredField("time")
        if not isinstance(self.time, CveTimestamp):
            self.time = CveTimestamp(self.time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveCredit(YAMLRoot):
    """
    Thanks to someone who helped, in one language.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveCredit"]
    class_class_curie: ClassVar[str] = "cve:CveCredit"
    class_name: ClassVar[str] = "CveCredit"
    class_model_uri: ClassVar[URIRef] = CVE.CveCredit

    lang: Union[str, CveLanguage] = None
    value: Union[str, CveText4096] = None
    type: Optional[Union[str, "CveCreditType"]] = 'finder'
    user: Optional[Union[str, CveUuid]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, CveLanguage):
            self.lang = CveLanguage(self.lang)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, CveText4096):
            self.value = CveText4096(self.value)

        if self.type is not None and not isinstance(self.type, CveCreditType):
            self.type = CveCreditType(self.type)

        if self.user is not None and not isinstance(self.user, CveUuid):
            self.user = CveUuid(self.user)

        super().__post_init__(**kwargs)


class CveSource(YAMLRoot):
    """
    How the vulnerability came to light, as an object the provider shapes as it likes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveSource"]
    class_class_curie: ClassVar[str] = "cve:CveSource"
    class_name: ClassVar[str] = "CveSource"
    class_model_uri: ClassVar[URIRef] = CVE.CveSource


@dataclass(repr=False)
class CveTaxonomyMapping(YAMLRoot):
    """
    How the vulnerability relates to one version of an outside taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveTaxonomyMapping"]
    class_class_curie: ClassVar[str] = "cve:CveTaxonomyMapping"
    class_name: ClassVar[str] = "CveTaxonomyMapping"
    class_model_uri: ClassVar[URIRef] = CVE.CveTaxonomyMapping

    taxonomyName: Union[str, CveText128] = None
    taxonomyRelations: Union[Union[dict, "CveTaxonomyRelation"], list[Union[dict, "CveTaxonomyRelation"]]] = None
    taxonomyVersion: Optional[Union[str, CveText128]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomyName):
            self.MissingRequiredField("taxonomyName")
        if not isinstance(self.taxonomyName, CveText128):
            self.taxonomyName = CveText128(self.taxonomyName)

        if self._is_empty(self.taxonomyRelations):
            self.MissingRequiredField("taxonomyRelations")
        self._normalize_inlined_as_list(slot_name="taxonomyRelations", slot_type=CveTaxonomyRelation, key_name="taxonomyId", keyed=False)

        if self.taxonomyVersion is not None and not isinstance(self.taxonomyVersion, CveText128):
            self.taxonomyVersion = CveText128(self.taxonomyVersion)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CveTaxonomyRelation(YAMLRoot):
    """
    One relationship from an item in a taxonomy to this CVE or to another item.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CveTaxonomyRelation"]
    class_class_curie: ClassVar[str] = "cve:CveTaxonomyRelation"
    class_name: ClassVar[str] = "CveTaxonomyRelation"
    class_model_uri: ClassVar[URIRef] = CVE.CveTaxonomyRelation

    taxonomyId: Union[str, CveText2048] = None
    relationshipName: Union[str, CveText128] = None
    relationshipValue: Union[str, CveText2048] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.taxonomyId):
            self.MissingRequiredField("taxonomyId")
        if not isinstance(self.taxonomyId, CveText2048):
            self.taxonomyId = CveText2048(self.taxonomyId)

        if self._is_empty(self.relationshipName):
            self.MissingRequiredField("relationshipName")
        if not isinstance(self.relationshipName, CveText128):
            self.relationshipName = CveText128(self.relationshipName)

        if self._is_empty(self.relationshipValue):
            self.MissingRequiredField("relationshipValue")
        if not isinstance(self.relationshipValue, CveText2048):
            self.relationshipValue = CveText2048(self.relationshipValue)

        super().__post_init__(**kwargs)


# Enumerations
class CvssSeverity(EnumDefinitionImpl):
    """
    A CVSS rating in words.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No severity at all, for a score of 0.",
        meaning=SPDX_SECURITY["CvssSeverityType/none"])
    LOW = PermissibleValue(
        text="LOW",
        description="The lowest rating above none.",
        meaning=SPDX_SECURITY["CvssSeverityType/low"])
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="The middle rating.",
        meaning=SPDX_SECURITY["CvssSeverityType/medium"])
    HIGH = PermissibleValue(
        text="HIGH",
        description="The rating below critical.",
        meaning=SPDX_SECURITY["CvssSeverityType/high"])
    CRITICAL = PermissibleValue(
        text="CRITICAL",
        description="The highest rating.",
        meaning=SPDX_SECURITY["CvssSeverityType/critical"])

    _defn = EnumDefinition(
        name="CvssSeverity",
        description="A CVSS rating in words.",
    )

class CvssV2AccessVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 2.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from the same local network segment.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only with an account on the system or hands on it.")

    _defn = EnumDefinition(
        name="CvssV2AccessVector",
        description="How far away an attacker can be, in CVSS 2.0's terms.",
    )

class CvssV2AccessComplexity(EnumDefinitionImpl):
    """
    How hard the flaw is to use, in CVSS 2.0's terms.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Only under unusual, hard-to-arrange conditions.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="Under conditions that take some arranging.")
    LOW = PermissibleValue(
        text="LOW",
        description="With no special conditions.")

    _defn = EnumDefinition(
        name="CvssV2AccessComplexity",
        description="How hard the flaw is to use, in CVSS 2.0's terms.",
    )

class CvssV2Authentication(EnumDefinitionImpl):
    """
    How many logins an attacker needs, in CVSS 2.0's terms.
    """
    MULTIPLE = PermissibleValue(
        text="MULTIPLE",
        description="More than one login.")
    SINGLE = PermissibleValue(
        text="SINGLE",
        description="One login.")
    NONE = PermissibleValue(
        text="NONE",
        description="No login at all.")

    _defn = EnumDefinition(
        name="CvssV2Authentication",
        description="How many logins an attacker needs, in CVSS 2.0's terms.",
    )

class CvssV2Impact(EnumDefinitionImpl):
    """
    How much of one security property an attack could cost, in CVSS 2.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="Some is lost, and the attacker cannot choose all of it.")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="All of it is lost.")

    _defn = EnumDefinition(
        name="CvssV2Impact",
        description="How much of one security property an attack could cost, in CVSS 2.0's terms.",
    )

class CvssExploitCodeMaturity(EnumDefinitionImpl):
    """
    How far working attack code has come.
    """
    UNPROVEN = PermissibleValue(
        text="UNPROVEN",
        description="No attack code is known, or the attack is only theory.")
    PROOF_OF_CONCEPT = PermissibleValue(
        text="PROOF_OF_CONCEPT",
        description="A demonstration exists that needs skilled work to use.")
    FUNCTIONAL = PermissibleValue(
        text="FUNCTIONAL",
        description="Working attack code exists for most situations.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Attack code is reliable and widely available, or no code is needed.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssExploitCodeMaturity",
        description="How far working attack code has come.",
    )

class CvssRemediationLevel(EnumDefinitionImpl):
    """
    What kind of fix is available.
    """
    OFFICIAL_FIX = PermissibleValue(
        text="OFFICIAL_FIX",
        description="The vendor offers a complete fix.")
    TEMPORARY_FIX = PermissibleValue(
        text="TEMPORARY_FIX",
        description="The vendor offers a stopgap for now.")
    WORKAROUND = PermissibleValue(
        text="WORKAROUND",
        description="Others offer a way round the flaw that is not from the vendor.")
    UNAVAILABLE = PermissibleValue(
        text="UNAVAILABLE",
        description="No fix exists, or it cannot be applied.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssRemediationLevel",
        description="What kind of fix is available.",
    )

class CvssV2ReportConfidence(EnumDefinitionImpl):
    """
    How far the flaw has been confirmed, in CVSS 2.0's terms.
    """
    UNCONFIRMED = PermissibleValue(
        text="UNCONFIRMED",
        description="A single report or conflicting reports that nobody has checked.")
    UNCORROBORATED = PermissibleValue(
        text="UNCORROBORATED",
        description="Several unofficial sources agree, with some doubt remaining.")
    CONFIRMED = PermissibleValue(
        text="CONFIRMED",
        description="The vendor accepts it, or a working attack shows it.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2ReportConfidence",
        description="How far the flaw has been confirmed, in CVSS 2.0's terms.",
    )

class CvssV2CollateralDamagePotential(EnumDefinitionImpl):
    """
    How much loss could follow beyond the system itself.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No such loss.")
    LOW = PermissibleValue(
        text="LOW",
        description="Slight loss.")
    LOW_MEDIUM = PermissibleValue(
        text="LOW_MEDIUM",
        description="Moderate loss.")
    MEDIUM_HIGH = PermissibleValue(
        text="MEDIUM_HIGH",
        description="Significant loss.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Catastrophic loss.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2CollateralDamagePotential",
        description="How much loss could follow beyond the system itself.",
    )

class CvssV2TargetDistribution(EnumDefinitionImpl):
    """
    How much of the environment the flaw exposes.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No systems at all, or only in a lab.")
    LOW = PermissibleValue(
        text="LOW",
        description="Up to about a quarter of systems.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="About a quarter to three quarters of systems.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="More than about three quarters of systems.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2TargetDistribution",
        description="How much of the environment the flaw exposes.",
    )

class CvssRequirement(EnumDefinitionImpl):
    """
    How much one security property matters to the scorer.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="A loss would have limited effect.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="A loss would have serious effect.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="A loss would have catastrophic effect.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssRequirement",
        description="How much one security property matters to the scorer.",
    )

class CvssV3AttackVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 3's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from a logically nearby network.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")

    _defn = EnumDefinition(
        name="CvssV3AttackVector",
        description="How far away an attacker can be, in CVSS 3's terms.",
    )

class CvssV3ModifiedAttackVector(EnumDefinitionImpl):
    """
    The attack vector as the scorer's environment changes it, in CVSS 3's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from a logically nearby network.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedAttackVector",
        description="The attack vector as the scorer's environment changes it, in CVSS 3's terms.",
    )

class CvssAttackComplexity(EnumDefinitionImpl):
    """
    How much is outside the attacker's control.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Success depends on conditions the attacker must overcome or wait for.")
    LOW = PermissibleValue(
        text="LOW",
        description="The attacker can succeed again and again with no special effort.")

    _defn = EnumDefinition(
        name="CvssAttackComplexity",
        description="How much is outside the attacker's control.",
    )

class CvssModifiedAttackComplexity(EnumDefinitionImpl):
    """
    The attack complexity as the scorer's environment changes it.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Success depends on conditions the attacker must overcome or wait for.")
    LOW = PermissibleValue(
        text="LOW",
        description="The attacker can succeed again and again with no special effort.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedAttackComplexity",
        description="The attack complexity as the scorer's environment changes it.",
    )

class CvssPrivilegesRequired(EnumDefinitionImpl):
    """
    What access an attacker needs beforehand.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Administrator-level access.")
    LOW = PermissibleValue(
        text="LOW",
        description="Ordinary user access.")
    NONE = PermissibleValue(
        text="NONE",
        description="No access at all.")

    _defn = EnumDefinition(
        name="CvssPrivilegesRequired",
        description="What access an attacker needs beforehand.",
    )

class CvssModifiedPrivilegesRequired(EnumDefinitionImpl):
    """
    The access needed as the scorer's environment changes it.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Administrator-level access.")
    LOW = PermissibleValue(
        text="LOW",
        description="Ordinary user access.")
    NONE = PermissibleValue(
        text="NONE",
        description="No access at all.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedPrivilegesRequired",
        description="The access needed as the scorer's environment changes it.",
    )

class CvssV3UserInteraction(EnumDefinitionImpl):
    """
    Whether someone else has to take part, in CVSS 3's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    REQUIRED = PermissibleValue(
        text="REQUIRED",
        description="Someone other than the attacker has to do something.")

    _defn = EnumDefinition(
        name="CvssV3UserInteraction",
        description="Whether someone else has to take part, in CVSS 3's terms.",
    )

class CvssV3ModifiedUserInteraction(EnumDefinitionImpl):
    """
    The user interaction as the scorer's environment changes it, in CVSS 3's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    REQUIRED = PermissibleValue(
        text="REQUIRED",
        description="Someone other than the attacker has to do something.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedUserInteraction",
        description="The user interaction as the scorer's environment changes it, in CVSS 3's terms.",
    )

class CvssV3Scope(EnumDefinitionImpl):
    """
    Whether an attack can reach beyond the flawed component.
    """
    UNCHANGED = PermissibleValue(
        text="UNCHANGED",
        description="The harm stays within the same security authority.")
    CHANGED = PermissibleValue(
        text="CHANGED",
        description="The harm can reach something under another security authority.")

    _defn = EnumDefinition(
        name="CvssV3Scope",
        description="Whether an attack can reach beyond the flawed component.",
    )

class CvssV3ModifiedScope(EnumDefinitionImpl):
    """
    The scope as the scorer's environment changes it.
    """
    UNCHANGED = PermissibleValue(
        text="UNCHANGED",
        description="The harm stays within the same security authority.")
    CHANGED = PermissibleValue(
        text="CHANGED",
        description="The harm can reach something under another security authority.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedScope",
        description="The scope as the scorer's environment changes it.",
    )

class CvssImpact(EnumDefinitionImpl):
    """
    How much of one security property an attack could cost.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")

    _defn = EnumDefinition(
        name="CvssImpact",
        description="How much of one security property an attack could cost.",
    )

class CvssModifiedImpact(EnumDefinitionImpl):
    """
    The impact on one security property as the scorer's environment changes it.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedImpact",
        description="The impact on one security property as the scorer's environment changes it.",
    )

class CvssV3ReportConfidence(EnumDefinitionImpl):
    """
    How far the flaw has been confirmed, in CVSS 3's terms.
    """
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Reports say something is wrong, but the cause is not clear.")
    REASONABLE = PermissibleValue(
        text="REASONABLE",
        description="Solid details exist, without full confirmation of the cause.")
    CONFIRMED = PermissibleValue(
        text="CONFIRMED",
        description="The flaw is shown beyond doubt, or the vendor accepts it.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV3ReportConfidence",
        description="How far the flaw has been confirmed, in CVSS 3's terms.",
    )

class CvssV4AttackVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 4.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT = PermissibleValue(
        text="ADJACENT",
        description="Only from something logically or physically nearby.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")

    _defn = EnumDefinition(
        name="CvssV4AttackVector",
        description="How far away an attacker can be, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedAttackVector(EnumDefinitionImpl):
    """
    The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT = PermissibleValue(
        text="ADJACENT",
        description="Only from something logically or physically nearby.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedAttackVector",
        description="The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.",
    )

class CvssV4AttackRequirements(EnumDefinitionImpl):
    """
    Whether the attack needs conditions in the target beyond the attacker's control.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack works whatever the target's state.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The attack works only when the target is in a certain state.")

    _defn = EnumDefinition(
        name="CvssV4AttackRequirements",
        description="Whether the attack needs conditions in the target beyond the attacker's control.",
    )

class CvssV4ModifiedAttackRequirements(EnumDefinitionImpl):
    """
    The attack requirements as the scorer's environment changes them.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack works whatever the target's state.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The attack works only when the target is in a certain state.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedAttackRequirements",
        description="The attack requirements as the scorer's environment changes them.",
    )

class CvssV4UserInteraction(EnumDefinitionImpl):
    """
    Whether someone else has to take part, in CVSS 4.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    PASSIVE = PermissibleValue(
        text="PASSIVE",
        description="Someone has to act only in the ordinary course of their work.")
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Someone has to take a deliberate step.")

    _defn = EnumDefinition(
        name="CvssV4UserInteraction",
        description="Whether someone else has to take part, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedUserInteraction(EnumDefinitionImpl):
    """
    The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    PASSIVE = PermissibleValue(
        text="PASSIVE",
        description="Someone has to act only in the ordinary course of their work.")
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Someone has to take a deliberate step.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedUserInteraction",
        description="The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedSubsequentImpact(EnumDefinitionImpl):
    """
    The integrity or availability impact on connected systems as the scorer's environment changes it, which may
    include a risk to safety.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")
    SAFETY = PermissibleValue(
        text="SAFETY",
        description="The loss could injure people.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedSubsequentImpact",
        description="""The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.""",
    )

class CvssV4ExploitMaturity(EnumDefinitionImpl):
    """
    How much is known about attacks on the flaw.
    """
    UNREPORTED = PermissibleValue(
        text="UNREPORTED",
        description="No demonstration or attack has been reported.")
    PROOF_OF_CONCEPT = PermissibleValue(
        text="PROOF_OF_CONCEPT",
        description="A demonstration is public, with no reported attack.")
    ATTACKED = PermissibleValue(
        text="ATTACKED",
        description="Attacks have been reported, or tools for them are public.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the worst case is assumed.")

    _defn = EnumDefinition(
        name="CvssV4ExploitMaturity",
        description="How much is known about attacks on the flaw.",
    )

class CvssV4Safety(EnumDefinitionImpl):
    """
    Whether an attack could put people's safety at risk.
    """
    NEGLIGIBLE = PermissibleValue(
        text="NEGLIGIBLE",
        description="Any harm to people would be slight at most.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="People could be seriously hurt.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Safety",
        description="Whether an attack could put people's safety at risk.",
    )

class CvssV4Automatable(EnumDefinitionImpl):
    """
    Whether every step of an attack could be automated across many targets.
    """
    NO = PermissibleValue(
        text="NO",
        description="At least one step resists automation.")
    YES = PermissibleValue(
        text="YES",
        description="Every step can be automated.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Automatable",
        description="Whether every step of an attack could be automated across many targets.",
    )

class CvssV4Recovery(EnumDefinitionImpl):
    """
    How the affected system comes back after an attack.
    """
    AUTOMATIC = PermissibleValue(
        text="AUTOMATIC",
        description="The system recovers by itself.")
    USER = PermissibleValue(
        text="USER",
        description="Someone has to step in and restore it.")
    IRRECOVERABLE = PermissibleValue(
        text="IRRECOVERABLE",
        description="The system cannot be restored.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Recovery",
        description="How the affected system comes back after an attack.",
    )

class CvssV4ValueDensity(EnumDefinitionImpl):
    """
    How much of a resource one successful attack gains the attacker.
    """
    DIFFUSE = PermissibleValue(
        text="DIFFUSE",
        description="Each target holds little, so an attacker must take many.")
    CONCENTRATED = PermissibleValue(
        text="CONCENTRATED",
        description="A single target holds a lot.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ValueDensity",
        description="How much of a resource one successful attack gains the attacker.",
    )

class CvssV4ResponseEffort(EnumDefinitionImpl):
    """
    How much work it takes a consumer to respond to the flaw.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="Little work, such as reading advice or a small configuration change.")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Some work, with a noticeable effect on the service.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Much work, or a long outage.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ResponseEffort",
        description="How much work it takes a consumer to respond to the flaw.",
    )

class CvssV4ProviderUrgency(EnumDefinitionImpl):
    """
    How urgent the product's supplier says the flaw is, as a colour.
    """
    CLEAR = PermissibleValue(
        text="CLEAR",
        description="The supplier sees little or no urgency.")
    GREEN = PermissibleValue(
        text="GREEN",
        description="The supplier says the flaw can wait for regular work.")
    AMBER = PermissibleValue(
        text="AMBER",
        description="The supplier says the flaw matters soon.")
    RED = PermissibleValue(
        text="RED",
        description="The supplier says the flaw is at the highest urgency.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ProviderUrgency",
        description="How urgent the product's supplier says the flaw is, as a colour.",
    )

class CveDataType(EnumDefinitionImpl):
    """
    The kind of document a CVE record is.
    """
    CVE_RECORD = PermissibleValue(
        text="CVE_RECORD",
        description="A document in the CVE Record Format.")

    _defn = EnumDefinition(
        name="CveDataType",
        description="The kind of document a CVE record is.",
    )

class CveRecordState(EnumDefinitionImpl):
    """
    Whether a record is in use.
    """
    PUBLISHED = PermissibleValue(
        text="PUBLISHED",
        description="The assigning authority has filled the record in and made it public.")
    REJECTED = PermissibleValue(
        text="REJECTED",
        description="The identifier and its record are withdrawn from use.")

    _defn = EnumDefinition(
        name="CveRecordState",
        description="Whether a record is in use.",
    )

class CvePublishedState(EnumDefinitionImpl):
    """
    The state of a published record.
    """
    PUBLISHED = PermissibleValue(
        text="PUBLISHED",
        description="The assigning authority has filled the record in and made it public.")

    _defn = EnumDefinition(
        name="CvePublishedState",
        description="The state of a published record.",
    )

class CveRejectedState(EnumDefinitionImpl):
    """
    The state of a rejected record.
    """
    REJECTED = PermissibleValue(
        text="REJECTED",
        description="The identifier and its record are withdrawn from use.")

    _defn = EnumDefinition(
        name="CveRejectedState",
        description="The state of a rejected record.",
    )

class CveVersionStatus(EnumDefinitionImpl):
    """
    Whether a version is affected.
    """
    affected = PermissibleValue(
        text="affected",
        description="The vulnerability is present in this version.")
    unaffected = PermissibleValue(
        text="unaffected",
        description="The vulnerability is not present in this version.")
    unknown = PermissibleValue(
        text="unknown",
        description="It is not known whether the vulnerability is present.")

    _defn = EnumDefinition(
        name="CveVersionStatus",
        description="Whether a version is affected.",
    )

class CveCpeOperator(EnumDefinitionImpl):
    """
    How the parts of a CPE statement combine.
    """
    AND = PermissibleValue(
        text="AND",
        description="All of the parts must hold.")
    OR = PermissibleValue(
        text="OR",
        description="At least one of the parts must hold.")

    _defn = EnumDefinition(
        name="CveCpeOperator",
        description="How the parts of a CPE statement combine.",
    )

class CveCreditType(EnumDefinitionImpl):
    """
    The part a credited person or organisation played.
    """
    finder = PermissibleValue(
        text="finder",
        description="Found the vulnerability.")
    reporter = PermissibleValue(
        text="reporter",
        description="Told the vendor or a CVE Numbering Authority about it.")
    analyst = PermissibleValue(
        text="analyst",
        description="Checked that it is accurate or how severe it is.")
    coordinator = PermissibleValue(
        text="coordinator",
        description="Organised the response among those involved.")
    tool = PermissibleValue(
        text="tool",
        description="A tool used to find or identify it.")
    sponsor = PermissibleValue(
        text="sponsor",
        description="Supported the work of finding or fixing it.")
    other = PermissibleValue(
        text="other",
        description="Any other part.")

    _defn = EnumDefinition(
        name="CveCreditType",
        description="The part a credited person or organisation played.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "remediation developer",
            PermissibleValue(
                text="remediation developer",
                title="remediation_developer",
                description="Prepared the code change or plan that addresses it."))
        setattr(cls, "remediation reviewer",
            PermissibleValue(
                text="remediation reviewer",
                title="remediation_reviewer",
                description="Reviewed that change or plan for how well it works."))
        setattr(cls, "remediation verifier",
            PermissibleValue(
                text="remediation verifier",
                title="remediation_verifier",
                description="Tested the vulnerability or the fix for it."))

class CveCnaTag(EnumDefinitionImpl):
    """
    A label the assigning authority can put on a record.
    """
    disputed = PermissibleValue(
        text="disputed",
        description="Someone disagrees that this is a vulnerability at all.")

    _defn = EnumDefinition(
        name="CveCnaTag",
        description="A label the assigning authority can put on a record.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unsupported-when-assigned",
            PermissibleValue(
                text="unsupported-when-assigned",
                description="Everything affected was out of support when the identifier was requested."))
        setattr(cls, "exclusively-hosted-service",
            PermissibleValue(
                text="exclusively-hosted-service",
                description="Everything affected exists only as a hosted service."))

class CveAdpTag(EnumDefinitionImpl):
    """
    A label an Authorized Data Publisher can put on a record.
    """
    disputed = PermissibleValue(
        text="disputed",
        description="Someone disagrees that this is a vulnerability at all.")

    _defn = EnumDefinition(
        name="CveAdpTag",
        description="A label an Authorized Data Publisher can put on a record.",
    )

class CveReferenceTag(EnumDefinitionImpl):
    """
    A label that says what a reference is.
    """
    exploit = PermissibleValue(
        text="exploit",
        description="It shows how to attack the flaw, or holds working attack code.")
    mitigation = PermissibleValue(
        text="mitigation",
        description="It says how to reduce the risk when no patch can be applied.")
    patch = PermissibleValue(
        text="patch",
        description="It holds an update that fixes the flaw.")
    product = PermissibleValue(
        text="product",
        description="It identifies the affected product, for naming schemes such as CPE.")
    related = PermissibleValue(
        text="related",
        description="It concerns a related flaw, not this one.")
    signature = PermissibleValue(
        text="signature",
        description="It holds a way to detect or block the flaw or attacks on it.")

    _defn = EnumDefinition(
        name="CveReferenceTag",
        description="A label that says what a reference is.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "broken-link",
            PermissibleValue(
                text="broken-link",
                description="The address no longer answers."))
        setattr(cls, "customer-entitlement",
            PermissibleValue(
                text="customer-entitlement",
                description="Only paying customers of the vendor can read it."))
        setattr(cls, "government-resource",
            PermissibleValue(
                text="government-resource",
                description="It comes from a government body."))
        setattr(cls, "issue-tracking",
            PermissibleValue(
                text="issue-tracking",
                description="It is a post in a bug tracker."))
        setattr(cls, "mailing-list",
            PermissibleValue(
                text="mailing-list",
                description="It comes from a mailing list."))
        setattr(cls, "not-applicable",
            PermissibleValue(
                text="not-applicable",
                description="It has nothing to do with this vulnerability and was linked by mistake."))
        setattr(cls, "permissions-required",
            PermissibleValue(
                text="permissions-required",
                description="A login blocks the way to it."))
        setattr(cls, "media-coverage",
            PermissibleValue(
                text="media-coverage",
                description="It is a news story or similar report."))
        setattr(cls, "release-notes",
            PermissibleValue(
                text="release-notes",
                description="It is a set of release notes."))
        setattr(cls, "technical-description",
            PermissibleValue(
                text="technical-description",
                description="It explains the flaw and how it is attacked, in technical depth."))
        setattr(cls, "third-party-advisory",
            PermissibleValue(
                text="third-party-advisory",
                description="It is an advisory from someone other than the vendor."))
        setattr(cls, "vendor-advisory",
            PermissibleValue(
                text="vendor-advisory",
                description="It is an advisory from the vendor."))
        setattr(cls, "vdb-entry",
            PermissibleValue(
                text="vdb-entry",
                description="It is an entry in a vulnerability database."))

# Slots
class slots:
    pass

slots.version = Slot(uri=CVE.version, name="version", curie=CVE.curie('version'),
                   model_uri=CVE.version, domain=None, range=Optional[str])

slots.vectorString = Slot(uri=CVE.vectorString, name="vectorString", curie=CVE.curie('vectorString'),
                   model_uri=CVE.vectorString, domain=None, range=str)

slots.baseScore = Slot(uri=CVE.baseScore, name="baseScore", curie=CVE.curie('baseScore'),
                   model_uri=CVE.baseScore, domain=None, range=float)

slots.baseSeverity = Slot(uri=CVE.baseSeverity, name="baseSeverity", curie=CVE.curie('baseSeverity'),
                   model_uri=CVE.baseSeverity, domain=None, range=Union[str, "CvssSeverity"])

slots.temporalScore = Slot(uri=CVE.temporalScore, name="temporalScore", curie=CVE.curie('temporalScore'),
                   model_uri=CVE.temporalScore, domain=None, range=Optional[float])

slots.temporalSeverity = Slot(uri=CVE.temporalSeverity, name="temporalSeverity", curie=CVE.curie('temporalSeverity'),
                   model_uri=CVE.temporalSeverity, domain=None, range=Optional[Union[str, "CvssSeverity"]])

slots.environmentalScore = Slot(uri=CVE.environmentalScore, name="environmentalScore", curie=CVE.curie('environmentalScore'),
                   model_uri=CVE.environmentalScore, domain=None, range=Optional[float])

slots.environmentalSeverity = Slot(uri=CVE.environmentalSeverity, name="environmentalSeverity", curie=CVE.curie('environmentalSeverity'),
                   model_uri=CVE.environmentalSeverity, domain=None, range=Optional[Union[str, "CvssSeverity"]])

slots.attackVector = Slot(uri=CVE.attackVector, name="attackVector", curie=CVE.curie('attackVector'),
                   model_uri=CVE.attackVector, domain=None, range=Optional[str])

slots.attackComplexity = Slot(uri=CVE.attackComplexity, name="attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=CVE.attackComplexity, domain=None, range=Optional[str])

slots.privilegesRequired = Slot(uri=CVE.privilegesRequired, name="privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=CVE.privilegesRequired, domain=None, range=Optional[str])

slots.userInteraction = Slot(uri=CVE.userInteraction, name="userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=CVE.userInteraction, domain=None, range=Optional[str])

slots.scope = Slot(uri=CVE.scope, name="scope", curie=CVE.curie('scope'),
                   model_uri=CVE.scope, domain=None, range=Optional[Union[str, "CvssV3Scope"]])

slots.confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=CVE.confidentialityImpact, domain=None, range=Optional[str])

slots.integrityImpact = Slot(uri=CVE.integrityImpact, name="integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=CVE.integrityImpact, domain=None, range=Optional[str])

slots.availabilityImpact = Slot(uri=CVE.availabilityImpact, name="availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=CVE.availabilityImpact, domain=None, range=Optional[str])

slots.exploitCodeMaturity = Slot(uri=CVE.exploitCodeMaturity, name="exploitCodeMaturity", curie=CVE.curie('exploitCodeMaturity'),
                   model_uri=CVE.exploitCodeMaturity, domain=None, range=Optional[Union[str, "CvssExploitCodeMaturity"]])

slots.remediationLevel = Slot(uri=CVE.remediationLevel, name="remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=CVE.remediationLevel, domain=None, range=Optional[str])

slots.reportConfidence = Slot(uri=CVE.reportConfidence, name="reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=CVE.reportConfidence, domain=None, range=Optional[str])

slots.confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=CVE.confidentialityRequirement, domain=None, range=Optional[str])

slots.integrityRequirement = Slot(uri=CVE.integrityRequirement, name="integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=CVE.integrityRequirement, domain=None, range=Optional[str])

slots.availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=CVE.availabilityRequirement, domain=None, range=Optional[str])

slots.modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=CVE.modifiedAttackVector, domain=None, range=Optional[str])

slots.modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=CVE.modifiedAttackComplexity, domain=None, range=Optional[str])

slots.modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=CVE.modifiedPrivilegesRequired, domain=None, range=Optional[str])

slots.modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=CVE.modifiedUserInteraction, domain=None, range=Optional[str])

slots.modifiedScope = Slot(uri=CVE.modifiedScope, name="modifiedScope", curie=CVE.curie('modifiedScope'),
                   model_uri=CVE.modifiedScope, domain=None, range=Optional[Union[str, "CvssV3ModifiedScope"]])

slots.modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=CVE.modifiedConfidentialityImpact, domain=None, range=Optional[str])

slots.modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=CVE.modifiedIntegrityImpact, domain=None, range=Optional[str])

slots.modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=CVE.modifiedAvailabilityImpact, domain=None, range=Optional[str])

slots.cveMetadata = Slot(uri=CVE.cveMetadata, name="cveMetadata", curie=CVE.curie('cveMetadata'),
                   model_uri=CVE.cveMetadata, domain=None, range=Union[dict, CveRecordMetadata])

slots.containers = Slot(uri=CVE.containers, name="containers", curie=CVE.curie('containers'),
                   model_uri=CVE.containers, domain=None, range=Union[dict, CveContainers])

slots.state = Slot(uri=CVE.state, name="state", curie=CVE.curie('state'),
                   model_uri=CVE.state, domain=None, range=Union[str, "CveRecordState"])

slots.dateUpdated = Slot(uri=CVE.dateUpdated, name="dateUpdated", curie=CVE.curie('dateUpdated'),
                   model_uri=CVE.dateUpdated, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.cna = Slot(uri=CVE.cna, name="cna", curie=CVE.curie('cna'),
                   model_uri=CVE.cna, domain=None, range=Union[dict, CveCnaContainer])

slots.providerMetadata = Slot(uri=CVE.providerMetadata, name="providerMetadata", curie=CVE.curie('providerMetadata'),
                   model_uri=CVE.providerMetadata, domain=None, range=Union[dict, CveProviderMetadata])

slots.datePublic = Slot(uri=CVE.datePublic, name="datePublic", curie=CVE.curie('datePublic'),
                   model_uri=CVE.datePublic, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.title = Slot(uri=CVE.title, name="title", curie=CVE.curie('title'),
                   model_uri=CVE.title, domain=None, range=Optional[Union[str, CveText256]])

slots.descriptions = Slot(uri=CVE.descriptions, name="descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.descriptions, domain=None, range=Optional[Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]]])

slots.affected = Slot(uri=CVE.affected, name="affected", curie=CVE.curie('affected'),
                   model_uri=CVE.affected, domain=None, range=Optional[Union[Union[dict, CveProduct], list[Union[dict, CveProduct]]]])

slots.cpeApplicability = Slot(uri=CVE.cpeApplicability, name="cpeApplicability", curie=CVE.curie('cpeApplicability'),
                   model_uri=CVE.cpeApplicability, domain=None, range=Optional[Union[Union[dict, CveCpeApplicabilityElement], list[Union[dict, CveCpeApplicabilityElement]]]])

slots.problemTypes = Slot(uri=CVE.problemTypes, name="problemTypes", curie=CVE.curie('problemTypes'),
                   model_uri=CVE.problemTypes, domain=None, range=Optional[Union[Union[dict, CveProblemType], list[Union[dict, CveProblemType]]]])

slots.references = Slot(uri=CVE.references, name="references", curie=CVE.curie('references'),
                   model_uri=CVE.references, domain=None, range=Optional[Union[Union[dict, CveReference], list[Union[dict, CveReference]]]])

slots.impacts = Slot(uri=CVE.impacts, name="impacts", curie=CVE.curie('impacts'),
                   model_uri=CVE.impacts, domain=None, range=Optional[Union[Union[dict, CveImpact], list[Union[dict, CveImpact]]]])

slots.metrics = Slot(uri=CVE.metrics, name="metrics", curie=CVE.curie('metrics'),
                   model_uri=CVE.metrics, domain=None, range=Optional[Union[Union[dict, CveMetric], list[Union[dict, CveMetric]]]])

slots.configurations = Slot(uri=CVE.configurations, name="configurations", curie=CVE.curie('configurations'),
                   model_uri=CVE.configurations, domain=None, range=Optional[Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]]])

slots.workarounds = Slot(uri=CVE.workarounds, name="workarounds", curie=CVE.curie('workarounds'),
                   model_uri=CVE.workarounds, domain=None, range=Optional[Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]]])

slots.solutions = Slot(uri=CVE.solutions, name="solutions", curie=CVE.curie('solutions'),
                   model_uri=CVE.solutions, domain=None, range=Optional[Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]]])

slots.exploits = Slot(uri=CVE.exploits, name="exploits", curie=CVE.curie('exploits'),
                   model_uri=CVE.exploits, domain=None, range=Optional[Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]]])

slots.timeline = Slot(uri=CVE.timeline, name="timeline", curie=CVE.curie('timeline'),
                   model_uri=CVE.timeline, domain=None, range=Optional[Union[Union[dict, CveTimelineEvent], list[Union[dict, CveTimelineEvent]]]])

slots.credits = Slot(uri=CVE.credits, name="credits", curie=CVE.curie('credits'),
                   model_uri=CVE.credits, domain=None, range=Optional[Union[Union[dict, CveCredit], list[Union[dict, CveCredit]]]])

slots.source = Slot(uri=CVE.source, name="source", curie=CVE.curie('source'),
                   model_uri=CVE.source, domain=None, range=Optional[Union[dict, CveSource]])

slots.taxonomyMappings = Slot(uri=CVE.taxonomyMappings, name="taxonomyMappings", curie=CVE.curie('taxonomyMappings'),
                   model_uri=CVE.taxonomyMappings, domain=None, range=Optional[Union[Union[dict, CveTaxonomyMapping], list[Union[dict, CveTaxonomyMapping]]]])

slots.tags = Slot(uri=CVE.tags, name="tags", curie=CVE.curie('tags'),
                   model_uri=CVE.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.operator = Slot(uri=CVE.operator, name="operator", curie=CVE.curie('operator'),
                   model_uri=CVE.operator, domain=None, range=Optional[Union[str, "CveCpeOperator"]])

slots.negate = Slot(uri=CVE.negate, name="negate", curie=CVE.curie('negate'),
                   model_uri=CVE.negate, domain=None, range=Optional[Union[bool, Bool]])

slots.lang = Slot(uri=CVE.lang, name="lang", curie=CVE.curie('lang'),
                   model_uri=CVE.lang, domain=None, range=Optional[Union[str, CveLanguage]])

slots.value = Slot(uri=CVE.value, name="value", curie=CVE.curie('value'),
                   model_uri=CVE.value, domain=None, range=Optional[str])

slots.type = Slot(uri=CVE.type, name="type", curie=CVE.curie('type'),
                   model_uri=CVE.type, domain=None, range=Optional[str])

slots.description = Slot(uri=CVE.description, name="description", curie=CVE.curie('description'),
                   model_uri=CVE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=CVE.name, name="name", curie=CVE.curie('name'),
                   model_uri=CVE.name, domain=None, range=Optional[str])

slots.url = Slot(uri=CVE.url, name="url", curie=CVE.curie('url'),
                   model_uri=CVE.url, domain=None, range=Optional[Union[str, CveUri]])

slots.status = Slot(uri=CVE.status, name="status", curie=CVE.curie('status'),
                   model_uri=CVE.status, domain=None, range=Optional[Union[str, "CveVersionStatus"]])

slots.at = Slot(uri=CVE.at, name="at", curie=CVE.curie('at'),
                   model_uri=CVE.at, domain=None, range=Optional[Union[str, CveVersion]])

slots.cvssV20__accessVector = Slot(uri=CVE.accessVector, name="cvssV20__accessVector", curie=CVE.curie('accessVector'),
                   model_uri=CVE.cvssV20__accessVector, domain=None, range=Optional[Union[str, "CvssV2AccessVector"]])

slots.cvssV20__accessComplexity = Slot(uri=CVE.accessComplexity, name="cvssV20__accessComplexity", curie=CVE.curie('accessComplexity'),
                   model_uri=CVE.cvssV20__accessComplexity, domain=None, range=Optional[Union[str, "CvssV2AccessComplexity"]])

slots.cvssV20__authentication = Slot(uri=CVE.authentication, name="cvssV20__authentication", curie=CVE.curie('authentication'),
                   model_uri=CVE.cvssV20__authentication, domain=None, range=Optional[Union[str, "CvssV2Authentication"]])

slots.cvssV20__exploitability = Slot(uri=CVE.exploitability, name="cvssV20__exploitability", curie=CVE.curie('exploitability'),
                   model_uri=CVE.cvssV20__exploitability, domain=None, range=Optional[Union[str, "CvssExploitCodeMaturity"]])

slots.cvssV20__collateralDamagePotential = Slot(uri=CVE.collateralDamagePotential, name="cvssV20__collateralDamagePotential", curie=CVE.curie('collateralDamagePotential'),
                   model_uri=CVE.cvssV20__collateralDamagePotential, domain=None, range=Optional[Union[str, "CvssV2CollateralDamagePotential"]])

slots.cvssV20__targetDistribution = Slot(uri=CVE.targetDistribution, name="cvssV20__targetDistribution", curie=CVE.curie('targetDistribution'),
                   model_uri=CVE.cvssV20__targetDistribution, domain=None, range=Optional[Union[str, "CvssV2TargetDistribution"]])

slots.cvssV40__attackRequirements = Slot(uri=CVE.attackRequirements, name="cvssV40__attackRequirements", curie=CVE.curie('attackRequirements'),
                   model_uri=CVE.cvssV40__attackRequirements, domain=None, range=Optional[Union[str, "CvssV4AttackRequirements"]])

slots.cvssV40__vulnConfidentialityImpact = Slot(uri=CVE.vulnConfidentialityImpact, name="cvssV40__vulnConfidentialityImpact", curie=CVE.curie('vulnConfidentialityImpact'),
                   model_uri=CVE.cvssV40__vulnConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__vulnIntegrityImpact = Slot(uri=CVE.vulnIntegrityImpact, name="cvssV40__vulnIntegrityImpact", curie=CVE.curie('vulnIntegrityImpact'),
                   model_uri=CVE.cvssV40__vulnIntegrityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__vulnAvailabilityImpact = Slot(uri=CVE.vulnAvailabilityImpact, name="cvssV40__vulnAvailabilityImpact", curie=CVE.curie('vulnAvailabilityImpact'),
                   model_uri=CVE.cvssV40__vulnAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subConfidentialityImpact = Slot(uri=CVE.subConfidentialityImpact, name="cvssV40__subConfidentialityImpact", curie=CVE.curie('subConfidentialityImpact'),
                   model_uri=CVE.cvssV40__subConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subIntegrityImpact = Slot(uri=CVE.subIntegrityImpact, name="cvssV40__subIntegrityImpact", curie=CVE.curie('subIntegrityImpact'),
                   model_uri=CVE.cvssV40__subIntegrityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subAvailabilityImpact = Slot(uri=CVE.subAvailabilityImpact, name="cvssV40__subAvailabilityImpact", curie=CVE.curie('subAvailabilityImpact'),
                   model_uri=CVE.cvssV40__subAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__exploitMaturity = Slot(uri=CVE.exploitMaturity, name="cvssV40__exploitMaturity", curie=CVE.curie('exploitMaturity'),
                   model_uri=CVE.cvssV40__exploitMaturity, domain=None, range=Optional[Union[str, "CvssV4ExploitMaturity"]])

slots.cvssV40__modifiedAttackRequirements = Slot(uri=CVE.modifiedAttackRequirements, name="cvssV40__modifiedAttackRequirements", curie=CVE.curie('modifiedAttackRequirements'),
                   model_uri=CVE.cvssV40__modifiedAttackRequirements, domain=None, range=Optional[Union[str, "CvssV4ModifiedAttackRequirements"]])

slots.cvssV40__modifiedVulnConfidentialityImpact = Slot(uri=CVE.modifiedVulnConfidentialityImpact, name="cvssV40__modifiedVulnConfidentialityImpact", curie=CVE.curie('modifiedVulnConfidentialityImpact'),
                   model_uri=CVE.cvssV40__modifiedVulnConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedVulnIntegrityImpact = Slot(uri=CVE.modifiedVulnIntegrityImpact, name="cvssV40__modifiedVulnIntegrityImpact", curie=CVE.curie('modifiedVulnIntegrityImpact'),
                   model_uri=CVE.cvssV40__modifiedVulnIntegrityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedVulnAvailabilityImpact = Slot(uri=CVE.modifiedVulnAvailabilityImpact, name="cvssV40__modifiedVulnAvailabilityImpact", curie=CVE.curie('modifiedVulnAvailabilityImpact'),
                   model_uri=CVE.cvssV40__modifiedVulnAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedSubConfidentialityImpact = Slot(uri=CVE.modifiedSubConfidentialityImpact, name="cvssV40__modifiedSubConfidentialityImpact", curie=CVE.curie('modifiedSubConfidentialityImpact'),
                   model_uri=CVE.cvssV40__modifiedSubConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedSubIntegrityImpact = Slot(uri=CVE.modifiedSubIntegrityImpact, name="cvssV40__modifiedSubIntegrityImpact", curie=CVE.curie('modifiedSubIntegrityImpact'),
                   model_uri=CVE.cvssV40__modifiedSubIntegrityImpact, domain=None, range=Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]])

slots.cvssV40__modifiedSubAvailabilityImpact = Slot(uri=CVE.modifiedSubAvailabilityImpact, name="cvssV40__modifiedSubAvailabilityImpact", curie=CVE.curie('modifiedSubAvailabilityImpact'),
                   model_uri=CVE.cvssV40__modifiedSubAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]])

slots.cvssV40__Safety = Slot(uri=CVE.Safety, name="cvssV40__Safety", curie=CVE.curie('Safety'),
                   model_uri=CVE.cvssV40__Safety, domain=None, range=Optional[Union[str, "CvssV4Safety"]])

slots.cvssV40__Automatable = Slot(uri=CVE.Automatable, name="cvssV40__Automatable", curie=CVE.curie('Automatable'),
                   model_uri=CVE.cvssV40__Automatable, domain=None, range=Optional[Union[str, "CvssV4Automatable"]])

slots.cvssV40__Recovery = Slot(uri=CVE.Recovery, name="cvssV40__Recovery", curie=CVE.curie('Recovery'),
                   model_uri=CVE.cvssV40__Recovery, domain=None, range=Optional[Union[str, "CvssV4Recovery"]])

slots.cvssV40__valueDensity = Slot(uri=CVE.valueDensity, name="cvssV40__valueDensity", curie=CVE.curie('valueDensity'),
                   model_uri=CVE.cvssV40__valueDensity, domain=None, range=Optional[Union[str, "CvssV4ValueDensity"]])

slots.cvssV40__vulnerabilityResponseEffort = Slot(uri=CVE.vulnerabilityResponseEffort, name="cvssV40__vulnerabilityResponseEffort", curie=CVE.curie('vulnerabilityResponseEffort'),
                   model_uri=CVE.cvssV40__vulnerabilityResponseEffort, domain=None, range=Optional[Union[str, "CvssV4ResponseEffort"]])

slots.cvssV40__providerUrgency = Slot(uri=CVE.providerUrgency, name="cvssV40__providerUrgency", curie=CVE.curie('providerUrgency'),
                   model_uri=CVE.cvssV40__providerUrgency, domain=None, range=Optional[Union[str, "CvssV4ProviderUrgency"]])

slots.cveRecord__dataType = Slot(uri=CVE.dataType, name="cveRecord__dataType", curie=CVE.curie('dataType'),
                   model_uri=CVE.cveRecord__dataType, domain=None, range=Union[str, "CveDataType"])

slots.cveRecord__dataVersion = Slot(uri=CVE.dataVersion, name="cveRecord__dataVersion", curie=CVE.curie('dataVersion'),
                   model_uri=CVE.cveRecord__dataVersion, domain=None, range=Union[str, CveDataVersion])

slots.cveRecordMetadata__cveId = Slot(uri=CVE.cveId, name="cveRecordMetadata__cveId", curie=CVE.curie('cveId'),
                   model_uri=CVE.cveRecordMetadata__cveId, domain=None, range=Union[str, CveIdentifier])

slots.cveRecordMetadata__assignerOrgId = Slot(uri=CVE.assignerOrgId, name="cveRecordMetadata__assignerOrgId", curie=CVE.curie('assignerOrgId'),
                   model_uri=CVE.cveRecordMetadata__assignerOrgId, domain=None, range=Union[str, CveUuid])

slots.cveRecordMetadata__assignerShortName = Slot(uri=CVE.assignerShortName, name="cveRecordMetadata__assignerShortName", curie=CVE.curie('assignerShortName'),
                   model_uri=CVE.cveRecordMetadata__assignerShortName, domain=None, range=Optional[Union[str, CveShortName]])

slots.cveRecordMetadata__serial = Slot(uri=CVE.serial, name="cveRecordMetadata__serial", curie=CVE.curie('serial'),
                   model_uri=CVE.cveRecordMetadata__serial, domain=None, range=Optional[int])

slots.cveRecordMetadata__dateReserved = Slot(uri=CVE.dateReserved, name="cveRecordMetadata__dateReserved", curie=CVE.curie('dateReserved'),
                   model_uri=CVE.cveRecordMetadata__dateReserved, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.cveRecordMetadata__datePublished = Slot(uri=CVE.datePublished, name="cveRecordMetadata__datePublished", curie=CVE.curie('datePublished'),
                   model_uri=CVE.cveRecordMetadata__datePublished, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.cveMetadataPublished__requesterUserId = Slot(uri=CVE.requesterUserId, name="cveMetadataPublished__requesterUserId", curie=CVE.curie('requesterUserId'),
                   model_uri=CVE.cveMetadataPublished__requesterUserId, domain=None, range=Optional[Union[str, CveUuid]])

slots.cveMetadataRejected__dateRejected = Slot(uri=CVE.dateRejected, name="cveMetadataRejected__dateRejected", curie=CVE.curie('dateRejected'),
                   model_uri=CVE.cveMetadataRejected__dateRejected, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.cvePublishedContainers__adp = Slot(uri=CVE.adp, name="cvePublishedContainers__adp", curie=CVE.curie('adp'),
                   model_uri=CVE.cvePublishedContainers__adp, domain=None, range=Optional[Union[Union[dict, CveAdpContainer], list[Union[dict, CveAdpContainer]]]])

slots.cveProviderMetadata__orgId = Slot(uri=CVE.orgId, name="cveProviderMetadata__orgId", curie=CVE.curie('orgId'),
                   model_uri=CVE.cveProviderMetadata__orgId, domain=None, range=Union[str, CveUuid])

slots.cveProviderMetadata__shortName = Slot(uri=CVE.shortName, name="cveProviderMetadata__shortName", curie=CVE.curie('shortName'),
                   model_uri=CVE.cveProviderMetadata__shortName, domain=None, range=Optional[Union[str, CveShortName]])

slots.cveCnaPublishedContainer__dateAssigned = Slot(uri=CVE.dateAssigned, name="cveCnaPublishedContainer__dateAssigned", curie=CVE.curie('dateAssigned'),
                   model_uri=CVE.cveCnaPublishedContainer__dateAssigned, domain=None, range=Optional[Union[str, CveTimestamp]])

slots.cveCnaRejectedContainer__rejectedReasons = Slot(uri=CVE.rejectedReasons, name="cveCnaRejectedContainer__rejectedReasons", curie=CVE.curie('rejectedReasons'),
                   model_uri=CVE.cveCnaRejectedContainer__rejectedReasons, domain=None, range=Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]])

slots.cveCnaRejectedContainer__replacedBy = Slot(uri=CVE.replacedBy, name="cveCnaRejectedContainer__replacedBy", curie=CVE.curie('replacedBy'),
                   model_uri=CVE.cveCnaRejectedContainer__replacedBy, domain=None, range=Optional[Union[Union[str, CveIdentifier], list[Union[str, CveIdentifier]]]])

slots.cveProduct__vendor = Slot(uri=CVE.vendor, name="cveProduct__vendor", curie=CVE.curie('vendor'),
                   model_uri=CVE.cveProduct__vendor, domain=None, range=Optional[Union[str, CveText512]])

slots.cveProduct__product = Slot(uri=CVE.product, name="cveProduct__product", curie=CVE.curie('product'),
                   model_uri=CVE.cveProduct__product, domain=None, range=Optional[Union[str, CveText2048]])

slots.cveProduct__collectionURL = Slot(uri=CVE.collectionURL, name="cveProduct__collectionURL", curie=CVE.curie('collectionURL'),
                   model_uri=CVE.cveProduct__collectionURL, domain=None, range=Optional[Union[str, CveUri]])

slots.cveProduct__packageName = Slot(uri=CVE.packageName, name="cveProduct__packageName", curie=CVE.curie('packageName'),
                   model_uri=CVE.cveProduct__packageName, domain=None, range=Optional[Union[str, CveText2048]])

slots.cveProduct__packageURL = Slot(uri=CVE.packageURL, name="cveProduct__packageURL", curie=CVE.curie('packageURL'),
                   model_uri=CVE.cveProduct__packageURL, domain=None, range=Optional[Union[str, CveUri]])

slots.cveProduct__cpes = Slot(uri=CVE.cpes, name="cveProduct__cpes", curie=CVE.curie('cpes'),
                   model_uri=CVE.cveProduct__cpes, domain=None, range=Optional[Union[Union[str, CveCpe22and23], list[Union[str, CveCpe22and23]]]])

slots.cveProduct__modules = Slot(uri=CVE.modules, name="cveProduct__modules", curie=CVE.curie('modules'),
                   model_uri=CVE.cveProduct__modules, domain=None, range=Optional[Union[Union[str, CveText4096], list[Union[str, CveText4096]]]])

slots.cveProduct__programFiles = Slot(uri=CVE.programFiles, name="cveProduct__programFiles", curie=CVE.curie('programFiles'),
                   model_uri=CVE.cveProduct__programFiles, domain=None, range=Optional[Union[Union[str, CveText1024], list[Union[str, CveText1024]]]])

slots.cveProduct__programRoutines = Slot(uri=CVE.programRoutines, name="cveProduct__programRoutines", curie=CVE.curie('programRoutines'),
                   model_uri=CVE.cveProduct__programRoutines, domain=None, range=Optional[Union[Union[dict, CveProgramRoutine], list[Union[dict, CveProgramRoutine]]]])

slots.cveProduct__platforms = Slot(uri=CVE.platforms, name="cveProduct__platforms", curie=CVE.curie('platforms'),
                   model_uri=CVE.cveProduct__platforms, domain=None, range=Optional[Union[Union[str, CveTextUpTo1024], list[Union[str, CveTextUpTo1024]]]])

slots.cveProduct__repo = Slot(uri=CVE.repo, name="cveProduct__repo", curie=CVE.curie('repo'),
                   model_uri=CVE.cveProduct__repo, domain=None, range=Optional[Union[str, CveUri]])

slots.cveProduct__defaultStatus = Slot(uri=CVE.defaultStatus, name="cveProduct__defaultStatus", curie=CVE.curie('defaultStatus'),
                   model_uri=CVE.cveProduct__defaultStatus, domain=None, range=Optional[Union[str, "CveVersionStatus"]])

slots.cveProduct__versions = Slot(uri=CVE.versions, name="cveProduct__versions", curie=CVE.curie('versions'),
                   model_uri=CVE.cveProduct__versions, domain=None, range=Optional[Union[Union[dict, CveProductVersion], list[Union[dict, CveProductVersion]]]])

slots.cveProductVersion__versionType = Slot(uri=CVE.versionType, name="cveProductVersion__versionType", curie=CVE.curie('versionType'),
                   model_uri=CVE.cveProductVersion__versionType, domain=None, range=Optional[Union[str, CveText128]])

slots.cveProductVersion__lessThan = Slot(uri=CVE.lessThan, name="cveProductVersion__lessThan", curie=CVE.curie('lessThan'),
                   model_uri=CVE.cveProductVersion__lessThan, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveProductVersion__lessThanOrEqual = Slot(uri=CVE.lessThanOrEqual, name="cveProductVersion__lessThanOrEqual", curie=CVE.curie('lessThanOrEqual'),
                   model_uri=CVE.cveProductVersion__lessThanOrEqual, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveProductVersion__changes = Slot(uri=CVE.changes, name="cveProductVersion__changes", curie=CVE.curie('changes'),
                   model_uri=CVE.cveProductVersion__changes, domain=None, range=Optional[Union[Union[dict, CveVersionChange], list[Union[dict, CveVersionChange]]]])

slots.cveCpeApplicabilityElement__nodes = Slot(uri=CVE.nodes, name="cveCpeApplicabilityElement__nodes", curie=CVE.curie('nodes'),
                   model_uri=CVE.cveCpeApplicabilityElement__nodes, domain=None, range=Union[Union[dict, CveCpeNode], list[Union[dict, CveCpeNode]]])

slots.cveCpeNode__cpeMatch = Slot(uri=CVE.cpeMatch, name="cveCpeNode__cpeMatch", curie=CVE.curie('cpeMatch'),
                   model_uri=CVE.cveCpeNode__cpeMatch, domain=None, range=Union[Union[dict, CveCpeMatch], list[Union[dict, CveCpeMatch]]])

slots.cveCpeMatch__vulnerable = Slot(uri=CVE.vulnerable, name="cveCpeMatch__vulnerable", curie=CVE.curie('vulnerable'),
                   model_uri=CVE.cveCpeMatch__vulnerable, domain=None, range=Union[bool, Bool])

slots.cveCpeMatch__criteria = Slot(uri=CVE.criteria, name="cveCpeMatch__criteria", curie=CVE.curie('criteria'),
                   model_uri=CVE.cveCpeMatch__criteria, domain=None, range=Union[str, CveCpe23])

slots.cveCpeMatch__matchCriteriaId = Slot(uri=CVE.matchCriteriaId, name="cveCpeMatch__matchCriteriaId", curie=CVE.curie('matchCriteriaId'),
                   model_uri=CVE.cveCpeMatch__matchCriteriaId, domain=None, range=Optional[Union[str, CveUuid]])

slots.cveCpeMatch__versionStartExcluding = Slot(uri=CVE.versionStartExcluding, name="cveCpeMatch__versionStartExcluding", curie=CVE.curie('versionStartExcluding'),
                   model_uri=CVE.cveCpeMatch__versionStartExcluding, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveCpeMatch__versionStartIncluding = Slot(uri=CVE.versionStartIncluding, name="cveCpeMatch__versionStartIncluding", curie=CVE.curie('versionStartIncluding'),
                   model_uri=CVE.cveCpeMatch__versionStartIncluding, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveCpeMatch__versionEndExcluding = Slot(uri=CVE.versionEndExcluding, name="cveCpeMatch__versionEndExcluding", curie=CVE.curie('versionEndExcluding'),
                   model_uri=CVE.cveCpeMatch__versionEndExcluding, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveCpeMatch__versionEndIncluding = Slot(uri=CVE.versionEndIncluding, name="cveCpeMatch__versionEndIncluding", curie=CVE.curie('versionEndIncluding'),
                   model_uri=CVE.cveCpeMatch__versionEndIncluding, domain=None, range=Optional[Union[str, CveVersion]])

slots.cveDescription__supportingMedia = Slot(uri=CVE.supportingMedia, name="cveDescription__supportingMedia", curie=CVE.curie('supportingMedia'),
                   model_uri=CVE.cveDescription__supportingMedia, domain=None, range=Optional[Union[Union[dict, CveSupportingMedia], list[Union[dict, CveSupportingMedia]]]])

slots.cveSupportingMedia__base64 = Slot(uri=CVE.base64, name="cveSupportingMedia__base64", curie=CVE.curie('base64'),
                   model_uri=CVE.cveSupportingMedia__base64, domain=None, range=Optional[Union[bool, Bool]])

slots.cveProblemTypeDescription__cweId = Slot(uri=CVE.cweId, name="cveProblemTypeDescription__cweId", curie=CVE.curie('cweId'),
                   model_uri=CVE.cveProblemTypeDescription__cweId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CWE-[1-9][0-9]*$'))

slots.cveImpact__capecId = Slot(uri=CVE.capecId, name="cveImpact__capecId", curie=CVE.curie('capecId'),
                   model_uri=CVE.cveImpact__capecId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CAPEC-[1-9][0-9]{0,4}$'))

slots.cveMetric__format = Slot(uri=CVE.format, name="cveMetric__format", curie=CVE.curie('format'),
                   model_uri=CVE.cveMetric__format, domain=None, range=Optional[Union[str, CveText64]])

slots.cveMetric__scenarios = Slot(uri=CVE.scenarios, name="cveMetric__scenarios", curie=CVE.curie('scenarios'),
                   model_uri=CVE.cveMetric__scenarios, domain=None, range=Optional[Union[Union[dict, CveMetricScenario], list[Union[dict, CveMetricScenario]]]])

slots.cveMetric__cvssV4_0 = Slot(uri=CVE.cvssV4_0, name="cveMetric__cvssV4_0", curie=CVE.curie('cvssV4_0'),
                   model_uri=CVE.cveMetric__cvssV4_0, domain=None, range=Optional[Union[dict, CvssV40]])

slots.cveMetric__cvssV3_1 = Slot(uri=CVE.cvssV3_1, name="cveMetric__cvssV3_1", curie=CVE.curie('cvssV3_1'),
                   model_uri=CVE.cveMetric__cvssV3_1, domain=None, range=Optional[Union[dict, CvssV31]])

slots.cveMetric__cvssV3_0 = Slot(uri=CVE.cvssV3_0, name="cveMetric__cvssV3_0", curie=CVE.curie('cvssV3_0'),
                   model_uri=CVE.cveMetric__cvssV3_0, domain=None, range=Optional[Union[dict, CvssV30]])

slots.cveMetric__cvssV2_0 = Slot(uri=CVE.cvssV2_0, name="cveMetric__cvssV2_0", curie=CVE.curie('cvssV2_0'),
                   model_uri=CVE.cveMetric__cvssV2_0, domain=None, range=Optional[Union[dict, CvssV20]])

slots.cveMetric__other = Slot(uri=CVE.other, name="cveMetric__other", curie=CVE.curie('other'),
                   model_uri=CVE.cveMetric__other, domain=None, range=Optional[Union[dict, CveOtherMetric]])

slots.cveOtherMetric__content = Slot(uri=CVE.content, name="cveOtherMetric__content", curie=CVE.curie('content'),
                   model_uri=CVE.cveOtherMetric__content, domain=None, range=Union[dict, CveOtherMetricContent])

slots.cveTimelineEvent__time = Slot(uri=CVE.time, name="cveTimelineEvent__time", curie=CVE.curie('time'),
                   model_uri=CVE.cveTimelineEvent__time, domain=None, range=Union[str, CveTimestamp])

slots.cveCredit__user = Slot(uri=CVE.user, name="cveCredit__user", curie=CVE.curie('user'),
                   model_uri=CVE.cveCredit__user, domain=None, range=Optional[Union[str, CveUuid]])

slots.cveTaxonomyMapping__taxonomyName = Slot(uri=CVE.taxonomyName, name="cveTaxonomyMapping__taxonomyName", curie=CVE.curie('taxonomyName'),
                   model_uri=CVE.cveTaxonomyMapping__taxonomyName, domain=None, range=Union[str, CveText128])

slots.cveTaxonomyMapping__taxonomyVersion = Slot(uri=CVE.taxonomyVersion, name="cveTaxonomyMapping__taxonomyVersion", curie=CVE.curie('taxonomyVersion'),
                   model_uri=CVE.cveTaxonomyMapping__taxonomyVersion, domain=None, range=Optional[Union[str, CveText128]])

slots.cveTaxonomyMapping__taxonomyRelations = Slot(uri=CVE.taxonomyRelations, name="cveTaxonomyMapping__taxonomyRelations", curie=CVE.curie('taxonomyRelations'),
                   model_uri=CVE.cveTaxonomyMapping__taxonomyRelations, domain=None, range=Union[Union[dict, CveTaxonomyRelation], list[Union[dict, CveTaxonomyRelation]]])

slots.cveTaxonomyRelation__taxonomyId = Slot(uri=CVE.taxonomyId, name="cveTaxonomyRelation__taxonomyId", curie=CVE.curie('taxonomyId'),
                   model_uri=CVE.cveTaxonomyRelation__taxonomyId, domain=None, range=Union[str, CveText2048])

slots.cveTaxonomyRelation__relationshipName = Slot(uri=CVE.relationshipName, name="cveTaxonomyRelation__relationshipName", curie=CVE.curie('relationshipName'),
                   model_uri=CVE.cveTaxonomyRelation__relationshipName, domain=None, range=Union[str, CveText128])

slots.cveTaxonomyRelation__relationshipValue = Slot(uri=CVE.relationshipValue, name="cveTaxonomyRelation__relationshipValue", curie=CVE.curie('relationshipValue'),
                   model_uri=CVE.cveTaxonomyRelation__relationshipValue, domain=None, range=Union[str, CveText2048])

slots.CvssV20_version = Slot(uri=CVE.version, name="CvssV20_version", curie=CVE.curie('version'),
                   model_uri=CVE.CvssV20_version, domain=CvssV20, range=str)

slots.CvssV20_vectorString = Slot(uri=CVE.vectorString, name="CvssV20_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=CVE.CvssV20_vectorString, domain=CvssV20, range=str,
                   pattern=re.compile(r'^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'))

slots.CvssV20_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV20_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=CVE.CvssV20_confidentialityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV20_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=CVE.CvssV20_integrityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV20_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=CVE.CvssV20_availabilityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV20_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=CVE.CvssV20_remediationLevel, domain=CvssV20, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV20_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV20_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=CVE.CvssV20_reportConfidence, domain=CvssV20, range=Optional[Union[str, "CvssV2ReportConfidence"]])

slots.CvssV20_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV20_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=CVE.CvssV20_confidentialityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV20_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV20_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=CVE.CvssV20_integrityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV20_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV20_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=CVE.CvssV20_availabilityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_version = Slot(uri=CVE.version, name="CvssV30_version", curie=CVE.curie('version'),
                   model_uri=CVE.CvssV30_version, domain=CvssV30, range=str)

slots.CvssV30_vectorString = Slot(uri=CVE.vectorString, name="CvssV30_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=CVE.CvssV30_vectorString, domain=CvssV30, range=str,
                   pattern=re.compile(r'^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'))

slots.CvssV30_attackVector = Slot(uri=CVE.attackVector, name="CvssV30_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=CVE.CvssV30_attackVector, domain=CvssV30, range=Optional[Union[str, "CvssV3AttackVector"]])

slots.CvssV30_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV30_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=CVE.CvssV30_attackComplexity, domain=CvssV30, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV30_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV30_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=CVE.CvssV30_privilegesRequired, domain=CvssV30, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV30_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV30_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=CVE.CvssV30_userInteraction, domain=CvssV30, range=Optional[Union[str, "CvssV3UserInteraction"]])

slots.CvssV30_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV30_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=CVE.CvssV30_confidentialityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV30_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=CVE.CvssV30_integrityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV30_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=CVE.CvssV30_availabilityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV30_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=CVE.CvssV30_remediationLevel, domain=CvssV30, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV30_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV30_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=CVE.CvssV30_reportConfidence, domain=CvssV30, range=Optional[Union[str, "CvssV3ReportConfidence"]])

slots.CvssV30_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV30_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=CVE.CvssV30_confidentialityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV30_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=CVE.CvssV30_integrityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV30_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=CVE.CvssV30_availabilityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV30_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=CVE.CvssV30_modifiedAttackVector, domain=CvssV30, range=Optional[Union[str, "CvssV3ModifiedAttackVector"]])

slots.CvssV30_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV30_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=CVE.CvssV30_modifiedAttackComplexity, domain=CvssV30, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV30_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV30_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=CVE.CvssV30_modifiedPrivilegesRequired, domain=CvssV30, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV30_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV30_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=CVE.CvssV30_modifiedUserInteraction, domain=CvssV30, range=Optional[Union[str, "CvssV3ModifiedUserInteraction"]])

slots.CvssV30_modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="CvssV30_modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=CVE.CvssV30_modifiedConfidentialityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV30_modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="CvssV30_modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=CVE.CvssV30_modifiedIntegrityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV30_modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="CvssV30_modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=CVE.CvssV30_modifiedAvailabilityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_version = Slot(uri=CVE.version, name="CvssV31_version", curie=CVE.curie('version'),
                   model_uri=CVE.CvssV31_version, domain=CvssV31, range=str)

slots.CvssV31_vectorString = Slot(uri=CVE.vectorString, name="CvssV31_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=CVE.CvssV31_vectorString, domain=CvssV31, range=str,
                   pattern=re.compile(r'^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'))

slots.CvssV31_attackVector = Slot(uri=CVE.attackVector, name="CvssV31_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=CVE.CvssV31_attackVector, domain=CvssV31, range=Optional[Union[str, "CvssV3AttackVector"]])

slots.CvssV31_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV31_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=CVE.CvssV31_attackComplexity, domain=CvssV31, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV31_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV31_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=CVE.CvssV31_privilegesRequired, domain=CvssV31, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV31_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV31_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=CVE.CvssV31_userInteraction, domain=CvssV31, range=Optional[Union[str, "CvssV3UserInteraction"]])

slots.CvssV31_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV31_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=CVE.CvssV31_confidentialityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV31_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=CVE.CvssV31_integrityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV31_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=CVE.CvssV31_availabilityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV31_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=CVE.CvssV31_remediationLevel, domain=CvssV31, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV31_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV31_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=CVE.CvssV31_reportConfidence, domain=CvssV31, range=Optional[Union[str, "CvssV3ReportConfidence"]])

slots.CvssV31_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV31_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=CVE.CvssV31_confidentialityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV31_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=CVE.CvssV31_integrityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV31_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=CVE.CvssV31_availabilityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV31_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=CVE.CvssV31_modifiedAttackVector, domain=CvssV31, range=Optional[Union[str, "CvssV3ModifiedAttackVector"]])

slots.CvssV31_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV31_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=CVE.CvssV31_modifiedAttackComplexity, domain=CvssV31, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV31_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV31_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=CVE.CvssV31_modifiedPrivilegesRequired, domain=CvssV31, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV31_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV31_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=CVE.CvssV31_modifiedUserInteraction, domain=CvssV31, range=Optional[Union[str, "CvssV3ModifiedUserInteraction"]])

slots.CvssV31_modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="CvssV31_modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=CVE.CvssV31_modifiedConfidentialityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="CvssV31_modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=CVE.CvssV31_modifiedIntegrityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="CvssV31_modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=CVE.CvssV31_modifiedAvailabilityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV40_version = Slot(uri=CVE.version, name="CvssV40_version", curie=CVE.curie('version'),
                   model_uri=CVE.CvssV40_version, domain=CvssV40, range=str)

slots.CvssV40_vectorString = Slot(uri=CVE.vectorString, name="CvssV40_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=CVE.CvssV40_vectorString, domain=CvssV40, range=str,
                   pattern=re.compile(r'^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'))

slots.CvssV40_attackVector = Slot(uri=CVE.attackVector, name="CvssV40_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=CVE.CvssV40_attackVector, domain=CvssV40, range=Optional[Union[str, "CvssV4AttackVector"]])

slots.CvssV40_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV40_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=CVE.CvssV40_attackComplexity, domain=CvssV40, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV40_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV40_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=CVE.CvssV40_privilegesRequired, domain=CvssV40, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV40_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV40_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=CVE.CvssV40_userInteraction, domain=CvssV40, range=Optional[Union[str, "CvssV4UserInteraction"]])

slots.CvssV40_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV40_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=CVE.CvssV40_confidentialityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV40_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=CVE.CvssV40_integrityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV40_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=CVE.CvssV40_availabilityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV40_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=CVE.CvssV40_modifiedAttackVector, domain=CvssV40, range=Optional[Union[str, "CvssV4ModifiedAttackVector"]])

slots.CvssV40_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV40_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=CVE.CvssV40_modifiedAttackComplexity, domain=CvssV40, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV40_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV40_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=CVE.CvssV40_modifiedPrivilegesRequired, domain=CvssV40, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV40_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV40_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=CVE.CvssV40_modifiedUserInteraction, domain=CvssV40, range=Optional[Union[str, "CvssV4ModifiedUserInteraction"]])

slots.CvePublishedRecord_cveMetadata = Slot(uri=CVE.cveMetadata, name="CvePublishedRecord_cveMetadata", curie=CVE.curie('cveMetadata'),
                   model_uri=CVE.CvePublishedRecord_cveMetadata, domain=CvePublishedRecord, range=Union[dict, "CveMetadataPublished"])

slots.CvePublishedRecord_containers = Slot(uri=CVE.containers, name="CvePublishedRecord_containers", curie=CVE.curie('containers'),
                   model_uri=CVE.CvePublishedRecord_containers, domain=CvePublishedRecord, range=Union[dict, "CvePublishedContainers"])

slots.CveRejectedRecord_cveMetadata = Slot(uri=CVE.cveMetadata, name="CveRejectedRecord_cveMetadata", curie=CVE.curie('cveMetadata'),
                   model_uri=CVE.CveRejectedRecord_cveMetadata, domain=CveRejectedRecord, range=Union[dict, "CveMetadataRejected"])

slots.CveRejectedRecord_containers = Slot(uri=CVE.containers, name="CveRejectedRecord_containers", curie=CVE.curie('containers'),
                   model_uri=CVE.CveRejectedRecord_containers, domain=CveRejectedRecord, range=Union[dict, "CveRejectedContainers"])

slots.CveMetadataPublished_state = Slot(uri=CVE.state, name="CveMetadataPublished_state", curie=CVE.curie('state'),
                   model_uri=CVE.CveMetadataPublished_state, domain=CveMetadataPublished, range=Union[str, "CvePublishedState"])

slots.CveMetadataRejected_state = Slot(uri=CVE.state, name="CveMetadataRejected_state", curie=CVE.curie('state'),
                   model_uri=CVE.CveMetadataRejected_state, domain=CveMetadataRejected, range=Union[str, "CveRejectedState"])

slots.CvePublishedContainers_cna = Slot(uri=CVE.cna, name="CvePublishedContainers_cna", curie=CVE.curie('cna'),
                   model_uri=CVE.CvePublishedContainers_cna, domain=CvePublishedContainers, range=Union[dict, "CveCnaPublishedContainer"])

slots.CveRejectedContainers_cna = Slot(uri=CVE.cna, name="CveRejectedContainers_cna", curie=CVE.curie('cna'),
                   model_uri=CVE.CveRejectedContainers_cna, domain=CveRejectedContainers, range=Union[dict, "CveCnaRejectedContainer"])

slots.CveCnaPublishedContainer_descriptions = Slot(uri=CVE.descriptions, name="CveCnaPublishedContainer_descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.CveCnaPublishedContainer_descriptions, domain=CveCnaPublishedContainer, range=Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]])

slots.CveCnaPublishedContainer_affected = Slot(uri=CVE.affected, name="CveCnaPublishedContainer_affected", curie=CVE.curie('affected'),
                   model_uri=CVE.CveCnaPublishedContainer_affected, domain=CveCnaPublishedContainer, range=Union[Union[dict, "CveProduct"], list[Union[dict, "CveProduct"]]])

slots.CveCnaPublishedContainer_references = Slot(uri=CVE.references, name="CveCnaPublishedContainer_references", curie=CVE.curie('references'),
                   model_uri=CVE.CveCnaPublishedContainer_references, domain=CveCnaPublishedContainer, range=Union[Union[dict, "CveReference"], list[Union[dict, "CveReference"]]])

slots.CveCnaPublishedContainer_tags = Slot(uri=CVE.tags, name="CveCnaPublishedContainer_tags", curie=CVE.curie('tags'),
                   model_uri=CVE.CveCnaPublishedContainer_tags, domain=CveCnaPublishedContainer, range=Optional[Union[str, list[str]]])

slots.CveAdpContainer_descriptions = Slot(uri=CVE.descriptions, name="CveAdpContainer_descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.CveAdpContainer_descriptions, domain=CveAdpContainer, range=Optional[Union[Union[dict, "CveDescription"], list[Union[dict, "CveDescription"]]]])

slots.CveAdpContainer_tags = Slot(uri=CVE.tags, name="CveAdpContainer_tags", curie=CVE.curie('tags'),
                   model_uri=CVE.CveAdpContainer_tags, domain=CveAdpContainer, range=Optional[Union[str, list[str]]])

slots.CveProgramRoutine_name = Slot(uri=CVE.name, name="CveProgramRoutine_name", curie=CVE.curie('name'),
                   model_uri=CVE.CveProgramRoutine_name, domain=CveProgramRoutine, range=Union[str, CveText4096])

slots.CveProductVersion_version = Slot(uri=CVE.version, name="CveProductVersion_version", curie=CVE.curie('version'),
                   model_uri=CVE.CveProductVersion_version, domain=CveProductVersion, range=Union[str, CveVersion])

slots.CveProductVersion_status = Slot(uri=CVE.status, name="CveProductVersion_status", curie=CVE.curie('status'),
                   model_uri=CVE.CveProductVersion_status, domain=CveProductVersion, range=Union[str, "CveVersionStatus"])

slots.CveVersionChange_at = Slot(uri=CVE.at, name="CveVersionChange_at", curie=CVE.curie('at'),
                   model_uri=CVE.CveVersionChange_at, domain=CveVersionChange, range=Union[str, CveVersion])

slots.CveVersionChange_status = Slot(uri=CVE.status, name="CveVersionChange_status", curie=CVE.curie('status'),
                   model_uri=CVE.CveVersionChange_status, domain=CveVersionChange, range=Union[str, "CveVersionStatus"])

slots.CveCpeNode_operator = Slot(uri=CVE.operator, name="CveCpeNode_operator", curie=CVE.curie('operator'),
                   model_uri=CVE.CveCpeNode_operator, domain=CveCpeNode, range=Union[str, "CveCpeOperator"])

slots.CveDescription_lang = Slot(uri=CVE.lang, name="CveDescription_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CveDescription_lang, domain=CveDescription, range=Union[str, CveLanguage])

slots.CveDescription_value = Slot(uri=CVE.value, name="CveDescription_value", curie=CVE.curie('value'),
                   model_uri=CVE.CveDescription_value, domain=CveDescription, range=Union[str, CveText4096])

slots.CveSupportingMedia_type = Slot(uri=CVE.type, name="CveSupportingMedia_type", curie=CVE.curie('type'),
                   model_uri=CVE.CveSupportingMedia_type, domain=CveSupportingMedia, range=Union[str, CveText256])

slots.CveSupportingMedia_value = Slot(uri=CVE.value, name="CveSupportingMedia_value", curie=CVE.curie('value'),
                   model_uri=CVE.CveSupportingMedia_value, domain=CveSupportingMedia, range=Union[str, CveText16384])

slots.CveProblemType_descriptions = Slot(uri=CVE.descriptions, name="CveProblemType_descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.CveProblemType_descriptions, domain=CveProblemType, range=Union[Union[dict, "CveProblemTypeDescription"], list[Union[dict, "CveProblemTypeDescription"]]])

slots.CveProblemTypeDescription_lang = Slot(uri=CVE.lang, name="CveProblemTypeDescription_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CveProblemTypeDescription_lang, domain=CveProblemTypeDescription, range=Union[str, CveLanguage])

slots.CveProblemTypeDescription_description = Slot(uri=CVE.description, name="CveProblemTypeDescription_description", curie=CVE.curie('description'),
                   model_uri=CVE.CveProblemTypeDescription_description, domain=CveProblemTypeDescription, range=Union[str, CveText4096])

slots.CveProblemTypeDescription_type = Slot(uri=CVE.type, name="CveProblemTypeDescription_type", curie=CVE.curie('type'),
                   model_uri=CVE.CveProblemTypeDescription_type, domain=CveProblemTypeDescription, range=Optional[Union[str, CveText128]])

slots.CveReference_url = Slot(uri=CVE.url, name="CveReference_url", curie=CVE.curie('url'),
                   model_uri=CVE.CveReference_url, domain=CveReference, range=Union[str, CveUri])

slots.CveReference_name = Slot(uri=CVE.name, name="CveReference_name", curie=CVE.curie('name'),
                   model_uri=CVE.CveReference_name, domain=CveReference, range=Optional[Union[str, CveText512]])

slots.CveReference_tags = Slot(uri=CVE.tags, name="CveReference_tags", curie=CVE.curie('tags'),
                   model_uri=CVE.CveReference_tags, domain=CveReference, range=Optional[Union[str, list[str]]])

slots.CveImpact_descriptions = Slot(uri=CVE.descriptions, name="CveImpact_descriptions", curie=CVE.curie('descriptions'),
                   model_uri=CVE.CveImpact_descriptions, domain=CveImpact, range=Union[Union[dict, CveDescription], list[Union[dict, CveDescription]]])

slots.CveMetricScenario_lang = Slot(uri=CVE.lang, name="CveMetricScenario_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CveMetricScenario_lang, domain=CveMetricScenario, range=Union[str, CveLanguage])

slots.CveMetricScenario_value = Slot(uri=CVE.value, name="CveMetricScenario_value", curie=CVE.curie('value'),
                   model_uri=CVE.CveMetricScenario_value, domain=CveMetricScenario, range=Union[str, CveText4096])

slots.CveOtherMetric_type = Slot(uri=CVE.type, name="CveOtherMetric_type", curie=CVE.curie('type'),
                   model_uri=CVE.CveOtherMetric_type, domain=CveOtherMetric, range=Union[str, CveText128])

slots.CveTimelineEvent_lang = Slot(uri=CVE.lang, name="CveTimelineEvent_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CveTimelineEvent_lang, domain=CveTimelineEvent, range=Union[str, CveLanguage])

slots.CveTimelineEvent_value = Slot(uri=CVE.value, name="CveTimelineEvent_value", curie=CVE.curie('value'),
                   model_uri=CVE.CveTimelineEvent_value, domain=CveTimelineEvent, range=Union[str, CveText4096])

slots.CveCredit_lang = Slot(uri=CVE.lang, name="CveCredit_lang", curie=CVE.curie('lang'),
                   model_uri=CVE.CveCredit_lang, domain=CveCredit, range=Union[str, CveLanguage])

slots.CveCredit_value = Slot(uri=CVE.value, name="CveCredit_value", curie=CVE.curie('value'),
                   model_uri=CVE.CveCredit_value, domain=CveCredit, range=Union[str, CveText4096])

slots.CveCredit_type = Slot(uri=CVE.type, name="CveCredit_type", curie=CVE.curie('type'),
                   model_uri=CVE.CveCredit_type, domain=CveCredit, range=Optional[Union[str, "CveCreditType"]])
