package example;

/* metamodel_version: 1.12.0 */
/* version: 5.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A single version or a stretch of versions, and whether it is affected.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveProductVersion  {

  private String version;
  private String status;
  private String versionType;
  private String lessThan;
  private String lessThanOrEqual;
  private List<CveVersionChange> changes;


}