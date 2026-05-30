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
  A set of structures (called containers) used to store vulnerability information related to a specific CVE ID. At minimum a 'cna' container is required.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Containers  {

  private CnaContainer cna;
  private List<AdpContainer> adp;


}