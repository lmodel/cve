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
  A group of CPE matches, combined by an operator.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveCpeNode  {

  private String operator;
  private Boolean negate;
  private List<CveCpeMatch> cpeMatch;


}