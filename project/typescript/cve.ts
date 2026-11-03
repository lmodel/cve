/**
* A CVSS rating in words.
*/
export enum CvssSeverity {
    
    /** No severity at all, for a score of 0. */
    NONE = "NONE",
    /** The lowest rating above none. */
    LOW = "LOW",
    /** The middle rating. */
    MEDIUM = "MEDIUM",
    /** The rating below critical. */
    HIGH = "HIGH",
    /** The highest rating. */
    CRITICAL = "CRITICAL",
};
/**
* How far away an attacker can be, in CVSS 2.0's terms.
*/
export enum CvssV2AccessVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from the same local network segment. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only with an account on the system or hands on it. */
    LOCAL = "LOCAL",
};
/**
* How hard the flaw is to use, in CVSS 2.0's terms.
*/
export enum CvssV2AccessComplexity {
    
    /** Only under unusual, hard-to-arrange conditions. */
    HIGH = "HIGH",
    /** Under conditions that take some arranging. */
    MEDIUM = "MEDIUM",
    /** With no special conditions. */
    LOW = "LOW",
};
/**
* How many logins an attacker needs, in CVSS 2.0's terms.
*/
export enum CvssV2Authentication {
    
    /** More than one login. */
    MULTIPLE = "MULTIPLE",
    /** One login. */
    SINGLE = "SINGLE",
    /** No login at all. */
    NONE = "NONE",
};
/**
* How much of one security property an attack could cost, in CVSS 2.0's terms.
*/
export enum CvssV2Impact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, and the attacker cannot choose all of it. */
    PARTIAL = "PARTIAL",
    /** All of it is lost. */
    COMPLETE = "COMPLETE",
};
/**
* How far working attack code has come.
*/
export enum CvssExploitCodeMaturity {
    
    /** No attack code is known, or the attack is only theory. */
    UNPROVEN = "UNPROVEN",
    /** A demonstration exists that needs skilled work to use. */
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    /** Working attack code exists for most situations. */
    FUNCTIONAL = "FUNCTIONAL",
    /** Attack code is reliable and widely available, or no code is needed. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* What kind of fix is available.
*/
export enum CvssRemediationLevel {
    
    /** The vendor offers a complete fix. */
    OFFICIAL_FIX = "OFFICIAL_FIX",
    /** The vendor offers a stopgap for now. */
    TEMPORARY_FIX = "TEMPORARY_FIX",
    /** Others offer a way round the flaw that is not from the vendor. */
    WORKAROUND = "WORKAROUND",
    /** No fix exists, or it cannot be applied. */
    UNAVAILABLE = "UNAVAILABLE",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far the flaw has been confirmed, in CVSS 2.0's terms.
*/
export enum CvssV2ReportConfidence {
    
    /** A single report or conflicting reports that nobody has checked. */
    UNCONFIRMED = "UNCONFIRMED",
    /** Several unofficial sources agree, with some doubt remaining. */
    UNCORROBORATED = "UNCORROBORATED",
    /** The vendor accepts it, or a working attack shows it. */
    CONFIRMED = "CONFIRMED",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much loss could follow beyond the system itself.
*/
export enum CvssV2CollateralDamagePotential {
    
    /** No such loss. */
    NONE = "NONE",
    /** Slight loss. */
    LOW = "LOW",
    /** Moderate loss. */
    LOW_MEDIUM = "LOW_MEDIUM",
    /** Significant loss. */
    MEDIUM_HIGH = "MEDIUM_HIGH",
    /** Catastrophic loss. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of the environment the flaw exposes.
*/
export enum CvssV2TargetDistribution {
    
    /** No systems at all, or only in a lab. */
    NONE = "NONE",
    /** Up to about a quarter of systems. */
    LOW = "LOW",
    /** About a quarter to three quarters of systems. */
    MEDIUM = "MEDIUM",
    /** More than about three quarters of systems. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much one security property matters to the scorer.
*/
export enum CvssRequirement {
    
    /** A loss would have limited effect. */
    LOW = "LOW",
    /** A loss would have serious effect. */
    MEDIUM = "MEDIUM",
    /** A loss would have catastrophic effect. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far away an attacker can be, in CVSS 3's terms.
*/
export enum CvssV3AttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from a logically nearby network. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
};
/**
* The attack vector as the scorer's environment changes it, in CVSS 3's terms.
*/
export enum CvssV3ModifiedAttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from a logically nearby network. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much is outside the attacker's control.
*/
export enum CvssAttackComplexity {
    
    /** Success depends on conditions the attacker must overcome or wait for. */
    HIGH = "HIGH",
    /** The attacker can succeed again and again with no special effort. */
    LOW = "LOW",
};
/**
* The attack complexity as the scorer's environment changes it.
*/
export enum CvssModifiedAttackComplexity {
    
    /** Success depends on conditions the attacker must overcome or wait for. */
    HIGH = "HIGH",
    /** The attacker can succeed again and again with no special effort. */
    LOW = "LOW",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* What access an attacker needs beforehand.
*/
export enum CvssPrivilegesRequired {
    
    /** Administrator-level access. */
    HIGH = "HIGH",
    /** Ordinary user access. */
    LOW = "LOW",
    /** No access at all. */
    NONE = "NONE",
};
/**
* The access needed as the scorer's environment changes it.
*/
export enum CvssModifiedPrivilegesRequired {
    
    /** Administrator-level access. */
    HIGH = "HIGH",
    /** Ordinary user access. */
    LOW = "LOW",
    /** No access at all. */
    NONE = "NONE",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether someone else has to take part, in CVSS 3's terms.
*/
export enum CvssV3UserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone other than the attacker has to do something. */
    REQUIRED = "REQUIRED",
};
/**
* The user interaction as the scorer's environment changes it, in CVSS 3's terms.
*/
export enum CvssV3ModifiedUserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone other than the attacker has to do something. */
    REQUIRED = "REQUIRED",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether an attack can reach beyond the flawed component.
*/
export enum CvssV3Scope {
    
    /** The harm stays within the same security authority. */
    UNCHANGED = "UNCHANGED",
    /** The harm can reach something under another security authority. */
    CHANGED = "CHANGED",
};
/**
* The scope as the scorer's environment changes it.
*/
export enum CvssV3ModifiedScope {
    
    /** The harm stays within the same security authority. */
    UNCHANGED = "UNCHANGED",
    /** The harm can reach something under another security authority. */
    CHANGED = "CHANGED",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of one security property an attack could cost.
*/
export enum CvssImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
};
/**
* The impact on one security property as the scorer's environment changes it.
*/
export enum CvssModifiedImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far the flaw has been confirmed, in CVSS 3's terms.
*/
export enum CvssV3ReportConfidence {
    
    /** Reports say something is wrong, but the cause is not clear. */
    UNKNOWN = "UNKNOWN",
    /** Solid details exist, without full confirmation of the cause. */
    REASONABLE = "REASONABLE",
    /** The flaw is shown beyond doubt, or the vendor accepts it. */
    CONFIRMED = "CONFIRMED",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far away an attacker can be, in CVSS 4.0's terms.
*/
export enum CvssV4AttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from something logically or physically nearby. */
    ADJACENT = "ADJACENT",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
};
/**
* The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
*/
export enum CvssV4ModifiedAttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from something logically or physically nearby. */
    ADJACENT = "ADJACENT",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether the attack needs conditions in the target beyond the attacker's control.
*/
export enum CvssV4AttackRequirements {
    
    /** The attack works whatever the target's state. */
    NONE = "NONE",
    /** The attack works only when the target is in a certain state. */
    PRESENT = "PRESENT",
};
/**
* The attack requirements as the scorer's environment changes them.
*/
export enum CvssV4ModifiedAttackRequirements {
    
    /** The attack works whatever the target's state. */
    NONE = "NONE",
    /** The attack works only when the target is in a certain state. */
    PRESENT = "PRESENT",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether someone else has to take part, in CVSS 4.0's terms.
*/
export enum CvssV4UserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone has to act only in the ordinary course of their work. */
    PASSIVE = "PASSIVE",
    /** Someone has to take a deliberate step. */
    ACTIVE = "ACTIVE",
};
/**
* The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
*/
export enum CvssV4ModifiedUserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone has to act only in the ordinary course of their work. */
    PASSIVE = "PASSIVE",
    /** Someone has to take a deliberate step. */
    ACTIVE = "ACTIVE",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.
*/
export enum CvssV4ModifiedSubsequentImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
    /** The loss could injure people. */
    SAFETY = "SAFETY",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much is known about attacks on the flaw.
*/
export enum CvssV4ExploitMaturity {
    
    /** No demonstration or attack has been reported. */
    UNREPORTED = "UNREPORTED",
    /** A demonstration is public, with no reported attack. */
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    /** Attacks have been reported, or tools for them are public. */
    ATTACKED = "ATTACKED",
    /** The scorer gave no value, so the worst case is assumed. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether an attack could put people's safety at risk.
*/
export enum CvssV4Safety {
    
    /** Any harm to people would be slight at most. */
    NEGLIGIBLE = "NEGLIGIBLE",
    /** People could be seriously hurt. */
    PRESENT = "PRESENT",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether every step of an attack could be automated across many targets.
*/
export enum CvssV4Automatable {
    
    /** At least one step resists automation. */
    NO = "NO",
    /** Every step can be automated. */
    YES = "YES",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How the affected system comes back after an attack.
*/
export enum CvssV4Recovery {
    
    /** The system recovers by itself. */
    AUTOMATIC = "AUTOMATIC",
    /** Someone has to step in and restore it. */
    USER = "USER",
    /** The system cannot be restored. */
    IRRECOVERABLE = "IRRECOVERABLE",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of a resource one successful attack gains the attacker.
*/
export enum CvssV4ValueDensity {
    
    /** Each target holds little, so an attacker must take many. */
    DIFFUSE = "DIFFUSE",
    /** A single target holds a lot. */
    CONCENTRATED = "CONCENTRATED",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much work it takes a consumer to respond to the flaw.
*/
export enum CvssV4ResponseEffort {
    
    /** Little work, such as reading advice or a small configuration change. */
    LOW = "LOW",
    /** Some work, with a noticeable effect on the service. */
    MODERATE = "MODERATE",
    /** Much work, or a long outage. */
    HIGH = "HIGH",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How urgent the product's supplier says the flaw is, as a colour.
*/
export enum CvssV4ProviderUrgency {
    
    /** The supplier sees little or no urgency. */
    CLEAR = "CLEAR",
    /** The supplier says the flaw can wait for regular work. */
    GREEN = "GREEN",
    /** The supplier says the flaw matters soon. */
    AMBER = "AMBER",
    /** The supplier says the flaw is at the highest urgency. */
    RED = "RED",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* The kind of document a CVE record is.
*/
export enum CveDataType {
    
    /** A document in the CVE Record Format. */
    CVE_RECORD = "CVE_RECORD",
};
/**
* Whether a record is in use.
*/
export enum CveRecordState {
    
    /** The assigning authority has filled the record in and made it public. */
    PUBLISHED = "PUBLISHED",
    /** The identifier and its record are withdrawn from use. */
    REJECTED = "REJECTED",
};
/**
* The state of a published record.
*/
export enum CvePublishedState {
    
    /** The assigning authority has filled the record in and made it public. */
    PUBLISHED = "PUBLISHED",
};
/**
* The state of a rejected record.
*/
export enum CveRejectedState {
    
    /** The identifier and its record are withdrawn from use. */
    REJECTED = "REJECTED",
};
/**
* Whether a version is affected.
*/
export enum CveVersionStatus {
    
    /** The vulnerability is present in this version. */
    affected = "affected",
    /** The vulnerability is not present in this version. */
    unaffected = "unaffected",
    /** It is not known whether the vulnerability is present. */
    unknown = "unknown",
};
/**
* How the parts of a CPE statement combine.
*/
export enum CveCpeOperator {
    
    /** All of the parts must hold. */
    AND = "AND",
    /** At least one of the parts must hold. */
    OR = "OR",
};
/**
* The part a credited person or organisation played.
*/
export enum CveCreditType {
    
    /** Found the vulnerability. */
    finder = "finder",
    /** Told the vendor or a CVE Numbering Authority about it. */
    reporter = "reporter",
    /** Checked that it is accurate or how severe it is. */
    analyst = "analyst",
    /** Organised the response among those involved. */
    coordinator = "coordinator",
    /** Prepared the code change or plan that addresses it. */
    remediation_developer = "remediation developer",
    /** Reviewed that change or plan for how well it works. */
    remediation_reviewer = "remediation reviewer",
    /** Tested the vulnerability or the fix for it. */
    remediation_verifier = "remediation verifier",
    /** A tool used to find or identify it. */
    tool = "tool",
    /** Supported the work of finding or fixing it. */
    sponsor = "sponsor",
    /** Any other part. */
    other = "other",
};
/**
* A label the assigning authority can put on a record.
*/
export enum CveCnaTag {
    
    /** Everything affected was out of support when the identifier was requested. */
    unsupported_when_assigned = "unsupported-when-assigned",
    /** Everything affected exists only as a hosted service. */
    exclusively_hosted_service = "exclusively-hosted-service",
    /** Someone disagrees that this is a vulnerability at all. */
    disputed = "disputed",
};
/**
* A label an Authorized Data Publisher can put on a record.
*/
export enum CveAdpTag {
    
    /** Someone disagrees that this is a vulnerability at all. */
    disputed = "disputed",
};
/**
* A label that says what a reference is.
*/
export enum CveReferenceTag {
    
    /** The address no longer answers. */
    broken_link = "broken-link",
    /** Only paying customers of the vendor can read it. */
    customer_entitlement = "customer-entitlement",
    /** It shows how to attack the flaw, or holds working attack code. */
    exploit = "exploit",
    /** It comes from a government body. */
    government_resource = "government-resource",
    /** It is a post in a bug tracker. */
    issue_tracking = "issue-tracking",
    /** It comes from a mailing list. */
    mailing_list = "mailing-list",
    /** It says how to reduce the risk when no patch can be applied. */
    mitigation = "mitigation",
    /** It has nothing to do with this vulnerability and was linked by mistake. */
    not_applicable = "not-applicable",
    /** It holds an update that fixes the flaw. */
    patch = "patch",
    /** A login blocks the way to it. */
    permissions_required = "permissions-required",
    /** It is a news story or similar report. */
    media_coverage = "media-coverage",
    /** It identifies the affected product, for naming schemes such as CPE. */
    product = "product",
    /** It concerns a related flaw, not this one. */
    related = "related",
    /** It is a set of release notes. */
    release_notes = "release-notes",
    /** It holds a way to detect or block the flaw or attacks on it. */
    signature = "signature",
    /** It explains the flaw and how it is attacked, in technical depth. */
    technical_description = "technical-description",
    /** It is an advisory from someone other than the vendor. */
    third_party_advisory = "third-party-advisory",
    /** It is an advisory from the vendor. */
    vendor_advisory = "vendor-advisory",
    /** It is an entry in a vulnerability database. */
    vdb_entry = "vdb-entry",
};


/**
 * The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
 */
export interface CvssSeverityBandsMixin {
    /** The score from 0 to 10 for what is inherent in the flaw. */
    baseScore: number,
    /** The rating in words that the base score falls under. */
    baseSeverity: string,
}


/**
 * A score under CVSS version 2.0, which has no severity bands.
 */
export interface CvssV20 {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** The score from 0 to 10 for what is inherent in the flaw. */
    baseScore: number,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** How far away an attacker can be when using the flaw, in CVSS 2.0's terms. */
    accessVector?: string,
    /** How hard the flaw is to use once the attacker can reach it. */
    accessComplexity?: string,
    /** How many times an attacker must log in before using the flaw. */
    authentication?: string,
    /** How far working attack code has come, in CVSS 2.0's terms. */
    exploitability?: string,
    /** How much loss a successful attack could cause beyond the system itself. */
    collateralDamagePotential?: string,
    /** How much of the scorer's environment is exposed to the flaw. */
    targetDistribution?: string,
}


/**
 * A score under CVSS version 3.0.
 */
export interface CvssV30 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** Whether an attack can reach beyond the component that holds the flaw. */
    scope?: string,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** How far working attack code has come. */
    exploitCodeMaturity?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** The rating in words for the temporal score. */
    temporalSeverity?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** The scope as the scorer's own environment changes it. */
    modifiedScope?: string,
    /** The confidentiality impact as the scorer's own environment changes it. */
    modifiedConfidentialityImpact?: string,
    /** The integrity impact as the scorer's own environment changes it. */
    modifiedIntegrityImpact?: string,
    /** The availability impact as the scorer's own environment changes it. */
    modifiedAvailabilityImpact?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** The rating in words for the environmental score. */
    environmentalSeverity?: string,
}


/**
 * A score under CVSS version 3.1.
 */
export interface CvssV31 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** Whether an attack can reach beyond the component that holds the flaw. */
    scope?: string,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** How far working attack code has come. */
    exploitCodeMaturity?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** The rating in words for the temporal score. */
    temporalSeverity?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** The scope as the scorer's own environment changes it. */
    modifiedScope?: string,
    /** The confidentiality impact as the scorer's own environment changes it. */
    modifiedConfidentialityImpact?: string,
    /** The integrity impact as the scorer's own environment changes it. */
    modifiedIntegrityImpact?: string,
    /** The availability impact as the scorer's own environment changes it. */
    modifiedAvailabilityImpact?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** The rating in words for the environmental score. */
    environmentalSeverity?: string,
}


/**
 * A score under CVSS version 4.0.
 */
export interface CvssV40 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** Whether the attack needs conditions in the target that the attacker does not control. */
    attackRequirements?: string,
    /** How much information in the vulnerable system an attack could expose. */
    vulnConfidentialityImpact?: string,
    /** How much an attack could change in the vulnerable system. */
    vulnIntegrityImpact?: string,
    /** How much an attack could disrupt the vulnerable system. */
    vulnAvailabilityImpact?: string,
    /** How much information in other, connected systems an attack could expose. */
    subConfidentialityImpact?: string,
    /** How much an attack could change in other, connected systems. */
    subIntegrityImpact?: string,
    /** How much an attack could disrupt other, connected systems. */
    subAvailabilityImpact?: string,
    /** How much is known about attacks on this flaw, in CVSS 4.0's terms. */
    exploitMaturity?: string,
    /** The attack requirements as the scorer's own environment changes them. */
    modifiedAttackRequirements?: string,
    /** The confidentiality impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnConfidentialityImpact?: string,
    /** The integrity impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnIntegrityImpact?: string,
    /** The availability impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnAvailabilityImpact?: string,
    /** The confidentiality impact on connected systems, in the scorer's environment. */
    modifiedSubConfidentialityImpact?: string,
    /** The integrity impact on connected systems, in the scorer's environment. */
    modifiedSubIntegrityImpact?: string,
    /** The availability impact on connected systems, in the scorer's environment. */
    modifiedSubAvailabilityImpact?: string,
    /** Whether an attack could put people's safety at risk. */
    Safety?: string,
    /** Whether an attacker could automate every step of an attack across many targets. */
    Automatable?: string,
    /** How the affected system comes back after an attack. */
    Recovery?: string,
    /** Whether one successful attack gains the attacker a little or a lot of a resource. */
    valueDensity?: string,
    /** How much work it takes a consumer to respond to the flaw. */
    vulnerabilityResponseEffort?: string,
    /** How urgent the product's supplier says the flaw is, as a colour. */
    providerUrgency?: string,
}


/**
 * A record of one vulnerability under one CVE identifier, in the CVE Program's format.
 */
export interface CveRecord {
    /** The facts about the record itself. */
    cveMetadata: CveRecordMetadata,
    /** The vulnerability information, grouped by who provided it. */
    containers: CveContainers,
    /** The kind of document this is, which is always a CVE record. */
    dataType: string,
    /** The version of the record format that this record follows. */
    dataVersion: string,
}


/**
 * A record whose assigning organisation has filled it in and made it public.
 */
export interface CvePublishedRecord extends CveRecord {
}


/**
 * A record that should no longer be used, kept so that people can see it is invalid.
 */
export interface CveRejectedRecord extends CveRecord {
}


/**
 * The facts about a record itself, as distinct from the vulnerability it describes.
 */
export interface CveRecordMetadata {
    /** When the record or container was last updated. */
    dateUpdated?: string,
    /** Whether the record is published or rejected. */
    state: string,
    /** The CVE identifier that the record belongs to. */
    cveId: string,
    /** The UUID of the organisation that was given the CVE identifier. */
    assignerOrgId: string,
    /** The short name of the organisation that was given the CVE identifier. */
    assignerShortName?: string,
    /** A counter that the system of record raises each time a provider changes the record. */
    serial?: number,
    /** When the CVE identifier was reserved. */
    dateReserved?: string,
    /** When the record first appeared in the CVE List. */
    datePublished?: string,
}


/**
 * The metadata of a published record.
 */
export interface CveMetadataPublished extends CveRecordMetadata {
    /** The UUID of the user who asked for the CVE identifier. */
    requesterUserId?: string,
}


/**
 * The metadata of a rejected record.
 */
export interface CveMetadataRejected extends CveRecordMetadata {
    /** When the CVE identifier was rejected. */
    dateRejected?: string,
}


/**
 * The sets of vulnerability information in a record, one per providing organisation.
 */
export interface CveContainers {
    /** The container from the authority that assigned the identifier. */
    cna: CveCnaContainer,
}


/**
 * The containers of a published record, the assigning organisation's and any others'.
 */
export interface CvePublishedContainers extends CveContainers {
    /** The containers added by Authorized Data Publishers. */
    adp?: CveAdpContainer[],
}


/**
 * The container of a rejected record, which only the assigning organisation provides.
 */
export interface CveRejectedContainers extends CveContainers {
}


/**
 * Who provided a container, and when it was last updated.
 */
export interface CveProviderMetadata {
    /** When the record or container was last updated. */
    dateUpdated?: string,
    /** The UUID of the organisation that provided the container. */
    orgId: string,
    /** The short name of the organisation that provided the container. */
    shortName?: string,
}


/**
 * The container from the CVE Numbering Authority that assigned the identifier.
 */
export interface CveCnaContainer {
    /** Who provided the container. */
    providerMetadata: CveProviderMetadata,
}


/**
 * The assigning authority's account of a published vulnerability.
 */
export interface CveCnaPublishedContainer extends CveCnaContainer {
    /** When the vulnerability was made public, if known. */
    datePublic?: string,
    /** A short headline for the record or for what the container adds. */
    title?: string,
    /** The same text in one or more languages. */
    descriptions: CveDescription[],
    /** The products or packages the vulnerability affects. */
    affected: CveProduct[],
    /** Statements in the CPE Applicability Language of which platforms are affected. */
    cpeApplicability?: CveCpeApplicabilityElement[],
    /** The kinds of problem the vulnerability is, such as a weakness type. */
    problemTypes?: CveProblemType[],
    /** Links to more about the vulnerability. */
    references: CveReference[],
    /** The consequences of the vulnerability, in words. */
    impacts?: CveImpact[],
    /** The scorings of the vulnerability. */
    metrics?: CveMetric[],
    /** What must be set up for the vulnerability to be exploitable. */
    configurations?: CveDescription[],
    /** Ways to reduce the risk without a full fix. */
    workarounds?: CveDescription[],
    /** Ways to fix the vulnerability. */
    solutions?: CveDescription[],
    /** What is known about attacks on the vulnerability. */
    exploits?: CveDescription[],
    /** The dated events in the vulnerability's history. */
    timeline?: CveTimelineEvent[],
    /** Thanks to those who helped. */
    credits?: CveCredit[],
    /** How the vulnerability came to light, in the provider's own shape. */
    source?: CveSource,
    /** Short labels from the upstream's list, or the publisher's own beginning x_. */
    tags?: string[],
    /** How the vulnerability relates to outside taxonomies. */
    taxonomyMappings?: CveTaxonomyMapping[],
    /** When the authority tied the CVE identifier to a vulnerability. */
    dateAssigned?: string,
}


/**
 * The assigning authority's account of why a record was rejected.
 */
export interface CveCnaRejectedContainer extends CveCnaContainer {
    /** Why the record was rejected, in one or more languages. */
    rejectedReasons: CveDescription[],
    /** The CVE identifiers to use instead of this one. */
    replacedBy?: string[],
}


/**
 * What an Authorized Data Publisher adds to a record beside the assigning authority's account.
 */
export interface CveAdpContainer {
    /** Who provided the container. */
    providerMetadata: CveProviderMetadata,
    /** When the vulnerability was made public, if known. */
    datePublic?: string,
    /** A short headline for the record or for what the container adds. */
    title?: string,
    /** The same text in one or more languages. */
    descriptions?: CveDescription[],
    /** The products or packages the vulnerability affects. */
    affected?: CveProduct[],
    /** Statements in the CPE Applicability Language of which platforms are affected. */
    cpeApplicability?: CveCpeApplicabilityElement[],
    /** The kinds of problem the vulnerability is, such as a weakness type. */
    problemTypes?: CveProblemType[],
    /** Links to more about the vulnerability. */
    references?: CveReference[],
    /** The consequences of the vulnerability, in words. */
    impacts?: CveImpact[],
    /** The scorings of the vulnerability. */
    metrics?: CveMetric[],
    /** What must be set up for the vulnerability to be exploitable. */
    configurations?: CveDescription[],
    /** Ways to reduce the risk without a full fix. */
    workarounds?: CveDescription[],
    /** Ways to fix the vulnerability. */
    solutions?: CveDescription[],
    /** What is known about attacks on the vulnerability. */
    exploits?: CveDescription[],
    /** The dated events in the vulnerability's history. */
    timeline?: CveTimelineEvent[],
    /** Thanks to those who helped. */
    credits?: CveCredit[],
    /** How the vulnerability came to light, in the provider's own shape. */
    source?: CveSource,
    /** Short labels from the upstream's list, or the publisher's own beginning x_. */
    tags?: string[],
    /** How the vulnerability relates to outside taxonomies. */
    taxonomyMappings?: CveTaxonomyMapping[],
}


/**
 * One affected product or package, and which of its versions are affected.
 */
export interface CveProduct {
    /** Who makes or maintains the product. It can be N/A. */
    vendor?: string,
    /** The name of the affected product. */
    product?: string,
    /** The address of the package collection that gives packageName its meaning. */
    collectionURL?: string,
    /** The package's name or identifier within its collection. */
    packageName?: string,
    /** A Package URL for the package, with no version in it. */
    packageURL?: string,
    /** Common Platform Enumeration names for the product. */
    cpes?: string[],
    /** The affected parts of the product, such as components, commands or APIs. */
    modules?: string[],
    /** The affected source files. */
    programFiles?: string[],
    /** The affected functions or similar routines in the source. */
    programRoutines?: CveProgramRoutine[],
    /** The platforms the flaw is limited to. Without this, it applies to all of them. */
    platforms?: string[],
    /** The address of the product's source code repository. */
    repo?: string,
    /** The status of every version the versions list does not cover. */
    defaultStatus?: string,
    /** The versions or ranges of versions, each with its status. */
    versions?: CveProductVersion[],
}


/**
 * One affected function, method or similar routine in the source.
 */
export interface CveProgramRoutine {
    /** A name, of a reference or of a routine. */
    name: string,
}


/**
 * A single version or a stretch of versions, and whether it is affected.
 */
export interface CveProductVersion {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** Whether a version is affected. */
    status: string,
    /** The numbering system that says how these versions compare, such as semver or git. */
    versionType?: string,
    /** The first version above the range, which is not itself in it. */
    lessThan?: string,
    /** The last version in the range. */
    lessThanOrEqual?: string,
    /** The points within the range where the status changes. */
    changes?: CveVersionChange[],
}


/**
 * A point in a range of versions from which the status changes.
 */
export interface CveVersionChange {
    /** The version from which a new status starts. */
    at: string,
    /** Whether a version is affected. */
    status: string,
}


/**
 * A statement in the CPE Applicability Language of which platforms are affected.
 */
export interface CveCpeApplicabilityElement {
    /** How the parts combine, all of them or any of them. */
    operator?: string,
    /** Whether the combined result is reversed. */
    negate?: boolean,
    /** The groups of matches that the statement combines. */
    nodes: CveCpeNode[],
}


/**
 * A group of CPE matches, combined by an operator.
 */
export interface CveCpeNode {
    /** How the parts combine, all of them or any of them. */
    operator: string,
    /** Whether the combined result is reversed. */
    negate?: boolean,
    /** The CPE matches in the group. */
    cpeMatch: CveCpeMatch[],
}


/**
 * One CPE name, optionally bounded by versions, and whether it is vulnerable.
 */
export interface CveCpeMatch {
    /** Whether what this match covers is vulnerable. */
    vulnerable: boolean,
    /** The CPE name to match. */
    criteria: string,
    /** A UUID for this match. */
    matchCriteriaId?: string,
    /** The version the match starts just above. */
    versionStartExcluding?: string,
    /** The version the match starts at. */
    versionStartIncluding?: string,
    /** The version the match ends just below. */
    versionEndExcluding?: string,
    /** The version the match ends at. */
    versionEndIncluding?: string,
}


/**
 * A piece of text in one language, with any media that support it.
 */
export interface CveDescription {
    /** The language of the text beside it. */
    lang: string,
    /** The text or content itself. */
    value: string,
    /** Richer forms of the text, such as Markdown or an image. */
    supportingMedia?: CveSupportingMedia[],
}


/**
 * A richer form of a description, as a media type and its content.
 */
export interface CveSupportingMedia {
    /** What kind of thing this is. Each class that uses it says what the choices are. */
    type: string,
    /** The text or content itself. */
    value: string,
    /** Whether value is base64 encoded rather than plain UTF-8. */
    base64?: boolean,
}


/**
 * One kind of problem the vulnerability is, in one or more languages.
 */
export interface CveProblemType {
    /** The same text in one or more languages. */
    descriptions: CveProblemTypeDescription[],
}


/**
 * A problem type described in one language, often by a weakness identifier and its title.
 */
export interface CveProblemTypeDescription {
    /** The language of the text beside it. */
    lang: string,
    /** The text of a problem type, or the title of a weakness. */
    description: string,
    /** What kind of thing this is. Each class that uses it says what the choices are. */
    type?: string,
    /** Links to more about the vulnerability. */
    references?: CveReference[],
    /** The Common Weakness Enumeration identifier that best fits, such as CWE-79. */
    cweId?: string,
}


/**
 * A link to something about the vulnerability, such as an advisory or a patch.
 */
export interface CveReference {
    /** The address the reference points to. */
    url: string,
    /** A name, of a reference or of a routine. */
    name?: string,
    /** Short labels from the upstream's list, or the publisher's own beginning x_. */
    tags?: string[],
}


/**
 * A consequence of the vulnerability, in words.
 */
export interface CveImpact {
    /** The same text in one or more languages. */
    descriptions: CveDescription[],
    /** The Common Attack Pattern Enumeration identifier that best fits, such as CAPEC-63. */
    capecId?: string,
}


/**
 * One scoring of the vulnerability, in a CVSS version or another format, and where it applies.
 */
export interface CveMetric {
    /** The name of the scoring format. */
    format?: string,
    /** The situations this scoring applies to. */
    scenarios?: CveMetricScenario[],
    /** A score under CVSS version 4.0. */
    cvssV4_0?: CvssV40,
    /** A score under CVSS version 3.1. */
    cvssV3_1?: CvssV31,
    /** A score under CVSS version 3.0. */
    cvssV3_0?: CvssV30,
    /** A score under CVSS version 2.0. */
    cvssV2_0?: CvssV20,
    /** A score or impact statement in some other format. */
    other?: CveOtherMetric,
}


/**
 * A situation a scoring applies to, in one language.
 */
export interface CveMetricScenario {
    /** The language of the text beside it. */
    lang: string,
    /** The text or content itself. */
    value: string,
}


/**
 * A score or impact statement in a format the record format does not name.
 */
export interface CveOtherMetric {
    /** What kind of thing this is. Each class that uses it says what the choices are. */
    type: string,
    /** The statement itself, as an object in whatever shape its format has. */
    content: CveOtherMetricContent,
}


/**
 * The free-form object inside a metric of another format.
 */
export interface CveOtherMetricContent {
}


/**
 * One dated event in the vulnerability's history.
 */
export interface CveTimelineEvent {
    /** The language of the text beside it. */
    lang: string,
    /** The text or content itself. */
    value: string,
    /** When the event happened. */
    time: string,
}


/**
 * Thanks to someone who helped, in one language.
 */
export interface CveCredit {
    /** The language of the text beside it. */
    lang: string,
    /** The text or content itself. */
    value: string,
    /** What kind of thing this is. Each class that uses it says what the choices are. */
    type?: string,
    /** The UUID of the credited person, when the CVE user registry holds them. */
    user?: string,
}


/**
 * How the vulnerability came to light, as an object the provider shapes as it likes.
 */
export interface CveSource {
}


/**
 * How the vulnerability relates to one version of an outside taxonomy.
 */
export interface CveTaxonomyMapping {
    /** The name of the taxonomy, such as ATT&CK or CWE. */
    taxonomyName: string,
    /** The version of the taxonomy. */
    taxonomyVersion?: string,
    /** The relationships to items in the taxonomy. */
    taxonomyRelations: CveTaxonomyRelation[],
}


/**
 * One relationship from an item in a taxonomy to this CVE or to another item.
 */
export interface CveTaxonomyRelation {
    /** The item in the taxonomy, which is the relationship's subject. */
    taxonomyId: string,
    /** What the relationship is. */
    relationshipName: string,
    /** The relationship's target, which is this CVE identifier or another taxonomy item. */
    relationshipValue: string,
}


/**
 * Any one CVE record, published or rejected, as a file or an API answer holds it.
 */
export interface CveRecordRoot {
}



