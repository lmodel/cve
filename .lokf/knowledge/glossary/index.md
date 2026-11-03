# Glossary

* [CVE record](cve-record.md) - A CVE record: one document in the CVE Record Format, about one CVE identifier, either published or rejected. It holds `dataType`, `dataVersion`, `cveMetadata` and `containers`.
* [CNA](cna.md) - A CVE Numbering Authority: the organisation that assigned a CVE identifier, and that provides a record's one `cna` container. The class is `CveCnaPublishedContainer` or `CveCnaRejectedContainer`, by the record's state.
* [ADP](adp.md) - An Authorized Data Publisher: an organisation other than the assigning authority that adds a container to a published record. The class is `CveAdpContainer`, and it must hold something beside its provider's metadata.
* [CVSS](cvss.md) - The Common Vulnerability Scoring System: a way to score a vulnerability from 0 to 10, in versions 2.0, 3.0, 3.1 and 4.0. A metric in a record may hold a score in any of them, as `CvssV20`, `CvssV30`, `CvssV31` or `CvssV40`.
* [Extension key](extension-key.md) - A key a publisher adds to a container, whose name begins `x_` and holds no full stop, such as `x_generator`. The upstream allows it on the three containers, and a tag may take the same `x_` form.
* [Adapt copy](adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept` and each name LOKF also defines renamed.
