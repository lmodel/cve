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
  The assigning authority's account of why a record was rejected.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveCnaRejectedContainer extends CveCnaContainer {

  private List<CveDescription> rejectedReasons;
  private List<String> replacedBy;


}