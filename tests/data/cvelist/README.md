# Real CVE records

`manifest.json` pins a varied sample of real records from [CVEProject/cvelistV5](https://github.com/CVEProject/cvelistV5) by path, size, SHA-256 and git object hash, at one commit. Its `selection` key says how they were chosen. The list itself stays out of git.

`extract/` holds a few of them, copied unchanged, so `just test` validates real records with no network. [TERMS.txt](TERMS.txt) carries MITRE's copyright designation and licence, as the Terms of Use ask of every copy. They were picked as the smallest records that show each feature and credit no person.

`just fetch-cve-records` downloads the rest into `tmp/cvelist/`, and `just test-cve-records` validates each one unchanged.
