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
  Metadata for a CVE Record in the REJECTED state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveMetadataRejected extends CveMetadata {

  private String recordCveId;
  private String assignerOrgId;
  private String assignerShortName;
  private Integer serial;
  private String dateUpdated;
  private String dateReserved;
  private String datePublished;
  private String dateRejected;
  private String rejectedState;


}