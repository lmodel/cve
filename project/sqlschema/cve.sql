-- # Class: Any Description: A linkml placeholder class accepting any JSON-compatible value (string, number, boolean, object, or array). Use for slots that hold arbitrary or schema-less data.
--     * Slot: id
-- # Class: CVERecord Description: Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™ Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected records.This class deliberately does NOT inherit from ``vulnerability_core.Vulnerability``: the upstream CVE Record Format places the CVE ID inside ``cveMetadata.cveId`` rather than at the record root. Semantic equivalence with the broader ``Vulnerability`` concept is preserved via ``exact_mappings``.
--     * Slot: id
--     * Slot: data_type Description: Indicates the type of information represented in the JSON instance.
--     * Slot: data_version Description: The version of the CVE schema used for validating this record. Supports multiple versions of the format (e.g., '5.2.0').
--     * Slot: cve_metadata_id Description: Metadata about the CVE ID. A Published record uses CveMetadataPublished; a Rejected record uses CveMetadataRejected.
--     * Slot: containers_id Description: A set of containers (CNA and optionally ADP) holding vulnerability information related to the CVE ID.
-- # Abstract Class: CveMetadata Description: Abstract base for CVE Record metadata. Represents either a Published or Rejected record's metadata. All fields are controlled by CVE Services. Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CveMetadataPublished``, ``CveMetadataRejected``); slot-level ``any_of`` on the ``cve_metadata`` slot preserves the choice for generators (e.g. JSON Schema ``anyOf``).
--     * Slot: id
-- # Class: CveMetadataPublished Description: Metadata for a CVE Record in the PUBLISHED state.
--     * Slot: id
--     * Slot: record_cve_id Description: The CVE identifier that this record pertains to.
--     * Slot: assigner_org_id Description: The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service.
--     * Slot: assigner_short_name Description: The short name for the organization to which the CVE ID was originally assigned.
--     * Slot: serial Description: Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record.
--     * Slot: date_updated Description: The date/time the record was last updated.
--     * Slot: date_reserved Description: The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed.
--     * Slot: requester_user_id Description: The user that requested the CVE identifier.
--     * Slot: date_published Description: The date/time the CVE Record was first published in the CVE List.
--     * Slot: published_state Description: State of the CVE Record. For published records, this is always PUBLISHED.
-- # Class: CveMetadataRejected Description: Metadata for a CVE Record in the REJECTED state.
--     * Slot: id
--     * Slot: record_cve_id Description: The CVE identifier that this record pertains to.
--     * Slot: assigner_org_id Description: The UUID for the organization to which the CVE ID was originally assigned. This UUID can be used to lookup the organization record in the user registry service.
--     * Slot: assigner_short_name Description: The short name for the organization to which the CVE ID was originally assigned.
--     * Slot: serial Description: Monotonically increasing integer, starting at 1, incremented each time a submission from a data provider changes this CVE Record.
--     * Slot: date_updated Description: The date/time the record was last updated.
--     * Slot: date_reserved Description: The date/time this CVE ID was reserved in the CVE automation workgroup services system. This date does not necessarily indicate when the vulnerability was discovered, shared with the vendor, or publicly disclosed.
--     * Slot: date_published Description: The date/time the CVE Record was first published in the CVE List.
--     * Slot: date_rejected Description: The date/time the CVE ID was rejected.
--     * Slot: rejected_state Description: State of the CVE Record. For rejected records, this is always REJECTED.
-- # Class: Containers Description: A set of structures (called containers) used to store vulnerability information related to a specific CVE ID. At minimum a 'cna' container is required.
--     * Slot: id
--     * Slot: cna_id Description: The CNA container holding vulnerability information for this CVE ID. For published records, this is a CnaPublishedContainer. For rejected records, this is a CnaRejectedContainer.
-- # Class: ProviderMetadata Description: Details related to the information container provider (CNA or ADP).
--     * Slot: id
--     * Slot: org_id Description: The container provider's organizational UUID.
--     * Slot: short_name Description: The container provider's organizational short name (2-32 characters).
--     * Slot: date_updated Description: The date/time the record was last updated.
-- # Abstract Class: CnaContainer Description: Abstract base for CNA containers (published and rejected). Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CnaPublishedContainer``, ``CnaRejectedContainer``); slot-level ``any_of`` on the ``cna`` slot preserves the choice for generators.
--     * Slot: id
-- # Class: CnaPublishedContainer Description: An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a published CVE ID. There can only be one CNA container per CVE record since there can only be one assigning CNA.
--     * Slot: id
--     * Slot: date_assigned Description: The date/time this CVE ID was associated with a vulnerability by a CNA.
--     * Slot: date_public Description: If known, the date/time the vulnerability was disclosed publicly.
--     * Slot: title Description: Short human-readable title or name for this entity.
--     * Slot: provider_metadata_id Description: Details related to the information container provider (CNA or ADP).
--     * Slot: cna_source_id Description: Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information.
-- # Class: CnaRejectedContainer Description: An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a rejected CVE ID. There can only be one CNA container per CVE record.
--     * Slot: id
--     * Slot: provider_metadata_id Description: Details related to the information container provider (CNA or ADP).
-- # Class: AdpContainer Description: An object containing vulnerability information provided by an Authorized Data Publisher (ADP). Multiple ADPs can provide containers for a single CVE ID.
--     * Slot: id
--     * Slot: date_public Description: If known, the date/time the vulnerability was disclosed publicly.
--     * Slot: title Description: Short human-readable title or name for this entity.
--     * Slot: Containers_id Description: Autocreated FK slot
--     * Slot: provider_metadata_id Description: Details related to the information container provider (CNA or ADP).
--     * Slot: cna_source_id Description: Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information.
-- # Class: AffectedProduct Description: Information about the set of products and services affected by a vulnerability. At least one of (vendor + product) or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.Note: this class deliberately does NOT inherit from ``vulnerability_core.Product``. The upstream CVE ``product`` definition uses a multivalued ``versions`` slot (range ``VersionEntry``), which conflicts with ``Product.version`` (singular string). The ``vendor``, ``name`` (= upstream ``product``), and ``platforms`` slots are reused from the core schema directly. Semantic equivalence is preserved via ``exact_mappings``.
--     * Slot: id
--     * Slot: vendor Description: Name of the vendor or organization responsible for the product.
--     * Slot: name Description: Name of the affected product (upstream field ``product``).
--     * Slot: collection_url Description: URL identifying a package collection (determines the meaning of packageName).
--     * Slot: package_name Description: Name or identifier of the affected software package as used in the package collection.
--     * Slot: repo Description: The URL of the source code repository, for informational purposes and/or to resolve git hash version ranges.
--     * Slot: default_status Description: The default status for versions not otherwise listed in the versions list. Defaults to 'unknown' if not specified. Versions or defaultStatus may be omitted, but not both.
--     * Slot: package_url Description: A Package URL (PURL), a unified URL specification for identifying packages hosted by known package hosts. The Package URL MUST NOT include a version.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: ProgramRoutine Description: An affected source code function, method, subroutine, or procedure.
--     * Slot: id
--     * Slot: routine_name Description: Name of the affected source code function, method, subroutine, or procedure.
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
-- # Class: VersionEntry Description: A single version or a range of versions of a product with associated vulnerability status. An entry with only version and status is a point version; an entry with versionType and a less-than limit describes a range.
--     * Slot: id
--     * Slot: version_value Description: The single version being described, or the version at the start of the range. By convention, '0' denotes the earliest possible version.
--     * Slot: version_status Description: The vulnerability status for the version or range of versions. For a range, the status may be refined by the 'changes' list.
--     * Slot: version_type Description: The version numbering system used for specifying the range (e.g., semver, git, maven, rpm, python, custom). Defines the semantics of comparison.
--     * Slot: less_than Description: The non-inclusive upper limit of the range. This is the least version NOT in the range. Supports wildcard '*' suffix.
--     * Slot: less_than_or_equal Description: The inclusive upper limit of the range. This is the greatest version contained in the range. Only one of lessThan and lessThanOrEqual should be specified.
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
-- # Class: VersionChange Description: A status change that takes place at a specific point within a version range.
--     * Slot: id
--     * Slot: change_at Description: The version at which a status change occurs within a range.
--     * Slot: change_status Description: The new status in the range starting at the given version.
--     * Slot: VersionEntry_id Description: Autocreated FK slot
-- # Class: MultiLangDescription Description: Text in a particular language with optional alternate markup or formatted representation (e.g., Markdown) or embedded media. Used for vulnerability descriptions, rejected reasons, configurations, workarounds, solutions, and exploits.
--     * Slot: id
--     * Slot: lang Description: BCP 47 language code indicating the language of accompanying text.
--     * Slot: description_value Description: Plain text description (up to 4096 characters).
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CnaRejectedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
--     * Slot: ImpactEntry_id Description: Autocreated FK slot
-- # Class: SupportingMedia Description: Supporting media data for a description such as markdown, diagrams, etc. Similar to RFC 2397, each media object has a media type, data value, and an optional base64 flag.
--     * Slot: id
--     * Slot: media_type Description: RFC2046 compliant IANA Media type (e.g., text/markdown, text/html, image/png, image/svg, audio/mp3).
--     * Slot: base64_encoded Description: If true, the media_value field contains the media data encoded in base64. If false, the media_value field contains UTF-8 media content.
--     * Slot: media_value Description: Supporting media content, up to 16K characters. If base64_encoded is true, this stores base64 encoded data.
--     * Slot: MultiLangDescription_id Description: Autocreated FK slot
-- # Class: ProblemType Description: Problem type information (e.g., CWE identifier). Wraps one or more problem type descriptions. The CNA requirement is [PROBLEMTYPE].
--     * Slot: id
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: ProblemTypeDescription Description: Individual problem type description entry.
--     * Slot: id
--     * Slot: lang Description: BCP 47 language code indicating the language of accompanying text.
--     * Slot: problem_description Description: Text description of the problem type, or title from CWE or OWASP.
--     * Slot: cwe_id Description: CWE identifier for the weakness classification (e.g. CWE-79).
--     * Slot: problem_source_type Description: Problem type source format (e.g., text, OWASP, CWE).
--     * Slot: ProblemType_id Description: Autocreated FK slot
-- # Class: CveReference Description: An external reference associated with a CVE Record. Extends the core Reference with optional descriptive tags characterizing the resource.
--     * Slot: id
--     * Slot: url Description: URL pointing to the reference resource.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
--     * Slot: ProblemTypeDescription_id Description: Autocreated FK slot
-- # Class: ImpactEntry Description: An impact entry linking an optional CAPEC attack pattern ID to one or more prose descriptions of the impact scenario.
--     * Slot: id
--     * Slot: capec_id Description: CAPEC ID that best relates to this impact (e.g., CAPEC-123).
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: MetricEntry Description: A metric entry containing scoring data in one of the CVSS formats (v4.0, v3.x, v2.0) or a custom format, with optional applicability scenarios. At least one of cvss_v4_0, cvss_v3, cvss_v2_0, or other_metric is required. CVSS 3.0 and 3.1 are both represented by CvssV3 (distinguished by the cvss3_version slot).
--     * Slot: id
--     * Slot: metric_format Description: Name of the scoring format (e.g., cvssV4_0, cvssV3_1). Provides future-proofing and supports proprietary format inclusion.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
--     * Slot: cvss_v4_0_id Description: CVSS version 4.0 scoring data.
--     * Slot: cvss_v3_id Description: CVSS version 3.x scoring data (covers both 3.0 and 3.1). The version is distinguished by the cvss3_version field within the CvssV3 object.
--     * Slot: cvss_v2_0_id Description: CVSS version 2.0 scoring data.
--     * Slot: other_metric_id Description: A non-standard impact description or score.
-- # Class: MetricScenario Description: A scenario description indicating the context in which a metric applies. If no specific scenario is given, GENERAL is used as the default.
--     * Slot: id
--     * Slot: lang Description: BCP 47 language code indicating the language of accompanying text.
--     * Slot: scenario_value Description: Description of the scenario this metrics object applies to.
--     * Slot: MetricEntry_id Description: Autocreated FK slot
-- # Class: CvssV4_0 Description: CVSS version 4.0 scoring object. Requires version, vectorString, baseScore, and baseSeverity. All other fields are optional.
--     * Slot: id
--     * Slot: cvss4_version Description: CVSS version identifier. Must be '4.0' for CVSS v4.0 objects.
--     * Slot: cvss4_vector_string Description: CVSS 4.0 vector string encoding all base, threat, and environmental metrics.
--     * Slot: cvss4_base_score Description: CVSS 4.0 base score (0.0 – 10.0 in 0.1 increments).
--     * Slot: cvss4_base_severity Description: CVSS 4.0 qualitative base severity rating.
--     * Slot: cvss4_attack_vector
--     * Slot: cvss4_attack_complexity
--     * Slot: cvss4_attack_requirements
--     * Slot: cvss4_privileges_required
--     * Slot: cvss4_user_interaction
--     * Slot: cvss4_vuln_confidentiality_impact
--     * Slot: cvss4_vuln_integrity_impact
--     * Slot: cvss4_vuln_availability_impact
--     * Slot: cvss4_sub_confidentiality_impact
--     * Slot: cvss4_sub_integrity_impact
--     * Slot: cvss4_sub_availability_impact
--     * Slot: cvss4_exploit_maturity
--     * Slot: cvss4_confidentiality_requirement
--     * Slot: cvss4_integrity_requirement
--     * Slot: cvss4_availability_requirement
--     * Slot: cvss4_modified_attack_vector
--     * Slot: cvss4_modified_attack_complexity
--     * Slot: cvss4_modified_attack_requirements
--     * Slot: cvss4_modified_privileges_required
--     * Slot: cvss4_modified_user_interaction
--     * Slot: cvss4_modified_vuln_confidentiality_impact
--     * Slot: cvss4_modified_vuln_integrity_impact
--     * Slot: cvss4_modified_vuln_availability_impact
--     * Slot: cvss4_modified_sub_confidentiality_impact
--     * Slot: cvss4_modified_sub_integrity_impact
--     * Slot: cvss4_modified_sub_availability_impact
--     * Slot: cvss4_safety
--     * Slot: cvss4_automatable
--     * Slot: cvss4_recovery
--     * Slot: cvss4_value_density
--     * Slot: cvss4_vulnerability_response_effort
--     * Slot: cvss4_provider_urgency
-- # Class: CvssV3 Description: CVSS version 3.x scoring object covering both CVSS 3.0 and CVSS 3.1. The two versions share an identical metric model; the 3.1 spec was a clarification, not a structural change. The cvss3_version slot distinguishes between them. Requires version ('3.0' or '3.1'), vectorString, baseScore, and baseSeverity.
--     * Slot: id
--     * Slot: cvss3_version Description: CVSS version identifier ('3.0' or '3.1') within a CvssV3 object.
--     * Slot: cvss3_vector_string Description: CVSS 3.x vector string encoding all metric values. CVSS 3.1 strings begin with 'CVSS:3.1/'; CVSS 3.0 strings begin with 'CVSS:3.0/'.
--     * Slot: cvss3_attack_vector
--     * Slot: cvss3_attack_complexity
--     * Slot: cvss3_privileges_required
--     * Slot: cvss3_user_interaction
--     * Slot: cvss3_scope
--     * Slot: cvss3_confidentiality_impact
--     * Slot: cvss3_integrity_impact
--     * Slot: cvss3_availability_impact
--     * Slot: cvss3_base_score Description: CVSS 3.x base score (0.0 – 10.0 in 0.1 increments).
--     * Slot: cvss3_base_severity
--     * Slot: cvss3_exploit_code_maturity
--     * Slot: cvss3_remediation_level
--     * Slot: cvss3_report_confidence
--     * Slot: cvss3_temporal_score Description: CVSS 3.x temporal score.
--     * Slot: cvss3_temporal_severity
--     * Slot: cvss3_confidentiality_requirement
--     * Slot: cvss3_integrity_requirement
--     * Slot: cvss3_availability_requirement
--     * Slot: cvss3_modified_attack_vector
--     * Slot: cvss3_modified_attack_complexity
--     * Slot: cvss3_modified_privileges_required
--     * Slot: cvss3_modified_user_interaction
--     * Slot: cvss3_modified_scope
--     * Slot: cvss3_modified_confidentiality_impact
--     * Slot: cvss3_modified_integrity_impact
--     * Slot: cvss3_modified_availability_impact
--     * Slot: cvss3_environmental_score Description: CVSS 3.x environmental score.
--     * Slot: cvss3_environmental_severity
-- # Class: CvssV2_0 Description: CVSS version 2.0 scoring object. Requires version ('2.0'), vectorString, and baseScore.
--     * Slot: id
--     * Slot: cvss2_version Description: CVSS version identifier. Must be '2.0' for CVSS v2.0 objects.
--     * Slot: cvss2_vector_string Description: CVSS 2.0 vector string encoding all base, temporal, and environmental metrics.
--     * Slot: cvss2_access_vector
--     * Slot: cvss2_access_complexity
--     * Slot: cvss2_authentication
--     * Slot: cvss2_confidentiality_impact
--     * Slot: cvss2_integrity_impact
--     * Slot: cvss2_availability_impact
--     * Slot: cvss2_base_score Description: CVSS 2.0 base score (0.0 – 10.0).
--     * Slot: cvss2_exploitability
--     * Slot: cvss2_remediation_level
--     * Slot: cvss2_report_confidence
--     * Slot: cvss2_temporal_score Description: CVSS 2.0 temporal score.
--     * Slot: cvss2_collateral_damage_potential
--     * Slot: cvss2_target_distribution
--     * Slot: cvss2_confidentiality_requirement
--     * Slot: cvss2_integrity_requirement
--     * Slot: cvss2_availability_requirement
--     * Slot: cvss2_environmental_score Description: CVSS 2.0 environmental score.
-- # Class: OtherMetric Description: A non-standard impact description in a custom format. May be a prose description or an arbitrary JSON-compatible object.
--     * Slot: id
--     * Slot: other_metric_type Description: Name of the non-standard impact metrics format used.
--     * Slot: other_metric_content_id Description: Arbitrary JSON-compatible object (or prose string) containing non-standard metric data not covered by the CVSS formats. Upstream JSON Schema defines this as 'type: object, minProperties: 1'; range: Any allows any value.
-- # Class: TimelineEntry Description: A timeline event recording a significant event about the vulnerability or changes to the CVE Record. Requires time, lang, and value.
--     * Slot: id
--     * Slot: event_time Description: Timestamp representing when the event in the timeline occurred. Format is RFC3339 / ISO8601 with optional timezone.
--     * Slot: lang Description: BCP 47 language code indicating the language of accompanying text.
--     * Slot: event_value Description: A summary of the timeline event (up to 4096 characters).
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: CreditEntry Description: A credit acknowledging a specific person, organization, or tool for work related to the research, discovery, remediation, or coordination of the vulnerability.
--     * Slot: id
--     * Slot: lang Description: BCP 47 language code indicating the language of accompanying text.
--     * Slot: credit_value Description: The name or description of the credited party (up to 4096 characters).
--     * Slot: credit_user Description: UUID of the user being credited, if present in the CVE User Registry. This UUID can be used to lookup the user record in the user registry service.
--     * Slot: credit_type Description: Type or role of the entity being credited.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: SourceInformation Description: Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. This is an open object — at least one property must be present.
--     * Slot: id
--     * Slot: source_advisory Description: Advisory identifier associated with the vulnerability discovery.
--     * Slot: source_discovery Description: How the vulnerability was discovered (e.g., INTERNAL, EXTERNAL, USER).
-- # Class: TaxonomyMapping Description: A taxonomy mapping identifying the taxonomy by name and version, along with a list of relations relevant to the CVE (e.g., ATT&CK, D3FEND, CWE).
--     * Slot: id
--     * Slot: taxonomy_name Description: The name of the taxonomy (e.g., ATT&CK, D3FEND, CWE, CVSS).
--     * Slot: taxonomy_version Description: The version of the taxonomy the identifiers come from.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: TaxonomyRelation Description: A relationship between a taxonomy item and a CVE or another taxonomy item. Provides subject (taxonomyId), predicate (relationshipName), and object (relationshipValue).
--     * Slot: id
--     * Slot: taxonomy_id Description: Identifier of the item in the taxonomy. Used as the subject of the relationship.
--     * Slot: relationship_name Description: A description of the relationship between the taxonomy item and the CVE.
--     * Slot: relationship_value Description: The target of the relationship. Can be the CVE ID or another taxonomy identifier.
--     * Slot: TaxonomyMapping_id Description: Autocreated FK slot
-- # Class: CpeApplicabilityElement Description: Affected products defined using an implementation of the CPE Applicability Language. An operator property allows AND or OR logic between CPEs or combinations of CPEs.
--     * Slot: id
--     * Slot: cpe_operator Description: Logical operator (AND/OR) used between CPE criteria in this node.
--     * Slot: cpe_negate Description: If true, negates the applicability of this element.
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: AdpContainer_id Description: Autocreated FK slot
-- # Class: CpeNode Description: Defines a CPE configuration node in an applicability statement.
--     * Slot: id
--     * Slot: cpe_operator Description: Logical operator (AND/OR) used between CPE criteria in this node.
--     * Slot: cpe_negate Description: If true, negates the applicability of this element.
--     * Slot: CpeApplicabilityElement_id Description: Autocreated FK slot
-- # Class: CpeMatch Description: CPE match string or range within a CPE applicability node.
--     * Slot: id
--     * Slot: cpe_vulnerable Description: Whether this CPE match describes a vulnerable configuration.
--     * Slot: cpe_criteria Description: CPE 2.3 formatted name match string or match criteria.
--     * Slot: match_criteria_id Description: UUID identifying the CPE match criteria set.
--     * Slot: version_start_excluding Description: The start of a version range, exclusive (versions strictly greater than this).
--     * Slot: version_start_including Description: The start of a version range, inclusive (versions greater than or equal to this).
--     * Slot: version_end_excluding Description: The end of a version range, exclusive (versions strictly less than this).
--     * Slot: version_end_including Description: The end of a version range, inclusive (versions less than or equal to this).
--     * Slot: CpeNode_id Description: Autocreated FK slot
-- # Abstract Class: Vulnerability Description: Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
--     * Slot: cve_id Description: The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.
--     * Slot: title Description: Short human-readable title or name for this entity.
--     * Slot: description Description: Narrative description of the vulnerability.
--     * Slot: published_date Description: Date and time the vulnerability was first published.
--     * Slot: last_modified_date Description: Date and time the vulnerability record was last modified.
--     * Slot: status Description: Current lifecycle state of the vulnerability record.
--     * Slot: impact_id Description: Impact and severity assessment for this vulnerability.
-- # Class: Product Description: Software or hardware entity affected by the vulnerability.
--     * Slot: id
--     * Slot: vendor Description: Name of the vendor or organization responsible for the product.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: version Description: Version string of the affected product.
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Reference Description: External reference such as an advisory or article.
--     * Slot: id
--     * Slot: url Description: URL pointing to the reference resource.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Weakness Description: Weakness classification from CWE or a similar taxonomy.
--     * Slot: id
--     * Slot: cwe_id Description: CWE identifier for the weakness classification (e.g. CWE-79).
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: description Description: Narrative description of the vulnerability.
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Impact Description: Assessment of the vulnerability's impact and severity.
--     * Slot: id
--     * Slot: severity Description: Qualitative severity rating.
--     * Slot: vector Description: CVSS vector string or equivalent scoring vector expression.
--     * Slot: score Description: Numeric vulnerability score (e.g. CVSS base score).
-- # Class: Configuration Description: Logical grouping of CPE match expressions.
--     * Slot: id
--     * Slot: cpe_uri Description: CPE 2.2 URI identifying an affected product configuration.
--     * Slot: operator Description: Logical operator (AND/OR) used in configuration node groupings.
-- # Class: CnaPublishedContainer_cna_tags
--     * Slot: CnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: cna_tags Description: Tags provided by a CNA describing the CVE Record.
-- # Class: CnaRejectedContainer_replaced_by
--     * Slot: CnaRejectedContainer_id Description: Autocreated FK slot
--     * Slot: replaced_by Description: CVE IDs that this CVE ID was rejected in favor of because this CVE ID was incorrectly assigned to the same vulnerabilities.
-- # Class: AdpContainer_adp_tags
--     * Slot: AdpContainer_id Description: Autocreated FK slot
--     * Slot: adp_tags Description: Tags provided by an ADP describing the CVE Record.
-- # Class: AffectedProduct_platforms
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
--     * Slot: platforms Description: Platforms or operating environments affected.
-- # Class: AffectedProduct_cpes
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
--     * Slot: cpes Description: Affected products defined by CPE (Common Platform Enumeration) names in either 2.2 or 2.3 format.
-- # Class: AffectedProduct_modules
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
--     * Slot: modules Description: A list of the affected components, features, modules, sub-components, sub-products, APIs, commands, utilities, programs, or functionalities.
-- # Class: AffectedProduct_program_files
--     * Slot: AffectedProduct_id Description: Autocreated FK slot
--     * Slot: program_files Description: A list of the affected source code files.
-- # Class: CveReference_reference_tags
--     * Slot: CveReference_id Description: Autocreated FK slot
--     * Slot: reference_tags Description: An array of tags describing the resource referenced by the URL.
-- # Class: SourceInformation_source_defects
--     * Slot: SourceInformation_id Description: Autocreated FK slot
--     * Slot: source_defects Description: Bug tracking system IDs (e.g., JIRA ticket IDs) related to the vulnerability.
-- # Class: Product_platforms
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: platforms Description: Platforms or operating environments affected.

CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Any_id" ON "Any" (id);

CREATE TABLE "CveMetadata" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadata_id" ON "CveMetadata" (id);

CREATE TABLE "CveMetadataPublished" (
	id INTEGER NOT NULL,
	record_cve_id TEXT NOT NULL,
	assigner_org_id TEXT NOT NULL,
	assigner_short_name TEXT,
	serial INTEGER,
	date_updated TEXT,
	date_reserved TEXT,
	requester_user_id TEXT,
	date_published TEXT,
	published_state VARCHAR(9) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadataPublished_id" ON "CveMetadataPublished" (id);

CREATE TABLE "CveMetadataRejected" (
	id INTEGER NOT NULL,
	record_cve_id TEXT NOT NULL,
	assigner_org_id TEXT NOT NULL,
	assigner_short_name TEXT,
	serial INTEGER,
	date_updated TEXT,
	date_reserved TEXT,
	date_published TEXT,
	date_rejected TEXT,
	rejected_state VARCHAR(9) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadataRejected_id" ON "CveMetadataRejected" (id);

CREATE TABLE "ProviderMetadata" (
	id INTEGER NOT NULL,
	org_id TEXT NOT NULL,
	short_name TEXT,
	date_updated TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_ProviderMetadata_id" ON "ProviderMetadata" (id);

CREATE TABLE "CnaContainer" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CnaContainer_id" ON "CnaContainer" (id);

CREATE TABLE "CvssV4_0" (
	id INTEGER NOT NULL,
	cvss4_version TEXT NOT NULL,
	cvss4_vector_string TEXT NOT NULL,
	cvss4_base_score FLOAT NOT NULL,
	cvss4_base_severity VARCHAR(8) NOT NULL,
	cvss4_attack_vector VARCHAR(8),
	cvss4_attack_complexity VARCHAR(4),
	cvss4_attack_requirements VARCHAR(7),
	cvss4_privileges_required VARCHAR(4),
	cvss4_user_interaction VARCHAR(7),
	cvss4_vuln_confidentiality_impact VARCHAR(4),
	cvss4_vuln_integrity_impact VARCHAR(4),
	cvss4_vuln_availability_impact VARCHAR(4),
	cvss4_sub_confidentiality_impact VARCHAR(4),
	cvss4_sub_integrity_impact VARCHAR(4),
	cvss4_sub_availability_impact VARCHAR(4),
	cvss4_exploit_maturity VARCHAR(16),
	cvss4_confidentiality_requirement VARCHAR(11),
	cvss4_integrity_requirement VARCHAR(11),
	cvss4_availability_requirement VARCHAR(11),
	cvss4_modified_attack_vector VARCHAR(11),
	cvss4_modified_attack_complexity VARCHAR(11),
	cvss4_modified_attack_requirements VARCHAR(11),
	cvss4_modified_privileges_required VARCHAR(11),
	cvss4_modified_user_interaction VARCHAR(11),
	cvss4_modified_vuln_confidentiality_impact VARCHAR(11),
	cvss4_modified_vuln_integrity_impact VARCHAR(11),
	cvss4_modified_vuln_availability_impact VARCHAR(11),
	cvss4_modified_sub_confidentiality_impact VARCHAR(11),
	cvss4_modified_sub_integrity_impact VARCHAR(11),
	cvss4_modified_sub_availability_impact VARCHAR(11),
	cvss4_safety VARCHAR(11),
	cvss4_automatable VARCHAR(11),
	cvss4_recovery VARCHAR(13),
	cvss4_value_density VARCHAR(12),
	cvss4_vulnerability_response_effort VARCHAR(11),
	cvss4_provider_urgency VARCHAR(11),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV4_0_id" ON "CvssV4_0" (id);

CREATE TABLE "CvssV3" (
	id INTEGER NOT NULL,
	cvss3_version VARCHAR(3) NOT NULL,
	cvss3_vector_string TEXT NOT NULL,
	cvss3_attack_vector VARCHAR(16),
	cvss3_attack_complexity VARCHAR(4),
	cvss3_privileges_required VARCHAR(4),
	cvss3_user_interaction VARCHAR(8),
	cvss3_scope VARCHAR(9),
	cvss3_confidentiality_impact VARCHAR(4),
	cvss3_integrity_impact VARCHAR(4),
	cvss3_availability_impact VARCHAR(4),
	cvss3_base_score FLOAT NOT NULL,
	cvss3_base_severity VARCHAR(8) NOT NULL,
	cvss3_exploit_code_maturity VARCHAR(16),
	cvss3_remediation_level VARCHAR(13),
	cvss3_report_confidence VARCHAR(11),
	cvss3_temporal_score FLOAT,
	cvss3_temporal_severity VARCHAR(8),
	cvss3_confidentiality_requirement VARCHAR(11),
	cvss3_integrity_requirement VARCHAR(11),
	cvss3_availability_requirement VARCHAR(11),
	cvss3_modified_attack_vector VARCHAR(16),
	cvss3_modified_attack_complexity VARCHAR(11),
	cvss3_modified_privileges_required VARCHAR(11),
	cvss3_modified_user_interaction VARCHAR(11),
	cvss3_modified_scope VARCHAR(11),
	cvss3_modified_confidentiality_impact VARCHAR(11),
	cvss3_modified_integrity_impact VARCHAR(11),
	cvss3_modified_availability_impact VARCHAR(11),
	cvss3_environmental_score FLOAT,
	cvss3_environmental_severity VARCHAR(8),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV3_id" ON "CvssV3" (id);

CREATE TABLE "CvssV2_0" (
	id INTEGER NOT NULL,
	cvss2_version TEXT NOT NULL,
	cvss2_vector_string TEXT NOT NULL,
	cvss2_access_vector VARCHAR(16),
	cvss2_access_complexity VARCHAR(6),
	cvss2_authentication VARCHAR(8),
	cvss2_confidentiality_impact VARCHAR(8),
	cvss2_integrity_impact VARCHAR(8),
	cvss2_availability_impact VARCHAR(8),
	cvss2_base_score FLOAT NOT NULL,
	cvss2_exploitability VARCHAR(16),
	cvss2_remediation_level VARCHAR(13),
	cvss2_report_confidence VARCHAR(14),
	cvss2_temporal_score FLOAT,
	cvss2_collateral_damage_potential VARCHAR(11),
	cvss2_target_distribution VARCHAR(11),
	cvss2_confidentiality_requirement VARCHAR(11),
	cvss2_integrity_requirement VARCHAR(11),
	cvss2_availability_requirement VARCHAR(11),
	cvss2_environmental_score FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV2_0_id" ON "CvssV2_0" (id);

CREATE TABLE "SourceInformation" (
	id INTEGER NOT NULL,
	source_advisory TEXT,
	source_discovery TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_SourceInformation_id" ON "SourceInformation" (id);

CREATE TABLE "Impact" (
	id INTEGER NOT NULL,
	severity VARCHAR(8),
	vector TEXT,
	score FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Impact_id" ON "Impact" (id);

CREATE TABLE "Configuration" (
	id INTEGER NOT NULL,
	cpe_uri TEXT,
	operator TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Configuration_id" ON "Configuration" (id);

CREATE TABLE "Containers" (
	id INTEGER NOT NULL,
	cna_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(cna_id) REFERENCES "CnaContainer" (id)
);
CREATE INDEX "ix_Containers_id" ON "Containers" (id);

CREATE TABLE "CnaPublishedContainer" (
	id INTEGER NOT NULL,
	date_assigned TEXT,
	date_public TEXT,
	title TEXT,
	provider_metadata_id INTEGER NOT NULL,
	cna_source_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(provider_metadata_id) REFERENCES "ProviderMetadata" (id),
	FOREIGN KEY(cna_source_id) REFERENCES "SourceInformation" (id)
);
CREATE INDEX "ix_CnaPublishedContainer_id" ON "CnaPublishedContainer" (id);

CREATE TABLE "CnaRejectedContainer" (
	id INTEGER NOT NULL,
	provider_metadata_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(provider_metadata_id) REFERENCES "ProviderMetadata" (id)
);
CREATE INDEX "ix_CnaRejectedContainer_id" ON "CnaRejectedContainer" (id);

CREATE TABLE "OtherMetric" (
	id INTEGER NOT NULL,
	other_metric_type TEXT NOT NULL,
	other_metric_content_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(other_metric_content_id) REFERENCES "Any" (id)
);
CREATE INDEX "ix_OtherMetric_id" ON "OtherMetric" (id);

CREATE TABLE "Vulnerability" (
	cve_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	published_date DATETIME,
	last_modified_date DATETIME,
	status VARCHAR(10),
	impact_id INTEGER,
	PRIMARY KEY (cve_id),
	FOREIGN KEY(impact_id) REFERENCES "Impact" (id)
);
CREATE INDEX "ix_Vulnerability_cve_id" ON "Vulnerability" (cve_id);

CREATE TABLE "SourceInformation_source_defects" (
	"SourceInformation_id" INTEGER,
	source_defects TEXT,
	PRIMARY KEY ("SourceInformation_id", source_defects),
	FOREIGN KEY("SourceInformation_id") REFERENCES "SourceInformation" (id)
);
CREATE INDEX "ix_SourceInformation_source_defects_source_defects" ON "SourceInformation_source_defects" (source_defects);
CREATE INDEX "ix_SourceInformation_source_defects_SourceInformation_id" ON "SourceInformation_source_defects" ("SourceInformation_id");

CREATE TABLE "CVERecord" (
	id INTEGER NOT NULL,
	data_type VARCHAR(10),
	data_version TEXT,
	cve_metadata_id INTEGER NOT NULL,
	containers_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(cve_metadata_id) REFERENCES "CveMetadata" (id),
	FOREIGN KEY(containers_id) REFERENCES "Containers" (id)
);
CREATE INDEX "ix_CVERecord_id" ON "CVERecord" (id);

CREATE TABLE "AdpContainer" (
	id INTEGER NOT NULL,
	date_public TEXT,
	title TEXT,
	"Containers_id" INTEGER,
	provider_metadata_id INTEGER NOT NULL,
	cna_source_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Containers_id") REFERENCES "Containers" (id),
	FOREIGN KEY(provider_metadata_id) REFERENCES "ProviderMetadata" (id),
	FOREIGN KEY(cna_source_id) REFERENCES "SourceInformation" (id)
);
CREATE INDEX "ix_AdpContainer_id" ON "AdpContainer" (id);

CREATE TABLE "Product" (
	id INTEGER NOT NULL,
	vendor TEXT,
	name TEXT,
	version TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Product_id" ON "Product" (id);

CREATE TABLE "Reference" (
	id INTEGER NOT NULL,
	url TEXT,
	name TEXT,
	source TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Reference_id" ON "Reference" (id);

CREATE TABLE "Weakness" (
	id INTEGER NOT NULL,
	cwe_id TEXT,
	name TEXT,
	description TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Weakness_id" ON "Weakness" (id);

CREATE TABLE "CnaPublishedContainer_cna_tags" (
	"CnaPublishedContainer_id" INTEGER,
	cna_tags TEXT,
	PRIMARY KEY ("CnaPublishedContainer_id", cna_tags),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id)
);
CREATE INDEX "ix_CnaPublishedContainer_cna_tags_cna_tags" ON "CnaPublishedContainer_cna_tags" (cna_tags);
CREATE INDEX "ix_CnaPublishedContainer_cna_tags_CnaPublishedContainer_id" ON "CnaPublishedContainer_cna_tags" ("CnaPublishedContainer_id");

CREATE TABLE "CnaRejectedContainer_replaced_by" (
	"CnaRejectedContainer_id" INTEGER,
	replaced_by TEXT,
	PRIMARY KEY ("CnaRejectedContainer_id", replaced_by),
	FOREIGN KEY("CnaRejectedContainer_id") REFERENCES "CnaRejectedContainer" (id)
);
CREATE INDEX "ix_CnaRejectedContainer_replaced_by_CnaRejectedContainer_id" ON "CnaRejectedContainer_replaced_by" ("CnaRejectedContainer_id");
CREATE INDEX "ix_CnaRejectedContainer_replaced_by_replaced_by" ON "CnaRejectedContainer_replaced_by" (replaced_by);

CREATE TABLE "AffectedProduct" (
	id INTEGER NOT NULL,
	vendor TEXT,
	name TEXT,
	collection_url TEXT,
	package_name TEXT,
	repo TEXT,
	default_status VARCHAR(10),
	package_url TEXT,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_AffectedProduct_id" ON "AffectedProduct" (id);

CREATE TABLE "ProblemType" (
	id INTEGER NOT NULL,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_ProblemType_id" ON "ProblemType" (id);

CREATE TABLE "ImpactEntry" (
	id INTEGER NOT NULL,
	capec_id TEXT,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_ImpactEntry_id" ON "ImpactEntry" (id);

CREATE TABLE "MetricEntry" (
	id INTEGER NOT NULL,
	metric_format TEXT,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	cvss_v4_0_id INTEGER,
	cvss_v3_id INTEGER,
	cvss_v2_0_id INTEGER,
	other_metric_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id),
	FOREIGN KEY(cvss_v4_0_id) REFERENCES "CvssV4_0" (id),
	FOREIGN KEY(cvss_v3_id) REFERENCES "CvssV3" (id),
	FOREIGN KEY(cvss_v2_0_id) REFERENCES "CvssV2_0" (id),
	FOREIGN KEY(other_metric_id) REFERENCES "OtherMetric" (id)
);
CREATE INDEX "ix_MetricEntry_id" ON "MetricEntry" (id);

CREATE TABLE "TimelineEntry" (
	id INTEGER NOT NULL,
	event_time TEXT NOT NULL,
	lang TEXT NOT NULL,
	event_value TEXT NOT NULL,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_TimelineEntry_id" ON "TimelineEntry" (id);

CREATE TABLE "CreditEntry" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	credit_value TEXT NOT NULL,
	credit_user TEXT,
	credit_type VARCHAR(21),
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_CreditEntry_id" ON "CreditEntry" (id);

CREATE TABLE "TaxonomyMapping" (
	id INTEGER NOT NULL,
	taxonomy_name TEXT NOT NULL,
	taxonomy_version TEXT,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_TaxonomyMapping_id" ON "TaxonomyMapping" (id);

CREATE TABLE "CpeApplicabilityElement" (
	id INTEGER NOT NULL,
	cpe_operator VARCHAR(3),
	cpe_negate BOOLEAN,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_CpeApplicabilityElement_id" ON "CpeApplicabilityElement" (id);

CREATE TABLE "AdpContainer_adp_tags" (
	"AdpContainer_id" INTEGER,
	adp_tags TEXT,
	PRIMARY KEY ("AdpContainer_id", adp_tags),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id)
);
CREATE INDEX "ix_AdpContainer_adp_tags_adp_tags" ON "AdpContainer_adp_tags" (adp_tags);
CREATE INDEX "ix_AdpContainer_adp_tags_AdpContainer_id" ON "AdpContainer_adp_tags" ("AdpContainer_id");

CREATE TABLE "Product_platforms" (
	"Product_id" INTEGER,
	platforms TEXT,
	PRIMARY KEY ("Product_id", platforms),
	FOREIGN KEY("Product_id") REFERENCES "Product" (id)
);
CREATE INDEX "ix_Product_platforms_Product_id" ON "Product_platforms" ("Product_id");
CREATE INDEX "ix_Product_platforms_platforms" ON "Product_platforms" (platforms);

CREATE TABLE "ProgramRoutine" (
	id INTEGER NOT NULL,
	routine_name TEXT NOT NULL,
	"AffectedProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_ProgramRoutine_id" ON "ProgramRoutine" (id);

CREATE TABLE "VersionEntry" (
	id INTEGER NOT NULL,
	version_value TEXT NOT NULL,
	version_status VARCHAR(10) NOT NULL,
	version_type TEXT,
	less_than TEXT,
	less_than_or_equal TEXT,
	"AffectedProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_VersionEntry_id" ON "VersionEntry" (id);

CREATE TABLE "MultiLangDescription" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	description_value TEXT NOT NULL,
	"CnaPublishedContainer_id" INTEGER,
	"CnaRejectedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	"ImpactEntry_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("CnaRejectedContainer_id") REFERENCES "CnaRejectedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id),
	FOREIGN KEY("ImpactEntry_id") REFERENCES "ImpactEntry" (id)
);
CREATE INDEX "ix_MultiLangDescription_id" ON "MultiLangDescription" (id);

CREATE TABLE "ProblemTypeDescription" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	problem_description TEXT NOT NULL,
	cwe_id TEXT,
	problem_source_type TEXT,
	"ProblemType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("ProblemType_id") REFERENCES "ProblemType" (id)
);
CREATE INDEX "ix_ProblemTypeDescription_id" ON "ProblemTypeDescription" (id);

CREATE TABLE "MetricScenario" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	scenario_value TEXT NOT NULL,
	"MetricEntry_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MetricEntry_id") REFERENCES "MetricEntry" (id)
);
CREATE INDEX "ix_MetricScenario_id" ON "MetricScenario" (id);

CREATE TABLE "TaxonomyRelation" (
	id INTEGER NOT NULL,
	taxonomy_id TEXT NOT NULL,
	relationship_name TEXT NOT NULL,
	relationship_value TEXT NOT NULL,
	"TaxonomyMapping_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("TaxonomyMapping_id") REFERENCES "TaxonomyMapping" (id)
);
CREATE INDEX "ix_TaxonomyRelation_id" ON "TaxonomyRelation" (id);

CREATE TABLE "CpeNode" (
	id INTEGER NOT NULL,
	cpe_operator VARCHAR(3) NOT NULL,
	cpe_negate BOOLEAN,
	"CpeApplicabilityElement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CpeApplicabilityElement_id") REFERENCES "CpeApplicabilityElement" (id)
);
CREATE INDEX "ix_CpeNode_id" ON "CpeNode" (id);

CREATE TABLE "AffectedProduct_platforms" (
	"AffectedProduct_id" INTEGER,
	platforms TEXT,
	PRIMARY KEY ("AffectedProduct_id", platforms),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_AffectedProduct_platforms_AffectedProduct_id" ON "AffectedProduct_platforms" ("AffectedProduct_id");
CREATE INDEX "ix_AffectedProduct_platforms_platforms" ON "AffectedProduct_platforms" (platforms);

CREATE TABLE "AffectedProduct_cpes" (
	"AffectedProduct_id" INTEGER,
	cpes TEXT,
	PRIMARY KEY ("AffectedProduct_id", cpes),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_AffectedProduct_cpes_AffectedProduct_id" ON "AffectedProduct_cpes" ("AffectedProduct_id");
CREATE INDEX "ix_AffectedProduct_cpes_cpes" ON "AffectedProduct_cpes" (cpes);

CREATE TABLE "AffectedProduct_modules" (
	"AffectedProduct_id" INTEGER,
	modules TEXT,
	PRIMARY KEY ("AffectedProduct_id", modules),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_AffectedProduct_modules_AffectedProduct_id" ON "AffectedProduct_modules" ("AffectedProduct_id");
CREATE INDEX "ix_AffectedProduct_modules_modules" ON "AffectedProduct_modules" (modules);

CREATE TABLE "AffectedProduct_program_files" (
	"AffectedProduct_id" INTEGER,
	program_files TEXT,
	PRIMARY KEY ("AffectedProduct_id", program_files),
	FOREIGN KEY("AffectedProduct_id") REFERENCES "AffectedProduct" (id)
);
CREATE INDEX "ix_AffectedProduct_program_files_AffectedProduct_id" ON "AffectedProduct_program_files" ("AffectedProduct_id");
CREATE INDEX "ix_AffectedProduct_program_files_program_files" ON "AffectedProduct_program_files" (program_files);

CREATE TABLE "VersionChange" (
	id INTEGER NOT NULL,
	change_at TEXT NOT NULL,
	change_status VARCHAR(10) NOT NULL,
	"VersionEntry_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("VersionEntry_id") REFERENCES "VersionEntry" (id)
);
CREATE INDEX "ix_VersionChange_id" ON "VersionChange" (id);

CREATE TABLE "SupportingMedia" (
	id INTEGER NOT NULL,
	media_type TEXT NOT NULL,
	base64_encoded BOOLEAN,
	media_value TEXT NOT NULL,
	"MultiLangDescription_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MultiLangDescription_id") REFERENCES "MultiLangDescription" (id)
);
CREATE INDEX "ix_SupportingMedia_id" ON "SupportingMedia" (id);

CREATE TABLE "CveReference" (
	id INTEGER NOT NULL,
	url TEXT NOT NULL,
	name TEXT,
	source TEXT,
	"CnaPublishedContainer_id" INTEGER,
	"AdpContainer_id" INTEGER,
	"ProblemTypeDescription_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CnaPublishedContainer_id") REFERENCES "CnaPublishedContainer" (id),
	FOREIGN KEY("AdpContainer_id") REFERENCES "AdpContainer" (id),
	FOREIGN KEY("ProblemTypeDescription_id") REFERENCES "ProblemTypeDescription" (id)
);
CREATE INDEX "ix_CveReference_id" ON "CveReference" (id);

CREATE TABLE "CpeMatch" (
	id INTEGER NOT NULL,
	cpe_vulnerable BOOLEAN NOT NULL,
	cpe_criteria TEXT NOT NULL,
	match_criteria_id TEXT,
	version_start_excluding TEXT,
	version_start_including TEXT,
	version_end_excluding TEXT,
	version_end_including TEXT,
	"CpeNode_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CpeNode_id") REFERENCES "CpeNode" (id)
);
CREATE INDEX "ix_CpeMatch_id" ON "CpeMatch" (id);

CREATE TABLE "CveReference_reference_tags" (
	"CveReference_id" INTEGER,
	reference_tags VARCHAR(21),
	PRIMARY KEY ("CveReference_id", reference_tags),
	FOREIGN KEY("CveReference_id") REFERENCES "CveReference" (id)
);
CREATE INDEX "ix_CveReference_reference_tags_CveReference_id" ON "CveReference_reference_tags" ("CveReference_id");
CREATE INDEX "ix_CveReference_reference_tags_reference_tags" ON "CveReference_reference_tags" (reference_tags);
