# References

* [CVE Record Format](cve-record-format.md) - The JSON format in which the CVE Program publishes a record of a vulnerability: `schema/CVE_Record_Format.json` in `CVEProject/cve-schema`, version 5.2.0, published on 29 October 2025 under CC0 1.0. The schema renders this edition.
* [CVSS schemas](cvss-schemas.md) - The JSON schemas of the Common Vulnerability Scoring System (CVSS), versions 2.0, 3.0, 3.1 and 4.0, which FIRST maintains and the CVE Program keeps as local modified copies in `schema/imports/cvss/`. The module follows the CVE Program's copies.
* [CVE list](cve-list.md) - `CVEProject/cvelistV5`, the repository that holds real CVE records in this format, where the sample of real records is pinned at one commit. It states no licence of its own and points to the CVE Program's Terms of Use.
* [CVE Program Terms of Use](cve-terms-of-use.md) - The terms real CVE records come under. They allow copies provided each reproduces MITRE's copyright designation and the licence, which NOTICE and `tests/data/cvelist/TERMS.txt` do. The watch reads the page's source file, because the page is written by script.
