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
  A single version or a range of versions of a product with associated vulnerability status. An entry with only version and status is a point version; an entry with versionType and a less-than limit describes a range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VersionEntry  {

  private String versionValue;
  private String versionStatus;
  private String versionType;
  private String lessThan;
  private String lessThanOrEqual;
  private List<VersionChange> versionChanges;


}