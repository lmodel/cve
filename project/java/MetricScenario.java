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
  A scenario description indicating the context in which a metric applies. If no specific scenario is given, GENERAL is used as the default.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetricScenario  {

  private String lang;
  private String scenarioValue;


}