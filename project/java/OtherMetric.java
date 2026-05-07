package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A non-standard impact description in a custom format. May be a prose description or an arbitrary JSON-compatible object.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OtherMetric  {

  private String otherMetricType;
  private Any otherMetricContent;

}