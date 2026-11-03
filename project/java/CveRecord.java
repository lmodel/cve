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
  A record of one vulnerability under one CVE identifier, in the CVE Program's format.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CveRecord  {

  private CveMetadata cveMetadata;
  private CveContainers containers;
  private String dataType;
  private String dataVersion;


}