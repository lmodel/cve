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


metamodel_version = "1.12.0"
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


linkml_meta = LinkMLMeta({'annotations': {'upstream_commit': {'tag': 'upstream_commit',
                                         'value': '5533f6038cc0434e544e69240c704906d591de46'},
                     'upstream_licence': {'tag': 'upstream_licence',
                                          'value': 'CC0-1.0'},
                     'upstream_published': {'tag': 'upstream_published',
                                            'value': '2025-10-29'}},
     'comments': ['The version is the edition of the format that the schema '
                  "renders. upstream/ holds that edition's files unchanged, "
                  'tests/test_coverage.py holds the schema to them, and '
                  'scripts/check_upstream_release.py reports when the edition '
                  'moves.'],
     'default_prefix': 'cve',
     'default_range': 'string',
     'description': 'A LinkML model of the CVE Record Format, in which the CVE '
                    'Program publishes each vulnerability record, with its CVSS '
                    "scores. It keeps the format's own keys and values, so a real "
                    'record validates unchanged.',
     'id': 'https://w3id.org/lmodel/cve',
     'imports': ['linkml:types', './cve_cvss', './cve_record'],
     'license': 'Apache-2.0',
     'name': 'cve',
     'prefixes': {'cve': {'prefix_prefix': 'cve',
                          'prefix_reference': 'https://w3id.org/lmodel/cve/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'see_also': ['https://lmodel.github.io/cve', 'https://www.cve.org/'],
     'source': 'https://github.com/CVEProject/cve-schema/blob/v5.2.0/schema/CVE_Record_Format.json',
     'source_file': 'src/cve/schema/cve.yaml',
     'title': 'Common Vulnerabilities and Exposures (CVE) Record Format'} )

class CvssSeverity(str, Enum):
    """
    A CVSS rating in words.
    """
    NONE = "NONE"
    """
    No severity at all, for a score of 0.
    """
    LOW = "LOW"
    """
    The lowest rating above none.
    """
    MEDIUM = "MEDIUM"
    """
    The middle rating.
    """
    HIGH = "HIGH"
    """
    The rating below critical.
    """
    CRITICAL = "CRITICAL"
    """
    The highest rating.
    """


class CvssV2AccessVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 2.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from the same local network segment.
    """
    LOCAL = "LOCAL"
    """
    Only with an account on the system or hands on it.
    """


class CvssV2AccessComplexity(str, Enum):
    """
    How hard the flaw is to use, in CVSS 2.0's terms.
    """
    HIGH = "HIGH"
    """
    Only under unusual, hard-to-arrange conditions.
    """
    MEDIUM = "MEDIUM"
    """
    Under conditions that take some arranging.
    """
    LOW = "LOW"
    """
    With no special conditions.
    """


class CvssV2Authentication(str, Enum):
    """
    How many logins an attacker needs, in CVSS 2.0's terms.
    """
    MULTIPLE = "MULTIPLE"
    """
    More than one login.
    """
    SINGLE = "SINGLE"
    """
    One login.
    """
    NONE = "NONE"
    """
    No login at all.
    """


class CvssV2Impact(str, Enum):
    """
    How much of one security property an attack could cost, in CVSS 2.0's terms.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    PARTIAL = "PARTIAL"
    """
    Some is lost, and the attacker cannot choose all of it.
    """
    COMPLETE = "COMPLETE"
    """
    All of it is lost.
    """


class CvssExploitCodeMaturity(str, Enum):
    """
    How far working attack code has come.
    """
    UNPROVEN = "UNPROVEN"
    """
    No attack code is known, or the attack is only theory.
    """
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    """
    A demonstration exists that needs skilled work to use.
    """
    FUNCTIONAL = "FUNCTIONAL"
    """
    Working attack code exists for most situations.
    """
    HIGH = "HIGH"
    """
    Attack code is reliable and widely available, or no code is needed.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssRemediationLevel(str, Enum):
    """
    What kind of fix is available.
    """
    OFFICIAL_FIX = "OFFICIAL_FIX"
    """
    The vendor offers a complete fix.
    """
    TEMPORARY_FIX = "TEMPORARY_FIX"
    """
    The vendor offers a stopgap for now.
    """
    WORKAROUND = "WORKAROUND"
    """
    Others offer a way round the flaw that is not from the vendor.
    """
    UNAVAILABLE = "UNAVAILABLE"
    """
    No fix exists, or it cannot be applied.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2ReportConfidence(str, Enum):
    """
    How far the flaw has been confirmed, in CVSS 2.0's terms.
    """
    UNCONFIRMED = "UNCONFIRMED"
    """
    A single report or conflicting reports that nobody has checked.
    """
    UNCORROBORATED = "UNCORROBORATED"
    """
    Several unofficial sources agree, with some doubt remaining.
    """
    CONFIRMED = "CONFIRMED"
    """
    The vendor accepts it, or a working attack shows it.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2CollateralDamagePotential(str, Enum):
    """
    How much loss could follow beyond the system itself.
    """
    NONE = "NONE"
    """
    No such loss.
    """
    LOW = "LOW"
    """
    Slight loss.
    """
    LOW_MEDIUM = "LOW_MEDIUM"
    """
    Moderate loss.
    """
    MEDIUM_HIGH = "MEDIUM_HIGH"
    """
    Significant loss.
    """
    HIGH = "HIGH"
    """
    Catastrophic loss.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2TargetDistribution(str, Enum):
    """
    How much of the environment the flaw exposes.
    """
    NONE = "NONE"
    """
    No systems at all, or only in a lab.
    """
    LOW = "LOW"
    """
    Up to about a quarter of systems.
    """
    MEDIUM = "MEDIUM"
    """
    About a quarter to three quarters of systems.
    """
    HIGH = "HIGH"
    """
    More than about three quarters of systems.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssRequirement(str, Enum):
    """
    How much one security property matters to the scorer.
    """
    LOW = "LOW"
    """
    A loss would have limited effect.
    """
    MEDIUM = "MEDIUM"
    """
    A loss would have serious effect.
    """
    HIGH = "HIGH"
    """
    A loss would have catastrophic effect.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV3AttackVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 3's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from a logically nearby network.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """


class CvssV3ModifiedAttackVector(str, Enum):
    """
    The attack vector as the scorer's environment changes it, in CVSS 3's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from a logically nearby network.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssAttackComplexity(str, Enum):
    """
    How much is outside the attacker's control.
    """
    HIGH = "HIGH"
    """
    Success depends on conditions the attacker must overcome or wait for.
    """
    LOW = "LOW"
    """
    The attacker can succeed again and again with no special effort.
    """


class CvssModifiedAttackComplexity(str, Enum):
    """
    The attack complexity as the scorer's environment changes it.
    """
    HIGH = "HIGH"
    """
    Success depends on conditions the attacker must overcome or wait for.
    """
    LOW = "LOW"
    """
    The attacker can succeed again and again with no special effort.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssPrivilegesRequired(str, Enum):
    """
    What access an attacker needs beforehand.
    """
    HIGH = "HIGH"
    """
    Administrator-level access.
    """
    LOW = "LOW"
    """
    Ordinary user access.
    """
    NONE = "NONE"
    """
    No access at all.
    """


class CvssModifiedPrivilegesRequired(str, Enum):
    """
    The access needed as the scorer's environment changes it.
    """
    HIGH = "HIGH"
    """
    Administrator-level access.
    """
    LOW = "LOW"
    """
    Ordinary user access.
    """
    NONE = "NONE"
    """
    No access at all.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3UserInteraction(str, Enum):
    """
    Whether someone else has to take part, in CVSS 3's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    REQUIRED = "REQUIRED"
    """
    Someone other than the attacker has to do something.
    """


class CvssV3ModifiedUserInteraction(str, Enum):
    """
    The user interaction as the scorer's environment changes it, in CVSS 3's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    REQUIRED = "REQUIRED"
    """
    Someone other than the attacker has to do something.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3Scope(str, Enum):
    """
    Whether an attack can reach beyond the flawed component.
    """
    UNCHANGED = "UNCHANGED"
    """
    The harm stays within the same security authority.
    """
    CHANGED = "CHANGED"
    """
    The harm can reach something under another security authority.
    """


class CvssV3ModifiedScope(str, Enum):
    """
    The scope as the scorer's environment changes it.
    """
    UNCHANGED = "UNCHANGED"
    """
    The harm stays within the same security authority.
    """
    CHANGED = "CHANGED"
    """
    The harm can reach something under another security authority.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssImpact(str, Enum):
    """
    How much of one security property an attack could cost.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """


class CvssModifiedImpact(str, Enum):
    """
    The impact on one security property as the scorer's environment changes it.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3ReportConfidence(str, Enum):
    """
    How far the flaw has been confirmed, in CVSS 3's terms.
    """
    UNKNOWN = "UNKNOWN"
    """
    Reports say something is wrong, but the cause is not clear.
    """
    REASONABLE = "REASONABLE"
    """
    Solid details exist, without full confirmation of the cause.
    """
    CONFIRMED = "CONFIRMED"
    """
    The flaw is shown beyond doubt, or the vendor accepts it.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV4AttackVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 4.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT = "ADJACENT"
    """
    Only from something logically or physically nearby.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """


class CvssV4ModifiedAttackVector(str, Enum):
    """
    The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT = "ADJACENT"
    """
    Only from something logically or physically nearby.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4AttackRequirements(str, Enum):
    """
    Whether the attack needs conditions in the target beyond the attacker's control.
    """
    NONE = "NONE"
    """
    The attack works whatever the target's state.
    """
    PRESENT = "PRESENT"
    """
    The attack works only when the target is in a certain state.
    """


class CvssV4ModifiedAttackRequirements(str, Enum):
    """
    The attack requirements as the scorer's environment changes them.
    """
    NONE = "NONE"
    """
    The attack works whatever the target's state.
    """
    PRESENT = "PRESENT"
    """
    The attack works only when the target is in a certain state.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4UserInteraction(str, Enum):
    """
    Whether someone else has to take part, in CVSS 4.0's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    PASSIVE = "PASSIVE"
    """
    Someone has to act only in the ordinary course of their work.
    """
    ACTIVE = "ACTIVE"
    """
    Someone has to take a deliberate step.
    """


class CvssV4ModifiedUserInteraction(str, Enum):
    """
    The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    PASSIVE = "PASSIVE"
    """
    Someone has to act only in the ordinary course of their work.
    """
    ACTIVE = "ACTIVE"
    """
    Someone has to take a deliberate step.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4ModifiedSubsequentImpact(str, Enum):
    """
    The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """
    SAFETY = "SAFETY"
    """
    The loss could injure people.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4ExploitMaturity(str, Enum):
    """
    How much is known about attacks on the flaw.
    """
    UNREPORTED = "UNREPORTED"
    """
    No demonstration or attack has been reported.
    """
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    """
    A demonstration is public, with no reported attack.
    """
    ATTACKED = "ATTACKED"
    """
    Attacks have been reported, or tools for them are public.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the worst case is assumed.
    """


class CvssV4Safety(str, Enum):
    """
    Whether an attack could put people's safety at risk.
    """
    NEGLIGIBLE = "NEGLIGIBLE"
    """
    Any harm to people would be slight at most.
    """
    PRESENT = "PRESENT"
    """
    People could be seriously hurt.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4Automatable(str, Enum):
    """
    Whether every step of an attack could be automated across many targets.
    """
    NO = "NO"
    """
    At least one step resists automation.
    """
    YES = "YES"
    """
    Every step can be automated.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4Recovery(str, Enum):
    """
    How the affected system comes back after an attack.
    """
    AUTOMATIC = "AUTOMATIC"
    """
    The system recovers by itself.
    """
    USER = "USER"
    """
    Someone has to step in and restore it.
    """
    IRRECOVERABLE = "IRRECOVERABLE"
    """
    The system cannot be restored.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ValueDensity(str, Enum):
    """
    How much of a resource one successful attack gains the attacker.
    """
    DIFFUSE = "DIFFUSE"
    """
    Each target holds little, so an attacker must take many.
    """
    CONCENTRATED = "CONCENTRATED"
    """
    A single target holds a lot.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ResponseEffort(str, Enum):
    """
    How much work it takes a consumer to respond to the flaw.
    """
    LOW = "LOW"
    """
    Little work, such as reading advice or a small configuration change.
    """
    MODERATE = "MODERATE"
    """
    Some work, with a noticeable effect on the service.
    """
    HIGH = "HIGH"
    """
    Much work, or a long outage.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ProviderUrgency(str, Enum):
    """
    How urgent the product's supplier says the flaw is, as a colour.
    """
    CLEAR = "CLEAR"
    """
    The supplier sees little or no urgency.
    """
    GREEN = "GREEN"
    """
    The supplier says the flaw can wait for regular work.
    """
    AMBER = "AMBER"
    """
    The supplier says the flaw matters soon.
    """
    RED = "RED"
    """
    The supplier says the flaw is at the highest urgency.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CveDataType(str, Enum):
    """
    The kind of document a CVE record is.
    """
    CVE_RECORD = "CVE_RECORD"
    """
    A document in the CVE Record Format.
    """


class CveRecordState(str, Enum):
    """
    Whether a record is in use.
    """
    PUBLISHED = "PUBLISHED"
    """
    The assigning authority has filled the record in and made it public.
    """
    REJECTED = "REJECTED"
    """
    The identifier and its record are withdrawn from use.
    """


class CvePublishedState(str, Enum):
    """
    The state of a published record.
    """
    PUBLISHED = "PUBLISHED"
    """
    The assigning authority has filled the record in and made it public.
    """


class CveRejectedState(str, Enum):
    """
    The state of a rejected record.
    """
    REJECTED = "REJECTED"
    """
    The identifier and its record are withdrawn from use.
    """


class CveVersionStatus(str, Enum):
    """
    Whether a version is affected.
    """
    affected = "affected"
    """
    The vulnerability is present in this version.
    """
    unaffected = "unaffected"
    """
    The vulnerability is not present in this version.
    """
    unknown = "unknown"
    """
    It is not known whether the vulnerability is present.
    """


class CveCpeOperator(str, Enum):
    """
    How the parts of a CPE statement combine.
    """
    AND = "AND"
    """
    All of the parts must hold.
    """
    OR = "OR"
    """
    At least one of the parts must hold.
    """


class CveCreditType(str, Enum):
    """
    The part a credited person or organisation played.
    """
    finder = "finder"
    """
    Found the vulnerability.
    """
    reporter = "reporter"
    """
    Told the vendor or a CVE Numbering Authority about it.
    """
    analyst = "analyst"
    """
    Checked that it is accurate or how severe it is.
    """
    coordinator = "coordinator"
    """
    Organised the response among those involved.
    """
    remediation_developer = "remediation developer"
    """
    Prepared the code change or plan that addresses it.
    """
    remediation_reviewer = "remediation reviewer"
    """
    Reviewed that change or plan for how well it works.
    """
    remediation_verifier = "remediation verifier"
    """
    Tested the vulnerability or the fix for it.
    """
    tool = "tool"
    """
    A tool used to find or identify it.
    """
    sponsor = "sponsor"
    """
    Supported the work of finding or fixing it.
    """
    other = "other"
    """
    Any other part.
    """


class CveCnaTag(str, Enum):
    """
    A label the assigning authority can put on a record.
    """
    unsupported_when_assigned = "unsupported-when-assigned"
    """
    Everything affected was out of support when the identifier was requested.
    """
    exclusively_hosted_service = "exclusively-hosted-service"
    """
    Everything affected exists only as a hosted service.
    """
    disputed = "disputed"
    """
    Someone disagrees that this is a vulnerability at all.
    """


class CveAdpTag(str, Enum):
    """
    A label an Authorized Data Publisher can put on a record.
    """
    disputed = "disputed"
    """
    Someone disagrees that this is a vulnerability at all.
    """


class CveReferenceTag(str, Enum):
    """
    A label that says what a reference is.
    """
    broken_link = "broken-link"
    """
    The address no longer answers.
    """
    customer_entitlement = "customer-entitlement"
    """
    Only paying customers of the vendor can read it.
    """
    exploit = "exploit"
    """
    It shows how to attack the flaw, or holds working attack code.
    """
    government_resource = "government-resource"
    """
    It comes from a government body.
    """
    issue_tracking = "issue-tracking"
    """
    It is a post in a bug tracker.
    """
    mailing_list = "mailing-list"
    """
    It comes from a mailing list.
    """
    mitigation = "mitigation"
    """
    It says how to reduce the risk when no patch can be applied.
    """
    not_applicable = "not-applicable"
    """
    It has nothing to do with this vulnerability and was linked by mistake.
    """
    patch = "patch"
    """
    It holds an update that fixes the flaw.
    """
    permissions_required = "permissions-required"
    """
    A login blocks the way to it.
    """
    media_coverage = "media-coverage"
    """
    It is a news story or similar report.
    """
    product = "product"
    """
    It identifies the affected product, for naming schemes such as CPE.
    """
    related = "related"
    """
    It concerns a related flaw, not this one.
    """
    release_notes = "release-notes"
    """
    It is a set of release notes.
    """
    signature = "signature"
    """
    It holds a way to detect or block the flaw or attacks on it.
    """
    technical_description = "technical-description"
    """
    It explains the flaw and how it is attacked, in technical depth.
    """
    third_party_advisory = "third-party-advisory"
    """
    It is an advisory from someone other than the vendor.
    """
    vendor_advisory = "vendor-advisory"
    """
    It is an advisory from the vendor.
    """
    vdb_entry = "vdb-entry"
    """
    It is an entry in a vulnerability database.
    """



class CvssSeverityBandsMixin(ConfiguredBaseModel):
    """
    The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/anyOf '
                                                    'imports/cvss/cvss-v3.1.json#/anyOf '
                                                    'imports/cvss/cvss-v4.0.json#/allOf/0/anyOf'}},
         'comments': ['The upstream also rules out a score that is not a multiple of '
                      '0.1, as a list of numbers no LinkML range can state. '
                      'tests/cve_rules.py checks that.'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixin': True,
         'rules': [{'description': 'A base severity of NONE goes with a base score of '
                                   'exactly 0.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 0,
                                                                         'minimum_value': 0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'NONE',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity NONE'},
                   {'description': 'A base severity of LOW goes with a base score from '
                                   '0.1 to 3.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 3.9,
                                                                         'minimum_value': 0.1,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'LOW',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity LOW'},
                   {'description': 'A base severity of MEDIUM goes with a base score '
                                   'from 4.0 to 6.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 6.9,
                                                                         'minimum_value': 4.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'MEDIUM',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity MEDIUM'},
                   {'description': 'A base severity of HIGH goes with a base score '
                                   'from 7.0 to 8.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 8.9,
                                                                         'minimum_value': 7.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'HIGH',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity HIGH'},
                   {'description': 'A base severity of CRITICAL goes with a base score '
                                   'from 9.0 to 10.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 10.0,
                                                                         'minimum_value': 9.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'CRITICAL',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity CRITICAL'}]})

    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin']} })


class CvssV20(ConfiguredBaseModel):
    """
    A score under CVSS version 2.0, which has no severity bands.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS2BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'related_mappings': ['spdx_security:CvssV2VulnAssessmentRelationship'],
         'slot_usage': {'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssV2Impact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssV2Impact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssV2Impact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV2ReportConfidence'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'},
                        'version': {'equals_string': '2.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["2.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40', 'CveProductVersion'],
         'equals_string': '2.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    confidentialityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV2ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    accessVector: Optional[CvssV2AccessVector] = Field(default=None, description="""How far away an attacker can be when using the flaw, in CVSS 2.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/accessVector'}},
         'close_mappings': ['sepses_cvss:accessVector'],
         'domain_of': ['CvssV20']} })
    accessComplexity: Optional[CvssV2AccessComplexity] = Field(default=None, description="""How hard the flaw is to use once the attacker can reach it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/accessComplexity'}},
         'close_mappings': ['sepses_cvss:accessComplexity'],
         'domain_of': ['CvssV20']} })
    authentication: Optional[CvssV2Authentication] = Field(default=None, description="""How many times an attacker must log in before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/authentication'}},
         'close_mappings': ['sepses_cvss:authentication'],
         'domain_of': ['CvssV20']} })
    exploitability: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come, in CVSS 2.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/exploitability'}},
         'domain_of': ['CvssV20']} })
    collateralDamagePotential: Optional[CvssV2CollateralDamagePotential] = Field(default=None, description="""How much loss a successful attack could cause beyond the system itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/collateralDamagePotential'}},
         'domain_of': ['CvssV20']} })
    targetDistribution: Optional[CvssV2TargetDistribution] = Field(default=None, description="""How much of the scorer's environment is exposed to the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/targetDistribution'}},
         'domain_of': ['CvssV20']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV30(CvssSeverityBandsMixin):
    """
    A score under CVSS version 3.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV3AttackVector'},
                        'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssImpact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssImpact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssImpact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'name': 'modifiedAttackVector',
                                                 'range': 'CvssV3ModifiedAttackVector'},
                        'modifiedAvailabilityImpact': {'name': 'modifiedAvailabilityImpact',
                                                       'range': 'CvssModifiedImpact'},
                        'modifiedConfidentialityImpact': {'name': 'modifiedConfidentialityImpact',
                                                          'range': 'CvssModifiedImpact'},
                        'modifiedIntegrityImpact': {'name': 'modifiedIntegrityImpact',
                                                    'range': 'CvssModifiedImpact'},
                        'modifiedPrivilegesRequired': {'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV3ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV3ReportConfidence'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV3UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'},
                        'version': {'equals_string': '3.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["3.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40', 'CveProductVersion'],
         'equals_string': '3.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV3AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV3UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    scope: Optional[CvssV3Scope] = Field(default=None, description="""Whether an attack can reach beyond the component that holds the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/scope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/scope'}},
         'close_mappings': ['sepses_cvss:scope'],
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    exploitCodeMaturity: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/exploitCodeMaturity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/exploitCodeMaturity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV3ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the temporal score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/temporalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackVector: Optional[CvssV3ModifiedAttackVector] = Field(default=None, description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=None, description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=None, description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedUserInteraction: Optional[CvssV3ModifiedUserInteraction] = Field(default=None, description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedScope: Optional[CvssV3ModifiedScope] = Field(default=None, description="""The scope as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedScope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedScope'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The confidentiality impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedConfidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedConfidentialityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The integrity impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedIntegrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedIntegrityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The availability impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAvailabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAvailabilityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    environmentalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the environmental score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/environmentalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV31(CvssSeverityBandsMixin):
    """
    A score under CVSS version 3.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.1.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV3AttackVector'},
                        'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssImpact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssImpact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssImpact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'name': 'modifiedAttackVector',
                                                 'range': 'CvssV3ModifiedAttackVector'},
                        'modifiedAvailabilityImpact': {'name': 'modifiedAvailabilityImpact',
                                                       'range': 'CvssModifiedImpact'},
                        'modifiedConfidentialityImpact': {'name': 'modifiedConfidentialityImpact',
                                                          'range': 'CvssModifiedImpact'},
                        'modifiedIntegrityImpact': {'name': 'modifiedIntegrityImpact',
                                                    'range': 'CvssModifiedImpact'},
                        'modifiedPrivilegesRequired': {'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV3ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV3ReportConfidence'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV3UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'},
                        'version': {'equals_string': '3.1',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["3.1"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40', 'CveProductVersion'],
         'equals_string': '3.1',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV3AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV3UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    scope: Optional[CvssV3Scope] = Field(default=None, description="""Whether an attack can reach beyond the component that holds the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/scope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/scope'}},
         'close_mappings': ['sepses_cvss:scope'],
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    exploitCodeMaturity: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/exploitCodeMaturity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/exploitCodeMaturity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV3ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the temporal score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/temporalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackVector: Optional[CvssV3ModifiedAttackVector] = Field(default=None, description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=None, description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=None, description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedUserInteraction: Optional[CvssV3ModifiedUserInteraction] = Field(default=None, description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedScope: Optional[CvssV3ModifiedScope] = Field(default=None, description="""The scope as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedScope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedScope'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The confidentiality impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedConfidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedConfidentialityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The integrity impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedIntegrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedIntegrityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The availability impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAvailabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAvailabilityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    environmentalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the environmental score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/environmentalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV40(CvssSeverityBandsMixin):
    """
    A score under CVSS version 4.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/'}},
         'broad_mappings': ['sepses_cvss:CVSS'],
         'comments': ["The upstream's rules name threatScore, threatSeverity, "
                      'environmentalScore and environmentalSeverity, but its list of '
                      'properties has none of them and it refuses any other key, so a '
                      'score object cannot carry them and this class has no such '
                      'slots.'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV4VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV4AttackVector'},
                        'availabilityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                    'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                       'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                 'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'ifabsent': 'CvssModifiedAttackComplexity(NOT_DEFINED)',
                                                     'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'ifabsent': 'CvssV4ModifiedAttackVector(NOT_DEFINED)',
                                                 'name': 'modifiedAttackVector',
                                                 'range': 'CvssV4ModifiedAttackVector'},
                        'modifiedPrivilegesRequired': {'ifabsent': 'CvssModifiedPrivilegesRequired(NOT_DEFINED)',
                                                       'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'ifabsent': 'CvssV4ModifiedUserInteraction(NOT_DEFINED)',
                                                    'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV4ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV4UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'},
                        'version': {'equals_string': '4.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["4.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40', 'CveProductVersion'],
         'equals_string': '4.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV4AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV4UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    modifiedAttackVector: Optional[CvssV4ModifiedAttackVector] = Field(default=CvssV4ModifiedAttackVector("NOT_DEFINED"), description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssV4ModifiedAttackVector(NOT_DEFINED)'} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=CvssModifiedAttackComplexity("NOT_DEFINED"), description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssModifiedAttackComplexity(NOT_DEFINED)'} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=CvssModifiedPrivilegesRequired("NOT_DEFINED"), description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssModifiedPrivilegesRequired(NOT_DEFINED)'} })
    modifiedUserInteraction: Optional[CvssV4ModifiedUserInteraction] = Field(default=CvssV4ModifiedUserInteraction("NOT_DEFINED"), description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssV4ModifiedUserInteraction(NOT_DEFINED)'} })
    attackRequirements: Optional[CvssV4AttackRequirements] = Field(default=None, description="""Whether the attack needs conditions in the target that the attacker does not control.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/attackRequirements'}},
         'domain_of': ['CvssV40']} })
    vulnConfidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information in the vulnerable system an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnConfidentialityImpact'}},
         'domain_of': ['CvssV40']} })
    vulnIntegrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change in the vulnerable system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnIntegrityImpact'}},
         'domain_of': ['CvssV40']} })
    vulnAvailabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the vulnerable system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnAvailabilityImpact'}},
         'domain_of': ['CvssV40']} })
    subConfidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information in other, connected systems an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subConfidentialityImpact'}},
         'domain_of': ['CvssV40']} })
    subIntegrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change in other, connected systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subIntegrityImpact'}},
         'domain_of': ['CvssV40']} })
    subAvailabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt other, connected systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subAvailabilityImpact'}},
         'domain_of': ['CvssV40']} })
    exploitMaturity: Optional[CvssV4ExploitMaturity] = Field(default=CvssV4ExploitMaturity("NOT_DEFINED"), description="""How much is known about attacks on this flaw, in CVSS 4.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/exploitMaturity'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ExploitMaturity(NOT_DEFINED)'} })
    modifiedAttackRequirements: Optional[CvssV4ModifiedAttackRequirements] = Field(default=CvssV4ModifiedAttackRequirements("NOT_DEFINED"), description="""The attack requirements as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackRequirements'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedAttackRequirements(NOT_DEFINED)'} })
    modifiedVulnConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The confidentiality impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnConfidentialityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedVulnIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The integrity impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnIntegrityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedVulnAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The availability impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnAvailabilityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedSubConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The confidentiality impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubConfidentialityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedSubIntegrityImpact: Optional[CvssV4ModifiedSubsequentImpact] = Field(default=CvssV4ModifiedSubsequentImpact("NOT_DEFINED"), description="""The integrity impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubIntegrityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedSubsequentImpact(NOT_DEFINED)'} })
    modifiedSubAvailabilityImpact: Optional[CvssV4ModifiedSubsequentImpact] = Field(default=CvssV4ModifiedSubsequentImpact("NOT_DEFINED"), description="""The availability impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubAvailabilityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedSubsequentImpact(NOT_DEFINED)'} })
    Safety: Optional[CvssV4Safety] = Field(default=CvssV4Safety("NOT_DEFINED"), description="""Whether an attack could put people's safety at risk.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Safety'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Safety(NOT_DEFINED)'} })
    Automatable: Optional[CvssV4Automatable] = Field(default=CvssV4Automatable("NOT_DEFINED"), description="""Whether an attacker could automate every step of an attack across many targets.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Automatable'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Automatable(NOT_DEFINED)'} })
    Recovery: Optional[CvssV4Recovery] = Field(default=CvssV4Recovery("NOT_DEFINED"), description="""How the affected system comes back after an attack.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Recovery'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Recovery(NOT_DEFINED)'} })
    valueDensity: Optional[CvssV4ValueDensity] = Field(default=CvssV4ValueDensity("NOT_DEFINED"), description="""Whether one successful attack gains the attacker a little or a lot of a resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/valueDensity'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ValueDensity(NOT_DEFINED)'} })
    vulnerabilityResponseEffort: Optional[CvssV4ResponseEffort] = Field(default=CvssV4ResponseEffort("NOT_DEFINED"), description="""How much work it takes a consumer to respond to the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnerabilityResponseEffort'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ResponseEffort(NOT_DEFINED)'} })
    providerUrgency: Optional[CvssV4ProviderUrgency] = Field(default=CvssV4ProviderUrgency("NOT_DEFINED"), description="""How urgent the product's supplier says the flaw is, as a colour.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/providerUrgency'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ProviderUrgency(NOT_DEFINED)'} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CveRecord(ConfiguredBaseModel):
    """
    A record of one vulnerability under one CVE identifier, in the CVE Program's format.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf'}},
         'close_mappings': ['sepses_cve:CVE',
                            'spdx_security:Vulnerability',
                            'stix:StixVulnerability'],
         'comments': ["Its two kinds are told apart by cveMetadata's state, nested "
                      "inside the record, so LinkML's type designator cannot choose "
                      'between them. A reader picks the class from the state, or '
                      'validates against CveRecordRoot.',
                      'wd:Q631425 is the idea of a vulnerability, which a record '
                      'describes and is not, so that mapping is only related. SEPSES, '
                      'SPDX and STIX each have a class for the description of one '
                      'vulnerability, so those are close.'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'related_mappings': ['wd:Q631425']})

    cveMetadata: CveRecordMetadata = Field(default=..., description="""The facts about the record itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/cveMetadata '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/cveMetadata'}},
         'domain_of': ['CveRecord']} })
    containers: CveContainers = Field(default=..., description="""The vulnerability information, grouped by who provided it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers'}},
         'domain_of': ['CveRecord']} })
    dataType: CveDataType = Field(default=..., description="""The kind of document this is, which is always a CVE record.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataType'}},
         'domain_of': ['CveRecord']} })
    dataVersion: str = Field(default=..., description="""The version of the record format that this record follows.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataVersion'}},
         'comments': ['The upstream gives 5.2.0 as a default, which cannot apply to a '
                      'required key.'],
         'domain_of': ['CveRecord']} })


class CvePublishedRecord(CveRecord):
    """
    A record whose assigning organisation has filled it in and made it public.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'containers': {'name': 'containers',
                                       'range': 'CvePublishedContainers'},
                        'cveMetadata': {'name': 'cveMetadata',
                                        'range': 'CveMetadataPublished'}}})

    cveMetadata: CveMetadataPublished = Field(default=..., description="""The facts about the record itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/cveMetadata '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/cveMetadata'}},
         'domain_of': ['CveRecord']} })
    containers: CvePublishedContainers = Field(default=..., description="""The vulnerability information, grouped by who provided it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers'}},
         'domain_of': ['CveRecord']} })
    dataType: CveDataType = Field(default=..., description="""The kind of document this is, which is always a CVE record.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataType'}},
         'domain_of': ['CveRecord']} })
    dataVersion: str = Field(default=..., description="""The version of the record format that this record follows.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataVersion'}},
         'comments': ['The upstream gives 5.2.0 as a default, which cannot apply to a '
                      'required key.'],
         'domain_of': ['CveRecord']} })


class CveRejectedRecord(CveRecord):
    """
    A record that should no longer be used, kept so that people can see it is invalid.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/1'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'containers': {'name': 'containers',
                                       'range': 'CveRejectedContainers'},
                        'cveMetadata': {'name': 'cveMetadata',
                                        'range': 'CveMetadataRejected'}}})

    cveMetadata: CveMetadataRejected = Field(default=..., description="""The facts about the record itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/cveMetadata '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/cveMetadata'}},
         'domain_of': ['CveRecord']} })
    containers: CveRejectedContainers = Field(default=..., description="""The vulnerability information, grouped by who provided it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers'}},
         'domain_of': ['CveRecord']} })
    dataType: CveDataType = Field(default=..., description="""The kind of document this is, which is always a CVE record.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataType'}},
         'domain_of': ['CveRecord']} })
    dataVersion: str = Field(default=..., description="""The version of the record format that this record follows.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/dataVersion'}},
         'comments': ['The upstream gives 5.2.0 as a default, which cannot apply to a '
                      'required key.'],
         'domain_of': ['CveRecord']} })


class CveRecordMetadata(ConfiguredBaseModel):
    """
    The facts about a record itself, as distinct from the vulnerability it describes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    dateUpdated: Optional[str] = Field(default=None, description="""When the record or container was last updated.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/providerMetadata/properties/dateUpdated'}},
         'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx_security:modifiedTime'],
         'domain_of': ['CveRecordMetadata', 'CveProviderMetadata']} })
    state: CveRecordState = Field(default=..., description="""Whether the record is published or rejected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/state '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/state'}},
         'domain_of': ['CveRecordMetadata']} })
    cveId: str = Field(default=..., description="""The CVE identifier that the record belongs to.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/cveId'}},
         'domain_of': ['CveRecordMetadata'],
         'narrow_mappings': ['dcterms:identifier', 'schema:identifier']} })
    assignerOrgId: str = Field(default=..., description="""The UUID of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerOrgId'}},
         'domain_of': ['CveRecordMetadata']} })
    assignerShortName: Optional[str] = Field(default=None, description="""The short name of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerShortName'}},
         'domain_of': ['CveRecordMetadata']} })
    serial: Optional[int] = Field(default=None, description="""A counter that the system of record raises each time a provider changes the record.""", ge=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/serial'}},
         'domain_of': ['CveRecordMetadata']} })
    dateReserved: Optional[str] = Field(default=None, description="""When the CVE identifier was reserved.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateReserved'}},
         'comments': ['This says nothing about when the flaw was found, reported or '
                      'disclosed.'],
         'domain_of': ['CveRecordMetadata']} })
    datePublished: Optional[str] = Field(default=None, description="""When the record first appeared in the CVE List.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/datePublished'}},
         'close_mappings': ['dcterms:issued',
                            'schema:datePublished',
                            'spdx_security:publishedTime'],
         'domain_of': ['CveRecordMetadata']} })


class CveMetadataPublished(CveRecordMetadata):
    """
    The metadata of a published record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'state': {'name': 'state', 'range': 'CvePublishedState'}}})

    requesterUserId: Optional[str] = Field(default=None, description="""The UUID of the user who asked for the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/requesterUserId'}},
         'domain_of': ['CveMetadataPublished']} })
    dateUpdated: Optional[str] = Field(default=None, description="""When the record or container was last updated.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/providerMetadata/properties/dateUpdated'}},
         'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx_security:modifiedTime'],
         'domain_of': ['CveRecordMetadata', 'CveProviderMetadata']} })
    state: CvePublishedState = Field(default=..., description="""Whether the record is published or rejected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/state '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/state'}},
         'domain_of': ['CveRecordMetadata']} })
    cveId: str = Field(default=..., description="""The CVE identifier that the record belongs to.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/cveId'}},
         'domain_of': ['CveRecordMetadata'],
         'narrow_mappings': ['dcterms:identifier', 'schema:identifier']} })
    assignerOrgId: str = Field(default=..., description="""The UUID of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerOrgId'}},
         'domain_of': ['CveRecordMetadata']} })
    assignerShortName: Optional[str] = Field(default=None, description="""The short name of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerShortName'}},
         'domain_of': ['CveRecordMetadata']} })
    serial: Optional[int] = Field(default=None, description="""A counter that the system of record raises each time a provider changes the record.""", ge=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/serial'}},
         'domain_of': ['CveRecordMetadata']} })
    dateReserved: Optional[str] = Field(default=None, description="""When the CVE identifier was reserved.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateReserved'}},
         'comments': ['This says nothing about when the flaw was found, reported or '
                      'disclosed.'],
         'domain_of': ['CveRecordMetadata']} })
    datePublished: Optional[str] = Field(default=None, description="""When the record first appeared in the CVE List.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/datePublished'}},
         'close_mappings': ['dcterms:issued',
                            'schema:datePublished',
                            'spdx_security:publishedTime'],
         'domain_of': ['CveRecordMetadata']} })


class CveMetadataRejected(CveRecordMetadata):
    """
    The metadata of a rejected record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataRejected'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'state': {'name': 'state', 'range': 'CveRejectedState'}}})

    dateRejected: Optional[str] = Field(default=None, description="""When the CVE identifier was rejected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/dateRejected'}},
         'close_mappings': ['spdx_security:withdrawnTime'],
         'domain_of': ['CveMetadataRejected']} })
    dateUpdated: Optional[str] = Field(default=None, description="""When the record or container was last updated.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/providerMetadata/properties/dateUpdated'}},
         'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx_security:modifiedTime'],
         'domain_of': ['CveRecordMetadata', 'CveProviderMetadata']} })
    state: CveRejectedState = Field(default=..., description="""Whether the record is published or rejected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/state '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/state'}},
         'domain_of': ['CveRecordMetadata']} })
    cveId: str = Field(default=..., description="""The CVE identifier that the record belongs to.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/cveId'}},
         'domain_of': ['CveRecordMetadata'],
         'narrow_mappings': ['dcterms:identifier', 'schema:identifier']} })
    assignerOrgId: str = Field(default=..., description="""The UUID of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerOrgId'}},
         'domain_of': ['CveRecordMetadata']} })
    assignerShortName: Optional[str] = Field(default=None, description="""The short name of the organisation that was given the CVE identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/assignerShortName'}},
         'domain_of': ['CveRecordMetadata']} })
    serial: Optional[int] = Field(default=None, description="""A counter that the system of record raises each time a provider changes the record.""", ge=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/serial'}},
         'domain_of': ['CveRecordMetadata']} })
    dateReserved: Optional[str] = Field(default=None, description="""When the CVE identifier was reserved.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateReserved'}},
         'comments': ['This says nothing about when the flaw was found, reported or '
                      'disclosed.'],
         'domain_of': ['CveRecordMetadata']} })
    datePublished: Optional[str] = Field(default=None, description="""When the record first appeared in the CVE List.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/datePublished'}},
         'close_mappings': ['dcterms:issued',
                            'schema:datePublished',
                            'spdx_security:publishedTime'],
         'domain_of': ['CveRecordMetadata']} })


class CveContainers(ConfiguredBaseModel):
    """
    The sets of vulnerability information in a record, one per providing organisation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    cna: CveCnaContainer = Field(default=..., description="""The container from the authority that assigned the identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers/properties/cna '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers/properties/cna'}},
         'domain_of': ['CveContainers']} })


class CvePublishedContainers(CveContainers):
    """
    The containers of a published record, the assigning organisation's and any others'.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'cna': {'name': 'cna', 'range': 'CveCnaPublishedContainer'}}})

    adp: Optional[list[CveAdpContainer]] = Field(default=None, description="""The containers added by Authorized Data Publishers.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers/properties/adp'}},
         'domain_of': ['CvePublishedContainers'],
         'list_elements_unique': True} })
    cna: CveCnaPublishedContainer = Field(default=..., description="""The container from the authority that assigned the identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers/properties/cna '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers/properties/cna'}},
         'domain_of': ['CveContainers']} })


class CveRejectedContainers(CveContainers):
    """
    The container of a rejected record, which only the assigning organisation provides.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/1/properties/containers'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'cna': {'name': 'cna', 'range': 'CveCnaRejectedContainer'}}})

    cna: CveCnaRejectedContainer = Field(default=..., description="""The container from the authority that assigned the identifier.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/oneOf/0/properties/containers/properties/cna '
                                                    'CVE_Record_Format.json#/oneOf/1/properties/containers/properties/cna'}},
         'domain_of': ['CveContainers']} })


class CveProviderMetadata(ConfiguredBaseModel):
    """
    Who provided a container, and when it was last updated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/providerMetadata'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    dateUpdated: Optional[str] = Field(default=None, description="""When the record or container was last updated.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cveMetadataPublished/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/cveMetadataRejected/properties/dateUpdated '
                                                    'CVE_Record_Format.json#/definitions/providerMetadata/properties/dateUpdated'}},
         'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx_security:modifiedTime'],
         'domain_of': ['CveRecordMetadata', 'CveProviderMetadata']} })
    orgId: str = Field(default=..., description="""The UUID of the organisation that provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/providerMetadata/properties/orgId'}},
         'domain_of': ['CveProviderMetadata']} })
    shortName: Optional[str] = Field(default=None, description="""The short name of the organisation that provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/providerMetadata/properties/shortName'}},
         'domain_of': ['CveProviderMetadata']} })


class CveCnaContainer(ConfiguredBaseModel):
    """
    The container from the CVE Numbering Authority that assigned the identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer '
                                                    'CVE_Record_Format.json#/definitions/cnaRejectedContainer'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    providerMetadata: CveProviderMetadata = Field(default=..., description="""Who provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/providerMetadata'}},
         'domain_of': ['CveCnaContainer', 'CveAdpContainer']} })


class CveCnaPublishedContainer(CveCnaContainer):
    """
    The assigning authority's account of a published vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer'}},
         'comments': ["It accepts keys of the publisher's own, whose names must begin "
                      'x_ and hold no full stop. JSON Schema from LinkML 1.12.1 cannot '
                      'state that rule on a name, so tests/cve_rules.py checks each '
                      'extra key.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'affected': {'name': 'affected', 'required': True},
                        'descriptions': {'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                                                          'range': 'cve_english_language',
                                                                                                          'required': True}}}},
                                         'list_elements_unique': True,
                                         'minimum_cardinality': 1,
                                         'name': 'descriptions',
                                         'required': True},
                        'references': {'name': 'references', 'required': True},
                        'tags': {'any_of': [{'range': 'CveCnaTag'},
                                            {'range': 'cve_tag_extension'}],
                                 'name': 'tags'}}})

    datePublic: Optional[str] = Field(default=None, description="""When the vulnerability was made public, if known.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/datePublic '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/datePublic'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    title: Optional[str] = Field(default=None, description="""A short headline for the record or for what the container adds.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/title '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/title'}},
         'close_mappings': ['dcterms:title'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'slot_uri': 'cve:title'} })
    descriptions: list[CveDescription] = Field(default=..., description="""The same text in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/descriptions '
                                                    'CVE_Record_Format.json#/definitions/englishLanguageDescription'}},
         'close_mappings': ['dcterms:description'],
         'comments': ['A list of this kind must hold at least one member in English, '
                      "stated where a class uses it, since a problem type's own list "
                      'has no such rule.'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemType',
                       'CveImpact'],
         'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                          'range': 'cve_english_language',
                                                                          'required': True}}}},
         'list_elements_unique': True} })
    affected: list[CveProduct] = Field(default=..., description="""The products or packages the vulnerability affects.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/affected'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    cpeApplicability: Optional[list[CveCpeApplicabilityElement]] = Field(default=None, description="""Statements in the CPE Applicability Language of which platforms are affected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/cpeApplicability '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/cpeApplicability'}},
         'close_mappings': ['sepses_cve:hasVulnerableConfiguration'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    problemTypes: Optional[list[CveProblemType]] = Field(default=None, description="""The kinds of problem the vulnerability is, such as a weakness type.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    references: list[CveReference] = Field(default=..., description="""Links to more about the vulnerability.""", min_length=1, max_length=512, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/references'}},
         'close_mappings': ['dcterms:references', 'sepses_cve:hasReference'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemTypeDescription'],
         'list_elements_unique': True,
         'slot_uri': 'cve:references'} })
    impacts: Optional[list[CveImpact]] = Field(default=None, description="""The consequences of the vulnerability, in words.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/impacts'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    metrics: Optional[list[CveMetric]] = Field(default=None, description="""The scorings of the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics'}},
         'close_mappings': ['sepses_cvss:hasCVSS'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    configurations: Optional[list[CveDescription]] = Field(default=None, description="""What must be set up for the vulnerability to be exploitable.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/configurations'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    workarounds: Optional[list[CveDescription]] = Field(default=None, description="""Ways to reduce the risk without a full fix.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/workarounds'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    solutions: Optional[list[CveDescription]] = Field(default=None, description="""Ways to fix the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/solutions'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    exploits: Optional[list[CveDescription]] = Field(default=None, description="""What is known about attacks on the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/exploits'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    timeline: Optional[list[CveTimelineEvent]] = Field(default=None, description="""The dated events in the vulnerability's history.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/timeline'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    credits: Optional[list[CveCredit]] = Field(default=None, description="""Thanks to those who helped.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/credits'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    source: Optional[CveSource] = Field(default=None, description="""How the vulnerability came to light, in the provider's own shape.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/source'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'slot_uri': 'cve:source'} })
    tags: Optional[list[Union[CveCnaTag, str]]] = Field(default=None, description="""Short labels from the upstream's list, or the publisher's own beginning x_.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaTags '
                                                    'CVE_Record_Format.json#/definitions/adpTags '
                                                    'CVE_Record_Format.json#/definitions/reference/properties/tags'}},
         'any_of': [{'range': 'CveCnaTag'}, {'range': 'cve_tag_extension'}],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer', 'CveReference'],
         'list_elements_unique': True,
         'slot_uri': 'cve:tags'} })
    taxonomyMappings: Optional[list[CveTaxonomyMapping]] = Field(default=None, description="""How the vulnerability relates to outside taxonomies.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    dateAssigned: Optional[str] = Field(default=None, description="""When the authority tied the CVE identifier to a vulnerability.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/dateAssigned'}},
         'domain_of': ['CveCnaPublishedContainer']} })
    providerMetadata: CveProviderMetadata = Field(default=..., description="""Who provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/providerMetadata'}},
         'domain_of': ['CveCnaContainer', 'CveAdpContainer']} })


class CveCnaRejectedContainer(CveCnaContainer):
    """
    The assigning authority's account of why a record was rejected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaRejectedContainer'}},
         'comments': ["It accepts keys of the publisher's own, whose names must begin "
                      'x_ and hold no full stop. tests/cve_rules.py checks each extra '
                      'key.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    rejectedReasons: list[CveDescription] = Field(default=..., description="""Why the record was rejected, in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/rejectedReasons'}},
         'domain_of': ['CveCnaRejectedContainer'],
         'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                          'range': 'cve_english_language',
                                                                          'required': True}}}},
         'list_elements_unique': True} })
    replacedBy: Optional[list[str]] = Field(default=None, description="""The CVE identifiers to use instead of this one.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/replacedBy'}},
         'domain_of': ['CveCnaRejectedContainer'],
         'list_elements_unique': True} })
    providerMetadata: CveProviderMetadata = Field(default=..., description="""Who provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/providerMetadata'}},
         'domain_of': ['CveCnaContainer', 'CveAdpContainer']} })


class CveAdpContainer(ConfiguredBaseModel):
    """
    What an Authorized Data Publisher adds to a record beside the assigning authority's account.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/adpContainer'}},
         'comments': ["It accepts keys of the publisher's own, whose names must begin "
                      'x_ and hold no full stop, and it must hold something beside '
                      'providerMetadata. tests/cve_rules.py checks both, since LinkML '
                      '1.12.1 can state neither.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'descriptions': {'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                                                          'range': 'cve_english_language',
                                                                                                          'required': True}}}},
                                         'list_elements_unique': True,
                                         'minimum_cardinality': 1,
                                         'name': 'descriptions'},
                        'tags': {'any_of': [{'range': 'CveAdpTag'},
                                            {'range': 'cve_tag_extension'}],
                                 'name': 'tags'}}})

    providerMetadata: CveProviderMetadata = Field(default=..., description="""Who provided the container.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/cnaRejectedContainer/properties/providerMetadata '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/providerMetadata'}},
         'domain_of': ['CveCnaContainer', 'CveAdpContainer']} })
    datePublic: Optional[str] = Field(default=None, description="""When the vulnerability was made public, if known.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/datePublic '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/datePublic'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    title: Optional[str] = Field(default=None, description="""A short headline for the record or for what the container adds.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/title '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/title'}},
         'close_mappings': ['dcterms:title'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'slot_uri': 'cve:title'} })
    descriptions: Optional[list[CveDescription]] = Field(default=None, description="""The same text in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/descriptions '
                                                    'CVE_Record_Format.json#/definitions/englishLanguageDescription'}},
         'close_mappings': ['dcterms:description'],
         'comments': ['A list of this kind must hold at least one member in English, '
                      "stated where a class uses it, since a problem type's own list "
                      'has no such rule.'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemType',
                       'CveImpact'],
         'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                          'range': 'cve_english_language',
                                                                          'required': True}}}},
         'list_elements_unique': True} })
    affected: Optional[list[CveProduct]] = Field(default=None, description="""The products or packages the vulnerability affects.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/affected'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    cpeApplicability: Optional[list[CveCpeApplicabilityElement]] = Field(default=None, description="""Statements in the CPE Applicability Language of which platforms are affected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaPublishedContainer/properties/cpeApplicability '
                                                    'CVE_Record_Format.json#/definitions/adpContainer/properties/cpeApplicability'}},
         'close_mappings': ['sepses_cve:hasVulnerableConfiguration'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer']} })
    problemTypes: Optional[list[CveProblemType]] = Field(default=None, description="""The kinds of problem the vulnerability is, such as a weakness type.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    references: Optional[list[CveReference]] = Field(default=None, description="""Links to more about the vulnerability.""", min_length=1, max_length=512, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/references'}},
         'close_mappings': ['dcterms:references', 'sepses_cve:hasReference'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemTypeDescription'],
         'list_elements_unique': True,
         'slot_uri': 'cve:references'} })
    impacts: Optional[list[CveImpact]] = Field(default=None, description="""The consequences of the vulnerability, in words.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/impacts'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    metrics: Optional[list[CveMetric]] = Field(default=None, description="""The scorings of the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics'}},
         'close_mappings': ['sepses_cvss:hasCVSS'],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    configurations: Optional[list[CveDescription]] = Field(default=None, description="""What must be set up for the vulnerability to be exploitable.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/configurations'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    workarounds: Optional[list[CveDescription]] = Field(default=None, description="""Ways to reduce the risk without a full fix.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/workarounds'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    solutions: Optional[list[CveDescription]] = Field(default=None, description="""Ways to fix the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/solutions'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    exploits: Optional[list[CveDescription]] = Field(default=None, description="""What is known about attacks on the vulnerability.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/exploits'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    timeline: Optional[list[CveTimelineEvent]] = Field(default=None, description="""The dated events in the vulnerability's history.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/timeline'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    credits: Optional[list[CveCredit]] = Field(default=None, description="""Thanks to those who helped.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/credits'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })
    source: Optional[CveSource] = Field(default=None, description="""How the vulnerability came to light, in the provider's own shape.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/source'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'slot_uri': 'cve:source'} })
    tags: Optional[list[Union[CveAdpTag, str]]] = Field(default=None, description="""Short labels from the upstream's list, or the publisher's own beginning x_.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaTags '
                                                    'CVE_Record_Format.json#/definitions/adpTags '
                                                    'CVE_Record_Format.json#/definitions/reference/properties/tags'}},
         'any_of': [{'range': 'CveAdpTag'}, {'range': 'cve_tag_extension'}],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer', 'CveReference'],
         'list_elements_unique': True,
         'slot_uri': 'cve:tags'} })
    taxonomyMappings: Optional[list[CveTaxonomyMapping]] = Field(default=None, description="""How the vulnerability relates to outside taxonomies.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings'}},
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer'],
         'list_elements_unique': True} })


class CveProduct(ConfiguredBaseModel):
    """
    One affected product or package, and which of its versions are affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'all_of': [{'any_of': [{'slot_conditions': {'product': {'name': 'product',
                                                                 'value_presence': 'PRESENT'},
                                                     'vendor': {'name': 'vendor',
                                                                'value_presence': 'PRESENT'}}},
                                {'slot_conditions': {'collectionURL': {'name': 'collectionURL',
                                                                       'value_presence': 'PRESENT'},
                                                     'packageName': {'name': 'packageName',
                                                                     'value_presence': 'PRESENT'}}}]},
                    {'any_of': [{'slot_conditions': {'versions': {'name': 'versions',
                                                                  'value_presence': 'PRESENT'}}},
                                {'slot_conditions': {'defaultStatus': {'name': 'defaultStatus',
                                                                       'value_presence': 'PRESENT'}}}]}],
         'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    vendor: Optional[str] = Field(default=None, description="""Who makes or maintains the product. It can be N/A.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/vendor'}},
         'domain_of': ['CveProduct']} })
    product: Optional[str] = Field(default=None, description="""The name of the affected product.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/product'}},
         'domain_of': ['CveProduct']} })
    collectionURL: Optional[str] = Field(default=None, description="""The address of the package collection that gives packageName its meaning.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/collectionURL'}},
         'domain_of': ['CveProduct']} })
    packageName: Optional[str] = Field(default=None, description="""The package's name or identifier within its collection.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/packageName'}},
         'domain_of': ['CveProduct']} })
    packageURL: Optional[str] = Field(default=None, description="""A Package URL for the package, with no version in it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/packageURL'}},
         'close_mappings': ['spdx_software:packageUrl'],
         'domain_of': ['CveProduct']} })
    cpes: Optional[list[str]] = Field(default=None, description="""Common Platform Enumeration names for the product.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/cpes'}},
         'close_mappings': ['sepses_cve:hasCPE'],
         'comments': ['The upstream suggests cpeApplicability for new records.'],
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })
    modules: Optional[list[str]] = Field(default=None, description="""The affected parts of the product, such as components, commands or APIs.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/modules'}},
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })
    programFiles: Optional[list[str]] = Field(default=None, description="""The affected source files.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/programFiles'}},
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })
    programRoutines: Optional[list[CveProgramRoutine]] = Field(default=None, description="""The affected functions or similar routines in the source.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/programRoutines'}},
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })
    platforms: Optional[list[str]] = Field(default=None, description="""The platforms the flaw is limited to. Without this, it applies to all of them.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/platforms'}},
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })
    repo: Optional[str] = Field(default=None, description="""The address of the product's source code repository.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/repo'}},
         'close_mappings': ['schema:codeRepository'],
         'domain_of': ['CveProduct']} })
    defaultStatus: Optional[CveVersionStatus] = Field(default=None, description="""The status of every version the versions list does not cover.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/defaultStatus'}},
         'comments': ["Left out, it reads as unknown, as the upstream's text says."],
         'domain_of': ['CveProduct']} })
    versions: Optional[list[CveProductVersion]] = Field(default=None, description="""The versions or ranges of versions, each with its status.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions'}},
         'domain_of': ['CveProduct'],
         'list_elements_unique': True} })


class CveProgramRoutine(ConfiguredBaseModel):
    """
    One affected function, method or similar routine in the source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/programRoutines/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'name': {'name': 'name',
                                 'range': 'cve_text_4096',
                                 'required': True}}})

    name: str = Field(default=..., description="""A name, of a reference or of a routine.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/reference/properties/name '
                                                    'CVE_Record_Format.json#/definitions/product/properties/programRoutines/items/properties/name'}},
         'domain_of': ['CveProgramRoutine', 'CveReference'],
         'slot_uri': 'cve:name'} })


class CveProductVersion(ConfiguredBaseModel):
    """
    A single version or a stretch of versions, and whether it is affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'rules': [{'description': 'An entry with lessThan also has versionType.',
                    'postconditions': {'slot_conditions': {'versionType': {'name': 'versionType',
                                                                           'value_presence': 'PRESENT'}}},
                    'preconditions': {'slot_conditions': {'lessThan': {'name': 'lessThan',
                                                                       'value_presence': 'PRESENT'}}},
                    'title': 'a range below a limit names its version type'},
                   {'description': 'An entry with lessThanOrEqual also has '
                                   'versionType.',
                    'postconditions': {'slot_conditions': {'versionType': {'name': 'versionType',
                                                                           'value_presence': 'PRESENT'}}},
                    'preconditions': {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                              'value_presence': 'PRESENT'}}},
                    'title': 'a range up to a limit names its version type'},
                   {'description': 'An entry with lessThan has no lessThanOrEqual.',
                    'postconditions': {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                               'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'lessThan': {'name': 'lessThan',
                                                                       'value_presence': 'PRESENT'}}},
                    'title': 'a range has one upper limit'},
                   {'description': 'An entry with changes also has lessThan or '
                                   'lessThanOrEqual.',
                    'postconditions': {'any_of': [{'slot_conditions': {'lessThan': {'name': 'lessThan',
                                                                                    'value_presence': 'PRESENT'}}},
                                                  {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                                           'value_presence': 'PRESENT'}}}]},
                    'preconditions': {'slot_conditions': {'changes': {'name': 'changes',
                                                                      'value_presence': 'PRESENT'}}},
                    'title': 'status changes belong to a range'}],
         'slot_usage': {'status': {'name': 'status', 'required': True},
                        'version': {'name': 'version',
                                    'range': 'cve_version',
                                    'required': True}}})

    version: str = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40', 'CveProductVersion'],
         'slot_uri': 'cve:version'} })
    status: CveVersionStatus = Field(default=..., description="""Whether a version is affected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/status '
                                                    'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/changes/items/properties/status'}},
         'domain_of': ['CveProductVersion', 'CveVersionChange'],
         'slot_uri': 'cve:status'} })
    versionType: Optional[str] = Field(default=None, description="""The numbering system that says how these versions compare, such as semver or git.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/versionType'}},
         'comments': ['The upstream lists examples, not a closed list, so this is free '
                      'text.'],
         'domain_of': ['CveProductVersion']} })
    lessThan: Optional[str] = Field(default=None, description="""The first version above the range, which is not itself in it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/lessThan'}},
         'domain_of': ['CveProductVersion']} })
    lessThanOrEqual: Optional[str] = Field(default=None, description="""The last version in the range.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/lessThanOrEqual'}},
         'domain_of': ['CveProductVersion']} })
    changes: Optional[list[CveVersionChange]] = Field(default=None, description="""The points within the range where the status changes.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/changes'}},
         'comments': ['A reader must sort them, as the upstream says the order cannot '
                      'be trusted.'],
         'domain_of': ['CveProductVersion'],
         'list_elements_unique': True} })


class CveVersionChange(ConfiguredBaseModel):
    """
    A point in a range of versions from which the status changes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/changes/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'at': {'name': 'at', 'required': True},
                        'status': {'name': 'status', 'required': True}}})

    at: str = Field(default=..., description="""The version from which a new status starts.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/changes/items/properties/at'}},
         'domain_of': ['CveVersionChange'],
         'slot_uri': 'cve:at'} })
    status: CveVersionStatus = Field(default=..., description="""Whether a version is affected.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/status '
                                                    'CVE_Record_Format.json#/definitions/product/properties/versions/items/properties/changes/items/properties/status'}},
         'domain_of': ['CveProductVersion', 'CveVersionChange'],
         'slot_uri': 'cve:status'} })


class CveCpeApplicabilityElement(ConfiguredBaseModel):
    """
    A statement in the CPE Applicability Language of which platforms are affected.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement'}},
         'close_mappings': ['sepses_cve:VulnerableConfiguration'],
         'comments': ['The upstream does not close this object, so other keys are '
                      'allowed.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    operator: Optional[CveCpeOperator] = Field(default=None, description="""How the parts combine, all of them or any of them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement/properties/operator '
                                                    'CVE_Record_Format.json#/definitions/cpe_node/properties/operator'}},
         'domain_of': ['CveCpeApplicabilityElement', 'CveCpeNode']} })
    negate: Optional[bool] = Field(default=None, description="""Whether the combined result is reversed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement/properties/negate '
                                                    'CVE_Record_Format.json#/definitions/cpe_node/properties/negate'}},
         'domain_of': ['CveCpeApplicabilityElement', 'CveCpeNode']} })
    nodes: list[CveCpeNode] = Field(default=..., description="""The groups of matches that the statement combines.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement/properties/nodes'}},
         'domain_of': ['CveCpeApplicabilityElement']} })


class CveCpeNode(ConfiguredBaseModel):
    """
    A group of CPE matches, combined by an operator.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_node'}},
         'comments': ['The upstream does not close this object, so other keys are '
                      'allowed.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'operator': {'name': 'operator', 'required': True}}})

    operator: CveCpeOperator = Field(default=..., description="""How the parts combine, all of them or any of them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement/properties/operator '
                                                    'CVE_Record_Format.json#/definitions/cpe_node/properties/operator'}},
         'domain_of': ['CveCpeApplicabilityElement', 'CveCpeNode']} })
    negate: Optional[bool] = Field(default=None, description="""Whether the combined result is reversed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpeApplicabilityElement/properties/negate '
                                                    'CVE_Record_Format.json#/definitions/cpe_node/properties/negate'}},
         'domain_of': ['CveCpeApplicabilityElement', 'CveCpeNode']} })
    cpeMatch: list[CveCpeMatch] = Field(default=..., description="""The CPE matches in the group.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_node/properties/cpeMatch'}},
         'domain_of': ['CveCpeNode']} })


class CveCpeMatch(ConfiguredBaseModel):
    """
    One CPE name, optionally bounded by versions, and whether it is vulnerable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    vulnerable: bool = Field(default=..., description="""Whether what this match covers is vulnerable.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/vulnerable'}},
         'domain_of': ['CveCpeMatch']} })
    criteria: str = Field(default=..., description="""The CPE name to match.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/criteria'}},
         'domain_of': ['CveCpeMatch']} })
    matchCriteriaId: Optional[str] = Field(default=None, description="""A UUID for this match.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/matchCriteriaId'}},
         'domain_of': ['CveCpeMatch']} })
    versionStartExcluding: Optional[str] = Field(default=None, description="""The version the match starts just above.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/versionStartExcluding'}},
         'domain_of': ['CveCpeMatch']} })
    versionStartIncluding: Optional[str] = Field(default=None, description="""The version the match starts at.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/versionStartIncluding'}},
         'domain_of': ['CveCpeMatch']} })
    versionEndExcluding: Optional[str] = Field(default=None, description="""The version the match ends just below.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/versionEndExcluding'}},
         'domain_of': ['CveCpeMatch']} })
    versionEndIncluding: Optional[str] = Field(default=None, description="""The version the match ends at.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cpe_match/properties/versionEndIncluding'}},
         'domain_of': ['CveCpeMatch']} })


class CveDescription(ConfiguredBaseModel):
    """
    A piece of text in one language, with any media that support it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'lang': {'name': 'lang', 'required': True},
                        'value': {'name': 'value',
                                  'range': 'cve_text_4096',
                                  'required': True}}})

    lang: str = Field(default=..., description="""The language of the text beside it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/language'}},
         'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['CveDescription',
                       'CveProblemTypeDescription',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    value: str = Field(default=..., description="""The text or content itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/value '
                                                    'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/timeline/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/value'}},
         'domain_of': ['CveDescription',
                       'CveSupportingMedia',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    supportingMedia: Optional[list[CveSupportingMedia]] = Field(default=None, description="""Richer forms of the text, such as Markdown or an image.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia'}},
         'domain_of': ['CveDescription'],
         'list_elements_unique': True} })


class CveSupportingMedia(ConfiguredBaseModel):
    """
    A richer form of a description, as a media type and its content.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'type': {'name': 'type',
                                 'range': 'cve_text_256',
                                 'required': True},
                        'value': {'name': 'value',
                                  'range': 'cve_text_16384',
                                  'required': True}}})

    type: str = Field(default=..., description="""What kind of thing this is. Each class that uses it says what the choices are.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/type '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/type'}},
         'domain_of': ['CveSupportingMedia',
                       'CveProblemTypeDescription',
                       'CveOtherMetric',
                       'CveCredit'],
         'slot_uri': 'cve:type'} })
    value: str = Field(default=..., description="""The text or content itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/value '
                                                    'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/timeline/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/value'}},
         'domain_of': ['CveDescription',
                       'CveSupportingMedia',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    base64: Optional[bool] = Field(default=False, description="""Whether value is base64 encoded rather than plain UTF-8.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/base64'}},
         'domain_of': ['CveSupportingMedia'],
         'ifabsent': 'false'} })


class CveProblemType(ConfiguredBaseModel):
    """
    One kind of problem the vulnerability is, in one or more languages.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'descriptions': {'list_elements_unique': True,
                                         'minimum_cardinality': 1,
                                         'name': 'descriptions',
                                         'range': 'CveProblemTypeDescription',
                                         'required': True}}})

    descriptions: list[CveProblemTypeDescription] = Field(default=..., description="""The same text in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/descriptions '
                                                    'CVE_Record_Format.json#/definitions/englishLanguageDescription'}},
         'close_mappings': ['dcterms:description'],
         'comments': ['A list of this kind must hold at least one member in English, '
                      "stated where a class uses it, since a problem type's own list "
                      'has no such rule.'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemType',
                       'CveImpact'],
         'list_elements_unique': True} })


class CveProblemTypeDescription(ConfiguredBaseModel):
    """
    A problem type described in one language, often by a weakness identifier and its title.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'description': {'name': 'description',
                                        'range': 'cve_text_4096',
                                        'required': True},
                        'lang': {'name': 'lang', 'required': True},
                        'type': {'name': 'type', 'range': 'cve_text_128'}}})

    lang: str = Field(default=..., description="""The language of the text beside it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/language'}},
         'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['CveDescription',
                       'CveProblemTypeDescription',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    description: str = Field(default=..., description="""The text of a problem type, or the title of a weakness.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/description'}},
         'domain_of': ['CveProblemTypeDescription'],
         'slot_uri': 'cve:description'} })
    type: Optional[str] = Field(default=None, description="""What kind of thing this is. Each class that uses it says what the choices are.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/type '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/type'}},
         'domain_of': ['CveSupportingMedia',
                       'CveProblemTypeDescription',
                       'CveOtherMetric',
                       'CveCredit'],
         'slot_uri': 'cve:type'} })
    references: Optional[list[CveReference]] = Field(default=None, description="""Links to more about the vulnerability.""", min_length=1, max_length=512, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/references'}},
         'close_mappings': ['dcterms:references', 'sepses_cve:hasReference'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemTypeDescription'],
         'list_elements_unique': True,
         'slot_uri': 'cve:references'} })
    cweId: Optional[str] = Field(default=None, description="""The Common Weakness Enumeration identifier that best fits, such as CWE-79.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/cweId'}},
         'comments': ['The upstream also allows it 5 to 9 characters. '
                      'tests/cve_rules.py checks the length.'],
         'domain_of': ['CveProblemTypeDescription']} })

    @field_validator('cweId')
    def pattern_cweId(cls, v):
        pattern=re.compile(r"^CWE-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid cweId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid cweId format: {v}"
            raise ValueError(err_msg)
        return v


class CveReference(ConfiguredBaseModel):
    """
    A link to something about the vulnerability, such as an advisory or a patch.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/reference'}},
         'close_mappings': ['sepses_cve:Reference', 'stix:StixExternalReference'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'name': {'name': 'name', 'range': 'cve_text_512'},
                        'tags': {'any_of': [{'range': 'CveReferenceTag'},
                                            {'range': 'cve_tag_extension'}],
                                 'name': 'tags'},
                        'url': {'name': 'url', 'required': True}}})

    url: str = Field(default=..., description="""The address the reference points to.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/reference/properties/url'}},
         'close_mappings': ['sepses_cve:referenceUrl'],
         'domain_of': ['CveReference'],
         'slot_uri': 'cve:url'} })
    name: Optional[str] = Field(default=None, description="""A name, of a reference or of a routine.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/reference/properties/name '
                                                    'CVE_Record_Format.json#/definitions/product/properties/programRoutines/items/properties/name'}},
         'domain_of': ['CveProgramRoutine', 'CveReference'],
         'slot_uri': 'cve:name'} })
    tags: Optional[list[Union[CveReferenceTag, str]]] = Field(default=None, description="""Short labels from the upstream's list, or the publisher's own beginning x_.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/cnaTags '
                                                    'CVE_Record_Format.json#/definitions/adpTags '
                                                    'CVE_Record_Format.json#/definitions/reference/properties/tags'}},
         'any_of': [{'range': 'CveReferenceTag'}, {'range': 'cve_tag_extension'}],
         'domain_of': ['CveCnaPublishedContainer', 'CveAdpContainer', 'CveReference'],
         'list_elements_unique': True,
         'slot_uri': 'cve:tags'} })


class CveImpact(ConfiguredBaseModel):
    """
    A consequence of the vulnerability, in words.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/impacts/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'descriptions': {'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                                                          'range': 'cve_english_language',
                                                                                                          'required': True}}}},
                                         'list_elements_unique': True,
                                         'minimum_cardinality': 1,
                                         'name': 'descriptions',
                                         'required': True}}})

    descriptions: list[CveDescription] = Field(default=..., description="""The same text in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/descriptions '
                                                    'CVE_Record_Format.json#/definitions/englishLanguageDescription'}},
         'close_mappings': ['dcterms:description'],
         'comments': ['A list of this kind must hold at least one member in English, '
                      "stated where a class uses it, since a problem type's own list "
                      'has no such rule.'],
         'domain_of': ['CveCnaPublishedContainer',
                       'CveAdpContainer',
                       'CveProblemType',
                       'CveImpact'],
         'has_member': {'range_expression': {'slot_conditions': {'lang': {'name': 'lang',
                                                                          'range': 'cve_english_language',
                                                                          'required': True}}}},
         'list_elements_unique': True} })
    capecId: Optional[str] = Field(default=None, description="""The Common Attack Pattern Enumeration identifier that best fits, such as CAPEC-63.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/impacts/items/properties/capecId'}},
         'comments': ['The upstream also allows it 7 to 11 characters. '
                      'tests/cve_rules.py checks the length.'],
         'domain_of': ['CveImpact']} })

    @field_validator('capecId')
    def pattern_capecId(cls, v):
        pattern=re.compile(r"^CAPEC-[1-9][0-9]{0,4}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid capecId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid capecId format: {v}"
            raise ValueError(err_msg)
        return v


class CveMetric(ConfiguredBaseModel):
    """
    One scoring of the vulnerability, in a CVSS version or another format, and where it applies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items'}},
         'any_of': [{'slot_conditions': {'cvssV4_0': {'name': 'cvssV4_0',
                                                      'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'cvssV3_1': {'name': 'cvssV3_1',
                                                      'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'cvssV3_0': {'name': 'cvssV3_0',
                                                      'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'cvssV2_0': {'name': 'cvssV2_0',
                                                      'value_presence': 'PRESENT'}}},
                    {'slot_conditions': {'other': {'name': 'other',
                                                   'value_presence': 'PRESENT'}}}],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    format: Optional[str] = Field(default=None, description="""The name of the scoring format.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/format'}},
         'domain_of': ['CveMetric']} })
    scenarios: Optional[list[CveMetricScenario]] = Field(default=None, description="""The situations this scoring applies to.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios'}},
         'domain_of': ['CveMetric'],
         'list_elements_unique': True} })
    cvssV4_0: Optional[CvssV40] = Field(default=None, description="""A score under CVSS version 4.0.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/cvssV4_0'}},
         'domain_of': ['CveMetric']} })
    cvssV3_1: Optional[CvssV31] = Field(default=None, description="""A score under CVSS version 3.1.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/cvssV3_1'}},
         'domain_of': ['CveMetric']} })
    cvssV3_0: Optional[CvssV30] = Field(default=None, description="""A score under CVSS version 3.0.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/cvssV3_0'}},
         'domain_of': ['CveMetric']} })
    cvssV2_0: Optional[CvssV20] = Field(default=None, description="""A score under CVSS version 2.0.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/cvssV2_0'}},
         'domain_of': ['CveMetric']} })
    other: Optional[CveOtherMetric] = Field(default=None, description="""A score or impact statement in some other format.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/other'}},
         'domain_of': ['CveMetric']} })


class CveMetricScenario(ConfiguredBaseModel):
    """
    A situation a scoring applies to, in one language.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'lang': {'name': 'lang', 'required': True},
                        'value': {'name': 'value',
                                  'range': 'cve_text_4096',
                                  'required': True}}})

    lang: str = Field(default=..., description="""The language of the text beside it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/language'}},
         'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['CveDescription',
                       'CveProblemTypeDescription',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    value: str = Field(default=..., description="""The text or content itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/value '
                                                    'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/timeline/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/value'}},
         'domain_of': ['CveDescription',
                       'CveSupportingMedia',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })


class CveOtherMetric(ConfiguredBaseModel):
    """
    A score or impact statement in a format the record format does not name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/other'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'type': {'name': 'type',
                                 'range': 'cve_text_128',
                                 'required': True}}})

    type: str = Field(default=..., description="""What kind of thing this is. Each class that uses it says what the choices are.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/type '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/type'}},
         'domain_of': ['CveSupportingMedia',
                       'CveProblemTypeDescription',
                       'CveOtherMetric',
                       'CveCredit'],
         'slot_uri': 'cve:type'} })
    content: CveOtherMetricContent = Field(default=..., description="""The statement itself, as an object in whatever shape its format has.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/content'}},
         'domain_of': ['CveOtherMetric']} })


class CveOtherMetricContent(ConfiguredBaseModel):
    """
    The free-form object inside a metric of another format.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/content'}},
         'comments': ['The upstream asks for at least one key, which '
                      'tests/cve_rules.py checks.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    pass


class CveTimelineEvent(ConfiguredBaseModel):
    """
    One dated event in the vulnerability's history.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/timeline/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'lang': {'name': 'lang', 'required': True},
                        'value': {'name': 'value',
                                  'range': 'cve_text_4096',
                                  'required': True}}})

    lang: str = Field(default=..., description="""The language of the text beside it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/language'}},
         'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['CveDescription',
                       'CveProblemTypeDescription',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    value: str = Field(default=..., description="""The text or content itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/value '
                                                    'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/timeline/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/value'}},
         'domain_of': ['CveDescription',
                       'CveSupportingMedia',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    time: str = Field(default=..., description="""When the event happened.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/timeline/items/properties/time'}},
         'domain_of': ['CveTimelineEvent']} })


class CveCredit(ConfiguredBaseModel):
    """
    Thanks to someone who helped, in one language.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/credits/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record',
         'slot_usage': {'lang': {'name': 'lang', 'required': True},
                        'type': {'ifabsent': 'CveCreditType(finder)',
                                 'name': 'type',
                                 'range': 'CveCreditType'},
                        'value': {'name': 'value',
                                  'range': 'cve_text_4096',
                                  'required': True}}})

    lang: str = Field(default=..., description="""The language of the text beside it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/language'}},
         'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['CveDescription',
                       'CveProblemTypeDescription',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    value: str = Field(default=..., description="""The text or content itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/value '
                                                    'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/scenarios/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/timeline/items/properties/value '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/value'}},
         'domain_of': ['CveDescription',
                       'CveSupportingMedia',
                       'CveMetricScenario',
                       'CveTimelineEvent',
                       'CveCredit']} })
    type: Optional[CveCreditType] = Field(default=CveCreditType("finder"), description="""What kind of thing this is. Each class that uses it says what the choices are.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/description/properties/supportingMedia/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/problemTypes/items/properties/descriptions/items/properties/type '
                                                    'CVE_Record_Format.json#/definitions/metrics/items/properties/other/properties/type '
                                                    'CVE_Record_Format.json#/definitions/credits/items/properties/type'}},
         'domain_of': ['CveSupportingMedia',
                       'CveProblemTypeDescription',
                       'CveOtherMetric',
                       'CveCredit'],
         'ifabsent': 'CveCreditType(finder)',
         'slot_uri': 'cve:type'} })
    user: Optional[str] = Field(default=None, description="""The UUID of the credited person, when the CVE user registry holds them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/credits/items/properties/user'}},
         'domain_of': ['CveCredit']} })


class CveSource(ConfiguredBaseModel):
    """
    How the vulnerability came to light, as an object the provider shapes as it likes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/source'}},
         'comments': ['The upstream asks for at least one key, which '
                      'tests/cve_rules.py checks.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    pass


class CveTaxonomyMapping(ConfiguredBaseModel):
    """
    How the vulnerability relates to one version of an outside taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    taxonomyName: str = Field(default=..., description="""The name of the taxonomy, such as ATT&CK or CWE.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyName'}},
         'domain_of': ['CveTaxonomyMapping']} })
    taxonomyVersion: Optional[str] = Field(default=None, description="""The version of the taxonomy.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyVersion'}},
         'domain_of': ['CveTaxonomyMapping']} })
    taxonomyRelations: list[CveTaxonomyRelation] = Field(default=..., description="""The relationships to items in the taxonomy.""", min_length=1, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyRelations'}},
         'domain_of': ['CveTaxonomyMapping'],
         'list_elements_unique': True} })


class CveTaxonomyRelation(ConfiguredBaseModel):
    """
    One relationship from an item in a taxonomy to this CVE or to another item.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyRelations/items'}},
         'from_schema': 'https://w3id.org/lmodel/cve/cve_record'})

    taxonomyId: str = Field(default=..., description="""The item in the taxonomy, which is the relationship's subject.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyRelations/items/properties/taxonomyId'}},
         'domain_of': ['CveTaxonomyRelation']} })
    relationshipName: str = Field(default=..., description="""What the relationship is.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyRelations/items/properties/relationshipName'}},
         'domain_of': ['CveTaxonomyRelation']} })
    relationshipValue: str = Field(default=..., description="""The relationship's target, which is this CVE identifier or another taxonomy item.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/definitions/taxonomyMappings/items/properties/taxonomyRelations/items/properties/relationshipValue'}},
         'domain_of': ['CveTaxonomyRelation']} })


class CveRecordRoot(ConfiguredBaseModel):
    """
    Any one CVE record, published or rejected, as a file or an API answer holds it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'CVE_Record_Format.json#/'}},
         'comments': ['It has no keys of its own, and a record must be exactly one of '
                      'the two kinds, each of which is closed. So a rejected state '
                      'with a published container fails.'],
         'exactly_one_of': [{'is_a': 'CvePublishedRecord'},
                            {'is_a': 'CveRejectedRecord'}],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/cve',
         'tree_root': True})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CvssSeverityBandsMixin.model_rebuild()
CvssV20.model_rebuild()
CvssV30.model_rebuild()
CvssV31.model_rebuild()
CvssV40.model_rebuild()
CveRecord.model_rebuild()
CvePublishedRecord.model_rebuild()
CveRejectedRecord.model_rebuild()
CveRecordMetadata.model_rebuild()
CveMetadataPublished.model_rebuild()
CveMetadataRejected.model_rebuild()
CveContainers.model_rebuild()
CvePublishedContainers.model_rebuild()
CveRejectedContainers.model_rebuild()
CveProviderMetadata.model_rebuild()
CveCnaContainer.model_rebuild()
CveCnaPublishedContainer.model_rebuild()
CveCnaRejectedContainer.model_rebuild()
CveAdpContainer.model_rebuild()
CveProduct.model_rebuild()
CveProgramRoutine.model_rebuild()
CveProductVersion.model_rebuild()
CveVersionChange.model_rebuild()
CveCpeApplicabilityElement.model_rebuild()
CveCpeNode.model_rebuild()
CveCpeMatch.model_rebuild()
CveDescription.model_rebuild()
CveSupportingMedia.model_rebuild()
CveProblemType.model_rebuild()
CveProblemTypeDescription.model_rebuild()
CveReference.model_rebuild()
CveImpact.model_rebuild()
CveMetric.model_rebuild()
CveMetricScenario.model_rebuild()
CveOtherMetric.model_rebuild()
CveOtherMetricContent.model_rebuild()
CveTimelineEvent.model_rebuild()
CveCredit.model_rebuild()
CveSource.model_rebuild()
CveTaxonomyMapping.model_rebuild()
CveTaxonomyRelation.model_rebuild()
CveRecordRoot.model_rebuild()
