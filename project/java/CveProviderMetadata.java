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
  Who provided a container, and when it was last updated.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveProviderMetadata  {

  private ZonedDateTime dateUpdated;
  private String orgId;
  private String shortName;


}