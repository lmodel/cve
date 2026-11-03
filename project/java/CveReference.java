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
  A link to something about the vulnerability, such as an advisory or a patch.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveReference  {

  private URI url;
  private String name;
  private List<String> tags;


}