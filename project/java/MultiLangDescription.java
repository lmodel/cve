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
  Text in a particular language with optional alternate markup or formatted representation (e.g., Markdown) or embedded media. Used for vulnerability descriptions, rejected reasons, configurations, workarounds, solutions, and exploits.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MultiLangDescription  {

  private String lang;
  private String descriptionValue;
  private List<SupportingMedia> supportingMedia;


}