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
  Details related to the information container provider (CNA or ADP).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProviderMetadata  {

  private String orgId;
  private String shortName;
  private String dateUpdated;


}