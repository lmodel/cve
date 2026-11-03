// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/cve";
export const SITE = "https://lmodel.github.io";
export const BASE = "/cve";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "cve";
export const DESCRIPTION = "Common Vulnerabilities and Exposures (CVE) Record Format 5.2.0 (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = "auto";

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
export const DOCS = { dir: "docs", exclude: ["templates-linkml"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  "/about": "/docs/about/",
  "/elements": "/schema/",
  // The retired schema's element addresses, each to its successor where the
  // element has one, and the rest to the schema's index. A name that stayed the
  // same is covered by the /elements/[...slug] entry.
  "/elements/adp_tags": "/schema/tags/",
  "/elements/AdpContainer": "/schema/CveAdpContainer/",
  "/elements/ADPTag": "/schema/CveAdpTag/",
  "/elements/AffectedProduct": "/schema/CveProduct/",
  "/elements/Any": "/schema/",
  "/elements/assigner_org_id": "/schema/assignerOrgId/",
  "/elements/assigner_short_name": "/schema/assignerShortName/",
  "/elements/base64_encoded": "/schema/base64/",
  "/elements/capec_id": "/schema/capecId/",
  "/elements/change_at": "/schema/at/",
  "/elements/change_status": "/schema/status/",
  "/elements/cna_source": "/schema/source/",
  "/elements/cna_tags": "/schema/tags/",
  "/elements/CnaContainer": "/schema/CveCnaContainer/",
  "/elements/CnaMetadata": "/schema/",
  "/elements/CnaPublishedContainer": "/schema/CveCnaPublishedContainer/",
  "/elements/CnaRejectedContainer": "/schema/CveCnaRejectedContainer/",
  "/elements/CNATag": "/schema/CveCnaTag/",
  "/elements/collection_url": "/schema/collectionURL/",
  "/elements/Configuration": "/schema/",
  "/elements/configurations_text": "/schema/configurations/",
  "/elements/Containers": "/schema/CveContainers/",
  "/elements/Core": "/schema/",
  "/elements/cpe_applicability": "/schema/cpeApplicability/",
  "/elements/cpe_criteria": "/schema/criteria/",
  "/elements/cpe_match_criteria": "/schema/cpeMatch/",
  "/elements/cpe_negate": "/schema/negate/",
  "/elements/cpe_nodes": "/schema/nodes/",
  "/elements/cpe_operator": "/schema/operator/",
  "/elements/cpe_uri": "/schema/",
  "/elements/cpe_vulnerable": "/schema/vulnerable/",
  "/elements/CpeApplicabilityElement": "/schema/CveCpeApplicabilityElement/",
  "/elements/CpeMatch": "/schema/CveCpeMatch/",
  "/elements/CpeName23Type": "/schema/CveCpe23/",
  "/elements/CpeNameType": "/schema/CveCpe22and23/",
  "/elements/CpeNode": "/schema/CveCpeNode/",
  "/elements/CpeOperator": "/schema/CveCpeOperator/",
  "/elements/credit_type": "/schema/type/",
  "/elements/credit_user": "/schema/user/",
  "/elements/credit_value": "/schema/value/",
  "/elements/CreditEntry": "/schema/CveCredit/",
  "/elements/CreditType": "/schema/CveCreditType/",
  "/elements/cve_id": "/schema/cveId/",
  "/elements/cve_metadata": "/schema/cveMetadata/",
  "/elements/cve_references": "/schema/references/",
  "/elements/CveId": "/schema/CveIdentifier/",
  "/elements/CveMetadata": "/schema/CveRecordMetadata/",
  "/elements/CVERecord": "/schema/CveRecord/",
  "/elements/cvss2_access_complexity": "/schema/accessComplexity/",
  "/elements/cvss2_access_vector": "/schema/accessVector/",
  "/elements/cvss2_authentication": "/schema/authentication/",
  "/elements/cvss2_availability_impact": "/schema/availabilityImpact/",
  "/elements/cvss2_availability_requirement": "/schema/availabilityRequirement/",
  "/elements/cvss2_base_score": "/schema/baseScore/",
  "/elements/cvss2_collateral_damage_potential": "/schema/collateralDamagePotential/",
  "/elements/cvss2_confidentiality_impact": "/schema/confidentialityImpact/",
  "/elements/cvss2_confidentiality_requirement": "/schema/confidentialityRequirement/",
  "/elements/cvss2_environmental_score": "/schema/environmentalScore/",
  "/elements/cvss2_exploitability": "/schema/exploitability/",
  "/elements/cvss2_integrity_impact": "/schema/integrityImpact/",
  "/elements/cvss2_integrity_requirement": "/schema/integrityRequirement/",
  "/elements/cvss2_remediation_level": "/schema/remediationLevel/",
  "/elements/cvss2_report_confidence": "/schema/reportConfidence/",
  "/elements/cvss2_target_distribution": "/schema/targetDistribution/",
  "/elements/cvss2_temporal_score": "/schema/temporalScore/",
  "/elements/cvss2_vector_string": "/schema/vectorString/",
  "/elements/cvss2_version": "/schema/version/",
  "/elements/Cvss2AccessComplexity": "/schema/CvssV2AccessComplexity/",
  "/elements/Cvss2AccessVector": "/schema/CvssV2AccessVector/",
  "/elements/Cvss2Authentication": "/schema/CvssV2Authentication/",
  "/elements/Cvss2Cia": "/schema/CvssV2Impact/",
  "/elements/Cvss2CiaRequirement": "/schema/CvssRequirement/",
  "/elements/Cvss2CollateralDamagePotential": "/schema/CvssV2CollateralDamagePotential/",
  "/elements/Cvss2Exploitability": "/schema/CvssExploitCodeMaturity/",
  "/elements/Cvss2RemediationLevel": "/schema/CvssRemediationLevel/",
  "/elements/Cvss2ReportConfidence": "/schema/CvssV2ReportConfidence/",
  "/elements/Cvss2TargetDistribution": "/schema/CvssV2TargetDistribution/",
  "/elements/cvss3_attack_complexity": "/schema/attackComplexity/",
  "/elements/cvss3_attack_vector": "/schema/attackVector/",
  "/elements/cvss3_availability_impact": "/schema/availabilityImpact/",
  "/elements/cvss3_availability_requirement": "/schema/availabilityRequirement/",
  "/elements/cvss3_base_score": "/schema/baseScore/",
  "/elements/cvss3_base_severity": "/schema/baseSeverity/",
  "/elements/cvss3_confidentiality_impact": "/schema/confidentialityImpact/",
  "/elements/cvss3_confidentiality_requirement": "/schema/confidentialityRequirement/",
  "/elements/cvss3_environmental_score": "/schema/environmentalScore/",
  "/elements/cvss3_environmental_severity": "/schema/environmentalSeverity/",
  "/elements/cvss3_exploit_code_maturity": "/schema/exploitCodeMaturity/",
  "/elements/cvss3_integrity_impact": "/schema/integrityImpact/",
  "/elements/cvss3_integrity_requirement": "/schema/integrityRequirement/",
  "/elements/cvss3_modified_attack_complexity": "/schema/modifiedAttackComplexity/",
  "/elements/cvss3_modified_attack_vector": "/schema/modifiedAttackVector/",
  "/elements/cvss3_modified_availability_impact": "/schema/modifiedAvailabilityImpact/",
  "/elements/cvss3_modified_confidentiality_impact": "/schema/modifiedConfidentialityImpact/",
  "/elements/cvss3_modified_integrity_impact": "/schema/modifiedIntegrityImpact/",
  "/elements/cvss3_modified_privileges_required": "/schema/modifiedPrivilegesRequired/",
  "/elements/cvss3_modified_scope": "/schema/modifiedScope/",
  "/elements/cvss3_modified_user_interaction": "/schema/modifiedUserInteraction/",
  "/elements/cvss3_privileges_required": "/schema/privilegesRequired/",
  "/elements/cvss3_remediation_level": "/schema/remediationLevel/",
  "/elements/cvss3_report_confidence": "/schema/reportConfidence/",
  "/elements/cvss3_scope": "/schema/scope/",
  "/elements/cvss3_temporal_score": "/schema/temporalScore/",
  "/elements/cvss3_temporal_severity": "/schema/temporalSeverity/",
  "/elements/cvss3_user_interaction": "/schema/userInteraction/",
  "/elements/cvss3_vector_string": "/schema/vectorString/",
  "/elements/cvss3_version": "/schema/version/",
  "/elements/Cvss3AttackComplexity": "/schema/CvssAttackComplexity/",
  "/elements/Cvss3AttackVector": "/schema/CvssV3AttackVector/",
  "/elements/Cvss3Cia": "/schema/CvssImpact/",
  "/elements/Cvss3CiaRequirement": "/schema/CvssRequirement/",
  "/elements/Cvss3Confidence": "/schema/CvssV3ReportConfidence/",
  "/elements/Cvss3ExploitCodeMaturity": "/schema/CvssExploitCodeMaturity/",
  "/elements/Cvss3ModifiedAttackComplexity": "/schema/CvssModifiedAttackComplexity/",
  "/elements/Cvss3ModifiedAttackVector": "/schema/CvssV3ModifiedAttackVector/",
  "/elements/Cvss3ModifiedCia": "/schema/CvssModifiedImpact/",
  "/elements/Cvss3ModifiedPrivilegesRequired": "/schema/CvssModifiedPrivilegesRequired/",
  "/elements/Cvss3ModifiedScope": "/schema/CvssV3ModifiedScope/",
  "/elements/Cvss3ModifiedUserInteraction": "/schema/CvssV3ModifiedUserInteraction/",
  "/elements/Cvss3PrivilegesRequired": "/schema/CvssPrivilegesRequired/",
  "/elements/Cvss3RemediationLevel": "/schema/CvssRemediationLevel/",
  "/elements/Cvss3Scope": "/schema/CvssV3Scope/",
  "/elements/Cvss3Severity": "/schema/CvssSeverity/",
  "/elements/Cvss3UserInteraction": "/schema/CvssV3UserInteraction/",
  "/elements/cvss4_attack_complexity": "/schema/attackComplexity/",
  "/elements/cvss4_attack_requirements": "/schema/attackRequirements/",
  "/elements/cvss4_attack_vector": "/schema/attackVector/",
  "/elements/cvss4_automatable": "/schema/Automatable/",
  "/elements/cvss4_availability_requirement": "/schema/availabilityRequirement/",
  "/elements/cvss4_base_score": "/schema/baseScore/",
  "/elements/cvss4_base_severity": "/schema/baseSeverity/",
  "/elements/cvss4_confidentiality_requirement": "/schema/confidentialityRequirement/",
  "/elements/cvss4_exploit_maturity": "/schema/exploitMaturity/",
  "/elements/cvss4_integrity_requirement": "/schema/integrityRequirement/",
  "/elements/cvss4_modified_attack_complexity": "/schema/modifiedAttackComplexity/",
  "/elements/cvss4_modified_attack_requirements": "/schema/modifiedAttackRequirements/",
  "/elements/cvss4_modified_attack_vector": "/schema/modifiedAttackVector/",
  "/elements/cvss4_modified_privileges_required": "/schema/modifiedPrivilegesRequired/",
  "/elements/cvss4_modified_sub_availability_impact": "/schema/modifiedSubAvailabilityImpact/",
  "/elements/cvss4_modified_sub_confidentiality_impact": "/schema/modifiedSubConfidentialityImpact/",
  "/elements/cvss4_modified_sub_integrity_impact": "/schema/modifiedSubIntegrityImpact/",
  "/elements/cvss4_modified_user_interaction": "/schema/modifiedUserInteraction/",
  "/elements/cvss4_modified_vuln_availability_impact": "/schema/modifiedVulnAvailabilityImpact/",
  "/elements/cvss4_modified_vuln_confidentiality_impact": "/schema/modifiedVulnConfidentialityImpact/",
  "/elements/cvss4_modified_vuln_integrity_impact": "/schema/modifiedVulnIntegrityImpact/",
  "/elements/cvss4_privileges_required": "/schema/privilegesRequired/",
  "/elements/cvss4_provider_urgency": "/schema/providerUrgency/",
  "/elements/cvss4_recovery": "/schema/Recovery/",
  "/elements/cvss4_safety": "/schema/Safety/",
  "/elements/cvss4_sub_availability_impact": "/schema/subAvailabilityImpact/",
  "/elements/cvss4_sub_confidentiality_impact": "/schema/subConfidentialityImpact/",
  "/elements/cvss4_sub_integrity_impact": "/schema/subIntegrityImpact/",
  "/elements/cvss4_user_interaction": "/schema/userInteraction/",
  "/elements/cvss4_value_density": "/schema/valueDensity/",
  "/elements/cvss4_vector_string": "/schema/vectorString/",
  "/elements/cvss4_version": "/schema/version/",
  "/elements/cvss4_vuln_availability_impact": "/schema/vulnAvailabilityImpact/",
  "/elements/cvss4_vuln_confidentiality_impact": "/schema/vulnConfidentialityImpact/",
  "/elements/cvss4_vuln_integrity_impact": "/schema/vulnIntegrityImpact/",
  "/elements/cvss4_vulnerability_response_effort": "/schema/vulnerabilityResponseEffort/",
  "/elements/Cvss4AttackComplexity": "/schema/CvssAttackComplexity/",
  "/elements/Cvss4AttackRequirements": "/schema/CvssV4AttackRequirements/",
  "/elements/Cvss4AttackVector": "/schema/CvssV4AttackVector/",
  "/elements/Cvss4Automatable": "/schema/CvssV4Automatable/",
  "/elements/Cvss4CiaRequirement": "/schema/CvssRequirement/",
  "/elements/Cvss4ExploitMaturity": "/schema/CvssV4ExploitMaturity/",
  "/elements/Cvss4ModifiedAttackComplexity": "/schema/CvssModifiedAttackComplexity/",
  "/elements/Cvss4ModifiedAttackRequirements": "/schema/CvssV4ModifiedAttackRequirements/",
  "/elements/Cvss4ModifiedAttackVector": "/schema/CvssV4ModifiedAttackVector/",
  "/elements/Cvss4ModifiedPrivilegesRequired": "/schema/CvssModifiedPrivilegesRequired/",
  "/elements/Cvss4ModifiedSubC": "/schema/CvssModifiedImpact/",
  "/elements/Cvss4ModifiedSubIa": "/schema/CvssV4ModifiedSubsequentImpact/",
  "/elements/Cvss4ModifiedUserInteraction": "/schema/CvssV4ModifiedUserInteraction/",
  "/elements/Cvss4ModifiedVulnCia": "/schema/CvssModifiedImpact/",
  "/elements/Cvss4PrivilegesRequired": "/schema/CvssPrivilegesRequired/",
  "/elements/Cvss4ProviderUrgency": "/schema/CvssV4ProviderUrgency/",
  "/elements/Cvss4Recovery": "/schema/CvssV4Recovery/",
  "/elements/Cvss4Safety": "/schema/CvssV4Safety/",
  "/elements/Cvss4Severity": "/schema/CvssSeverity/",
  "/elements/Cvss4SubCia": "/schema/CvssImpact/",
  "/elements/Cvss4UserInteraction": "/schema/CvssV4UserInteraction/",
  "/elements/Cvss4ValueDensity": "/schema/CvssV4ValueDensity/",
  "/elements/Cvss4VulnCia": "/schema/CvssImpact/",
  "/elements/Cvss4VulnerabilityResponseEffort": "/schema/CvssV4ResponseEffort/",
  "/elements/cvss_v2_0": "/schema/cvssV2_0/",
  "/elements/cvss_v3": "/schema/cvssV3_1/",
  "/elements/cvss_v4_0": "/schema/cvssV4_0/",
  "/elements/CvssMetrics": "/schema/",
  "/elements/CvssV3": "/schema/CvssV31/",
  "/elements/CvssV3Version": "/schema/",
  "/elements/cwe_id": "/schema/cweId/",
  "/elements/data_type": "/schema/dataType/",
  "/elements/data_version": "/schema/dataVersion/",
  "/elements/DataType": "/schema/CveDataType/",
  "/elements/date_assigned": "/schema/dateAssigned/",
  "/elements/date_public": "/schema/datePublic/",
  "/elements/date_published": "/schema/datePublished/",
  "/elements/date_rejected": "/schema/dateRejected/",
  "/elements/date_reserved": "/schema/dateReserved/",
  "/elements/date_updated": "/schema/dateUpdated/",
  "/elements/Datestamp": "/schema/CveDatestamp/",
  "/elements/default_status": "/schema/defaultStatus/",
  "/elements/description_value": "/schema/value/",
  "/elements/event_time": "/schema/time/",
  "/elements/event_value": "/schema/value/",
  "/elements/Impact": "/schema/CveImpact/",
  "/elements/impact": "/schema/impacts/",
  "/elements/impact_descriptions": "/schema/descriptions/",
  "/elements/ImpactEntry": "/schema/CveImpact/",
  "/elements/ImpactSeverity": "/schema/",
  "/elements/IsoDate": "/schema/",
  "/elements/LanguageTag": "/schema/CveLanguage/",
  "/elements/last_modified_date": "/schema/dateUpdated/",
  "/elements/less_than": "/schema/lessThan/",
  "/elements/less_than_or_equal": "/schema/lessThanOrEqual/",
  "/elements/match_criteria_id": "/schema/matchCriteriaId/",
  "/elements/media_type": "/schema/type/",
  "/elements/media_value": "/schema/value/",
  "/elements/Metadata": "/schema/CveRecordMetadata/",
  "/elements/metric_format": "/schema/format/",
  "/elements/metric_scenarios": "/schema/scenarios/",
  "/elements/MetricEntry": "/schema/CveMetric/",
  "/elements/MetricScenario": "/schema/CveMetricScenario/",
  "/elements/MultiLangDescription": "/schema/CveDescription/",
  "/elements/org_id": "/schema/orgId/",
  "/elements/other_metric": "/schema/other/",
  "/elements/other_metric_content": "/schema/content/",
  "/elements/other_metric_type": "/schema/type/",
  "/elements/OtherMetric": "/schema/CveOtherMetric/",
  "/elements/package_name": "/schema/packageName/",
  "/elements/package_url": "/schema/packageURL/",
  "/elements/problem_description": "/schema/description/",
  "/elements/problem_references": "/schema/references/",
  "/elements/problem_source_type": "/schema/type/",
  "/elements/problem_type_descriptions": "/schema/descriptions/",
  "/elements/problem_types": "/schema/problemTypes/",
  "/elements/ProblemType": "/schema/CveProblemType/",
  "/elements/ProblemTypeDescription": "/schema/CveProblemTypeDescription/",
  "/elements/Product": "/schema/CveProduct/",
  "/elements/products": "/schema/affected/",
  "/elements/program_files": "/schema/programFiles/",
  "/elements/program_routines": "/schema/programRoutines/",
  "/elements/ProgramRoutine": "/schema/CveProgramRoutine/",
  "/elements/provider_metadata": "/schema/providerMetadata/",
  "/elements/ProviderMetadata": "/schema/CveProviderMetadata/",
  "/elements/published_date": "/schema/datePublished/",
  "/elements/published_state": "/schema/state/",
  "/elements/record_cve_id": "/schema/cveId/",
  "/elements/RecordState": "/schema/CveRecordState/",
  "/elements/Reference": "/schema/CveReference/",
  "/elements/reference_tags": "/schema/tags/",
  "/elements/ReferenceTag": "/schema/CveReferenceTag/",
  "/elements/rejected_reasons": "/schema/rejectedReasons/",
  "/elements/rejected_state": "/schema/state/",
  "/elements/relationship_name": "/schema/relationshipName/",
  "/elements/relationship_value": "/schema/relationshipValue/",
  "/elements/replaced_by": "/schema/replacedBy/",
  "/elements/requester_user_id": "/schema/requesterUserId/",
  "/elements/routine_name": "/schema/name/",
  "/elements/scenario_value": "/schema/value/",
  "/elements/score": "/schema/baseScore/",
  "/elements/severity": "/schema/baseSeverity/",
  "/elements/short_name": "/schema/shortName/",
  "/elements/source_advisory": "/schema/source/",
  "/elements/source_defects": "/schema/source/",
  "/elements/source_discovery": "/schema/source/",
  "/elements/SourceInformation": "/schema/CveSource/",
  "/elements/supporting_media": "/schema/supportingMedia/",
  "/elements/SupportingMedia": "/schema/CveSupportingMedia/",
  "/elements/taxonomy_id": "/schema/taxonomyId/",
  "/elements/taxonomy_mappings": "/schema/taxonomyMappings/",
  "/elements/taxonomy_name": "/schema/taxonomyName/",
  "/elements/taxonomy_relations": "/schema/taxonomyRelations/",
  "/elements/taxonomy_version": "/schema/taxonomyVersion/",
  "/elements/TaxonomyMapping": "/schema/CveTaxonomyMapping/",
  "/elements/TaxonomyRelation": "/schema/CveTaxonomyRelation/",
  "/elements/TimelineEntry": "/schema/CveTimelineEvent/",
  "/elements/Timestamp": "/schema/CveTimestamp/",
  "/elements/UuidType": "/schema/CveUuid/",
  "/elements/vector": "/schema/vectorString/",
  "/elements/version_changes": "/schema/changes/",
  "/elements/version_end_excluding": "/schema/versionEndExcluding/",
  "/elements/version_end_including": "/schema/versionEndIncluding/",
  "/elements/version_start_excluding": "/schema/versionStartExcluding/",
  "/elements/version_start_including": "/schema/versionStartIncluding/",
  "/elements/version_status": "/schema/status/",
  "/elements/version_type": "/schema/versionType/",
  "/elements/version_value": "/schema/version/",
  "/elements/VersionChange": "/schema/CveVersionChange/",
  "/elements/VersionEntry": "/schema/CveProductVersion/",
  "/elements/VersionStatus": "/schema/CveVersionStatus/",
  "/elements/VersionString": "/schema/CveVersion/",
  "/elements/Vulnerability": "/schema/",
  "/elements/VulnerabilityStatus": "/schema/",
  "/elements/Weakness": "/schema/",
  "/elements/weaknesses": "/schema/problemTypes/",
  "/elements/[...slug]": "/schema/[...slug]",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "auto";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe, else the sidecar's
// domain schema. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = "auto";

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
export const HOME = { source: "auto", tagline: null, actions: null };
