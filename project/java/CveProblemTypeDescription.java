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
  A problem type described in one language, often by a weakness identifier and its title.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveProblemTypeDescription  {

  private String lang;
  private String description;
  private String type;
  private List<CveReference> references;
  private String cweId;


}