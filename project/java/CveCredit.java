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
  Thanks to someone who helped, in one language.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveCredit  {

  private String lang;
  private String value;
  private String type;
  private String user;


}