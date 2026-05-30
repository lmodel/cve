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
  CPE match string or range within a CPE applicability node.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CpeMatch  {

  private boolean cpeVulnerable;
  private String cpeCriteria;
  private String matchCriteriaId;
  private String versionStartExcluding;
  private String versionStartIncluding;
  private String versionEndExcluding;
  private String versionEndIncluding;


}