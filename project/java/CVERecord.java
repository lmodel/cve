package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Official CVE Record corresponding to a CVE ID. Represents either a Published or Rejected record in the CVE™ Program. The dataType field is always CVE_RECORD. Use cveMetadata.state to distinguish Published from Rejected records.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CVERecord extends Vulnerability {

  private String dataType;
  private String dataVersion;
  private CveMetadata cveMetadata;
  private Containers containers;

}