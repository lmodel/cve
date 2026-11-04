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
  The facts about a record itself, as distinct from the vulnerability it describes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CveMetadata  {

  private ZonedDateTime dateUpdated;
  private String state;
  private String cveId;
  private String assignerOrgId;
  private String assignerShortName;
  private Integer serial;
  private ZonedDateTime dateReserved;
  private ZonedDateTime datePublished;


}