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
  A score or impact statement in a format the record format does not name.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveOtherMetric  {

  private String type;
  private CveOtherMetricContent content;


}