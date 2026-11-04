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
  One dated event in the vulnerability's history.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveTimelineEvent  {

  private String lang;
  private String value;
  private ZonedDateTime time;


}