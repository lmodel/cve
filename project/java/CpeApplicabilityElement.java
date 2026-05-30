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
  Affected products defined using an implementation of the CPE Applicability Language. An operator property allows AND or OR logic between CPEs or combinations of CPEs.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CpeApplicabilityElement  {

  private String cpeOperator;
  private Boolean cpeNegate;
  private List<CpeNode> cpeNodes;


}