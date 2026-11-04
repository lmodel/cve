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
  The containers of a published record, the assigning organisation's and any others'.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvePublishedContainers extends CveContainers {

  private List<CveAdpContainer> adp;


}