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
  A piece of text in one language, with any media that support it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveDescription  {

  private String lang;
  private String value;
  private List<CveSupportingMedia> supportingMedia;


}