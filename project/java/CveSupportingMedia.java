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
  A richer form of a description, as a media type and its content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveSupportingMedia  {

  private String type;
  private String value;
  private Boolean base64;


}