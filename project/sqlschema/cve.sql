-- # Class: CveRecordRoot Description: Any one CVE record, published or rejected, as a file or an API answer holds it.
--     * Slot: id
-- # Class: CvssSeverityBandsMixin Description: The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
--     * Slot: id
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV20 Description: A score under CVSS version 2.0, which has no severity bands.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: accessVector Description: How far away an attacker can be when using the flaw, in CVSS 2.0's terms.
--     * Slot: accessComplexity Description: How hard the flaw is to use once the attacker can reach it.
--     * Slot: authentication Description: How many times an attacker must log in before using the flaw.
--     * Slot: exploitability Description: How far working attack code has come, in CVSS 2.0's terms.
--     * Slot: collateralDamagePotential Description: How much loss a successful attack could cause beyond the system itself.
--     * Slot: targetDistribution Description: How much of the scorer's environment is exposed to the flaw.
-- # Class: CvssV30 Description: A score under CVSS version 3.0.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: scope Description: Whether an attack can reach beyond the component that holds the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: exploitCodeMaturity Description: How far working attack code has come.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: temporalSeverity Description: The rating in words for the temporal score.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: modifiedScope Description: The scope as the scorer's own environment changes it.
--     * Slot: modifiedConfidentialityImpact Description: The confidentiality impact as the scorer's own environment changes it.
--     * Slot: modifiedIntegrityImpact Description: The integrity impact as the scorer's own environment changes it.
--     * Slot: modifiedAvailabilityImpact Description: The availability impact as the scorer's own environment changes it.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: environmentalSeverity Description: The rating in words for the environmental score.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV31 Description: A score under CVSS version 3.1.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: scope Description: Whether an attack can reach beyond the component that holds the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: exploitCodeMaturity Description: How far working attack code has come.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: temporalSeverity Description: The rating in words for the temporal score.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: modifiedScope Description: The scope as the scorer's own environment changes it.
--     * Slot: modifiedConfidentialityImpact Description: The confidentiality impact as the scorer's own environment changes it.
--     * Slot: modifiedIntegrityImpact Description: The integrity impact as the scorer's own environment changes it.
--     * Slot: modifiedAvailabilityImpact Description: The availability impact as the scorer's own environment changes it.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: environmentalSeverity Description: The rating in words for the environmental score.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV40 Description: A score under CVSS version 4.0.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: attackRequirements Description: Whether the attack needs conditions in the target that the attacker does not control.
--     * Slot: vulnConfidentialityImpact Description: How much information in the vulnerable system an attack could expose.
--     * Slot: vulnIntegrityImpact Description: How much an attack could change in the vulnerable system.
--     * Slot: vulnAvailabilityImpact Description: How much an attack could disrupt the vulnerable system.
--     * Slot: subConfidentialityImpact Description: How much information in other, connected systems an attack could expose.
--     * Slot: subIntegrityImpact Description: How much an attack could change in other, connected systems.
--     * Slot: subAvailabilityImpact Description: How much an attack could disrupt other, connected systems.
--     * Slot: exploitMaturity Description: How much is known about attacks on this flaw, in CVSS 4.0's terms.
--     * Slot: modifiedAttackRequirements Description: The attack requirements as the scorer's own environment changes them.
--     * Slot: modifiedVulnConfidentialityImpact Description: The confidentiality impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedVulnIntegrityImpact Description: The integrity impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedVulnAvailabilityImpact Description: The availability impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedSubConfidentialityImpact Description: The confidentiality impact on connected systems, in the scorer's environment.
--     * Slot: modifiedSubIntegrityImpact Description: The integrity impact on connected systems, in the scorer's environment.
--     * Slot: modifiedSubAvailabilityImpact Description: The availability impact on connected systems, in the scorer's environment.
--     * Slot: Safety Description: Whether an attack could put people's safety at risk.
--     * Slot: Automatable Description: Whether an attacker could automate every step of an attack across many targets.
--     * Slot: Recovery Description: How the affected system comes back after an attack.
--     * Slot: valueDensity Description: Whether one successful attack gains the attacker a little or a lot of a resource.
--     * Slot: vulnerabilityResponseEffort Description: How much work it takes a consumer to respond to the flaw.
--     * Slot: providerUrgency Description: How urgent the product's supplier says the flaw is, as a colour.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Abstract Class: CveRecord Description: A record of one vulnerability under one CVE identifier, in the CVE Program's format.
--     * Slot: id
--     * Slot: dataType Description: The kind of document this is, which is always a CVE record.
--     * Slot: dataVersion Description: The version of the record format that this record follows.
--     * Slot: cveMetadata_id Description: The facts about the record itself.
--     * Slot: containers_id Description: The vulnerability information, grouped by who provided it.
-- # Class: CvePublishedRecord Description: A record whose assigning organisation has filled it in and made it public.
--     * Slot: id
--     * Slot: dataType Description: The kind of document this is, which is always a CVE record.
--     * Slot: dataVersion Description: The version of the record format that this record follows.
--     * Slot: cveMetadata_id Description: The facts about the record itself.
--     * Slot: containers_id Description: The vulnerability information, grouped by who provided it.
-- # Class: CveRejectedRecord Description: A record that should no longer be used, kept so that people can see it is invalid.
--     * Slot: id
--     * Slot: dataType Description: The kind of document this is, which is always a CVE record.
--     * Slot: dataVersion Description: The version of the record format that this record follows.
--     * Slot: cveMetadata_id Description: The facts about the record itself.
--     * Slot: containers_id Description: The vulnerability information, grouped by who provided it.
-- # Abstract Class: CveMetadata Description: The facts about a record itself, as distinct from the vulnerability it describes.
--     * Slot: id
--     * Slot: dateUpdated Description: When the record or container was last updated.
--     * Slot: state Description: Whether the record is published or rejected.
--     * Slot: cveId Description: The CVE identifier that the record belongs to.
--     * Slot: assignerOrgId Description: The UUID of the organisation that was given the CVE identifier.
--     * Slot: assignerShortName Description: The short name of the organisation that was given the CVE identifier.
--     * Slot: serial Description: A counter that the system of record raises each time a provider changes the record.
--     * Slot: dateReserved Description: When the CVE identifier was reserved.
--     * Slot: datePublished Description: When the record first appeared in the CVE List.
-- # Class: CveMetadataPublished Description: The metadata of a published record.
--     * Slot: id
--     * Slot: requesterUserId Description: The UUID of the user who asked for the CVE identifier.
--     * Slot: dateUpdated Description: When the record or container was last updated.
--     * Slot: state Description: Whether the record is published or rejected.
--     * Slot: cveId Description: The CVE identifier that the record belongs to.
--     * Slot: assignerOrgId Description: The UUID of the organisation that was given the CVE identifier.
--     * Slot: assignerShortName Description: The short name of the organisation that was given the CVE identifier.
--     * Slot: serial Description: A counter that the system of record raises each time a provider changes the record.
--     * Slot: dateReserved Description: When the CVE identifier was reserved.
--     * Slot: datePublished Description: When the record first appeared in the CVE List.
-- # Class: CveMetadataRejected Description: The metadata of a rejected record.
--     * Slot: id
--     * Slot: dateRejected Description: When the CVE identifier was rejected.
--     * Slot: dateUpdated Description: When the record or container was last updated.
--     * Slot: state Description: Whether the record is published or rejected.
--     * Slot: cveId Description: The CVE identifier that the record belongs to.
--     * Slot: assignerOrgId Description: The UUID of the organisation that was given the CVE identifier.
--     * Slot: assignerShortName Description: The short name of the organisation that was given the CVE identifier.
--     * Slot: serial Description: A counter that the system of record raises each time a provider changes the record.
--     * Slot: dateReserved Description: When the CVE identifier was reserved.
--     * Slot: datePublished Description: When the record first appeared in the CVE List.
-- # Abstract Class: CveContainers Description: The sets of vulnerability information in a record, one per providing organisation.
--     * Slot: id
--     * Slot: cna_id Description: The container from the authority that assigned the identifier.
-- # Class: CvePublishedContainers Description: The containers of a published record, the assigning organisation's and any others'.
--     * Slot: id
--     * Slot: cna_id Description: The container from the authority that assigned the identifier.
-- # Class: CveRejectedContainers Description: The container of a rejected record, which only the assigning organisation provides.
--     * Slot: id
--     * Slot: cna_id Description: The container from the authority that assigned the identifier.
-- # Class: CveProviderMetadata Description: Who provided a container, and when it was last updated.
--     * Slot: id
--     * Slot: dateUpdated Description: When the record or container was last updated.
--     * Slot: orgId Description: The UUID of the organisation that provided the container.
--     * Slot: shortName Description: The short name of the organisation that provided the container.
-- # Abstract Class: CveCnaContainer Description: The container from the CVE Numbering Authority that assigned the identifier.
--     * Slot: id
--     * Slot: providerMetadata_id Description: Who provided the container.
-- # Class: CveCnaPublishedContainer Description: The assigning authority's account of a published vulnerability.
--     * Slot: id
--     * Slot: datePublic Description: When the vulnerability was made public, if known.
--     * Slot: title Description: A short headline for the record or for what the container adds.
--     * Slot: dateAssigned Description: When the authority tied the CVE identifier to a vulnerability.
--     * Slot: source_id Description: How the vulnerability came to light, in the provider's own shape.
--     * Slot: providerMetadata_id Description: Who provided the container.
-- # Class: CveCnaRejectedContainer Description: The assigning authority's account of why a record was rejected.
--     * Slot: id
--     * Slot: providerMetadata_id Description: Who provided the container.
-- # Class: CveAdpContainer Description: What an Authorized Data Publisher adds to a record beside the assigning authority's account.
--     * Slot: id
--     * Slot: datePublic Description: When the vulnerability was made public, if known.
--     * Slot: title Description: A short headline for the record or for what the container adds.
--     * Slot: CvePublishedContainers_id Description: Autocreated FK slot
--     * Slot: providerMetadata_id Description: Who provided the container.
--     * Slot: source_id Description: How the vulnerability came to light, in the provider's own shape.
-- # Class: CveProduct Description: One affected product or package, and which of its versions are affected.
--     * Slot: id
--     * Slot: vendor Description: Who makes or maintains the product. It can be N/A.
--     * Slot: product Description: The name of the affected product.
--     * Slot: collectionURL Description: The address of the package collection that gives packageName its meaning.
--     * Slot: packageName Description: The package's name or identifier within its collection.
--     * Slot: packageURL Description: A Package URL for the package, with no version in it.
--     * Slot: repo Description: The address of the product's source code repository.
--     * Slot: defaultStatus Description: The status of every version the versions list does not cover.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveProgramRoutine Description: One affected function, method or similar routine in the source.
--     * Slot: id
--     * Slot: name Description: A name, of a reference or of a routine.
--     * Slot: CveProduct_id Description: Autocreated FK slot
-- # Class: CveProductVersion Description: A single version or a stretch of versions, and whether it is affected.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: status Description: Whether a version is affected.
--     * Slot: versionType Description: The numbering system that says how these versions compare, such as semver or git.
--     * Slot: lessThan Description: The first version above the range, which is not itself in it.
--     * Slot: lessThanOrEqual Description: The last version in the range.
--     * Slot: CveProduct_id Description: Autocreated FK slot
-- # Class: CveVersionChange Description: A point in a range of versions from which the status changes.
--     * Slot: id
--     * Slot: at Description: The version from which a new status starts.
--     * Slot: status Description: Whether a version is affected.
--     * Slot: CveProductVersion_id Description: Autocreated FK slot
-- # Class: CveCpeApplicabilityElement Description: A statement in the CPE Applicability Language of which platforms are affected.
--     * Slot: id
--     * Slot: operator Description: How the parts combine, all of them or any of them.
--     * Slot: negate Description: Whether the combined result is reversed.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveCpeNode Description: A group of CPE matches, combined by an operator.
--     * Slot: id
--     * Slot: operator Description: How the parts combine, all of them or any of them.
--     * Slot: negate Description: Whether the combined result is reversed.
--     * Slot: CveCpeApplicabilityElement_id Description: Autocreated FK slot
-- # Class: CveCpeMatch Description: One CPE name, optionally bounded by versions, and whether it is vulnerable.
--     * Slot: id
--     * Slot: vulnerable Description: Whether what this match covers is vulnerable.
--     * Slot: criteria Description: The CPE name to match.
--     * Slot: matchCriteriaId Description: A UUID for this match.
--     * Slot: versionStartExcluding Description: The version the match starts just above.
--     * Slot: versionStartIncluding Description: The version the match starts at.
--     * Slot: versionEndExcluding Description: The version the match ends just below.
--     * Slot: versionEndIncluding Description: The version the match ends at.
--     * Slot: CveCpeNode_id Description: Autocreated FK slot
-- # Class: CveDescription Description: A piece of text in one language, with any media that support it.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it.
--     * Slot: value Description: The text or content itself.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveCnaRejectedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
--     * Slot: CveImpact_id Description: Autocreated FK slot
-- # Class: CveSupportingMedia Description: A richer form of a description, as a media type and its content.
--     * Slot: id
--     * Slot: type Description: What kind of thing this is. Each class that uses it says what the choices are.
--     * Slot: value Description: The text or content itself.
--     * Slot: base64 Description: Whether value is base64 encoded rather than plain UTF-8.
--     * Slot: CveDescription_id Description: Autocreated FK slot
-- # Class: CveProblemType Description: One kind of problem the vulnerability is, in one or more languages.
--     * Slot: id
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveProblemTypeDescription Description: A problem type described in one language, often by a weakness identifier and its title.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it.
--     * Slot: description Description: The text of a problem type, or the title of a weakness.
--     * Slot: type Description: What kind of thing this is. Each class that uses it says what the choices are.
--     * Slot: cweId Description: The Common Weakness Enumeration identifier that best fits, such as CWE-79.
--     * Slot: CveProblemType_id Description: Autocreated FK slot
-- # Class: CveReference Description: A link to something about the vulnerability, such as an advisory or a patch.
--     * Slot: id
--     * Slot: url Description: The address the reference points to.
--     * Slot: name Description: A name, of a reference or of a routine.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
--     * Slot: CveProblemTypeDescription_id Description: Autocreated FK slot
-- # Class: CveImpact Description: A consequence of the vulnerability, in words.
--     * Slot: id
--     * Slot: capecId Description: The Common Attack Pattern Enumeration identifier that best fits, such as CAPEC-63.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveMetric Description: One scoring of the vulnerability, in a CVSS version or another format, and where it applies.
--     * Slot: id
--     * Slot: format Description: The name of the scoring format.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
--     * Slot: cvssV4_0_id Description: A score under CVSS version 4.0.
--     * Slot: cvssV3_1_id Description: A score under CVSS version 3.1.
--     * Slot: cvssV3_0_id Description: A score under CVSS version 3.0.
--     * Slot: cvssV2_0_id Description: A score under CVSS version 2.0.
--     * Slot: other_id Description: A score or impact statement in some other format.
-- # Class: CveMetricScenario Description: A situation a scoring applies to, in one language.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it.
--     * Slot: value Description: The text or content itself.
--     * Slot: CveMetric_id Description: Autocreated FK slot
-- # Class: CveOtherMetric Description: A score or impact statement in a format the record format does not name.
--     * Slot: id
--     * Slot: type Description: What kind of thing this is. Each class that uses it says what the choices are.
--     * Slot: content_id Description: The statement itself, as an object in whatever shape its format has.
-- # Class: CveOtherMetricContent Description: The free-form object inside a metric of another format.
--     * Slot: id
-- # Class: CveTimelineEvent Description: One dated event in the vulnerability's history.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it.
--     * Slot: value Description: The text or content itself.
--     * Slot: time Description: When the event happened.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveCredit Description: Thanks to someone who helped, in one language.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it.
--     * Slot: value Description: The text or content itself.
--     * Slot: type Description: What kind of thing this is. Each class that uses it says what the choices are.
--     * Slot: user Description: The UUID of the credited person, when the CVE user registry holds them.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveSource Description: How the vulnerability came to light, as an object the provider shapes as it likes.
--     * Slot: id
-- # Class: CveTaxonomyMapping Description: How the vulnerability relates to one version of an outside taxonomy.
--     * Slot: id
--     * Slot: taxonomyName Description: The name of the taxonomy, such as ATT&CK or CWE.
--     * Slot: taxonomyVersion Description: The version of the taxonomy.
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
-- # Class: CveTaxonomyRelation Description: One relationship from an item in a taxonomy to this CVE or to another item.
--     * Slot: id
--     * Slot: taxonomyId Description: The item in the taxonomy, which is the relationship's subject.
--     * Slot: relationshipName Description: What the relationship is.
--     * Slot: relationshipValue Description: The relationship's target, which is this CVE identifier or another taxonomy item.
--     * Slot: CveTaxonomyMapping_id Description: Autocreated FK slot
-- # Class: CveCnaPublishedContainer_tags
--     * Slot: CveCnaPublishedContainer_id Description: Autocreated FK slot
--     * Slot: tags Description: Short labels from the upstream's list, or the publisher's own beginning x_.
-- # Class: CveCnaRejectedContainer_replacedBy
--     * Slot: CveCnaRejectedContainer_id Description: Autocreated FK slot
--     * Slot: replacedBy Description: The CVE identifiers to use instead of this one.
-- # Class: CveAdpContainer_tags
--     * Slot: CveAdpContainer_id Description: Autocreated FK slot
--     * Slot: tags Description: Short labels from the upstream's list, or the publisher's own beginning x_.
-- # Class: CveProduct_cpes
--     * Slot: CveProduct_id Description: Autocreated FK slot
--     * Slot: cpes Description: Common Platform Enumeration names for the product.
-- # Class: CveProduct_modules
--     * Slot: CveProduct_id Description: Autocreated FK slot
--     * Slot: modules Description: The affected parts of the product, such as components, commands or APIs.
-- # Class: CveProduct_programFiles
--     * Slot: CveProduct_id Description: Autocreated FK slot
--     * Slot: programFiles Description: The affected source files.
-- # Class: CveProduct_platforms
--     * Slot: CveProduct_id Description: Autocreated FK slot
--     * Slot: platforms Description: The platforms the flaw is limited to. Without this, it applies to all of them.
-- # Class: CveReference_tags
--     * Slot: CveReference_id Description: Autocreated FK slot
--     * Slot: tags Description: Short labels from the upstream's list, or the publisher's own beginning x_.

CREATE TABLE "CveRecordRoot" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveRecordRoot_id" ON "CveRecordRoot" (id);

CREATE TABLE "CvssSeverityBandsMixin" (
	id INTEGER NOT NULL,
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssSeverityBandsMixin_id" ON "CvssSeverityBandsMixin" (id);

CREATE TABLE "CvssV20" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"baseScore" FLOAT NOT NULL,
	"confidentialityImpact" VARCHAR(8),
	"integrityImpact" VARCHAR(8),
	"availabilityImpact" VARCHAR(8),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(14),
	"temporalScore" FLOAT,
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"environmentalScore" FLOAT,
	"accessVector" VARCHAR(16),
	"accessComplexity" VARCHAR(6),
	authentication VARCHAR(8),
	exploitability VARCHAR(16),
	"collateralDamagePotential" VARCHAR(11),
	"targetDistribution" VARCHAR(11),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV20_id" ON "CvssV20" (id);

CREATE TABLE "CvssV30" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(16),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(8),
	scope VARCHAR(9),
	"confidentialityImpact" VARCHAR(4),
	"integrityImpact" VARCHAR(4),
	"availabilityImpact" VARCHAR(4),
	"exploitCodeMaturity" VARCHAR(16),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(11),
	"temporalScore" FLOAT,
	"temporalSeverity" VARCHAR(8),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(16),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"modifiedScope" VARCHAR(11),
	"modifiedConfidentialityImpact" VARCHAR(11),
	"modifiedIntegrityImpact" VARCHAR(11),
	"modifiedAvailabilityImpact" VARCHAR(11),
	"environmentalScore" FLOAT,
	"environmentalSeverity" VARCHAR(8),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV30_id" ON "CvssV30" (id);

CREATE TABLE "CvssV31" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(16),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(8),
	scope VARCHAR(9),
	"confidentialityImpact" VARCHAR(4),
	"integrityImpact" VARCHAR(4),
	"availabilityImpact" VARCHAR(4),
	"exploitCodeMaturity" VARCHAR(16),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(11),
	"temporalScore" FLOAT,
	"temporalSeverity" VARCHAR(8),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(16),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"modifiedScope" VARCHAR(11),
	"modifiedConfidentialityImpact" VARCHAR(11),
	"modifiedIntegrityImpact" VARCHAR(11),
	"modifiedAvailabilityImpact" VARCHAR(11),
	"environmentalScore" FLOAT,
	"environmentalSeverity" VARCHAR(8),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV31_id" ON "CvssV31" (id);

CREATE TABLE "CvssV40" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(8),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(7),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(11),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"attackRequirements" VARCHAR(7),
	"vulnConfidentialityImpact" VARCHAR(4),
	"vulnIntegrityImpact" VARCHAR(4),
	"vulnAvailabilityImpact" VARCHAR(4),
	"subConfidentialityImpact" VARCHAR(4),
	"subIntegrityImpact" VARCHAR(4),
	"subAvailabilityImpact" VARCHAR(4),
	"exploitMaturity" VARCHAR(16),
	"modifiedAttackRequirements" VARCHAR(11),
	"modifiedVulnConfidentialityImpact" VARCHAR(11),
	"modifiedVulnIntegrityImpact" VARCHAR(11),
	"modifiedVulnAvailabilityImpact" VARCHAR(11),
	"modifiedSubConfidentialityImpact" VARCHAR(11),
	"modifiedSubIntegrityImpact" VARCHAR(11),
	"modifiedSubAvailabilityImpact" VARCHAR(11),
	"Safety" VARCHAR(11),
	"Automatable" VARCHAR(11),
	"Recovery" VARCHAR(13),
	"valueDensity" VARCHAR(12),
	"vulnerabilityResponseEffort" VARCHAR(11),
	"providerUrgency" VARCHAR(11),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV40_id" ON "CvssV40" (id);

CREATE TABLE "CveMetadata" (
	id INTEGER NOT NULL,
	"dateUpdated" TEXT,
	state VARCHAR(9) NOT NULL,
	"cveId" TEXT NOT NULL,
	"assignerOrgId" TEXT NOT NULL,
	"assignerShortName" TEXT,
	serial INTEGER,
	"dateReserved" TEXT,
	"datePublished" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadata_id" ON "CveMetadata" (id);

CREATE TABLE "CveMetadataPublished" (
	id INTEGER NOT NULL,
	"requesterUserId" TEXT,
	"dateUpdated" TEXT,
	state VARCHAR(9) NOT NULL,
	"cveId" TEXT NOT NULL,
	"assignerOrgId" TEXT NOT NULL,
	"assignerShortName" TEXT,
	serial INTEGER,
	"dateReserved" TEXT,
	"datePublished" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadataPublished_id" ON "CveMetadataPublished" (id);

CREATE TABLE "CveMetadataRejected" (
	id INTEGER NOT NULL,
	"dateRejected" TEXT,
	"dateUpdated" TEXT,
	state VARCHAR(8) NOT NULL,
	"cveId" TEXT NOT NULL,
	"assignerOrgId" TEXT NOT NULL,
	"assignerShortName" TEXT,
	serial INTEGER,
	"dateReserved" TEXT,
	"datePublished" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveMetadataRejected_id" ON "CveMetadataRejected" (id);

CREATE TABLE "CveProviderMetadata" (
	id INTEGER NOT NULL,
	"dateUpdated" TEXT,
	"orgId" TEXT NOT NULL,
	"shortName" TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveProviderMetadata_id" ON "CveProviderMetadata" (id);

CREATE TABLE "CveOtherMetricContent" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveOtherMetricContent_id" ON "CveOtherMetricContent" (id);

CREATE TABLE "CveSource" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CveSource_id" ON "CveSource" (id);

CREATE TABLE "CveCnaContainer" (
	id INTEGER NOT NULL,
	"providerMetadata_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("providerMetadata_id") REFERENCES "CveProviderMetadata" (id)
);
CREATE INDEX "ix_CveCnaContainer_id" ON "CveCnaContainer" (id);

CREATE TABLE "CveCnaPublishedContainer" (
	id INTEGER NOT NULL,
	"datePublic" TEXT,
	title TEXT,
	"dateAssigned" TEXT,
	source_id INTEGER,
	"providerMetadata_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(source_id) REFERENCES "CveSource" (id),
	FOREIGN KEY("providerMetadata_id") REFERENCES "CveProviderMetadata" (id)
);
CREATE INDEX "ix_CveCnaPublishedContainer_id" ON "CveCnaPublishedContainer" (id);

CREATE TABLE "CveCnaRejectedContainer" (
	id INTEGER NOT NULL,
	"providerMetadata_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("providerMetadata_id") REFERENCES "CveProviderMetadata" (id)
);
CREATE INDEX "ix_CveCnaRejectedContainer_id" ON "CveCnaRejectedContainer" (id);

CREATE TABLE "CveOtherMetric" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	content_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(content_id) REFERENCES "CveOtherMetricContent" (id)
);
CREATE INDEX "ix_CveOtherMetric_id" ON "CveOtherMetric" (id);

CREATE TABLE "CveContainers" (
	id INTEGER NOT NULL,
	cna_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(cna_id) REFERENCES "CveCnaContainer" (id)
);
CREATE INDEX "ix_CveContainers_id" ON "CveContainers" (id);

CREATE TABLE "CvePublishedContainers" (
	id INTEGER NOT NULL,
	cna_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(cna_id) REFERENCES "CveCnaPublishedContainer" (id)
);
CREATE INDEX "ix_CvePublishedContainers_id" ON "CvePublishedContainers" (id);

CREATE TABLE "CveRejectedContainers" (
	id INTEGER NOT NULL,
	cna_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(cna_id) REFERENCES "CveCnaRejectedContainer" (id)
);
CREATE INDEX "ix_CveRejectedContainers_id" ON "CveRejectedContainers" (id);

CREATE TABLE "CveCnaPublishedContainer_tags" (
	"CveCnaPublishedContainer_id" INTEGER,
	tags TEXT,
	PRIMARY KEY ("CveCnaPublishedContainer_id", tags),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id)
);
CREATE INDEX "ix_CveCnaPublishedContainer_tags_tags" ON "CveCnaPublishedContainer_tags" (tags);
CREATE INDEX "ix_CveCnaPublishedContainer_tags_CveCnaPublishedContainer_id" ON "CveCnaPublishedContainer_tags" ("CveCnaPublishedContainer_id");

CREATE TABLE "CveCnaRejectedContainer_replacedBy" (
	"CveCnaRejectedContainer_id" INTEGER,
	"replacedBy" TEXT,
	PRIMARY KEY ("CveCnaRejectedContainer_id", "replacedBy"),
	FOREIGN KEY("CveCnaRejectedContainer_id") REFERENCES "CveCnaRejectedContainer" (id)
);
CREATE INDEX "ix_CveCnaRejectedContainer_replacedBy_CveCnaRejectedContainer_id" ON "CveCnaRejectedContainer_replacedBy" ("CveCnaRejectedContainer_id");
CREATE INDEX "ix_CveCnaRejectedContainer_replacedBy_replacedBy" ON "CveCnaRejectedContainer_replacedBy" ("replacedBy");

CREATE TABLE "CveRecord" (
	id INTEGER NOT NULL,
	"dataType" VARCHAR(10) NOT NULL,
	"dataVersion" TEXT NOT NULL,
	"cveMetadata_id" INTEGER NOT NULL,
	containers_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("cveMetadata_id") REFERENCES "CveMetadata" (id),
	FOREIGN KEY(containers_id) REFERENCES "CveContainers" (id)
);
CREATE INDEX "ix_CveRecord_id" ON "CveRecord" (id);

CREATE TABLE "CvePublishedRecord" (
	id INTEGER NOT NULL,
	"dataType" VARCHAR(10) NOT NULL,
	"dataVersion" TEXT NOT NULL,
	"cveMetadata_id" INTEGER NOT NULL,
	containers_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("cveMetadata_id") REFERENCES "CveMetadataPublished" (id),
	FOREIGN KEY(containers_id) REFERENCES "CvePublishedContainers" (id)
);
CREATE INDEX "ix_CvePublishedRecord_id" ON "CvePublishedRecord" (id);

CREATE TABLE "CveRejectedRecord" (
	id INTEGER NOT NULL,
	"dataType" VARCHAR(10) NOT NULL,
	"dataVersion" TEXT NOT NULL,
	"cveMetadata_id" INTEGER NOT NULL,
	containers_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("cveMetadata_id") REFERENCES "CveMetadataRejected" (id),
	FOREIGN KEY(containers_id) REFERENCES "CveRejectedContainers" (id)
);
CREATE INDEX "ix_CveRejectedRecord_id" ON "CveRejectedRecord" (id);

CREATE TABLE "CveAdpContainer" (
	id INTEGER NOT NULL,
	"datePublic" TEXT,
	title TEXT,
	"CvePublishedContainers_id" INTEGER,
	"providerMetadata_id" INTEGER NOT NULL,
	source_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CvePublishedContainers_id") REFERENCES "CvePublishedContainers" (id),
	FOREIGN KEY("providerMetadata_id") REFERENCES "CveProviderMetadata" (id),
	FOREIGN KEY(source_id) REFERENCES "CveSource" (id)
);
CREATE INDEX "ix_CveAdpContainer_id" ON "CveAdpContainer" (id);

CREATE TABLE "CveProduct" (
	id INTEGER NOT NULL,
	vendor TEXT,
	product TEXT,
	"collectionURL" TEXT,
	"packageName" TEXT,
	"packageURL" TEXT,
	repo TEXT,
	"defaultStatus" VARCHAR(10),
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveProduct_id" ON "CveProduct" (id);

CREATE TABLE "CveCpeApplicabilityElement" (
	id INTEGER NOT NULL,
	operator VARCHAR(3),
	negate BOOLEAN,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveCpeApplicabilityElement_id" ON "CveCpeApplicabilityElement" (id);

CREATE TABLE "CveProblemType" (
	id INTEGER NOT NULL,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveProblemType_id" ON "CveProblemType" (id);

CREATE TABLE "CveImpact" (
	id INTEGER NOT NULL,
	"capecId" TEXT,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveImpact_id" ON "CveImpact" (id);

CREATE TABLE "CveMetric" (
	id INTEGER NOT NULL,
	format TEXT,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	"cvssV4_0_id" INTEGER,
	"cvssV3_1_id" INTEGER,
	"cvssV3_0_id" INTEGER,
	"cvssV2_0_id" INTEGER,
	other_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id),
	FOREIGN KEY("cvssV4_0_id") REFERENCES "CvssV40" (id),
	FOREIGN KEY("cvssV3_1_id") REFERENCES "CvssV31" (id),
	FOREIGN KEY("cvssV3_0_id") REFERENCES "CvssV30" (id),
	FOREIGN KEY("cvssV2_0_id") REFERENCES "CvssV20" (id),
	FOREIGN KEY(other_id) REFERENCES "CveOtherMetric" (id)
);
CREATE INDEX "ix_CveMetric_id" ON "CveMetric" (id);

CREATE TABLE "CveTimelineEvent" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	value TEXT NOT NULL,
	time TEXT NOT NULL,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveTimelineEvent_id" ON "CveTimelineEvent" (id);

CREATE TABLE "CveCredit" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	value TEXT NOT NULL,
	type VARCHAR(21),
	user TEXT,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveCredit_id" ON "CveCredit" (id);

CREATE TABLE "CveTaxonomyMapping" (
	id INTEGER NOT NULL,
	"taxonomyName" TEXT NOT NULL,
	"taxonomyVersion" TEXT,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveTaxonomyMapping_id" ON "CveTaxonomyMapping" (id);

CREATE TABLE "CveAdpContainer_tags" (
	"CveAdpContainer_id" INTEGER,
	tags TEXT,
	PRIMARY KEY ("CveAdpContainer_id", tags),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id)
);
CREATE INDEX "ix_CveAdpContainer_tags_CveAdpContainer_id" ON "CveAdpContainer_tags" ("CveAdpContainer_id");
CREATE INDEX "ix_CveAdpContainer_tags_tags" ON "CveAdpContainer_tags" (tags);

CREATE TABLE "CveProgramRoutine" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"CveProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProgramRoutine_id" ON "CveProgramRoutine" (id);

CREATE TABLE "CveProductVersion" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	"versionType" TEXT,
	"lessThan" TEXT,
	"lessThanOrEqual" TEXT,
	"CveProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProductVersion_id" ON "CveProductVersion" (id);

CREATE TABLE "CveCpeNode" (
	id INTEGER NOT NULL,
	operator VARCHAR(3) NOT NULL,
	negate BOOLEAN,
	"CveCpeApplicabilityElement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCpeApplicabilityElement_id") REFERENCES "CveCpeApplicabilityElement" (id)
);
CREATE INDEX "ix_CveCpeNode_id" ON "CveCpeNode" (id);

CREATE TABLE "CveDescription" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	value TEXT NOT NULL,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveCnaRejectedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	"CveImpact_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveCnaRejectedContainer_id") REFERENCES "CveCnaRejectedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id),
	FOREIGN KEY("CveImpact_id") REFERENCES "CveImpact" (id)
);
CREATE INDEX "ix_CveDescription_id" ON "CveDescription" (id);

CREATE TABLE "CveProblemTypeDescription" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	description TEXT NOT NULL,
	type TEXT,
	"cweId" TEXT,
	"CveProblemType_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveProblemType_id") REFERENCES "CveProblemType" (id)
);
CREATE INDEX "ix_CveProblemTypeDescription_id" ON "CveProblemTypeDescription" (id);

CREATE TABLE "CveMetricScenario" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	value TEXT NOT NULL,
	"CveMetric_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveMetric_id") REFERENCES "CveMetric" (id)
);
CREATE INDEX "ix_CveMetricScenario_id" ON "CveMetricScenario" (id);

CREATE TABLE "CveTaxonomyRelation" (
	id INTEGER NOT NULL,
	"taxonomyId" TEXT NOT NULL,
	"relationshipName" TEXT NOT NULL,
	"relationshipValue" TEXT NOT NULL,
	"CveTaxonomyMapping_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveTaxonomyMapping_id") REFERENCES "CveTaxonomyMapping" (id)
);
CREATE INDEX "ix_CveTaxonomyRelation_id" ON "CveTaxonomyRelation" (id);

CREATE TABLE "CveProduct_cpes" (
	"CveProduct_id" INTEGER,
	cpes TEXT,
	PRIMARY KEY ("CveProduct_id", cpes),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProduct_cpes_CveProduct_id" ON "CveProduct_cpes" ("CveProduct_id");
CREATE INDEX "ix_CveProduct_cpes_cpes" ON "CveProduct_cpes" (cpes);

CREATE TABLE "CveProduct_modules" (
	"CveProduct_id" INTEGER,
	modules TEXT,
	PRIMARY KEY ("CveProduct_id", modules),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProduct_modules_modules" ON "CveProduct_modules" (modules);
CREATE INDEX "ix_CveProduct_modules_CveProduct_id" ON "CveProduct_modules" ("CveProduct_id");

CREATE TABLE "CveProduct_programFiles" (
	"CveProduct_id" INTEGER,
	"programFiles" TEXT,
	PRIMARY KEY ("CveProduct_id", "programFiles"),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProduct_programFiles_CveProduct_id" ON "CveProduct_programFiles" ("CveProduct_id");
CREATE INDEX "ix_CveProduct_programFiles_programFiles" ON "CveProduct_programFiles" ("programFiles");

CREATE TABLE "CveProduct_platforms" (
	"CveProduct_id" INTEGER,
	platforms TEXT,
	PRIMARY KEY ("CveProduct_id", platforms),
	FOREIGN KEY("CveProduct_id") REFERENCES "CveProduct" (id)
);
CREATE INDEX "ix_CveProduct_platforms_CveProduct_id" ON "CveProduct_platforms" ("CveProduct_id");
CREATE INDEX "ix_CveProduct_platforms_platforms" ON "CveProduct_platforms" (platforms);

CREATE TABLE "CveVersionChange" (
	id INTEGER NOT NULL,
	at TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	"CveProductVersion_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveProductVersion_id") REFERENCES "CveProductVersion" (id)
);
CREATE INDEX "ix_CveVersionChange_id" ON "CveVersionChange" (id);

CREATE TABLE "CveCpeMatch" (
	id INTEGER NOT NULL,
	vulnerable BOOLEAN NOT NULL,
	criteria TEXT NOT NULL,
	"matchCriteriaId" TEXT,
	"versionStartExcluding" TEXT,
	"versionStartIncluding" TEXT,
	"versionEndExcluding" TEXT,
	"versionEndIncluding" TEXT,
	"CveCpeNode_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCpeNode_id") REFERENCES "CveCpeNode" (id)
);
CREATE INDEX "ix_CveCpeMatch_id" ON "CveCpeMatch" (id);

CREATE TABLE "CveSupportingMedia" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	value TEXT NOT NULL,
	base64 BOOLEAN,
	"CveDescription_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveDescription_id") REFERENCES "CveDescription" (id)
);
CREATE INDEX "ix_CveSupportingMedia_id" ON "CveSupportingMedia" (id);

CREATE TABLE "CveReference" (
	id INTEGER NOT NULL,
	url TEXT NOT NULL,
	name TEXT,
	"CveCnaPublishedContainer_id" INTEGER,
	"CveAdpContainer_id" INTEGER,
	"CveProblemTypeDescription_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CveCnaPublishedContainer_id") REFERENCES "CveCnaPublishedContainer" (id),
	FOREIGN KEY("CveAdpContainer_id") REFERENCES "CveAdpContainer" (id),
	FOREIGN KEY("CveProblemTypeDescription_id") REFERENCES "CveProblemTypeDescription" (id)
);
CREATE INDEX "ix_CveReference_id" ON "CveReference" (id);

CREATE TABLE "CveReference_tags" (
	"CveReference_id" INTEGER,
	tags TEXT,
	PRIMARY KEY ("CveReference_id", tags),
	FOREIGN KEY("CveReference_id") REFERENCES "CveReference" (id)
);
CREATE INDEX "ix_CveReference_tags_tags" ON "CveReference_tags" (tags);
CREATE INDEX "ix_CveReference_tags_CveReference_id" ON "CveReference_tags" ("CveReference_id");
