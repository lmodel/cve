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
  One CPE name, optionally bounded by versions, and whether it is vulnerable.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveCpeMatch  {

  private boolean vulnerable;
  private String criteria;
  private String matchCriteriaId;
  private String versionStartExcluding;
  private String versionStartIncluding;
  private String versionEndExcluding;
  private String versionEndIncluding;


}