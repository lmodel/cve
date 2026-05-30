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
  Defines a CPE configuration node in an applicability statement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CpeNode  {

  private String cpeOperator;
  private Boolean cpeNegate;
  private List<CpeMatch> cpeMatchCriteria;


}