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
  An external reference associated with a CVE Record. Extends the core Reference with optional descriptive tags characterizing the resource.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveReference extends Reference {

  private List<String> referenceTags;


}