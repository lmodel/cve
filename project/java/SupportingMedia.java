package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Supporting media data for a description such as markdown, diagrams, etc. Similar to RFC 2397, each media object has a media type, data value, and an optional base64 flag.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SupportingMedia  {

  private String mediaType;
  private boolean base64Encoded;
  private String mediaValue;

}