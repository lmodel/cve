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
  The sets of vulnerability information in a record, one per providing organisation.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CveContainers  {

  private CveCnaContainer cna;


}