export type VulnerabilityCveId = string;
/**
* Lifecycle state of a vulnerability record.
*/
export enum VulnerabilityStatus {
    
    /** Vulnerability is actively maintained and published. */
    ACTIVE = "ACTIVE",
    /** CVE ID was rejected and should not be used. */
    REJECTED = "REJECTED",
    /** The vulnerability details are disputed by a party. */
    DISPUTED = "DISPUTED",
    /** CVE ID is reserved but details are not yet published. */
    RESERVED = "RESERVED",
    /** Entry has been superseded or withdrawn. */
    DEPRECATED = "DEPRECATED",
};
/**
* CVSS qualitative severity rating.
*/
export enum ImpactSeverity {
    
    /** No measurable impact. */
    NONE = "NONE",
    /** Limited impact; exploitation requires specific conditions. */
    LOW = "LOW",
    /** Moderate impact; partial compromise of security properties. */
    MEDIUM = "MEDIUM",
    /** High impact; significant compromise of security properties. */
    HIGH = "HIGH",
    /** Critical impact; complete compromise; remote exploitation likely. */
    CRITICAL = "CRITICAL",
    /** Severity has not been assessed or is unavailable. */
    UNKNOWN = "UNKNOWN",
};
/**
* Indicates the type of information represented in a CVE JSON instance.
*/
export enum DataType {
    
    /** The instance is a CVE Record. */
    CVE_RECORD = "CVE_RECORD",
};
/**
* Lifecycle state of a CVE Record (PUBLISHED or REJECTED).
*/
export enum RecordState {
    
    /** The CVE ID has associated vulnerability data published in the CVE List. */
    PUBLISHED = "PUBLISHED",
    /** The CVE ID has been rejected and should not be used. */
    REJECTED = "REJECTED",
};
/**
* The vulnerability status of a given version or range of versions of a product.
*/
export enum VersionStatus {
    
    /** The version is affected by the vulnerability. */
    affected = "affected",
    /** The version is not affected by the vulnerability. */
    unaffected = "unaffected",
    /** It is unknown or unspecified whether the version is affected. */
    unknown = "unknown",
};
/**
* A tag describing the type or nature of the resource referenced by a URL.
*/
export enum ReferenceTag {
    
    /** The reference link is returning a 404 error, or the site is no longer online. */
    broken_link = "broken-link",
    /** Similar to Privileges Required, but specific to references that require non-public or paid access for customers of the particular vendor. */
    customer_entitlement = "customer-entitlement",
    /** Reference contains an in-depth description of steps to exploit a vulnerability OR contains legitimate Proof of Concept (PoC) code or an exploit kit. */
    exploit = "exploit",
    /** All reference links that are from a government agency or organization. */
    government_resource = "government-resource",
    /** The reference is a post from a bug tracking tool such as MantisBT, Bugzilla, JIRA, GitHub Issues, etc. */
    issue_tracking = "issue-tracking",
    /** The reference is from a mailing list -- often specific to a product or vendor. */
    mailing_list = "mailing-list",
    /** The reference contains information on steps to mitigate against the vulnerability when a patch cannot be applied or is unavailable, or for EOL product situations. */
    mitigation = "mitigation",
    /** The reference link is not applicable to the vulnerability and was likely associated accidentally (should be used sparingly). */
    not_applicable = "not-applicable",
    /** The reference contains an update to the software that fixes the vulnerability. */
    patch = "patch",
    /** The reference link provided is blocked by a logon page. */
    permissions_required = "permissions-required",
    /** The reference is from a media outlet such as a newspaper, magazine, social media, or weblog. Not intended for individual personal social media accounts. */
    media_coverage = "media-coverage",
    /** A reference appropriate for describing a product for the purpose of CPE or SWID. */
    product = "product",
    /** A reference that is for a related (but not the same) vulnerability. */
    related = "related",
    /** The reference is in the format of a vendor or open source project's release notes or change log. */
    release_notes = "release-notes",
    /** The reference contains a method to detect or prevent the presence or exploitation of the vulnerability. */
    signature = "signature",
    /** The reference contains in-depth technical information about a vulnerability and its exploitation process, typically in the form of a presentation or whitepaper. */
    technical_description = "technical-description",
    /** Advisory is from an organization that is not the vulnerable product's vendor, publisher, or maintainer. */
    third_party_advisory = "third-party-advisory",
    /** Advisory is from the vendor, publisher, or maintainer of the product or the parent organization. */
    vendor_advisory = "vendor-advisory",
    /** VDBs are loosely defined as sites that provide information about this vulnerability, such as advisories, with identifiers. */
    vdb_entry = "vdb-entry",
};
/**
* Tags provided by a CNA describing the CVE Record.
*/
export enum CNATag {
    
    /** When a request for a CVE assignment was received, the product was already end-of-life (EOL) or a product or specific version was deemed not to be supported by the vendor. */
    unsupported_when_assigned = "unsupported-when-assigned",
    /** All known software and/or hardware affected by this CVE Record is known to exist only in the affected hosted service. */
    exclusively_hosted_service = "exclusively-hosted-service",
    /** One party disagrees with another party's assertion that a particular issue in software is a vulnerability. */
    disputed = "disputed",
};
/**
* Tags provided by an ADP describing the CVE Record.
*/
export enum ADPTag {
    
    /** One party disagrees with another party's assertion that a particular issue in software is a vulnerability. */
    disputed = "disputed",
};
/**
* Type or role of the entity being credited.
*/
export enum CreditType {
    
    /** Identifies the vulnerability. */
    finder = "finder",
    /** Notifies the vendor of the vulnerability to a CNA. */
    reporter = "reporter",
    /** Validates the vulnerability to ensure accuracy or severity. */
    analyst = "analyst",
    /** Facilitates the coordinated response process. */
    coordinator = "coordinator",
    /** Prepares a code change or other remediation plans. */
    remediation_developer = "remediation developer",
    /** Reviews vulnerability remediation plans or code changes for effectiveness and completeness. */
    remediation_reviewer = "remediation reviewer",
    /** Tests and verifies the vulnerability or its remediation. */
    remediation_verifier = "remediation verifier",
    /** Names of tools used in vulnerability discovery or identification. */
    tool = "tool",
    /** Supports the vulnerability identification or remediation activities. */
    sponsor = "sponsor",
    /** Other credit type not covered by the above categories. */
    other = "other",
};
/**
* Logical operator used in CPE applicability nodes.
*/
export enum CpeOperator {
    
    /** All CPE match criteria must be satisfied. */
    AND = "AND",
    /** Any one CPE match criterion must be satisfied. */
    OR = "OR",
};
/**
* CVSS 4.0 attack vector base metric.
*/
export enum Cvss4AttackVector {
    
    NETWORK = "NETWORK",
    ADJACENT = "ADJACENT",
    LOCAL = "LOCAL",
    PHYSICAL = "PHYSICAL",
};
/**
* CVSS 4.0 attack complexity base metric.
*/
export enum Cvss4AttackComplexity {
    
    HIGH = "HIGH",
    LOW = "LOW",
};
/**
* CVSS 4.0 attack requirements base metric.
*/
export enum Cvss4AttackRequirements {
    
    NONE = "NONE",
    PRESENT = "PRESENT",
};
/**
* CVSS 4.0 privileges required base metric.
*/
export enum Cvss4PrivilegesRequired {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NONE = "NONE",
};
/**
* CVSS 4.0 user interaction base metric.
*/
export enum Cvss4UserInteraction {
    
    NONE = "NONE",
    PASSIVE = "PASSIVE",
    ACTIVE = "ACTIVE",
};
/**
* CVSS 4.0 vulnerable system confidentiality/integrity/availability impact base metric.
*/
export enum Cvss4VulnCia {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
};
/**
* CVSS 4.0 subsequent system confidentiality/integrity/availability impact base metric.
*/
export enum Cvss4SubCia {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
};
/**
* CVSS 4.0 exploit maturity supplemental metric.
*/
export enum Cvss4ExploitMaturity {
    
    UNREPORTED = "UNREPORTED",
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    ATTACKED = "ATTACKED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 confidentiality/integrity/availability requirement environmental metric.
*/
export enum Cvss4CiaRequirement {
    
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 safety supplemental metric.
*/
export enum Cvss4Safety {
    
    NEGLIGIBLE = "NEGLIGIBLE",
    PRESENT = "PRESENT",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 automatable supplemental metric.
*/
export enum Cvss4Automatable {
    
    /** The attack cannot be automated. */
    NO = "NO",
    /** The attack can be automated. */
    YES = "YES",
    /** Automatable status is not defined. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 recovery supplemental metric.
*/
export enum Cvss4Recovery {
    
    AUTOMATIC = "AUTOMATIC",
    USER = "USER",
    IRRECOVERABLE = "IRRECOVERABLE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 value density supplemental metric.
*/
export enum Cvss4ValueDensity {
    
    DIFFUSE = "DIFFUSE",
    CONCENTRATED = "CONCENTRATED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 vulnerability response effort supplemental metric.
*/
export enum Cvss4VulnerabilityResponseEffort {
    
    LOW = "LOW",
    MODERATE = "MODERATE",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 provider urgency supplemental metric.
*/
export enum Cvss4ProviderUrgency {
    
    CLEAR = "CLEAR",
    GREEN = "GREEN",
    AMBER = "AMBER",
    RED = "RED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 qualitative severity rating.
*/
export enum Cvss4Severity {
    
    NONE = "NONE",
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    CRITICAL = "CRITICAL",
};
/**
* CVSS 4.0 modified attack vector environmental metric.
*/
export enum Cvss4ModifiedAttackVector {
    
    NETWORK = "NETWORK",
    ADJACENT = "ADJACENT",
    LOCAL = "LOCAL",
    PHYSICAL = "PHYSICAL",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified attack complexity environmental metric.
*/
export enum Cvss4ModifiedAttackComplexity {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified attack requirements environmental metric.
*/
export enum Cvss4ModifiedAttackRequirements {
    
    NONE = "NONE",
    PRESENT = "PRESENT",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified privileges required environmental metric.
*/
export enum Cvss4ModifiedPrivilegesRequired {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NONE = "NONE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified user interaction environmental metric.
*/
export enum Cvss4ModifiedUserInteraction {
    
    NONE = "NONE",
    PASSIVE = "PASSIVE",
    ACTIVE = "ACTIVE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified vulnerable system CIA environmental metric.
*/
export enum Cvss4ModifiedVulnCia {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified subsequent system confidentiality environmental metric.
*/
export enum Cvss4ModifiedSubC {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 4.0 modified subsequent system integrity/availability environmental metric (includes SAFETY value).
*/
export enum Cvss4ModifiedSubIa {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
    SAFETY = "SAFETY",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS version 3.x identifier. CVSS 3.0 and 3.1 share an identical metric model; the 3.1 spec was a clarification, not a structural change. The consolidated CvssV3 class accepts either via this enum.
*/
export enum CvssV3Version {
    
    /** CVSS version 3.0 (2015-2019) */
    number_3FULL_STOP0 = "3.0",
    /** CVSS version 3.1 (2019-present) */
    number_3FULL_STOP1 = "3.1",
};
/**
* CVSS 3.x attack vector base metric.
*/
export enum Cvss3AttackVector {
    
    NETWORK = "NETWORK",
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    LOCAL = "LOCAL",
    PHYSICAL = "PHYSICAL",
};
/**
* CVSS 3.x attack complexity base metric.
*/
export enum Cvss3AttackComplexity {
    
    HIGH = "HIGH",
    LOW = "LOW",
};
/**
* CVSS 3.x privileges required base metric.
*/
export enum Cvss3PrivilegesRequired {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NONE = "NONE",
};
/**
* CVSS 3.x user interaction base metric.
*/
export enum Cvss3UserInteraction {
    
    NONE = "NONE",
    REQUIRED = "REQUIRED",
};
/**
* CVSS 3.x scope base metric.
*/
export enum Cvss3Scope {
    
    UNCHANGED = "UNCHANGED",
    CHANGED = "CHANGED",
};
/**
* CVSS 3.x confidentiality/integrity/availability impact base metric.
*/
export enum Cvss3Cia {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
};
/**
* CVSS 3.x qualitative severity rating.
*/
export enum Cvss3Severity {
    
    NONE = "NONE",
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    CRITICAL = "CRITICAL",
};
/**
* CVSS 3.x exploit code maturity temporal metric.
*/
export enum Cvss3ExploitCodeMaturity {
    
    UNPROVEN = "UNPROVEN",
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    FUNCTIONAL = "FUNCTIONAL",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x remediation level temporal metric.
*/
export enum Cvss3RemediationLevel {
    
    OFFICIAL_FIX = "OFFICIAL_FIX",
    TEMPORARY_FIX = "TEMPORARY_FIX",
    WORKAROUND = "WORKAROUND",
    UNAVAILABLE = "UNAVAILABLE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x report confidence temporal metric.
*/
export enum Cvss3Confidence {
    
    UNKNOWN = "UNKNOWN",
    REASONABLE = "REASONABLE",
    CONFIRMED = "CONFIRMED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x CIA requirement environmental metric.
*/
export enum Cvss3CiaRequirement {
    
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified attack vector environmental metric.
*/
export enum Cvss3ModifiedAttackVector {
    
    NETWORK = "NETWORK",
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    LOCAL = "LOCAL",
    PHYSICAL = "PHYSICAL",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified attack complexity environmental metric.
*/
export enum Cvss3ModifiedAttackComplexity {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified privileges required environmental metric.
*/
export enum Cvss3ModifiedPrivilegesRequired {
    
    HIGH = "HIGH",
    LOW = "LOW",
    NONE = "NONE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified user interaction environmental metric.
*/
export enum Cvss3ModifiedUserInteraction {
    
    NONE = "NONE",
    REQUIRED = "REQUIRED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified scope environmental metric.
*/
export enum Cvss3ModifiedScope {
    
    UNCHANGED = "UNCHANGED",
    CHANGED = "CHANGED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 3.x modified CIA environmental metric.
*/
export enum Cvss3ModifiedCia {
    
    NONE = "NONE",
    LOW = "LOW",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 access vector base metric.
*/
export enum Cvss2AccessVector {
    
    NETWORK = "NETWORK",
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    LOCAL = "LOCAL",
};
/**
* CVSS 2.0 access complexity base metric.
*/
export enum Cvss2AccessComplexity {
    
    HIGH = "HIGH",
    MEDIUM = "MEDIUM",
    LOW = "LOW",
};
/**
* CVSS 2.0 authentication base metric.
*/
export enum Cvss2Authentication {
    
    MULTIPLE = "MULTIPLE",
    SINGLE = "SINGLE",
    NONE = "NONE",
};
/**
* CVSS 2.0 confidentiality/integrity/availability impact base metric.
*/
export enum Cvss2Cia {
    
    NONE = "NONE",
    PARTIAL = "PARTIAL",
    COMPLETE = "COMPLETE",
};
/**
* CVSS 2.0 exploitability temporal metric.
*/
export enum Cvss2Exploitability {
    
    UNPROVEN = "UNPROVEN",
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    FUNCTIONAL = "FUNCTIONAL",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 remediation level temporal metric.
*/
export enum Cvss2RemediationLevel {
    
    OFFICIAL_FIX = "OFFICIAL_FIX",
    TEMPORARY_FIX = "TEMPORARY_FIX",
    WORKAROUND = "WORKAROUND",
    UNAVAILABLE = "UNAVAILABLE",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 report confidence temporal metric.
*/
export enum Cvss2ReportConfidence {
    
    UNCONFIRMED = "UNCONFIRMED",
    UNCORROBORATED = "UNCORROBORATED",
    CONFIRMED = "CONFIRMED",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 collateral damage potential environmental metric.
*/
export enum Cvss2CollateralDamagePotential {
    
    NONE = "NONE",
    LOW = "LOW",
    LOW_MEDIUM = "LOW_MEDIUM",
    MEDIUM_HIGH = "MEDIUM_HIGH",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 target distribution environmental metric.
*/
export enum Cvss2TargetDistribution {
    
    NONE = "NONE",
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* CVSS 2.0 CIA requirement environmental metric.
*/
export enum Cvss2CiaRequirement {
    
    LOW = "LOW",
    MEDIUM = "MEDIUM",
    HIGH = "HIGH",
    NOT_DEFINED = "NOT_DEFINED",
};


/**
 * Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
 */
export interface Vulnerability {
    /** The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN. */
    cve_id: string,
    /** Short human-readable title or name for this entity. */
    title?: string,
    /** Narrative description of the vulnerability. */
    description?: string,
    /** Date and time the vulnerability was first published. */
    published_date?: string,
    /** Date and time the vulnerability record was last modified. */
    last_modified_date?: string,
    /** Products affected by this vulnerability. */
    products?: Product[],
    /** Weakness classifications (e.g. CWE) associated with this vulnerability. */
    weaknesses?: Weakness[],
    /** External references such as advisories and articles. */
    references?: Reference[],
    /** Impact and severity assessment for this vulnerability. */
    impact?: Impact,
    /** Current lifecycle state of the vulnerability record. */
    status?: string,
}


/**
 * Software or hardware entity affected by the vulnerability.
 */
export interface Product {
    /** Name of the vendor or organization responsible for the product. */
    vendor?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Version string of the affected product. */
    version?: string,
    /** Platforms or operating environments affected. */
    platforms?: string[],
}


/**
 * External reference such as an advisory or article.
 */
export interface Reference {
    /** URL pointing to the reference resource. */
    url?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Source or origin of the reference or data. */
    source?: string,
}


/**
 * Weakness classification from CWE or a similar taxonomy.
 */
export interface Weakness {
    /** CWE identifier for the weakness classification (e.g. CWE-79). */
    cwe_id?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Narrative description of the vulnerability. */
    description?: string,
}


/**
 * Assessment of the vulnerability's impact and severity.
 */
export interface Impact {
    /** Qualitative severity rating. */
    severity?: string,
    /** CVSS vector string or equivalent scoring vector expression. */
    vector?: string,
    /** Numeric vulnerability score (e.g. CVSS base score). */
    score?: number,
}


/**
 * Logical grouping of CPE match expressions.
 */
export interface Configuration {
    /** CPE 2.2 URI identifying an affected product configuration. */
    cpe_uri?: string,
    /** Logical operator (AND/OR) used in configuration node groupings. */
    operator?: string,
}


/**
 * A linkml placeholder class accepting any JSON-compatible value (string, number, boolean, object, or array). Use for slots that hold arbitrary or schema-less data.
 */
export interface Any {
}


/**
 * Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™ Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected records.
This class deliberately does NOT inherit from ``vulnerability_core.Vulnerability``: the upstream CVE Record Format places the CVE ID inside ``cveMetadata.cveId`` rather than at the record root. Semantic equivalence with the broader ``Vulnerability`` concept is preserved via ``exact_mappings``.
 */
export interface CVERecord {
    /** Indicates the type of information represented in the JSON instance. */
    data_type?: string,
    /** The version of the CVE schema used for validating this record. Supports multiple versions of the format (e.g., '5.2.0'). */
    data_version?: string,
    /** Metadata about the CVE ID. A Published record uses CveMetadataPublished; a Rejected record uses CveMetadataRejected. */
    cve_metadata: CveMetadata,
    /** A set of containers (CNA and optionally ADP) holding vulnerability information related to the CVE ID. */
    containers: Containers,
}


/**
 * Abstract base for CVE Record metadata. Represents either a Published or Rejected record's metadata. All fields are controlled by CVE Services. Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CveMetadataPublished``, ``CveMetadataRejected``); slot-level ``any_of`` on the ``cve_metadata`` slot preserves the choice for generators (e.g. JSON Schema ``anyOf``).
 */
export interface CveMetadata {
}


/**
 * Metadata for a CVE Record in the PUBLISHED state.
 */
export interface CveMetadataPublished extends CveMetadata {
    /** The CVE identifier that this record pertains to. */
    record_cve_id: string,
    /** The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service. */
    assigner_org_id: string,
    /** The short name for the organization to which the CVE ID was originally assigned. */
    assigner_short_name?: string,
    /** Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record. */
    serial?: number,
    /** The date/time the record was last updated. */
    date_updated?: string,
    /** The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed. */
    date_reserved?: string,
    /** The user that requested the CVE identifier. */
    requester_user_id?: string,
    /** The date/time the CVE Record was first published in the CVE List. */
    date_published?: string,
    /** State of the CVE Record. For published records, this is always PUBLISHED. */
    published_state: string,
}


/**
 * Metadata for a CVE Record in the REJECTED state.
 */
export interface CveMetadataRejected extends CveMetadata {
    /** The CVE identifier that this record pertains to. */
    record_cve_id: string,
    /** The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service. */
    assigner_org_id: string,
    /** The short name for the organization to which the CVE ID was originally assigned. */
    assigner_short_name?: string,
    /** Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record. */
    serial?: number,
    /** The date/time the record was last updated. */
    date_updated?: string,
    /** The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed. */
    date_reserved?: string,
    /** The date/time the CVE Record was first published in the CVE List. */
    date_published?: string,
    /** The date/time the CVE ID was rejected. */
    date_rejected?: string,
    /** State of the CVE Record. For rejected records, this is always REJECTED. */
    rejected_state: string,
}


/**
 * A set of structures (called containers) used to store vulnerability information related to a specific CVE ID. At minimum a 'cna' container is required.
 */
export interface Containers {
    /** The CNA container holding vulnerability information for this CVE ID. For published records, this is a CnaPublishedContainer. For rejected records, this is a CnaRejectedContainer. */
    cna: CnaContainer,
    /** One or more ADP containers providing additional vulnerability information. Multiple ADPs may contribute containers for the same CVE ID. */
    adp?: AdpContainer[],
}


/**
 * Details related to the information container provider (CNA or ADP).
 */
export interface ProviderMetadata {
    /** The container provider's organizational UUID. */
    org_id: string,
    /** The container provider's organizational short name (2-32 characters). */
    short_name?: string,
    /** The date/time the record was last updated. */
    date_updated?: string,
}


/**
 * Abstract base for CNA containers (published and rejected). Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CnaPublishedContainer``, ``CnaRejectedContainer``); slot-level ``any_of`` on the ``cna`` slot preserves the choice for generators.
 */
export interface CnaContainer {
}


/**
 * An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a published CVE ID. There can only be one CNA container per CVE record since there can only be one assigning CNA.
 */
export interface CnaPublishedContainer extends CnaContainer {
    /** Details related to the information container provider (CNA or ADP). */
    provider_metadata: ProviderMetadata,
    /** The date/time this CVE ID was associated with a vulnerability by a CNA. */
    date_assigned?: string,
    /** If known, the date/time the vulnerability was disclosed publicly. */
    date_public?: string,
    /** Short human-readable title or name for this entity. */
    title?: string,
    /** A list of multi-lingual descriptions of the vulnerability. Must contain at least one English language entry. E.g., [PROBLEMTYPE] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [VECTOR]. */
    descriptions: MultiLangDescription[],
    /** List of affected products and services. */
    affected: AffectedProduct[],
    /** Affected products defined using the CPE Applicability Language. When defined, this block should align with the data in the affected block. */
    cpe_applicability?: CpeApplicabilityElement[],
    /** Problem type information such as CWE identifiers. Must contain at least one entry. Entries can be text, OWASP, or CWE identifiers. */
    problem_types?: ProblemType[],
    /** Reference data in the form of URLs describing the vulnerability, such as advisories, patches, and exploit details. Required by CNA rules. */
    cve_references: CveReference[],
    /** Collection of impacts of this vulnerability, optionally linked to CAPEC IDs. */
    impacts?: ImpactEntry[],
    /** Collection of impact scores with attribution (CVSSv2, CVSSv3.0, CVSSv3.1, CVSSv4.0, or custom format). */
    metrics?: MetricEntry[],
    /** Configurations required for exploiting this vulnerability. */
    configurations_text?: MultiLangDescription[],
    /** Workarounds and mitigations for this vulnerability. */
    workarounds?: MultiLangDescription[],
    /** Information about solutions or remediations available for this vulnerability. */
    solutions?: MultiLangDescription[],
    /** Information about known exploits of this vulnerability. */
    exploits?: MultiLangDescription[],
    /** Timeline information for significant events about the vulnerability or changes to the CVE Record. */
    timeline?: TimelineEntry[],
    /** Statements acknowledging specific people, organizations, or tools for work related to research, discovery, remediation, or coordination of this CVE. */
    credits?: CreditEntry[],
    /** Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. */
    cna_source?: SourceInformation,
    /** Tags provided by a CNA describing the CVE Record. */
    cna_tags?: string[],
    /** List of taxonomy items (e.g., ATT&CK, CWE) related to the vulnerability. */
    taxonomy_mappings?: TaxonomyMapping[],
}


/**
 * An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a rejected CVE ID. There can only be one CNA container per CVE record.
 */
export interface CnaRejectedContainer extends CnaContainer {
    /** Details related to the information container provider (CNA or ADP). */
    provider_metadata: ProviderMetadata,
    /** Reasons for rejecting this CVE Record. */
    rejected_reasons: MultiLangDescription[],
    /** CVE IDs that this CVE ID was rejected in favor of because this CVE ID was incorrectly assigned to the same vulnerabilities. */
    replaced_by?: string[],
}


/**
 * An object containing vulnerability information provided by an Authorized Data Publisher (ADP). Multiple ADPs can provide containers for a single CVE ID.
 */
export interface AdpContainer {
    /** Details related to the information container provider (CNA or ADP). */
    provider_metadata: ProviderMetadata,
    /** If known, the date/time the vulnerability was disclosed publicly. */
    date_public?: string,
    /** Short human-readable title or name for this entity. */
    title?: string,
    /** A list of multi-lingual descriptions of the vulnerability. Must contain at least one English language entry. E.g., [PROBLEMTYPE] in [COMPONENT] in [VENDOR] [PRODUCT] [VERSION] on [PLATFORMS] allows [ATTACKER] to [IMPACT] via [VECTOR]. */
    descriptions?: MultiLangDescription[],
    /** List of affected products and services. */
    affected?: AffectedProduct[],
    /** Affected products defined using the CPE Applicability Language. When defined, this block should align with the data in the affected block. */
    cpe_applicability?: CpeApplicabilityElement[],
    /** Problem type information such as CWE identifiers. Must contain at least one entry. Entries can be text, OWASP, or CWE identifiers. */
    problem_types?: ProblemType[],
    /** Reference data in the form of URLs describing the vulnerability, such as advisories, patches, and exploit details. Required by CNA rules. */
    cve_references?: CveReference[],
    /** Collection of impacts of this vulnerability, optionally linked to CAPEC IDs. */
    impacts?: ImpactEntry[],
    /** Collection of impact scores with attribution (CVSSv2, CVSSv3.0, CVSSv3.1, CVSSv4.0, or custom format). */
    metrics?: MetricEntry[],
    /** Configurations required for exploiting this vulnerability. */
    configurations_text?: MultiLangDescription[],
    /** Workarounds and mitigations for this vulnerability. */
    workarounds?: MultiLangDescription[],
    /** Information about solutions or remediations available for this vulnerability. */
    solutions?: MultiLangDescription[],
    /** Information about known exploits of this vulnerability. */
    exploits?: MultiLangDescription[],
    /** Timeline information for significant events about the vulnerability or changes to the CVE Record. */
    timeline?: TimelineEntry[],
    /** Statements acknowledging specific people, organizations, or tools for work related to research, discovery, remediation, or coordination of this CVE. */
    credits?: CreditEntry[],
    /** Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. */
    cna_source?: SourceInformation,
    /** Tags provided by an ADP describing the CVE Record. */
    adp_tags?: string[],
    /** List of taxonomy items (e.g., ATT&CK, CWE) related to the vulnerability. */
    taxonomy_mappings?: TaxonomyMapping[],
}


/**
 * Information about the set of products and services affected by a vulnerability. At least one of (vendor + product) or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.
Note: this class deliberately does NOT inherit from ``vulnerability_core.Product``. The upstream CVE ``product`` definition uses a multivalued ``versions`` slot (range ``VersionEntry``), which conflicts with ``Product.version`` (singular string). The ``vendor``, ``name`` (= upstream ``product``), and ``platforms`` slots are reused from the core schema directly. Semantic equivalence is preserved via ``exact_mappings``.
 */
export interface AffectedProduct {
    /** Name of the vendor or organization responsible for the product. */
    vendor?: string,
    /** Name of the affected product (upstream field ``product``). */
    name?: string,
    /** Platforms or operating environments affected. */
    platforms?: string[],
    /** URL identifying a package collection (determines the meaning of packageName). */
    collection_url?: string,
    /** Name or identifier of the affected software package as used in the package collection. */
    package_name?: string,
    /** Affected products defined by CPE (Common Platform Enumeration) names in either 2.2 or 2.3 format. */
    cpes?: string[],
    /** A list of the affected components, features, modules, sub-components, sub-products, APIs, commands, utilities, programs, or functionalities. */
    modules?: string[],
    /** A list of the affected source code files. */
    program_files?: string[],
    /** A list of the affected source code functions, methods, subroutines, or procedures. */
    program_routines?: ProgramRoutine[],
    /** The URL of the source code repository, for informational purposes and/or to resolve git hash version ranges. */
    repo?: string,
    /** The default status for versions not otherwise listed in the versions list. Defaults to 'unknown' if not specified. Versions or defaultStatus may be omitted, but not both. */
    default_status?: string,
    /** Set of product versions or version ranges related to the vulnerability. Versions or defaultStatus may be omitted, but not both. */
    versions?: VersionEntry[],
    /** A Package URL (PURL), a unified URL specification for identifying packages hosted by known package hosts. The Package URL MUST NOT include a version. */
    package_url?: string,
}


/**
 * An affected source code function, method, subroutine, or procedure.
 */
export interface ProgramRoutine {
    /** Name of the affected source code function, method, subroutine, or procedure. */
    routine_name: string,
}


/**
 * A single version or a range of versions of a product with associated vulnerability status. An entry with only version and status is a point version; an entry with versionType and a less-than limit describes a range.
 */
export interface VersionEntry {
    /** The single version being described, or the version at the start of the range. By convention, '0' denotes the earliest possible version. */
    version_value: string,
    /** The vulnerability status for the version or range of versions. For a range, the status may be refined by the 'changes' list. */
    version_status: string,
    /** The version numbering system used for specifying the range (e.g., semver, git, maven, rpm, python, custom). Defines the semantics of comparison. */
    version_type?: string,
    /** The non-inclusive upper limit of the range. This is the least version NOT in the range. Supports wildcard '*' suffix. */
    less_than?: string,
    /** The inclusive upper limit of the range. This is the greatest version contained in the range. Only one of lessThan and lessThanOrEqual should be specified. */
    less_than_or_equal?: string,
    /** A list of status changes that take place during the version range. The array should be sorted by 'at' field according to versionType, but clients must re-sort rather than assume ordering. */
    version_changes?: VersionChange[],
}


/**
 * A status change that takes place at a specific point within a version range.
 */
export interface VersionChange {
    /** The version at which a status change occurs within a range. */
    change_at: string,
    /** The new status in the range starting at the given version. */
    change_status: string,
}


/**
 * Text in a particular language with optional alternate markup or formatted representation (e.g., Markdown) or embedded media. Used for vulnerability descriptions, rejected reasons, configurations, workarounds, solutions, and exploits.
 */
export interface MultiLangDescription {
    /** BCP 47 language code indicating the language of accompanying text. */
    lang: string,
    /** Plain text description (up to 4096 characters). */
    description_value: string,
    /** Supporting media data for the description such as markdown, diagrams, etc. Similar to RFC 2397, each object has a media type, data value, and optional base64 flag. */
    supporting_media?: SupportingMedia[],
}


/**
 * Supporting media data for a description such as markdown, diagrams, etc. Similar to RFC 2397, each media object has a media type, data value, and an optional base64 flag.
 */
export interface SupportingMedia {
    /** RFC2046 compliant IANA Media type (e.g., text/markdown, text/html, image/png, image/svg, audio/mp3). */
    media_type: string,
    /** If true, the media_value field contains the media data encoded in base64. If false, the media_value field contains UTF-8 media content. */
    base64_encoded?: boolean,
    /** Supporting media content, up to 16K characters. If base64_encoded is true, this stores base64 encoded data. */
    media_value: string,
}


/**
 * Problem type information (e.g., CWE identifier). Wraps one or more problem type descriptions. The CNA requirement is [PROBLEMTYPE].
 */
export interface ProblemType {
    /** One or more problem type descriptions (e.g., CWE IDs or OWASP categories). */
    problem_type_descriptions: ProblemTypeDescription[],
}


/**
 * Individual problem type description entry.
 */
export interface ProblemTypeDescription {
    /** BCP 47 language code indicating the language of accompanying text. */
    lang: string,
    /** Text description of the problem type, or title from CWE or OWASP. */
    problem_description: string,
    /** CWE identifier for the weakness classification (e.g. CWE-79). */
    cwe_id?: string,
    /** Problem type source format (e.g., text, OWASP, CWE). */
    problem_source_type?: string,
    /** References supporting this specific problem type. */
    problem_references?: CveReference[],
}


/**
 * An external reference associated with a CVE Record. Extends the core Reference with optional descriptive tags characterizing the resource.
 */
export interface CveReference extends Reference {
    /** An array of tags describing the resource referenced by the URL. */
    reference_tags?: string,
}


/**
 * An impact entry linking an optional CAPEC attack pattern ID to one or more prose descriptions of the impact scenario.
 */
export interface ImpactEntry {
    /** CAPEC ID that best relates to this impact (e.g., CAPEC-123). */
    capec_id?: string,
    /** Prose description of the impact scenario. At a minimum, provide the description given by CAPEC. */
    impact_descriptions: MultiLangDescription[],
}


/**
 * A metric entry containing scoring data in one of the CVSS formats (v4.0, v3.x, v2.0) or a custom format, with optional applicability scenarios. At least one of cvss_v4_0, cvss_v3, cvss_v2_0, or other_metric is required. CVSS 3.0 and 3.1 are both represented by CvssV3 (distinguished by the cvss3_version slot).
 */
export interface MetricEntry {
    /** Name of the scoring format (e.g., cvssV4_0, cvssV3_1). Provides future-proofing and supports proprietary format inclusion. */
    metric_format?: string,
    /** Scenarios this metrics object applies to. If no specific scenario is given, GENERAL applies when no more specific metric matches. */
    metric_scenarios?: MetricScenario[],
    /** CVSS version 4.0 scoring data. */
    cvss_v4_0?: CvssV40,
    /** CVSS version 3.x scoring data (covers both 3.0 and 3.1). The version is distinguished by the cvss3_version field within the CvssV3 object. */
    cvss_v3?: CvssV3,
    /** CVSS version 2.0 scoring data. */
    cvss_v2_0?: CvssV20,
    /** A non-standard impact description or score. */
    other_metric?: OtherMetric,
}


/**
 * A scenario description indicating the context in which a metric applies. If no specific scenario is given, GENERAL is used as the default.
 */
export interface MetricScenario {
    /** BCP 47 language code indicating the language of accompanying text. */
    lang: string,
    /** Description of the scenario this metrics object applies to. */
    scenario_value: string,
}


/**
 * CVSS version 4.0 scoring object. Requires version, vectorString, baseScore, and baseSeverity. All other fields are optional.
 */
export interface CvssV40 {
    /** CVSS version identifier. Must be '4.0' for CVSS v4.0 objects. */
    cvss4_version: string,
    /** CVSS 4.0 vector string encoding all base, threat, and environmental metrics. */
    cvss4_vector_string: string,
    /** CVSS 4.0 base score (0.0 – 10.0 in 0.1 increments). */
    cvss4_base_score: number,
    /** CVSS 4.0 qualitative base severity rating. */
    cvss4_base_severity: string,
    cvss4_attack_vector?: string,
    cvss4_attack_complexity?: string,
    cvss4_attack_requirements?: string,
    cvss4_privileges_required?: string,
    cvss4_user_interaction?: string,
    cvss4_vuln_confidentiality_impact?: string,
    cvss4_vuln_integrity_impact?: string,
    cvss4_vuln_availability_impact?: string,
    cvss4_sub_confidentiality_impact?: string,
    cvss4_sub_integrity_impact?: string,
    cvss4_sub_availability_impact?: string,
    cvss4_exploit_maturity?: string,
    cvss4_confidentiality_requirement?: string,
    cvss4_integrity_requirement?: string,
    cvss4_availability_requirement?: string,
    cvss4_modified_attack_vector?: string,
    cvss4_modified_attack_complexity?: string,
    cvss4_modified_attack_requirements?: string,
    cvss4_modified_privileges_required?: string,
    cvss4_modified_user_interaction?: string,
    cvss4_modified_vuln_confidentiality_impact?: string,
    cvss4_modified_vuln_integrity_impact?: string,
    cvss4_modified_vuln_availability_impact?: string,
    cvss4_modified_sub_confidentiality_impact?: string,
    cvss4_modified_sub_integrity_impact?: string,
    cvss4_modified_sub_availability_impact?: string,
    cvss4_safety?: string,
    cvss4_automatable?: string,
    cvss4_recovery?: string,
    cvss4_value_density?: string,
    cvss4_vulnerability_response_effort?: string,
    cvss4_provider_urgency?: string,
}


/**
 * CVSS version 3.x scoring object covering both CVSS 3.0 and CVSS 3.1. The two versions share an identical metric model; the 3.1 spec was a clarification, not a structural change. The cvss3_version slot distinguishes between them. Requires version ('3.0' or '3.1'), vectorString, baseScore, and baseSeverity.
 */
export interface CvssV3 {
    /** CVSS version identifier ('3.0' or '3.1') within a CvssV3 object. */
    cvss3_version: string,
    /** CVSS 3.x vector string encoding all metric values. CVSS 3.1 strings begin with 'CVSS:3.1/'; CVSS 3.0 strings begin with 'CVSS:3.0/'. */
    cvss3_vector_string: string,
    cvss3_attack_vector?: string,
    cvss3_attack_complexity?: string,
    cvss3_privileges_required?: string,
    cvss3_user_interaction?: string,
    cvss3_scope?: string,
    cvss3_confidentiality_impact?: string,
    cvss3_integrity_impact?: string,
    cvss3_availability_impact?: string,
    /** CVSS 3.x base score (0.0 – 10.0 in 0.1 increments). */
    cvss3_base_score: number,
    cvss3_base_severity: string,
    cvss3_exploit_code_maturity?: string,
    cvss3_remediation_level?: string,
    cvss3_report_confidence?: string,
    /** CVSS 3.x temporal score. */
    cvss3_temporal_score?: number,
    cvss3_temporal_severity?: string,
    cvss3_confidentiality_requirement?: string,
    cvss3_integrity_requirement?: string,
    cvss3_availability_requirement?: string,
    cvss3_modified_attack_vector?: string,
    cvss3_modified_attack_complexity?: string,
    cvss3_modified_privileges_required?: string,
    cvss3_modified_user_interaction?: string,
    cvss3_modified_scope?: string,
    cvss3_modified_confidentiality_impact?: string,
    cvss3_modified_integrity_impact?: string,
    cvss3_modified_availability_impact?: string,
    /** CVSS 3.x environmental score. */
    cvss3_environmental_score?: number,
    cvss3_environmental_severity?: string,
}


/**
 * CVSS version 2.0 scoring object. Requires version ('2.0'), vectorString, and baseScore.
 */
export interface CvssV20 {
    /** CVSS version identifier. Must be '2.0' for CVSS v2.0 objects. */
    cvss2_version: string,
    /** CVSS 2.0 vector string encoding all base, temporal, and environmental metrics. */
    cvss2_vector_string: string,
    cvss2_access_vector?: string,
    cvss2_access_complexity?: string,
    cvss2_authentication?: string,
    cvss2_confidentiality_impact?: string,
    cvss2_integrity_impact?: string,
    cvss2_availability_impact?: string,
    /** CVSS 2.0 base score (0.0 – 10.0). */
    cvss2_base_score: number,
    cvss2_exploitability?: string,
    cvss2_remediation_level?: string,
    cvss2_report_confidence?: string,
    /** CVSS 2.0 temporal score. */
    cvss2_temporal_score?: number,
    cvss2_collateral_damage_potential?: string,
    cvss2_target_distribution?: string,
    cvss2_confidentiality_requirement?: string,
    cvss2_integrity_requirement?: string,
    cvss2_availability_requirement?: string,
    /** CVSS 2.0 environmental score. */
    cvss2_environmental_score?: number,
}


/**
 * A non-standard impact description in a custom format. May be a prose description or an arbitrary JSON-compatible object.
 */
export interface OtherMetric {
    /** Name of the non-standard impact metrics format used. */
    other_metric_type: string,
    /** Arbitrary JSON-compatible object (or prose string) containing non-standard metric data not covered by the CVSS formats. Upstream JSON Schema defines this as 'type: object, minProperties: 1'; range: Any allows any value. */
    other_metric_content: Any,
}


/**
 * A timeline event recording a significant event about the vulnerability or changes to the CVE Record. Requires time, lang, and value.
 */
export interface TimelineEntry {
    /** Timestamp representing when the event in the timeline occurred. Format is RFC3339 / ISO8601 with optional timezone. */
    event_time: string,
    /** BCP 47 language code indicating the language of accompanying text. */
    lang: string,
    /** A summary of the timeline event (up to 4096 characters). */
    event_value: string,
}


/**
 * A credit acknowledging a specific person, organization, or tool for work related to the research, discovery, remediation, or coordination of the vulnerability.
 */
export interface CreditEntry {
    /** BCP 47 language code indicating the language of accompanying text. */
    lang: string,
    /** The name or description of the credited party (up to 4096 characters). */
    credit_value: string,
    /** UUID of the user being credited, if present in the CVE User Registry. This UUID can be used to lookup the user record in the user registry service. */
    credit_user?: string,
    /** Type or role of the entity being credited. */
    credit_type?: string,
}


/**
 * Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. This is an open object — at least one property must be present.
 */
export interface SourceInformation {
    /** Bug tracking system IDs (e.g., JIRA ticket IDs) related to the vulnerability. */
    source_defects?: string[],
    /** Advisory identifier associated with the vulnerability discovery. */
    source_advisory?: string,
    /** How the vulnerability was discovered (e.g., INTERNAL, EXTERNAL, USER). */
    source_discovery?: string,
}


/**
 * A taxonomy mapping identifying the taxonomy by name and version, along with a list of relations relevant to the CVE (e.g., ATT&CK, D3FEND, CWE).
 */
export interface TaxonomyMapping {
    /** The name of the taxonomy (e.g., ATT&CK, D3FEND, CWE, CVSS). */
    taxonomy_name: string,
    /** The version of the taxonomy the identifiers come from. */
    taxonomy_version?: string,
    /** List of relationships to the taxonomy for this vulnerability. */
    taxonomy_relations: TaxonomyRelation[],
}


/**
 * A relationship between a taxonomy item and a CVE or another taxonomy item. Provides subject (taxonomyId), predicate (relationshipName), and object (relationshipValue).
 */
export interface TaxonomyRelation {
    /** Identifier of the item in the taxonomy. Used as the subject of the relationship. */
    taxonomy_id: string,
    /** A description of the relationship between the taxonomy item and the CVE. */
    relationship_name: string,
    /** The target of the relationship. Can be the CVE ID or another taxonomy identifier. */
    relationship_value: string,
}


/**
 * Affected products defined using an implementation of the CPE Applicability Language. An operator property allows AND or OR logic between CPEs or combinations of CPEs.
 */
export interface CpeApplicabilityElement {
    /** Logical operator (AND/OR) used between CPE criteria in this node. */
    cpe_operator?: string,
    /** If true, negates the applicability of this element. */
    cpe_negate?: boolean,
    /** Array of CPE configuration nodes. */
    cpe_nodes: CpeNode[],
}


/**
 * Defines a CPE configuration node in an applicability statement.
 */
export interface CpeNode {
    /** Logical operator (AND/OR) used between CPE criteria in this node. */
    cpe_operator: string,
    /** If true, negates the applicability of this element. */
    cpe_negate?: boolean,
    /** Array of CPE match criteria within this node. */
    cpe_match_criteria: CpeMatch[],
}


/**
 * CPE match string or range within a CPE applicability node.
 */
export interface CpeMatch {
    /** Whether this CPE match describes a vulnerable configuration. */
    cpe_vulnerable: boolean,
    /** CPE 2.3 formatted name match string or match criteria. */
    cpe_criteria: string,
    /** UUID identifying the CPE match criteria set. */
    match_criteria_id?: string,
    /** The start of a version range, exclusive (versions strictly greater than this). */
    version_start_excluding?: string,
    /** The start of a version range, inclusive (versions greater than or equal to this). */
    version_start_including?: string,
    /** The end of a version range, exclusive (versions strictly less than this). */
    version_end_excluding?: string,
    /** The end of a version range, inclusive (versions less than or equal to this). */
    version_end_including?: string,
}



