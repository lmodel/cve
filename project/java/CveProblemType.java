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
  One kind of problem the vulnerability is, in one or more languages.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveProblemType  {

  private List<CveProblemTypeDescription> descriptions;


}