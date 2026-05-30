package None;

/* metamodel_version: 1.11.0 */
/* version: 5.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™ Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected records.
This class deliberately does NOT inherit from ``vulnerability_core.Vulnerability``: the upstream CVE Record Format places the CVE ID inside ``cveMetadata.cveId`` rather than at the record root. Semantic equivalence with the broader ``Vulnerability`` concept is preserved via ``exact_mappings``.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CVERecord  {

  private String dataType;
  private String dataVersion;
  private CveMetadata cveMetadata;
  private Containers containers;


}