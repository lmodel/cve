from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "5.2.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cve',
     'default_range': 'string',
     'description': 'Common Vulnerabilities and Exposures (CVE™) Program - LinkML '
                    'Schema.\n'
                    'Provides complete semantic coverage of the CVE Record Format '
                    'v5 JSON Schema, including published and rejected records, all '
                    'container types, CVSS 4.0/3.1/3.0/2.0 scoring, CPE '
                    'applicability, taxonomy mappings, credits, and timeline '
                    'entries.',
     'id': 'https://w3id.org/lmodel/cve',
     'imports': ['schema_vulnerability_core:vulnerability_core'],
     'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
     'name': 'cve',
     'prefixes': {'WIKIDATA': {'prefix_prefix': 'WIKIDATA',
                               'prefix_reference': 'https://www.wikidata.org/wiki/'},
                  'cve': {'prefix_prefix': 'cve',
                          'prefix_reference': 'https://w3id.org/lmodel/cve/'},
                  'cwe': {'prefix_prefix': 'cwe',
                          'prefix_reference': 'https://w3id.org/lmodel/cwe/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'kev_catalog': {'prefix_prefix': 'kev_catalog',
                                  'prefix_reference': 'https://w3id.org/lmodel/kev-catalog/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nvd': {'prefix_prefix': 'nvd',
                          'prefix_reference': 'https://w3id.org/lmodel/nist-nvd/'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'schema_vulnerability_core': {'prefix_prefix': 'schema_vulnerability_core',
                                                'prefix_reference': 'https://w3id.org/lmodel/vulnerability-core/schema/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/cve',
                  'https://www.cve.org/',
                  'https://cveproject.github.io/cve-schema/schema/CVE_Record_Format.json'],
     'source': 'https://github.com/CVEProject/cve-schema/blob/main/schema/CVE_Record_Format.json',
     'source_file': 'src/cve/schema/cve.yaml',
     'subsets': {'cna_metadata': {'description': 'CNA and program governance '
                                                 'metadata',
                                  'from_schema': 'https://w3id.org/lmodel/cve',
                                  'name': 'cna_metadata'},
                 'cve_record': {'description': 'Required CVE Record Format fields',
                                'from_schema': 'https://w3id.org/lmodel/cve',
                                'name': 'cve_record'},
                 'cvss_metrics': {'description': 'CVSS scoring metric fields',
                                  'from_schema': 'https://w3id.org/lmodel/cve',
                                  'name': 'cvss_metrics'}},
     'title': 'cve',
     'types': {'CpeName23Type': {'base': 'str',
                                 'description': 'Common Platform Enumeration (CPE) '
                                                'Name in 2.3 format only.',
                                 'from_schema': 'https://w3id.org/lmodel/cve',
                                 'name': 'CpeName23Type',
                                 'pattern': '(cpe:2\\.3:[aho*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!"#$%&\'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!"#$%&\'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){4})',
                                 'uri': 'xsd:string'},
               'CpeNameType': {'base': 'str',
                               'description': 'Common Platform Enumeration (CPE) '
                                              'Name in either 2.2 or 2.3 format.',
                               'from_schema': 'https://w3id.org/lmodel/cve',
                               'name': 'CpeNameType',
                               'pattern': '([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9._\\-~%]*){0,6})|(cpe:2\\.3:[aho*\\-](:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!"#$%&\'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[*\\-]))(:(((\\?*|\\*?)([a-zA-Z0-9\\-._]|(\\\\[\\\\*?!"#$%&\'()+,/:;<=>@\\[\\]\\^`{|}~]))+(\\?*|\\*?))|[*\\-])){4})',
                               'uri': 'xsd:string'},
               'Datestamp': {'base': 'str',
                             'description': 'Date format based on RFC3339 and ISO '
                                            'ISO8601 (date only, no time '
                                            'component).',
                             'from_schema': 'https://w3id.org/lmodel/cve',
                             'name': 'Datestamp',
                             'pattern': '^((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30))$',
                             'uri': 'xsd:date'},
               'LanguageTag': {'base': 'str',
                               'description': 'BCP 47 language code, '
                                              'language-region. The default value '
                                              "is 'en' (English).",
                               'from_schema': 'https://w3id.org/lmodel/cve',
                               'name': 'LanguageTag',
                               'pattern': '^[A-Za-z]{2,4}([_-][A-Za-z]{4})?([_-]([A-Za-z]{2}|[0-9]{3}))?$',
                               'uri': 'xsd:string'},
               'Timestamp': {'base': 'str',
                             'description': 'Date/time format based on RFC3339 and '
                                            'ISO ISO8601, with an optional '
                                            'timezone in the format '
                                            "'yyyy-MM-ddTHH:mm:ss[+-]ZH:ZM'. If "
                                            'timezone offset is not given, GMT '
                                            '(+00:00) is assumed.',
                             'from_schema': 'https://w3id.org/lmodel/cve',
                             'name': 'Timestamp',
                             'pattern': '^(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})?$',
                             'uri': 'xsd:string'},
               'UuidType': {'base': 'str',
                            'description': 'A version 4 (random) universally '
                                           'unique identifier (UUID) as defined by '
                                           'RFC 4122 section 4.1.3.',
                            'from_schema': 'https://w3id.org/lmodel/cve',
                            'name': 'UuidType',
                            'pattern': '^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}$',
                            'uri': 'xsd:string'},
               'VersionString': {'base': 'str',
                                 'description': 'A single version of a product, as '
                                                'expressed in its own version '
                                                'numbering scheme. May include '
                                                "wildcards such as '*' and version "
                                                'range notation.',
                                 'from_schema': 'https://w3id.org/lmodel/cve',
                                 'name': 'VersionString',
                                 'uri': 'xsd:string'}}} )

class VulnerabilityStatus(str, Enum):
    """
    Lifecycle state of a vulnerability record.
    """
    ACTIVE = "ACTIVE"
    """
    Vulnerability is actively maintained and published.
    """
    REJECTED = "REJECTED"
    """
    CVE ID was rejected and should not be used.
    """
    DISPUTED = "DISPUTED"
    """
    The vulnerability details are disputed by a party.
    """
    RESERVED = "RESERVED"
    """
    CVE ID is reserved but details are not yet published.
    """
    DEPRECATED = "DEPRECATED"
    """
    Entry has been superseded or withdrawn.
    """


class ImpactSeverity(str, Enum):
    """
    CVSS qualitative severity rating.
    """
    NONE = "NONE"
    """
    No measurable impact.
    """
    LOW = "LOW"
    """
    Limited impact; exploitation requires specific conditions.
    """
    MEDIUM = "MEDIUM"
    """
    Moderate impact; partial compromise of security properties.
    """
    HIGH = "HIGH"
    """
    High impact; significant compromise of security properties.
    """
    CRITICAL = "CRITICAL"
    """
    Critical impact; complete compromise; remote exploitation likely.
    """
    UNKNOWN = "UNKNOWN"
    """
    Severity has not been assessed or is unavailable.
    """


class DataType(str, Enum):
    """
    Indicates the type of information represented in a CVE JSON instance.
    """
    CVE_RECORD = "CVE_RECORD"
    """
    The instance is a CVE Record.
    """


class RecordState(str, Enum):
    """
    Lifecycle state of a CVE Record (PUBLISHED or REJECTED).
    """
    PUBLISHED = "PUBLISHED"
    """
    The CVE ID has associated vulnerability data published in the CVE List.
    """
    REJECTED = "REJECTED"
    """
    The CVE ID has been rejected and should not be used.
    """


class VersionStatus(str, Enum):
    """
    The vulnerability status of a given version or range of versions of a product.
    """
    affected = "affected"
    """
    The version is affected by the vulnerability.
    """
    unaffected = "unaffected"
    """
    The version is not affected by the vulnerability.
    """
    unknown = "unknown"
    """
    It is unknown or unspecified whether the version is affected.
    """


class ReferenceTag(str, Enum):
    """
    A tag describing the type or nature of the resource referenced by a URL.
    """
    broken_link = "broken-link"
    """
    The reference link is returning a 404 error, or the site is no longer online.
    """
    customer_entitlement = "customer-entitlement"
    """
    Similar to Privileges Required, but specific to references that require non-public or paid access for customers of the particular vendor.
    """
    exploit = "exploit"
    """
    Reference contains an in-depth description of steps to exploit a vulnerability OR contains legitimate Proof of Concept (PoC) code or an exploit kit.
    """
    government_resource = "government-resource"
    """
    All reference links that are from a government agency or organization.
    """
    issue_tracking = "issue-tracking"
    """
    The reference is a post from a bug tracking tool such as MantisBT, Bugzilla, JIRA, GitHub Issues, etc.
    """
    mailing_list = "mailing-list"
    """
    The reference is from a mailing list -- often specific to a product or vendor.
    """
    mitigation = "mitigation"
    """
    The reference contains information on steps to mitigate against the vulnerability when a patch cannot be applied or is unavailable, or for EOL product situations.
    """
    not_applicable = "not-applicable"
    """
    The reference link is not applicable to the vulnerability and was likely associated accidentally (should be used sparingly).
    """
    patch = "patch"
    """
    The reference contains an update to the software that fixes the vulnerability.
    """
    permissions_required = "permissions-required"
    """
    The reference link provided is blocked by a logon page.
    """
    media_coverage = "media-coverage"
    """
    The reference is from a media outlet such as a newspaper, magazine, social media, or weblog. Not intended for individual personal social media accounts.
    """
    product = "product"
    """
    A reference appropriate for describing a product for the purpose of CPE or SWID.
    """
    related = "related"
    """
    A reference that is for a related (but not the same) vulnerability.
    """
    release_notes = "release-notes"
    """
    The reference is in the format of a vendor or open source project's release notes or change log.
    """
    signature = "signature"
    """
    The reference contains a method to detect or prevent the presence or exploitation of the vulnerability.
    """
    technical_description = "technical-description"
    """
    The reference contains in-depth technical information about a vulnerability and its exploitation process, typically in the form of a presentation or whitepaper.
    """
    third_party_advisory = "third-party-advisory"
    """
    Advisory is from an organization that is not the vulnerable product's vendor, publisher, or maintainer.
    """
    vendor_advisory = "vendor-advisory"
    """
    Advisory is from the vendor, publisher, or maintainer of the product or the parent organization.
    """
    vdb_entry = "vdb-entry"
    """
    VDBs are loosely defined as sites that provide information about this vulnerability, such as advisories, with identifiers.
    """


class CNATag(str, Enum):
    """
    Tags provided by a CNA describing the CVE Record.
    """
    unsupported_when_assigned = "unsupported-when-assigned"
    """
    When a request for a CVE assignment was received, the product was already end-of-life (EOL) or a product or specific version was deemed not to be supported by the vendor.
    """
    exclusively_hosted_service = "exclusively-hosted-service"
    """
    All known software and/or hardware affected by this CVE Record is known to exist only in the affected hosted service.
    """
    disputed = "disputed"
    """
    One party disagrees with another party's assertion that a particular issue in software is a vulnerability.
    """


class ADPTag(str, Enum):
    """
    Tags provided by an ADP describing the CVE Record.
    """
    disputed = "disputed"
    """
    One party disagrees with another party's assertion that a particular issue in software is a vulnerability.
    """


class CreditType(str, Enum):
    """
    Type or role of the entity being credited.
    """
    finder = "finder"
    """
    Identifies the vulnerability.
    """
    reporter = "reporter"
    """
    Notifies the vendor of the vulnerability to a CNA.
    """
    analyst = "analyst"
    """
    Validates the vulnerability to ensure accuracy or severity.
    """
    coordinator = "coordinator"
    """
    Facilitates the coordinated response process.
    """
    remediation_developer = "remediation developer"
    """
    Prepares a code change or other remediation plans.
    """
    remediation_reviewer = "remediation reviewer"
    """
    Reviews vulnerability remediation plans or code changes for effectiveness and completeness.
    """
    remediation_verifier = "remediation verifier"
    """
    Tests and verifies the vulnerability or its remediation.
    """
    tool = "tool"
    """
    Names of tools used in vulnerability discovery or identification.
    """
    sponsor = "sponsor"
    """
    Supports the vulnerability identification or remediation activities.
    """
    other = "other"
    """
    Other credit type not covered by the above categories.
    """


class CpeOperator(str, Enum):
    """
    Logical operator used in CPE applicability nodes.
    """
    AND = "AND"
    """
    All CPE match criteria must be satisfied.
    """
    OR = "OR"
    """
    Any one CPE match criterion must be satisfied.
    """


class Cvss4AttackVector(str, Enum):
    """
    CVSS 4.0 attack vector base metric.
    """
    NETWORK = "NETWORK"
    ADJACENT = "ADJACENT"
    LOCAL = "LOCAL"
    PHYSICAL = "PHYSICAL"


class Cvss4AttackComplexity(str, Enum):
    """
    CVSS 4.0 attack complexity base metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"


class Cvss4AttackRequirements(str, Enum):
    """
    CVSS 4.0 attack requirements base metric.
    """
    NONE = "NONE"
    PRESENT = "PRESENT"


class Cvss4PrivilegesRequired(str, Enum):
    """
    CVSS 4.0 privileges required base metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"


class Cvss4UserInteraction(str, Enum):
    """
    CVSS 4.0 user interaction base metric.
    """
    NONE = "NONE"
    PASSIVE = "PASSIVE"
    ACTIVE = "ACTIVE"


class Cvss4VulnCia(str, Enum):
    """
    CVSS 4.0 vulnerable system confidentiality/integrity/availability impact base metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"


class Cvss4SubCia(str, Enum):
    """
    CVSS 4.0 subsequent system confidentiality/integrity/availability impact base metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"


class Cvss4ExploitMaturity(str, Enum):
    """
    CVSS 4.0 exploit maturity supplemental metric.
    """
    UNREPORTED = "UNREPORTED"
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    ATTACKED = "ATTACKED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4CiaRequirement(str, Enum):
    """
    CVSS 4.0 confidentiality/integrity/availability requirement environmental metric.
    """
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4Safety(str, Enum):
    """
    CVSS 4.0 safety supplemental metric.
    """
    NEGLIGIBLE = "NEGLIGIBLE"
    PRESENT = "PRESENT"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4Automatable(str, Enum):
    """
    CVSS 4.0 automatable supplemental metric.
    """
    NO = "NO"
    """
    The attack cannot be automated.
    """
    YES = "YES"
    """
    The attack can be automated.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    Automatable status is not defined.
    """


class Cvss4Recovery(str, Enum):
    """
    CVSS 4.0 recovery supplemental metric.
    """
    AUTOMATIC = "AUTOMATIC"
    USER = "USER"
    IRRECOVERABLE = "IRRECOVERABLE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ValueDensity(str, Enum):
    """
    CVSS 4.0 value density supplemental metric.
    """
    DIFFUSE = "DIFFUSE"
    CONCENTRATED = "CONCENTRATED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4VulnerabilityResponseEffort(str, Enum):
    """
    CVSS 4.0 vulnerability response effort supplemental metric.
    """
    LOW = "LOW"
    MODERATE = "MODERATE"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ProviderUrgency(str, Enum):
    """
    CVSS 4.0 provider urgency supplemental metric.
    """
    CLEAR = "CLEAR"
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4Severity(str, Enum):
    """
    CVSS 4.0 qualitative severity rating.
    """
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Cvss4ModifiedAttackVector(str, Enum):
    """
    CVSS 4.0 modified attack vector environmental metric.
    """
    NETWORK = "NETWORK"
    ADJACENT = "ADJACENT"
    LOCAL = "LOCAL"
    PHYSICAL = "PHYSICAL"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedAttackComplexity(str, Enum):
    """
    CVSS 4.0 modified attack complexity environmental metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedAttackRequirements(str, Enum):
    """
    CVSS 4.0 modified attack requirements environmental metric.
    """
    NONE = "NONE"
    PRESENT = "PRESENT"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedPrivilegesRequired(str, Enum):
    """
    CVSS 4.0 modified privileges required environmental metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedUserInteraction(str, Enum):
    """
    CVSS 4.0 modified user interaction environmental metric.
    """
    NONE = "NONE"
    PASSIVE = "PASSIVE"
    ACTIVE = "ACTIVE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedVulnCia(str, Enum):
    """
    CVSS 4.0 modified vulnerable system CIA environmental metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedSubC(str, Enum):
    """
    CVSS 4.0 modified subsequent system confidentiality environmental metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss4ModifiedSubIa(str, Enum):
    """
    CVSS 4.0 modified subsequent system integrity/availability environmental metric (includes SAFETY value).
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"
    SAFETY = "SAFETY"
    NOT_DEFINED = "NOT_DEFINED"


class CvssV3Version(str, Enum):
    """
    CVSS version 3.x identifier. CVSS 3.0 and 3.1 share an identical metric model; the 3.1 spec was a clarification, not a structural change. The consolidated CvssV3 class accepts either via this enum.
    """
    number_3FULL_STOP0 = "3.0"
    """
    CVSS version 3.0 (2015-2019)
    """
    number_3FULL_STOP1 = "3.1"
    """
    CVSS version 3.1 (2019-present)
    """


class Cvss3AttackVector(str, Enum):
    """
    CVSS 3.x attack vector base metric.
    """
    NETWORK = "NETWORK"
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    LOCAL = "LOCAL"
    PHYSICAL = "PHYSICAL"


class Cvss3AttackComplexity(str, Enum):
    """
    CVSS 3.x attack complexity base metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"


class Cvss3PrivilegesRequired(str, Enum):
    """
    CVSS 3.x privileges required base metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"


class Cvss3UserInteraction(str, Enum):
    """
    CVSS 3.x user interaction base metric.
    """
    NONE = "NONE"
    REQUIRED = "REQUIRED"


class Cvss3Scope(str, Enum):
    """
    CVSS 3.x scope base metric.
    """
    UNCHANGED = "UNCHANGED"
    CHANGED = "CHANGED"


class Cvss3Cia(str, Enum):
    """
    CVSS 3.x confidentiality/integrity/availability impact base metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"


class Cvss3Severity(str, Enum):
    """
    CVSS 3.x qualitative severity rating.
    """
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Cvss3ExploitCodeMaturity(str, Enum):
    """
    CVSS 3.x exploit code maturity temporal metric.
    """
    UNPROVEN = "UNPROVEN"
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    FUNCTIONAL = "FUNCTIONAL"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3RemediationLevel(str, Enum):
    """
    CVSS 3.x remediation level temporal metric.
    """
    OFFICIAL_FIX = "OFFICIAL_FIX"
    TEMPORARY_FIX = "TEMPORARY_FIX"
    WORKAROUND = "WORKAROUND"
    UNAVAILABLE = "UNAVAILABLE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3Confidence(str, Enum):
    """
    CVSS 3.x report confidence temporal metric.
    """
    UNKNOWN = "UNKNOWN"
    REASONABLE = "REASONABLE"
    CONFIRMED = "CONFIRMED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3CiaRequirement(str, Enum):
    """
    CVSS 3.x CIA requirement environmental metric.
    """
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedAttackVector(str, Enum):
    """
    CVSS 3.x modified attack vector environmental metric.
    """
    NETWORK = "NETWORK"
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    LOCAL = "LOCAL"
    PHYSICAL = "PHYSICAL"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedAttackComplexity(str, Enum):
    """
    CVSS 3.x modified attack complexity environmental metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedPrivilegesRequired(str, Enum):
    """
    CVSS 3.x modified privileges required environmental metric.
    """
    HIGH = "HIGH"
    LOW = "LOW"
    NONE = "NONE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedUserInteraction(str, Enum):
    """
    CVSS 3.x modified user interaction environmental metric.
    """
    NONE = "NONE"
    REQUIRED = "REQUIRED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedScope(str, Enum):
    """
    CVSS 3.x modified scope environmental metric.
    """
    UNCHANGED = "UNCHANGED"
    CHANGED = "CHANGED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss3ModifiedCia(str, Enum):
    """
    CVSS 3.x modified CIA environmental metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2AccessVector(str, Enum):
    """
    CVSS 2.0 access vector base metric.
    """
    NETWORK = "NETWORK"
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    LOCAL = "LOCAL"


class Cvss2AccessComplexity(str, Enum):
    """
    CVSS 2.0 access complexity base metric.
    """
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class Cvss2Authentication(str, Enum):
    """
    CVSS 2.0 authentication base metric.
    """
    MULTIPLE = "MULTIPLE"
    SINGLE = "SINGLE"
    NONE = "NONE"


class Cvss2Cia(str, Enum):
    """
    CVSS 2.0 confidentiality/integrity/availability impact base metric.
    """
    NONE = "NONE"
    PARTIAL = "PARTIAL"
    COMPLETE = "COMPLETE"


class Cvss2Exploitability(str, Enum):
    """
    CVSS 2.0 exploitability temporal metric.
    """
    UNPROVEN = "UNPROVEN"
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    FUNCTIONAL = "FUNCTIONAL"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2RemediationLevel(str, Enum):
    """
    CVSS 2.0 remediation level temporal metric.
    """
    OFFICIAL_FIX = "OFFICIAL_FIX"
    TEMPORARY_FIX = "TEMPORARY_FIX"
    WORKAROUND = "WORKAROUND"
    UNAVAILABLE = "UNAVAILABLE"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2ReportConfidence(str, Enum):
    """
    CVSS 2.0 report confidence temporal metric.
    """
    UNCONFIRMED = "UNCONFIRMED"
    UNCORROBORATED = "UNCORROBORATED"
    CONFIRMED = "CONFIRMED"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2CollateralDamagePotential(str, Enum):
    """
    CVSS 2.0 collateral damage potential environmental metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    LOW_MEDIUM = "LOW_MEDIUM"
    MEDIUM_HIGH = "MEDIUM_HIGH"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2TargetDistribution(str, Enum):
    """
    CVSS 2.0 target distribution environmental metric.
    """
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"


class Cvss2CiaRequirement(str, Enum):
    """
    CVSS 2.0 CIA requirement environmental metric.
    """
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NOT_DEFINED = "NOT_DEFINED"



class Vulnerability(ConfiguredBaseModel):
    """
    Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['nvd:NVDEntry', 'kev_catalog:KevEntry'],
         'exact_mappings': ['WIKIDATA:Q631425'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['schema:SoftwareApplication', 'cwe:Weakness'],
         'slot_usage': {'cve_id': {'name': 'cve_id', 'recommended': True},
                        'description': {'name': 'description', 'recommended': True}}})

    cve_id: str = Field(default=..., description="""The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveId'],
         'domain_of': ['Vulnerability'],
         'exact_mappings': ['schema:identifier', 'nvd:cve_id', 'kev_catalog:cve_id'],
         'in_subset': ['metadata'],
         'recommended': True,
         'slot_uri': 'dct:identifier'} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title or name for this entity.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:vulnerability_name'],
         'domain_of': ['Vulnerability', 'CnaPublishedContainer', 'AdpContainer'],
         'exact_mappings': ['schema:name'],
         'in_subset': ['metadata'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    published_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability was first published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'],
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:date_added'],
         'slot_uri': 'dct:created'} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'],
         'in_subset': ['core'],
         'slot_uri': 'dct:modified'} })
    products: Optional[list[Product]] = Field(default=None, description="""Products affected by this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    weaknesses: Optional[list[Weakness]] = Field(default=None, description="""Weakness classifications (e.g. CWE) associated with this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'],
         'in_subset': ['core'],
         'related_mappings': ['cwe:Weakness']} })
    references: Optional[list[Reference]] = Field(default=None, description="""External references such as advisories and articles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    impact: Optional[Impact] = Field(default=None, description="""Impact and severity assessment for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    status: Optional[VulnerabilityStatus] = Field(default=None, description="""Current lifecycle state of the vulnerability record.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:NVDWorkflowStatus'],
         'domain_of': ['Vulnerability'],
         'in_subset': ['core']} })


class Product(ConfiguredBaseModel):
    """
    Software or hardware entity affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['schema:SoftwareApplication'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:KevEntry']})

    vendor: Optional[str] = Field(default=None, description="""Name of the vendor or organization responsible for the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'AffectedProduct'], 'slot_uri': 'schema:name'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness', 'AffectedProduct'],
         'slot_uri': 'rdfs:label'} })
    version: Optional[str] = Field(default=None, description="""Version string of the affected product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product'], 'slot_uri': 'schema:version'} })
    platforms: Optional[list[str]] = Field(default=None, description="""Platforms or operating environments affected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'AffectedProduct']} })


class Reference(ConfiguredBaseModel):
    """
    External reference such as an advisory or article.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:ExternalReference', 'nvd:NVDReference'],
         'exact_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:notes']})

    url: Optional[str] = Field(default=None, description="""URL pointing to the reference resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference'], 'slot_uri': 'schema:url'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness', 'AffectedProduct'],
         'slot_uri': 'rdfs:label'} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference'], 'slot_uri': 'dct:source'} })


class Weakness(ConfiguredBaseModel):
    """
    Weakness classification from CWE or a similar taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:Weakness', 'nvd:NVDWeakness'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    cwe_id: Optional[str] = Field(default=None, description="""CWE identifier for the weakness classification (e.g. CWE-79).""", json_schema_extra = { "linkml_meta": {'aliases': ['cweId'],
         'domain_of': ['Weakness', 'ProblemTypeDescription'],
         'related_mappings': ['cwe:Weakness'],
         'slot_uri': 'dct:identifier'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness', 'AffectedProduct'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'slot_uri': 'dct:description'} })

    @field_validator('cwe_id')
    def pattern_cwe_id(cls, v):
        pattern=re.compile(r"^CWE-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cwe_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cwe_id format: {v}"
            raise ValueError(err_msg)
        return v


class Impact(ConfiguredBaseModel):
    """
    Assessment of the vulnerability's impact and severity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:CVSSMetric'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    severity: Optional[ImpactSeverity] = Field(default=None, description="""Qualitative severity rating.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:CVSSMetric'], 'domain_of': ['Impact']} })
    vector: Optional[str] = Field(default=None, description="""CVSS vector string or equivalent scoring vector expression.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:CVSSMetric'], 'domain_of': ['Impact']} })
    score: Optional[float] = Field(default=None, description="""Numeric vulnerability score (e.g. CVSS base score).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impact']} })


class Configuration(ConfiguredBaseModel):
    """
    Logical grouping of CPE match expressions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:CPEConfiguration'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    cpe_uri: Optional[str] = Field(default=None, description="""CPE 2.2 URI identifying an affected product configuration.""", json_schema_extra = { "linkml_meta": {'aliases': ['cpeUri'],
         'domain_of': ['Configuration'],
         'related_mappings': ['nvd:CPEMatch']} })
    operator: Optional[str] = Field(default=None, description="""Logical operator (AND/OR) used in configuration node groupings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Configuration']} })


class CVERecord(ConfiguredBaseModel):
    """
    Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™ Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected records.
    This class deliberately does NOT inherit from ``vulnerability_core.Vulnerability``: the upstream CVE Record Format places the CVE ID inside ``cveMetadata.cveId`` rather than at the record root. Semantic equivalence with the broader ``Vulnerability`` concept is preserved via ``exact_mappings``.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:NVDEntry'],
         'exact_mappings': ['WIKIDATA:Q631425', 'core:Vulnerability'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'in_subset': ['cve_record'],
         'related_mappings': ['kev_catalog:KevEntry'],
         'slot_usage': {'containers': {'name': 'containers', 'required': True},
                        'cve_metadata': {'name': 'cve_metadata', 'required': True}},
         'tree_root': True})

    data_type: Optional[DataType] = Field(default=DataType.CVE_RECORD, description="""Indicates the type of information represented in the JSON instance.""", json_schema_extra = { "linkml_meta": {'aliases': ['dataType'],
         'domain_of': ['CVERecord'],
         'ifabsent': 'DataType(CVE_RECORD)',
         'in_subset': ['cve_record']} })
    data_version: Optional[str] = Field(default="5.2.0", description="""The version of the CVE schema used for validating this record. Supports multiple versions of the format (e.g., '5.2.0').""", json_schema_extra = { "linkml_meta": {'aliases': ['dataVersion'],
         'domain_of': ['CVERecord'],
         'ifabsent': 'string(5.2.0)',
         'in_subset': ['cve_record']} })
    cve_metadata: Union[CveMetadataPublished, CveMetadataRejected] = Field(default=..., description="""Metadata about the CVE ID. A Published record uses CveMetadataPublished; a Rejected record uses CveMetadataRejected.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveMetadata'],
         'any_of': [{'range': 'CveMetadataPublished'},
                    {'range': 'CveMetadataRejected'}],
         'domain_of': ['CVERecord'],
         'in_subset': ['cve_record']} })
    containers: Containers = Field(default=..., description="""A set of containers (CNA and optionally ADP) holding vulnerability information related to the CVE ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CVERecord'], 'in_subset': ['cve_record']} })

    @field_validator('data_version')
    def pattern_data_version(cls, v):
        pattern=re.compile(r"^5\.(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid data_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid data_version format: {v}"
            raise ValueError(err_msg)
        return v


class CveMetadata(ConfiguredBaseModel):
    """
    Abstract base for CVE Record metadata. Represents either a Published or Rejected record's metadata. All fields are controlled by CVE Services. Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CveMetadataPublished``, ``CveMetadataRejected``); slot-level ``any_of`` on the ``cve_metadata`` slot preserves the choice for generators (e.g. JSON Schema ``anyOf``).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lmodel/cve'})

    pass


class CveMetadataPublished(CveMetadata):
    """
    Metadata for a CVE Record in the PUBLISHED state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'assigner_org_id': {'name': 'assigner_org_id',
                                            'required': True},
                        'published_state': {'name': 'published_state',
                                            'required': True},
                        'record_cve_id': {'name': 'record_cve_id', 'required': True}}})

    record_cve_id: str = Field(default=..., description="""The CVE identifier that this record pertains to.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveId'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    assigner_org_id: str = Field(default=..., description="""The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service.""", json_schema_extra = { "linkml_meta": {'aliases': ['assignerOrgId'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    assigner_short_name: Optional[str] = Field(default=None, description="""The short name for the organization to which the CVE ID was originally assigned.""", json_schema_extra = { "linkml_meta": {'aliases': ['assignerShortName'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    serial: Optional[int] = Field(default=None, description="""Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    date_updated: Optional[str] = Field(default=None, description="""The date/time the record was last updated.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateUpdated'],
         'domain_of': ['CveMetadataPublished',
                       'CveMetadataRejected',
                       'ProviderMetadata'],
         'in_subset': ['cna_metadata']} })
    date_reserved: Optional[str] = Field(default=None, description="""The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateReserved'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    requester_user_id: Optional[str] = Field(default=None, description="""The user that requested the CVE identifier.""", json_schema_extra = { "linkml_meta": {'aliases': ['requesterUserId'],
         'domain_of': ['CveMetadataPublished'],
         'in_subset': ['cna_metadata']} })
    date_published: Optional[str] = Field(default=None, description="""The date/time the CVE Record was first published in the CVE List.""", json_schema_extra = { "linkml_meta": {'aliases': ['datePublished'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata'],
         'related_mappings': ['kev_catalog:date_added']} })
    published_state: RecordState = Field(default=..., description="""State of the CVE Record. For published records, this is always PUBLISHED.""", json_schema_extra = { "linkml_meta": {'aliases': ['state'],
         'domain_of': ['CveMetadataPublished'],
         'in_subset': ['cna_metadata']} })

    @field_validator('record_cve_id')
    def pattern_record_cve_id(cls, v):
        pattern=re.compile(r"^CVE-[0-9]{4}-[0-9]{4,19}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid record_cve_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid record_cve_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('assigner_short_name')
    def pattern_assigner_short_name(cls, v):
        pattern=re.compile(r"^.{2,32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid assigner_short_name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid assigner_short_name format: {v}"
            raise ValueError(err_msg)
        return v


class CveMetadataRejected(CveMetadata):
    """
    Metadata for a CVE Record in the REJECTED state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'assigner_org_id': {'name': 'assigner_org_id',
                                            'required': True},
                        'record_cve_id': {'name': 'record_cve_id', 'required': True},
                        'rejected_state': {'name': 'rejected_state', 'required': True}}})

    record_cve_id: str = Field(default=..., description="""The CVE identifier that this record pertains to.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveId'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    assigner_org_id: str = Field(default=..., description="""The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service.""", json_schema_extra = { "linkml_meta": {'aliases': ['assignerOrgId'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    assigner_short_name: Optional[str] = Field(default=None, description="""The short name for the organization to which the CVE ID was originally assigned.""", json_schema_extra = { "linkml_meta": {'aliases': ['assignerShortName'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    serial: Optional[int] = Field(default=None, description="""Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    date_updated: Optional[str] = Field(default=None, description="""The date/time the record was last updated.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateUpdated'],
         'domain_of': ['CveMetadataPublished',
                       'CveMetadataRejected',
                       'ProviderMetadata'],
         'in_subset': ['cna_metadata']} })
    date_reserved: Optional[str] = Field(default=None, description="""The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateReserved'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    date_published: Optional[str] = Field(default=None, description="""The date/time the CVE Record was first published in the CVE List.""", json_schema_extra = { "linkml_meta": {'aliases': ['datePublished'],
         'domain_of': ['CveMetadataPublished', 'CveMetadataRejected'],
         'in_subset': ['cna_metadata'],
         'related_mappings': ['kev_catalog:date_added']} })
    date_rejected: Optional[str] = Field(default=None, description="""The date/time the CVE ID was rejected.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateRejected'],
         'domain_of': ['CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })
    rejected_state: RecordState = Field(default=..., description="""State of the CVE Record. For rejected records, this is always REJECTED.""", json_schema_extra = { "linkml_meta": {'aliases': ['state'],
         'domain_of': ['CveMetadataRejected'],
         'in_subset': ['cna_metadata']} })

    @field_validator('record_cve_id')
    def pattern_record_cve_id(cls, v):
        pattern=re.compile(r"^CVE-[0-9]{4}-[0-9]{4,19}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid record_cve_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid record_cve_id format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('assigner_short_name')
    def pattern_assigner_short_name(cls, v):
        pattern=re.compile(r"^.{2,32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid assigner_short_name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid assigner_short_name format: {v}"
            raise ValueError(err_msg)
        return v


class Containers(ConfiguredBaseModel):
    """
    A set of structures (called containers) used to store vulnerability information related to a specific CVE ID. At minimum a 'cna' container is required.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'cna': {'name': 'cna', 'required': True}}})

    cna: Union[CnaPublishedContainer, CnaRejectedContainer] = Field(default=..., description="""The CNA container holding vulnerability information for this CVE ID. For published records, this is a CnaPublishedContainer. For rejected records, this is a CnaRejectedContainer.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'CnaPublishedContainer'},
                    {'range': 'CnaRejectedContainer'}],
         'domain_of': ['Containers']} })
    adp: Optional[list[AdpContainer]] = Field(default=None, description="""One or more ADP containers providing additional vulnerability information. Multiple ADPs may contribute containers for the same CVE ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Containers']} })


class ProviderMetadata(ConfiguredBaseModel):
    """
    Details related to the information container provider (CNA or ADP).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'related_mappings': ['nvd:ScoreSource'],
         'slot_usage': {'org_id': {'name': 'org_id', 'required': True}}})

    org_id: str = Field(default=..., description="""The container provider's organizational UUID.""", json_schema_extra = { "linkml_meta": {'aliases': ['orgId'], 'domain_of': ['ProviderMetadata']} })
    short_name: Optional[str] = Field(default=None, description="""The container provider's organizational short name (2-32 characters).""", json_schema_extra = { "linkml_meta": {'aliases': ['shortName'], 'domain_of': ['ProviderMetadata']} })
    date_updated: Optional[str] = Field(default=None, description="""The date/time the record was last updated.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateUpdated'],
         'domain_of': ['CveMetadataPublished',
                       'CveMetadataRejected',
                       'ProviderMetadata'],
         'in_subset': ['cna_metadata']} })

    @field_validator('short_name')
    def pattern_short_name(cls, v):
        pattern=re.compile(r"^.{2,32}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid short_name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid short_name format: {v}"
            raise ValueError(err_msg)
        return v


class CnaContainer(ConfiguredBaseModel):
    """
    Abstract base for CNA containers (published and rejected). Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CnaPublishedContainer``, ``CnaRejectedContainer``); slot-level ``any_of`` on the ``cna`` slot preserves the choice for generators.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/lmodel/cve'})

    pass


class CnaPublishedContainer(CnaContainer):
    """
    An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a published CVE ID. There can only be one CNA container per CVE record since there can only be one assigning CNA.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'affected': {'name': 'affected', 'required': True},
                        'cve_references': {'name': 'cve_references', 'required': True},
                        'descriptions': {'name': 'descriptions', 'required': True},
                        'provider_metadata': {'name': 'provider_metadata',
                                              'required': True},
                        'title': {'annotations': {'max_length': {'tag': 'max_length',
                                                                 'value': 256},
                                                  'min_length': {'tag': 'min_length',
                                                                 'value': 1}},
                                  'name': 'title'}}})

    provider_metadata: ProviderMetadata = Field(default=..., description="""Details related to the information container provider (CNA or ADP).""", json_schema_extra = { "linkml_meta": {'aliases': ['providerMetadata'],
         'domain_of': ['CnaPublishedContainer', 'CnaRejectedContainer', 'AdpContainer']} })
    date_assigned: Optional[str] = Field(default=None, description="""The date/time this CVE ID was associated with a vulnerability by a CNA.""", json_schema_extra = { "linkml_meta": {'aliases': ['dateAssigned'], 'domain_of': ['CnaPublishedContainer']} })
    date_public: Optional[str] = Field(default=None, description="""If known, the date/time the vulnerability was disclosed publicly.""", json_schema_extra = { "linkml_meta": {'aliases': ['datePublic'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title or name for this entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 256},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'close_mappings': ['kev_catalog:vulnerability_name'],
         'domain_of': ['Vulnerability', 'CnaPublishedContainer', 'AdpContainer'],
         'exact_mappings': ['schema:name'],
         'in_subset': ['metadata'],
         'slot_uri': 'dct:title'} })
    descriptions: list[MultiLangDescription] = Field(default=..., description="""A list of multi-lingual descriptions of the vulnerability. Must contain at least one English language entry. E.g., [PROBLEMTYPE] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [VECTOR].""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    affected: list[AffectedProduct] = Field(default=..., description="""List of affected products and services.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cpe_applicability: Optional[list[CpeApplicabilityElement]] = Field(default=None, description="""Affected products defined using the CPE Applicability Language. When defined, this block should align with the data in the affected block.""", json_schema_extra = { "linkml_meta": {'aliases': ['cpeApplicability'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    problem_types: Optional[list[ProblemType]] = Field(default=None, description="""Problem type information such as CWE identifiers. Must contain at least one entry. Entries can be text, OWASP, or CWE identifiers.""", json_schema_extra = { "linkml_meta": {'aliases': ['problemTypes'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cve_references: list[CveReference] = Field(default=..., description="""Reference data in the form of URLs describing the vulnerability, such as advisories, patches, and exploit details. Required by CNA rules.""", min_length=1, max_length=512, json_schema_extra = { "linkml_meta": {'aliases': ['references'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    impacts: Optional[list[ImpactEntry]] = Field(default=None, description="""Collection of impacts of this vulnerability, optionally linked to CAPEC IDs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    metrics: Optional[list[MetricEntry]] = Field(default=None, description="""Collection of impact scores with attribution (CVSSv2, CVSSv3.0, CVSSv3.1, CVSSv4.0, or custom format).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    configurations_text: Optional[list[MultiLangDescription]] = Field(default=None, description="""Configurations required for exploiting this vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['configurations'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    workarounds: Optional[list[MultiLangDescription]] = Field(default=None, description="""Workarounds and mitigations for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    solutions: Optional[list[MultiLangDescription]] = Field(default=None, description="""Information about solutions or remediations available for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    exploits: Optional[list[MultiLangDescription]] = Field(default=None, description="""Information about known exploits of this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    timeline: Optional[list[TimelineEntry]] = Field(default=None, description="""Timeline information for significant events about the vulnerability or changes to the CVE Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    credits: Optional[list[CreditEntry]] = Field(default=None, description="""Statements acknowledging specific people, organizations, or tools for work related to research, discovery, remediation, or coordination of this CVE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cna_source: Optional[SourceInformation] = Field(default=None, description="""Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information.""", json_schema_extra = { "linkml_meta": {'aliases': ['source'], 'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cna_tags: Optional[list[Union[CNATag, str]]] = Field(default=None, description="""Tags provided by a CNA describing the CVE Record.""", json_schema_extra = { "linkml_meta": {'aliases': ['tags'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'any_of': [{'range': 'CNATag'}, {'pattern': '^x_.*$', 'range': 'string'}],
         'domain_of': ['CnaPublishedContainer']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""List of taxonomy items (e.g., ATT&CK, CWE) related to the vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyMappings'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })


class CnaRejectedContainer(CnaContainer):
    """
    An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a rejected CVE ID. There can only be one CNA container per CVE record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'provider_metadata': {'name': 'provider_metadata',
                                              'required': True},
                        'rejected_reasons': {'name': 'rejected_reasons',
                                             'required': True}}})

    provider_metadata: ProviderMetadata = Field(default=..., description="""Details related to the information container provider (CNA or ADP).""", json_schema_extra = { "linkml_meta": {'aliases': ['providerMetadata'],
         'domain_of': ['CnaPublishedContainer', 'CnaRejectedContainer', 'AdpContainer']} })
    rejected_reasons: list[MultiLangDescription] = Field(default=..., description="""Reasons for rejecting this CVE Record.""", json_schema_extra = { "linkml_meta": {'aliases': ['rejectedReasons'], 'domain_of': ['CnaRejectedContainer']} })
    replaced_by: Optional[list[str]] = Field(default=None, description="""CVE IDs that this CVE ID was rejected in favor of because this CVE ID was incorrectly assigned to the same vulnerabilities.""", json_schema_extra = { "linkml_meta": {'aliases': ['replacedBy'], 'domain_of': ['CnaRejectedContainer']} })


class AdpContainer(ConfiguredBaseModel):
    """
    An object containing vulnerability information provided by an Authorized Data Publisher (ADP). Multiple ADPs can provide containers for a single CVE ID.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'provider_metadata': {'name': 'provider_metadata',
                                              'required': True}}})

    provider_metadata: ProviderMetadata = Field(default=..., description="""Details related to the information container provider (CNA or ADP).""", json_schema_extra = { "linkml_meta": {'aliases': ['providerMetadata'],
         'domain_of': ['CnaPublishedContainer', 'CnaRejectedContainer', 'AdpContainer']} })
    date_public: Optional[str] = Field(default=None, description="""If known, the date/time the vulnerability was disclosed publicly.""", json_schema_extra = { "linkml_meta": {'aliases': ['datePublic'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title or name for this entity.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:vulnerability_name'],
         'domain_of': ['Vulnerability', 'CnaPublishedContainer', 'AdpContainer'],
         'exact_mappings': ['schema:name'],
         'in_subset': ['metadata'],
         'slot_uri': 'dct:title'} })
    descriptions: Optional[list[MultiLangDescription]] = Field(default=None, description="""A list of multi-lingual descriptions of the vulnerability. Must contain at least one English language entry. E.g., [PROBLEMTYPE] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [VECTOR].""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    affected: Optional[list[AffectedProduct]] = Field(default=None, description="""List of affected products and services.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cpe_applicability: Optional[list[CpeApplicabilityElement]] = Field(default=None, description="""Affected products defined using the CPE Applicability Language. When defined, this block should align with the data in the affected block.""", json_schema_extra = { "linkml_meta": {'aliases': ['cpeApplicability'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    problem_types: Optional[list[ProblemType]] = Field(default=None, description="""Problem type information such as CWE identifiers. Must contain at least one entry. Entries can be text, OWASP, or CWE identifiers.""", json_schema_extra = { "linkml_meta": {'aliases': ['problemTypes'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cve_references: Optional[list[CveReference]] = Field(default=None, description="""Reference data in the form of URLs describing the vulnerability, such as advisories, patches, and exploit details. Required by CNA rules.""", min_length=1, max_length=512, json_schema_extra = { "linkml_meta": {'aliases': ['references'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    impacts: Optional[list[ImpactEntry]] = Field(default=None, description="""Collection of impacts of this vulnerability, optionally linked to CAPEC IDs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    metrics: Optional[list[MetricEntry]] = Field(default=None, description="""Collection of impact scores with attribution (CVSSv2, CVSSv3.0, CVSSv3.1, CVSSv4.0, or custom format).""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    configurations_text: Optional[list[MultiLangDescription]] = Field(default=None, description="""Configurations required for exploiting this vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['configurations'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    workarounds: Optional[list[MultiLangDescription]] = Field(default=None, description="""Workarounds and mitigations for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    solutions: Optional[list[MultiLangDescription]] = Field(default=None, description="""Information about solutions or remediations available for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    exploits: Optional[list[MultiLangDescription]] = Field(default=None, description="""Information about known exploits of this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    timeline: Optional[list[TimelineEntry]] = Field(default=None, description="""Timeline information for significant events about the vulnerability or changes to the CVE Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    credits: Optional[list[CreditEntry]] = Field(default=None, description="""Statements acknowledging specific people, organizations, or tools for work related to research, discovery, remediation, or coordination of this CVE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    cna_source: Optional[SourceInformation] = Field(default=None, description="""Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information.""", json_schema_extra = { "linkml_meta": {'aliases': ['source'], 'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })
    adp_tags: Optional[list[Union[ADPTag, str]]] = Field(default=None, description="""Tags provided by an ADP describing the CVE Record.""", json_schema_extra = { "linkml_meta": {'aliases': ['tags'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'any_of': [{'range': 'ADPTag'}, {'pattern': '^x_.*$', 'range': 'string'}],
         'domain_of': ['AdpContainer']} })
    taxonomy_mappings: Optional[list[TaxonomyMapping]] = Field(default=None, description="""List of taxonomy items (e.g., ATT&CK, CWE) related to the vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyMappings'],
         'domain_of': ['CnaPublishedContainer', 'AdpContainer']} })


class AffectedProduct(ConfiguredBaseModel):
    """
    Information about the set of products and services affected by a vulnerability. At least one of (vendor + product) or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.
    Note: this class deliberately does NOT inherit from ``vulnerability_core.Product``. The upstream CVE ``product`` definition uses a multivalued ``versions`` slot (range ``VersionEntry``), which conflicts with ``Product.version`` (singular string). The ``vendor``, ``name`` (= upstream ``product``), and ``platforms`` slots are reused from the core schema directly. Semantic equivalence is preserved via ``exact_mappings``.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'all_of': [{'any_of': [{'slot_conditions': {'name': {'name': 'name',
                                                              'required': True},
                                                     'vendor': {'name': 'vendor',
                                                                'required': True}}},
                                {'slot_conditions': {'collection_url': {'name': 'collection_url',
                                                                        'required': True},
                                                     'package_name': {'name': 'package_name',
                                                                      'required': True}}}]},
                    {'any_of': [{'slot_conditions': {'versions': {'name': 'versions',
                                                                  'required': True}}},
                                {'slot_conditions': {'default_status': {'name': 'default_status',
                                                                        'required': True}}}]}],
         'exact_mappings': ['core:Product', 'schema:SoftwareApplication'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'related_mappings': ['kev_catalog:KevEntry'],
         'slot_usage': {'name': {'aliases': ['product'],
                                 'annotations': {'max_length': {'tag': 'max_length',
                                                                'value': 512},
                                                 'min_length': {'tag': 'min_length',
                                                                'value': 1}},
                                 'description': 'Name of the affected product '
                                                '(upstream field ``product``).',
                                 'name': 'name'},
                        'platforms': {'annotations': {'max_length': {'tag': 'max_length',
                                                                     'value': 1024},
                                                      'min_length': {'tag': 'min_length',
                                                                     'value': 1}},
                                      'name': 'platforms'},
                        'vendor': {'annotations': {'max_length': {'tag': 'max_length',
                                                                  'value': 512},
                                                   'min_length': {'tag': 'min_length',
                                                                  'value': 1}},
                                   'name': 'vendor'}}})

    vendor: Optional[str] = Field(default=None, description="""Name of the vendor or organization responsible for the product.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 512},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['Product', 'AffectedProduct'],
         'slot_uri': 'schema:name'} })
    name: Optional[str] = Field(default=None, description="""Name of the affected product (upstream field ``product``).""", json_schema_extra = { "linkml_meta": {'aliases': ['product'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 512},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['Product', 'Reference', 'Weakness', 'AffectedProduct'],
         'slot_uri': 'rdfs:label'} })
    platforms: Optional[list[str]] = Field(default=None, description="""Platforms or operating environments affected.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 1024},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['Product', 'AffectedProduct']} })
    collection_url: Optional[str] = Field(default=None, description="""URL identifying a package collection (determines the meaning of packageName).""", json_schema_extra = { "linkml_meta": {'aliases': ['collectionURL'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 2048},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })
    package_name: Optional[str] = Field(default=None, description="""Name or identifier of the affected software package as used in the package collection.""", json_schema_extra = { "linkml_meta": {'aliases': ['packageName'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 2048},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })
    cpes: Optional[list[str]] = Field(default=None, description="""Affected products defined by CPE (Common Platform Enumeration) names in either 2.2 or 2.3 format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AffectedProduct']} })
    modules: Optional[list[str]] = Field(default=None, description="""A list of the affected components, features, modules, sub-components, sub-products, APIs, commands, utilities, programs, or functionalities.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })
    program_files: Optional[list[str]] = Field(default=None, description="""A list of the affected source code files.""", json_schema_extra = { "linkml_meta": {'aliases': ['programFiles'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 1024},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })
    program_routines: Optional[list[ProgramRoutine]] = Field(default=None, description="""A list of the affected source code functions, methods, subroutines, or procedures.""", json_schema_extra = { "linkml_meta": {'aliases': ['programRoutines'], 'domain_of': ['AffectedProduct']} })
    repo: Optional[str] = Field(default=None, description="""The URL of the source code repository, for informational purposes and/or to resolve git hash version ranges.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 2048},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })
    default_status: Optional[VersionStatus] = Field(default=None, description="""The default status for versions not otherwise listed in the versions list. Defaults to 'unknown' if not specified. Versions or defaultStatus may be omitted, but not both.""", json_schema_extra = { "linkml_meta": {'aliases': ['defaultStatus'], 'domain_of': ['AffectedProduct']} })
    versions: Optional[list[VersionEntry]] = Field(default=None, description="""Set of product versions or version ranges related to the vulnerability. Versions or defaultStatus may be omitted, but not both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AffectedProduct']} })
    package_url: Optional[str] = Field(default=None, description="""A Package URL (PURL), a unified URL specification for identifying packages hosted by known package hosts. The Package URL MUST NOT include a version.""", json_schema_extra = { "linkml_meta": {'aliases': ['packageURL'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 2048},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['AffectedProduct']} })


class ProgramRoutine(ConfiguredBaseModel):
    """
    An affected source code function, method, subroutine, or procedure.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'routine_name': {'name': 'routine_name', 'required': True}}})

    routine_name: str = Field(default=..., description="""Name of the affected source code function, method, subroutine, or procedure.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['ProgramRoutine']} })


class VersionEntry(ConfiguredBaseModel):
    """
    A single version or a range of versions of a product with associated vulnerability status. An entry with only version and status is a point version; an entry with versionType and a less-than limit describes a range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'none_of': [{'slot_conditions': {'less_than': {'name': 'less_than',
                                                        'required': True},
                                          'less_than_or_equal': {'name': 'less_than_or_equal',
                                                                 'required': True}}}],
         'rules': [{'postconditions': {'slot_conditions': {'version_type': {'name': 'version_type',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'less_than': {'name': 'less_than',
                                                                        'required': True}}}},
                   {'postconditions': {'slot_conditions': {'version_type': {'name': 'version_type',
                                                                            'required': True}}},
                    'preconditions': {'slot_conditions': {'less_than_or_equal': {'name': 'less_than_or_equal',
                                                                                 'required': True}}}}],
         'slot_usage': {'version_status': {'name': 'version_status', 'required': True},
                        'version_value': {'name': 'version_value', 'required': True}}})

    version_value: str = Field(default=..., description="""The single version being described, or the version at the start of the range. By convention, '0' denotes the earliest possible version.""", json_schema_extra = { "linkml_meta": {'aliases': ['version'], 'domain_of': ['VersionEntry']} })
    version_status: VersionStatus = Field(default=..., description="""The vulnerability status for the version or range of versions. For a range, the status may be refined by the 'changes' list.""", json_schema_extra = { "linkml_meta": {'aliases': ['status'], 'domain_of': ['VersionEntry']} })
    version_type: Optional[str] = Field(default=None, description="""The version numbering system used for specifying the range (e.g., semver, git, maven, rpm, python, custom). Defines the semantics of comparison.""", json_schema_extra = { "linkml_meta": {'aliases': ['versionType'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['VersionEntry']} })
    less_than: Optional[str] = Field(default=None, description="""The non-inclusive upper limit of the range. This is the least version NOT in the range. Supports wildcard '*' suffix.""", json_schema_extra = { "linkml_meta": {'aliases': ['lessThan'], 'domain_of': ['VersionEntry']} })
    less_than_or_equal: Optional[str] = Field(default=None, description="""The inclusive upper limit of the range. This is the greatest version contained in the range. Only one of lessThan and lessThanOrEqual should be specified.""", json_schema_extra = { "linkml_meta": {'aliases': ['lessThanOrEqual'], 'domain_of': ['VersionEntry']} })
    version_changes: Optional[list[VersionChange]] = Field(default=None, description="""A list of status changes that take place during the version range. The array should be sorted by 'at' field according to versionType, but clients must re-sort rather than assume ordering.""", json_schema_extra = { "linkml_meta": {'aliases': ['changes'], 'domain_of': ['VersionEntry']} })


class VersionChange(ConfiguredBaseModel):
    """
    A status change that takes place at a specific point within a version range.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'change_at': {'name': 'change_at', 'required': True},
                        'change_status': {'name': 'change_status', 'required': True}}})

    change_at: str = Field(default=..., description="""The version at which a status change occurs within a range.""", json_schema_extra = { "linkml_meta": {'aliases': ['at'], 'domain_of': ['VersionChange']} })
    change_status: VersionStatus = Field(default=..., description="""The new status in the range starting at the given version.""", json_schema_extra = { "linkml_meta": {'aliases': ['status'], 'domain_of': ['VersionChange']} })


class MultiLangDescription(ConfiguredBaseModel):
    """
    Text in a particular language with optional alternate markup or formatted representation (e.g., Markdown) or embedded media. Used for vulnerability descriptions, rejected reasons, configurations, workarounds, solutions, and exploits.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'description_value': {'name': 'description_value',
                                              'required': True},
                        'lang': {'name': 'lang', 'required': True}}})

    lang: str = Field(default="en", description="""BCP 47 language code indicating the language of accompanying text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultiLangDescription',
                       'ProblemTypeDescription',
                       'MetricScenario',
                       'TimelineEntry',
                       'CreditEntry'],
         'ifabsent': 'string(en)'} })
    description_value: str = Field(default=..., description="""Plain text description (up to 4096 characters).""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['MultiLangDescription']} })
    supporting_media: Optional[list[SupportingMedia]] = Field(default=None, description="""Supporting media data for the description such as markdown, diagrams, etc. Similar to RFC 2397, each object has a media type, data value, and optional base64 flag.""", json_schema_extra = { "linkml_meta": {'aliases': ['supportingMedia'], 'domain_of': ['MultiLangDescription']} })


class SupportingMedia(ConfiguredBaseModel):
    """
    Supporting media data for a description such as markdown, diagrams, etc. Similar to RFC 2397, each media object has a media type, data value, and an optional base64 flag.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'media_type': {'name': 'media_type', 'required': True},
                        'media_value': {'name': 'media_value', 'required': True}}})

    media_type: str = Field(default=..., description="""RFC2046 compliant IANA Media type (e.g., text/markdown, text/html, image/png, image/svg, audio/mp3).""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 256},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['SupportingMedia']} })
    base64_encoded: Optional[bool] = Field(default=False, description="""If true, the media_value field contains the media data encoded in base64. If false, the media_value field contains UTF-8 media content.""", json_schema_extra = { "linkml_meta": {'aliases': ['base64'], 'domain_of': ['SupportingMedia'], 'ifabsent': 'False'} })
    media_value: str = Field(default=..., description="""Supporting media content, up to 16K characters. If base64_encoded is true, this stores base64 encoded data.""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 16384},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['SupportingMedia']} })


class ProblemType(ConfiguredBaseModel):
    """
    Problem type information (e.g., CWE identifier). Wraps one or more problem type descriptions. The CNA requirement is [PROBLEMTYPE].
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:Weakness', 'nvd:NVDWeakness'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'problem_type_descriptions': {'name': 'problem_type_descriptions',
                                                      'required': True}}})

    problem_type_descriptions: list[ProblemTypeDescription] = Field(default=..., description="""One or more problem type descriptions (e.g., CWE IDs or OWASP categories).""", json_schema_extra = { "linkml_meta": {'aliases': ['descriptions'], 'domain_of': ['ProblemType']} })


class ProblemTypeDescription(ConfiguredBaseModel):
    """
    Individual problem type description entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:Weakness'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'cwe_id': {'name': 'cwe_id',
                                   'related_mappings': ['cwe:Weakness']},
                        'lang': {'name': 'lang', 'required': True},
                        'problem_description': {'close_mappings': ['cwe:Weakness'],
                                                'name': 'problem_description',
                                                'required': True}}})

    lang: str = Field(default="en", description="""BCP 47 language code indicating the language of accompanying text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultiLangDescription',
                       'ProblemTypeDescription',
                       'MetricScenario',
                       'TimelineEntry',
                       'CreditEntry'],
         'ifabsent': 'string(en)'} })
    problem_description: str = Field(default=..., description="""Text description of the problem type, or title from CWE or OWASP.""", json_schema_extra = { "linkml_meta": {'aliases': ['description'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'close_mappings': ['cwe:Weakness'],
         'domain_of': ['ProblemTypeDescription']} })
    cwe_id: Optional[str] = Field(default=None, description="""CWE identifier for the weakness classification (e.g. CWE-79).""", json_schema_extra = { "linkml_meta": {'aliases': ['cweId'],
         'domain_of': ['Weakness', 'ProblemTypeDescription'],
         'related_mappings': ['cwe:Weakness'],
         'slot_uri': 'dct:identifier'} })
    problem_source_type: Optional[str] = Field(default=None, description="""Problem type source format (e.g., text, OWASP, CWE).""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 64},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['ProblemTypeDescription']} })
    problem_references: Optional[list[CveReference]] = Field(default=None, description="""References supporting this specific problem type.""", json_schema_extra = { "linkml_meta": {'aliases': ['references'], 'domain_of': ['ProblemTypeDescription']} })

    @field_validator('cwe_id')
    def pattern_cwe_id(cls, v):
        pattern=re.compile(r"^CWE-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cwe_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cwe_id format: {v}"
            raise ValueError(err_msg)
        return v


class CveReference(Reference):
    """
    An external reference associated with a CVE Record. Extends the core Reference with optional descriptive tags characterizing the resource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:NVDReference'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'related_mappings': ['cwe:ExternalReference'],
         'slot_usage': {'name': {'annotations': {'max_length': {'tag': 'max_length',
                                                                'value': 512},
                                                 'min_length': {'tag': 'min_length',
                                                                'value': 1}},
                                 'name': 'name'},
                        'url': {'annotations': {'max_length': {'tag': 'max_length',
                                                               'value': 2048},
                                                'min_length': {'tag': 'min_length',
                                                               'value': 1}},
                                'name': 'url',
                                'required': True}}})

    reference_tags: Optional[list[ReferenceTag]] = Field(default=None, description="""An array of tags describing the resource referenced by the URL.""", json_schema_extra = { "linkml_meta": {'aliases': ['tags'], 'domain_of': ['CveReference']} })
    url: str = Field(default=..., description="""URL pointing to the reference resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'max_length': {'tag': 'max_length', 'value': 2048},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['Reference'],
         'slot_uri': 'schema:url'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 512},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['Product', 'Reference', 'Weakness', 'AffectedProduct'],
         'slot_uri': 'rdfs:label'} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference'], 'slot_uri': 'dct:source'} })


class ImpactEntry(ConfiguredBaseModel):
    """
    An impact entry linking an optional CAPEC attack pattern ID to one or more prose descriptions of the impact scenario.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'impact_descriptions': {'name': 'impact_descriptions',
                                                'required': True}}})

    capec_id: Optional[str] = Field(default=None, description="""CAPEC ID that best relates to this impact (e.g., CAPEC-123).""", json_schema_extra = { "linkml_meta": {'aliases': ['capecId'], 'domain_of': ['ImpactEntry']} })
    impact_descriptions: list[MultiLangDescription] = Field(default=..., description="""Prose description of the impact scenario. At a minimum, provide the description given by CAPEC.""", json_schema_extra = { "linkml_meta": {'aliases': ['descriptions'], 'domain_of': ['ImpactEntry']} })

    @field_validator('capec_id')
    def pattern_capec_id(cls, v):
        pattern=re.compile(r"^CAPEC-[1-9][0-9]{0,4}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid capec_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid capec_id format: {v}"
            raise ValueError(err_msg)
        return v


class MetricEntry(ConfiguredBaseModel):
    """
    A metric entry containing scoring data in one of the CVSS formats (v4.0, v3.x, v2.0) or a custom format, with optional applicability scenarios. At least one of cvss_v4_0, cvss_v3, cvss_v2_0, or other_metric is required. CVSS 3.0 and 3.1 are both represented by CvssV3 (distinguished by the cvss3_version slot).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'cvss_v4_0': {'name': 'cvss_v4_0',
                                                       'required': True}}},
                    {'slot_conditions': {'cvss_v3': {'name': 'cvss_v3',
                                                     'required': True}}},
                    {'slot_conditions': {'cvss_v2_0': {'name': 'cvss_v2_0',
                                                       'required': True}}},
                    {'slot_conditions': {'other_metric': {'name': 'other_metric',
                                                          'required': True}}}],
         'close_mappings': ['nvd:MetricSet'],
         'from_schema': 'https://w3id.org/lmodel/cve'})

    metric_format: Optional[str] = Field(default=None, description="""Name of the scoring format (e.g., cvssV4_0, cvssV3_1). Provides future-proofing and supports proprietary format inclusion.""", json_schema_extra = { "linkml_meta": {'aliases': ['format'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 64},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['MetricEntry']} })
    metric_scenarios: Optional[list[MetricScenario]] = Field(default=None, description="""Scenarios this metrics object applies to. If no specific scenario is given, GENERAL applies when no more specific metric matches.""", json_schema_extra = { "linkml_meta": {'aliases': ['scenarios'], 'domain_of': ['MetricEntry']} })
    cvss_v4_0: Optional[CvssV40] = Field(default=None, description="""CVSS version 4.0 scoring data.""", json_schema_extra = { "linkml_meta": {'aliases': ['cvssV4_0'], 'domain_of': ['MetricEntry']} })
    cvss_v3: Optional[CvssV3] = Field(default=None, description="""CVSS version 3.x scoring data (covers both 3.0 and 3.1). The version is distinguished by the cvss3_version field within the CvssV3 object.""", json_schema_extra = { "linkml_meta": {'aliases': ['cvssV3', 'cvssV3_0', 'cvssV3_1'], 'domain_of': ['MetricEntry']} })
    cvss_v2_0: Optional[CvssV20] = Field(default=None, description="""CVSS version 2.0 scoring data.""", json_schema_extra = { "linkml_meta": {'aliases': ['cvssV2_0'], 'domain_of': ['MetricEntry']} })
    other_metric: Optional[OtherMetric] = Field(default=None, description="""A non-standard impact description or score.""", json_schema_extra = { "linkml_meta": {'aliases': ['other'], 'domain_of': ['MetricEntry']} })


class MetricScenario(ConfiguredBaseModel):
    """
    A scenario description indicating the context in which a metric applies. If no specific scenario is given, GENERAL is used as the default.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'lang': {'name': 'lang', 'required': True},
                        'scenario_value': {'name': 'scenario_value', 'required': True}}})

    lang: str = Field(default="en", description="""BCP 47 language code indicating the language of accompanying text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultiLangDescription',
                       'ProblemTypeDescription',
                       'MetricScenario',
                       'TimelineEntry',
                       'CreditEntry'],
         'ifabsent': 'string(en)'} })
    scenario_value: str = Field(default="GENERAL", description="""Description of the scenario this metrics object applies to.""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['MetricScenario'],
         'ifabsent': 'string(GENERAL)'} })


class CvssV40(ConfiguredBaseModel):
    """
    CVSS version 4.0 scoring object. Requires version, vectorString, baseScore, and baseSeverity. All other fields are optional.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'in_subset': ['cvss_metrics'],
         'narrow_mappings': ['nvd:CVSSMetric'],
         'slot_usage': {'cvss4_base_score': {'name': 'cvss4_base_score',
                                             'required': True},
                        'cvss4_base_severity': {'name': 'cvss4_base_severity',
                                                'required': True},
                        'cvss4_vector_string': {'name': 'cvss4_vector_string',
                                                'required': True},
                        'cvss4_version': {'name': 'cvss4_version', 'required': True}}})

    cvss4_version: str = Field(default=..., description="""CVSS version identifier. Must be '4.0' for CVSS v4.0 objects.""", json_schema_extra = { "linkml_meta": {'aliases': ['version'], 'domain_of': ['CvssV4_0']} })
    cvss4_vector_string: str = Field(default=..., description="""CVSS 4.0 vector string encoding all base, threat, and environmental metrics.""", json_schema_extra = { "linkml_meta": {'aliases': ['vectorString'], 'domain_of': ['CvssV4_0']} })
    cvss4_base_score: float = Field(default=..., description="""CVSS 4.0 base score (0.0 – 10.0 in 0.1 increments).""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['baseScore'], 'domain_of': ['CvssV4_0']} })
    cvss4_base_severity: Cvss4Severity = Field(default=..., description="""CVSS 4.0 qualitative base severity rating.""", json_schema_extra = { "linkml_meta": {'aliases': ['baseSeverity'], 'domain_of': ['CvssV4_0']} })
    cvss4_attack_vector: Optional[Cvss4AttackVector] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['attackVector'], 'domain_of': ['CvssV4_0']} })
    cvss4_attack_complexity: Optional[Cvss4AttackComplexity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['attackComplexity'], 'domain_of': ['CvssV4_0']} })
    cvss4_attack_requirements: Optional[Cvss4AttackRequirements] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['attackRequirements'], 'domain_of': ['CvssV4_0']} })
    cvss4_privileges_required: Optional[Cvss4PrivilegesRequired] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['privilegesRequired'], 'domain_of': ['CvssV4_0']} })
    cvss4_user_interaction: Optional[Cvss4UserInteraction] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['userInteraction'], 'domain_of': ['CvssV4_0']} })
    cvss4_vuln_confidentiality_impact: Optional[Cvss4VulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['vulnConfidentialityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_vuln_integrity_impact: Optional[Cvss4VulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['vulnIntegrityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_vuln_availability_impact: Optional[Cvss4VulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['vulnAvailabilityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_sub_confidentiality_impact: Optional[Cvss4SubCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['subConfidentialityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_sub_integrity_impact: Optional[Cvss4SubCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['subIntegrityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_sub_availability_impact: Optional[Cvss4SubCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['subAvailabilityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_exploit_maturity: Optional[Cvss4ExploitMaturity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['exploitMaturity'], 'domain_of': ['CvssV4_0']} })
    cvss4_confidentiality_requirement: Optional[Cvss4CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['confidentialityRequirement'], 'domain_of': ['CvssV4_0']} })
    cvss4_integrity_requirement: Optional[Cvss4CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['integrityRequirement'], 'domain_of': ['CvssV4_0']} })
    cvss4_availability_requirement: Optional[Cvss4CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['availabilityRequirement'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_attack_vector: Optional[Cvss4ModifiedAttackVector] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAttackVector'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_attack_complexity: Optional[Cvss4ModifiedAttackComplexity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAttackComplexity'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_attack_requirements: Optional[Cvss4ModifiedAttackRequirements] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAttackRequirements'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_privileges_required: Optional[Cvss4ModifiedPrivilegesRequired] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedPrivilegesRequired'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_user_interaction: Optional[Cvss4ModifiedUserInteraction] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedUserInteraction'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_vuln_confidentiality_impact: Optional[Cvss4ModifiedVulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedVulnConfidentialityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_vuln_integrity_impact: Optional[Cvss4ModifiedVulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedVulnIntegrityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_vuln_availability_impact: Optional[Cvss4ModifiedVulnCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedVulnAvailabilityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_sub_confidentiality_impact: Optional[Cvss4ModifiedSubC] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedSubConfidentialityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_sub_integrity_impact: Optional[Cvss4ModifiedSubIa] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedSubIntegrityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_modified_sub_availability_impact: Optional[Cvss4ModifiedSubIa] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedSubAvailabilityImpact'], 'domain_of': ['CvssV4_0']} })
    cvss4_safety: Optional[Cvss4Safety] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['Safety'], 'domain_of': ['CvssV4_0']} })
    cvss4_automatable: Optional[Cvss4Automatable] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['Automatable'], 'domain_of': ['CvssV4_0']} })
    cvss4_recovery: Optional[Cvss4Recovery] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['Recovery'], 'domain_of': ['CvssV4_0']} })
    cvss4_value_density: Optional[Cvss4ValueDensity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['valueDensity'], 'domain_of': ['CvssV4_0']} })
    cvss4_vulnerability_response_effort: Optional[Cvss4VulnerabilityResponseEffort] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['vulnerabilityResponseEffort'], 'domain_of': ['CvssV4_0']} })
    cvss4_provider_urgency: Optional[Cvss4ProviderUrgency] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['providerUrgency'], 'domain_of': ['CvssV4_0']} })

    @field_validator('cvss4_vector_string')
    def pattern_cvss4_vector_string(cls, v):
        pattern=re.compile(r"^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cvss4_vector_string format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cvss4_vector_string format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV3(ConfiguredBaseModel):
    """
    CVSS version 3.x scoring object covering both CVSS 3.0 and CVSS 3.1. The two versions share an identical metric model; the 3.1 spec was a clarification, not a structural change. The cvss3_version slot distinguishes between them. Requires version ('3.0' or '3.1'), vectorString, baseScore, and baseSeverity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'in_subset': ['cvss_metrics'],
         'narrow_mappings': ['nvd:CVSSMetric'],
         'slot_usage': {'cvss3_base_score': {'name': 'cvss3_base_score',
                                             'required': True},
                        'cvss3_base_severity': {'name': 'cvss3_base_severity',
                                                'required': True},
                        'cvss3_vector_string': {'name': 'cvss3_vector_string',
                                                'required': True},
                        'cvss3_version': {'name': 'cvss3_version', 'required': True}}})

    cvss3_version: CvssV3Version = Field(default=..., description="""CVSS version identifier ('3.0' or '3.1') within a CvssV3 object.""", json_schema_extra = { "linkml_meta": {'aliases': ['version'], 'domain_of': ['CvssV3']} })
    cvss3_vector_string: str = Field(default=..., description="""CVSS 3.x vector string encoding all metric values. CVSS 3.1 strings begin with 'CVSS:3.1/'; CVSS 3.0 strings begin with 'CVSS:3.0/'.""", json_schema_extra = { "linkml_meta": {'aliases': ['vectorString'], 'domain_of': ['CvssV3']} })
    cvss3_attack_vector: Optional[Cvss3AttackVector] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['attackVector'], 'domain_of': ['CvssV3']} })
    cvss3_attack_complexity: Optional[Cvss3AttackComplexity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['attackComplexity'], 'domain_of': ['CvssV3']} })
    cvss3_privileges_required: Optional[Cvss3PrivilegesRequired] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['privilegesRequired'], 'domain_of': ['CvssV3']} })
    cvss3_user_interaction: Optional[Cvss3UserInteraction] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['userInteraction'], 'domain_of': ['CvssV3']} })
    cvss3_scope: Optional[Cvss3Scope] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['scope'], 'domain_of': ['CvssV3']} })
    cvss3_confidentiality_impact: Optional[Cvss3Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['confidentialityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_integrity_impact: Optional[Cvss3Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['integrityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_availability_impact: Optional[Cvss3Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['availabilityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_base_score: float = Field(default=..., description="""CVSS 3.x base score (0.0 – 10.0 in 0.1 increments).""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['baseScore'], 'domain_of': ['CvssV3']} })
    cvss3_base_severity: Cvss3Severity = Field(default=..., json_schema_extra = { "linkml_meta": {'aliases': ['baseSeverity'], 'domain_of': ['CvssV3']} })
    cvss3_exploit_code_maturity: Optional[Cvss3ExploitCodeMaturity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['exploitCodeMaturity'], 'domain_of': ['CvssV3']} })
    cvss3_remediation_level: Optional[Cvss3RemediationLevel] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['remediationLevel'], 'domain_of': ['CvssV3']} })
    cvss3_report_confidence: Optional[Cvss3Confidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['reportConfidence'], 'domain_of': ['CvssV3']} })
    cvss3_temporal_score: Optional[float] = Field(default=None, description="""CVSS 3.x temporal score.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['temporalScore'], 'domain_of': ['CvssV3']} })
    cvss3_temporal_severity: Optional[Cvss3Severity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['temporalSeverity'], 'domain_of': ['CvssV3']} })
    cvss3_confidentiality_requirement: Optional[Cvss3CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['confidentialityRequirement'], 'domain_of': ['CvssV3']} })
    cvss3_integrity_requirement: Optional[Cvss3CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['integrityRequirement'], 'domain_of': ['CvssV3']} })
    cvss3_availability_requirement: Optional[Cvss3CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['availabilityRequirement'], 'domain_of': ['CvssV3']} })
    cvss3_modified_attack_vector: Optional[Cvss3ModifiedAttackVector] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAttackVector'], 'domain_of': ['CvssV3']} })
    cvss3_modified_attack_complexity: Optional[Cvss3ModifiedAttackComplexity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAttackComplexity'], 'domain_of': ['CvssV3']} })
    cvss3_modified_privileges_required: Optional[Cvss3ModifiedPrivilegesRequired] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedPrivilegesRequired'], 'domain_of': ['CvssV3']} })
    cvss3_modified_user_interaction: Optional[Cvss3ModifiedUserInteraction] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedUserInteraction'], 'domain_of': ['CvssV3']} })
    cvss3_modified_scope: Optional[Cvss3ModifiedScope] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedScope'], 'domain_of': ['CvssV3']} })
    cvss3_modified_confidentiality_impact: Optional[Cvss3ModifiedCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedConfidentialityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_modified_integrity_impact: Optional[Cvss3ModifiedCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedIntegrityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_modified_availability_impact: Optional[Cvss3ModifiedCia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['modifiedAvailabilityImpact'], 'domain_of': ['CvssV3']} })
    cvss3_environmental_score: Optional[float] = Field(default=None, description="""CVSS 3.x environmental score.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['environmentalScore'], 'domain_of': ['CvssV3']} })
    cvss3_environmental_severity: Optional[Cvss3Severity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['environmentalSeverity'], 'domain_of': ['CvssV3']} })


class CvssV20(ConfiguredBaseModel):
    """
    CVSS version 2.0 scoring object. Requires version ('2.0'), vectorString, and baseScore.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'in_subset': ['cvss_metrics'],
         'narrow_mappings': ['nvd:CVSSMetric'],
         'slot_usage': {'cvss2_base_score': {'name': 'cvss2_base_score',
                                             'required': True},
                        'cvss2_vector_string': {'name': 'cvss2_vector_string',
                                                'required': True},
                        'cvss2_version': {'ifabsent': 'string(2.0)',
                                          'name': 'cvss2_version',
                                          'required': True}}})

    cvss2_version: str = Field(default="2.0", description="""CVSS version identifier. Must be '2.0' for CVSS v2.0 objects.""", json_schema_extra = { "linkml_meta": {'aliases': ['version'], 'domain_of': ['CvssV2_0'], 'ifabsent': 'string(2.0)'} })
    cvss2_vector_string: str = Field(default=..., description="""CVSS 2.0 vector string encoding all base, temporal, and environmental metrics.""", json_schema_extra = { "linkml_meta": {'aliases': ['vectorString'], 'domain_of': ['CvssV2_0']} })
    cvss2_access_vector: Optional[Cvss2AccessVector] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['accessVector'], 'domain_of': ['CvssV2_0']} })
    cvss2_access_complexity: Optional[Cvss2AccessComplexity] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['accessComplexity'], 'domain_of': ['CvssV2_0']} })
    cvss2_authentication: Optional[Cvss2Authentication] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['authentication'], 'domain_of': ['CvssV2_0']} })
    cvss2_confidentiality_impact: Optional[Cvss2Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['confidentialityImpact'], 'domain_of': ['CvssV2_0']} })
    cvss2_integrity_impact: Optional[Cvss2Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['integrityImpact'], 'domain_of': ['CvssV2_0']} })
    cvss2_availability_impact: Optional[Cvss2Cia] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['availabilityImpact'], 'domain_of': ['CvssV2_0']} })
    cvss2_base_score: float = Field(default=..., description="""CVSS 2.0 base score (0.0 – 10.0).""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['baseScore'], 'domain_of': ['CvssV2_0']} })
    cvss2_exploitability: Optional[Cvss2Exploitability] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['exploitability'], 'domain_of': ['CvssV2_0']} })
    cvss2_remediation_level: Optional[Cvss2RemediationLevel] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['remediationLevel'], 'domain_of': ['CvssV2_0']} })
    cvss2_report_confidence: Optional[Cvss2ReportConfidence] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['reportConfidence'], 'domain_of': ['CvssV2_0']} })
    cvss2_temporal_score: Optional[float] = Field(default=None, description="""CVSS 2.0 temporal score.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['temporalScore'], 'domain_of': ['CvssV2_0']} })
    cvss2_collateral_damage_potential: Optional[Cvss2CollateralDamagePotential] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['collateralDamagePotential'], 'domain_of': ['CvssV2_0']} })
    cvss2_target_distribution: Optional[Cvss2TargetDistribution] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['targetDistribution'], 'domain_of': ['CvssV2_0']} })
    cvss2_confidentiality_requirement: Optional[Cvss2CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['confidentialityRequirement'], 'domain_of': ['CvssV2_0']} })
    cvss2_integrity_requirement: Optional[Cvss2CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['integrityRequirement'], 'domain_of': ['CvssV2_0']} })
    cvss2_availability_requirement: Optional[Cvss2CiaRequirement] = Field(default=None, json_schema_extra = { "linkml_meta": {'aliases': ['availabilityRequirement'], 'domain_of': ['CvssV2_0']} })
    cvss2_environmental_score: Optional[float] = Field(default=None, description="""CVSS 2.0 environmental score.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'aliases': ['environmentalScore'], 'domain_of': ['CvssV2_0']} })

    @field_validator('cvss2_vector_string')
    def pattern_cvss2_vector_string(cls, v):
        pattern=re.compile(r"^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cvss2_vector_string format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cvss2_vector_string format: {v}"
            raise ValueError(err_msg)
        return v


class OtherMetric(ConfiguredBaseModel):
    """
    A non-standard impact description in a custom format. May be a prose description or an arbitrary JSON-compatible object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'other_metric_content': {'name': 'other_metric_content',
                                                 'required': True},
                        'other_metric_type': {'name': 'other_metric_type',
                                              'required': True}}})

    other_metric_type: str = Field(default=..., description="""Name of the non-standard impact metrics format used.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['OtherMetric']} })
    other_metric_content: Any = Field(default=..., description="""Arbitrary JSON-compatible object (or prose string) containing non-standard metric data not covered by the CVSS formats. Upstream JSON Schema defines this as 'type: object, minProperties: 1'; range: Any allows any value.""", json_schema_extra = { "linkml_meta": {'aliases': ['content'], 'domain_of': ['OtherMetric']} })


class TimelineEntry(ConfiguredBaseModel):
    """
    A timeline event recording a significant event about the vulnerability or changes to the CVE Record. Requires time, lang, and value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'event_time': {'name': 'event_time', 'required': True},
                        'event_value': {'name': 'event_value', 'required': True},
                        'lang': {'name': 'lang', 'required': True}}})

    event_time: str = Field(default=..., description="""Timestamp representing when the event in the timeline occurred. Format is RFC3339 / ISO8601 with optional timezone.""", json_schema_extra = { "linkml_meta": {'aliases': ['time'], 'domain_of': ['TimelineEntry']} })
    lang: str = Field(default="en", description="""BCP 47 language code indicating the language of accompanying text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultiLangDescription',
                       'ProblemTypeDescription',
                       'MetricScenario',
                       'TimelineEntry',
                       'CreditEntry'],
         'ifabsent': 'string(en)'} })
    event_value: str = Field(default=..., description="""A summary of the timeline event (up to 4096 characters).""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TimelineEntry']} })


class CreditEntry(ConfiguredBaseModel):
    """
    A credit acknowledging a specific person, organization, or tool for work related to the research, discovery, remediation, or coordination of the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'credit_value': {'name': 'credit_value', 'required': True},
                        'lang': {'name': 'lang', 'required': True}}})

    lang: str = Field(default="en", description="""BCP 47 language code indicating the language of accompanying text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MultiLangDescription',
                       'ProblemTypeDescription',
                       'MetricScenario',
                       'TimelineEntry',
                       'CreditEntry'],
         'ifabsent': 'string(en)'} })
    credit_value: str = Field(default=..., description="""The name or description of the credited party (up to 4096 characters).""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['CreditEntry']} })
    credit_user: Optional[str] = Field(default=None, description="""UUID of the user being credited, if present in the CVE User Registry. This UUID can be used to lookup the user record in the user registry service.""", json_schema_extra = { "linkml_meta": {'aliases': ['user'], 'domain_of': ['CreditEntry']} })
    credit_type: Optional[CreditType] = Field(default=CreditType.finder, description="""Type or role of the entity being credited.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['CreditEntry'],
         'ifabsent': 'CreditType(finder)'} })


class SourceInformation(ConfiguredBaseModel):
    """
    Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. This is an open object — at least one property must be present.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve'})

    source_defects: Optional[list[str]] = Field(default=None, description="""Bug tracking system IDs (e.g., JIRA ticket IDs) related to the vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['defects'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['SourceInformation']} })
    source_advisory: Optional[str] = Field(default=None, description="""Advisory identifier associated with the vulnerability discovery.""", json_schema_extra = { "linkml_meta": {'aliases': ['advisory'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['SourceInformation']} })
    source_discovery: Optional[str] = Field(default=None, description="""How the vulnerability was discovered (e.g., INTERNAL, EXTERNAL, USER).""", json_schema_extra = { "linkml_meta": {'aliases': ['discovery'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['SourceInformation']} })


class TaxonomyMapping(ConfiguredBaseModel):
    """
    A taxonomy mapping identifying the taxonomy by name and version, along with a list of relations relevant to the CVE (e.g., ATT&CK, D3FEND, CWE).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['cwe:TaxonomyMapping'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'taxonomy_name': {'name': 'taxonomy_name', 'required': True},
                        'taxonomy_relations': {'name': 'taxonomy_relations',
                                               'required': True}}})

    taxonomy_name: str = Field(default=..., description="""The name of the taxonomy (e.g., ATT&CK, D3FEND, CWE, CVSS).""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyName'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TaxonomyMapping']} })
    taxonomy_version: Optional[str] = Field(default=None, description="""The version of the taxonomy the identifiers come from.""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyVersion'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TaxonomyMapping']} })
    taxonomy_relations: list[TaxonomyRelation] = Field(default=..., description="""List of relationships to the taxonomy for this vulnerability.""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyRelations'], 'domain_of': ['TaxonomyMapping']} })


class TaxonomyRelation(ConfiguredBaseModel):
    """
    A relationship between a taxonomy item and a CVE or another taxonomy item. Provides subject (taxonomyId), predicate (relationshipName), and object (relationshipValue).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:Relationship'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'relationship_name': {'name': 'relationship_name',
                                              'required': True},
                        'relationship_value': {'name': 'relationship_value',
                                               'required': True},
                        'taxonomy_id': {'name': 'taxonomy_id', 'required': True}}})

    taxonomy_id: str = Field(default=..., description="""Identifier of the item in the taxonomy. Used as the subject of the relationship.""", json_schema_extra = { "linkml_meta": {'aliases': ['taxonomyId'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TaxonomyRelation']} })
    relationship_name: str = Field(default=..., description="""A description of the relationship between the taxonomy item and the CVE.""", json_schema_extra = { "linkml_meta": {'aliases': ['relationshipName'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 128},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TaxonomyRelation']} })
    relationship_value: str = Field(default=..., description="""The target of the relationship. Can be the CVE ID or another taxonomy identifier.""", json_schema_extra = { "linkml_meta": {'aliases': ['relationshipValue'],
         'annotations': {'max_length': {'tag': 'max_length', 'value': 4096},
                         'min_length': {'tag': 'min_length', 'value': 1}},
         'domain_of': ['TaxonomyRelation']} })


class CpeApplicabilityElement(ConfiguredBaseModel):
    """
    Affected products defined using an implementation of the CPE Applicability Language. An operator property allows AND or OR logic between CPEs or combinations of CPEs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:CPEConfiguration'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'cpe_nodes': {'name': 'cpe_nodes', 'required': True}}})

    cpe_operator: Optional[CpeOperator] = Field(default=None, description="""Logical operator (AND/OR) used between CPE criteria in this node.""", json_schema_extra = { "linkml_meta": {'aliases': ['operator'], 'domain_of': ['CpeApplicabilityElement', 'CpeNode']} })
    cpe_negate: Optional[bool] = Field(default=None, description="""If true, negates the applicability of this element.""", json_schema_extra = { "linkml_meta": {'aliases': ['negate'], 'domain_of': ['CpeApplicabilityElement', 'CpeNode']} })
    cpe_nodes: list[CpeNode] = Field(default=..., description="""Array of CPE configuration nodes.""", json_schema_extra = { "linkml_meta": {'aliases': ['nodes'], 'domain_of': ['CpeApplicabilityElement']} })


class CpeNode(ConfiguredBaseModel):
    """
    Defines a CPE configuration node in an applicability statement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'cpe_match_criteria': {'name': 'cpe_match_criteria',
                                               'required': True},
                        'cpe_operator': {'name': 'cpe_operator', 'required': True}}})

    cpe_operator: CpeOperator = Field(default=..., description="""Logical operator (AND/OR) used between CPE criteria in this node.""", json_schema_extra = { "linkml_meta": {'aliases': ['operator'], 'domain_of': ['CpeApplicabilityElement', 'CpeNode']} })
    cpe_negate: Optional[bool] = Field(default=None, description="""If true, negates the applicability of this element.""", json_schema_extra = { "linkml_meta": {'aliases': ['negate'], 'domain_of': ['CpeApplicabilityElement', 'CpeNode']} })
    cpe_match_criteria: list[CpeMatch] = Field(default=..., description="""Array of CPE match criteria within this node.""", json_schema_extra = { "linkml_meta": {'aliases': ['cpeMatch'], 'domain_of': ['CpeNode']} })


class CpeMatch(ConfiguredBaseModel):
    """
    CPE match string or range within a CPE applicability node.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['nvd:CPEMatch'],
         'from_schema': 'https://w3id.org/lmodel/cve',
         'slot_usage': {'cpe_criteria': {'name': 'cpe_criteria', 'required': True},
                        'cpe_vulnerable': {'name': 'cpe_vulnerable', 'required': True}}})

    cpe_vulnerable: bool = Field(default=..., description="""Whether this CPE match describes a vulnerable configuration.""", json_schema_extra = { "linkml_meta": {'aliases': ['vulnerable'], 'domain_of': ['CpeMatch']} })
    cpe_criteria: str = Field(default=..., description="""CPE 2.3 formatted name match string or match criteria.""", json_schema_extra = { "linkml_meta": {'aliases': ['criteria'], 'domain_of': ['CpeMatch']} })
    match_criteria_id: Optional[str] = Field(default=None, description="""UUID identifying the CPE match criteria set.""", json_schema_extra = { "linkml_meta": {'aliases': ['matchCriteriaId'], 'domain_of': ['CpeMatch']} })
    version_start_excluding: Optional[str] = Field(default=None, description="""The start of a version range, exclusive (versions strictly greater than this).""", json_schema_extra = { "linkml_meta": {'aliases': ['versionStartExcluding'], 'domain_of': ['CpeMatch']} })
    version_start_including: Optional[str] = Field(default=None, description="""The start of a version range, inclusive (versions greater than or equal to this).""", json_schema_extra = { "linkml_meta": {'aliases': ['versionStartIncluding'], 'domain_of': ['CpeMatch']} })
    version_end_excluding: Optional[str] = Field(default=None, description="""The end of a version range, exclusive (versions strictly less than this).""", json_schema_extra = { "linkml_meta": {'aliases': ['versionEndExcluding'], 'domain_of': ['CpeMatch']} })
    version_end_including: Optional[str] = Field(default=None, description="""The end of a version range, inclusive (versions less than or equal to this).""", json_schema_extra = { "linkml_meta": {'aliases': ['versionEndIncluding'], 'domain_of': ['CpeMatch']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Vulnerability.model_rebuild()
Product.model_rebuild()
Reference.model_rebuild()
Weakness.model_rebuild()
Impact.model_rebuild()
Configuration.model_rebuild()
CVERecord.model_rebuild()
CveMetadata.model_rebuild()
CveMetadataPublished.model_rebuild()
CveMetadataRejected.model_rebuild()
Containers.model_rebuild()
ProviderMetadata.model_rebuild()
CnaContainer.model_rebuild()
CnaPublishedContainer.model_rebuild()
CnaRejectedContainer.model_rebuild()
AdpContainer.model_rebuild()
AffectedProduct.model_rebuild()
ProgramRoutine.model_rebuild()
VersionEntry.model_rebuild()
VersionChange.model_rebuild()
MultiLangDescription.model_rebuild()
SupportingMedia.model_rebuild()
ProblemType.model_rebuild()
ProblemTypeDescription.model_rebuild()
CveReference.model_rebuild()
ImpactEntry.model_rebuild()
MetricEntry.model_rebuild()
MetricScenario.model_rebuild()
CvssV40.model_rebuild()
CvssV3.model_rebuild()
CvssV20.model_rebuild()
OtherMetric.model_rebuild()
TimelineEntry.model_rebuild()
CreditEntry.model_rebuild()
SourceInformation.model_rebuild()
TaxonomyMapping.model_rebuild()
TaxonomyRelation.model_rebuild()
CpeApplicabilityElement.model_rebuild()
CpeNode.model_rebuild()
CpeMatch.model_rebuild()
