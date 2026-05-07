package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A timeline event recording a significant event about the vulnerability or changes to the CVE Record. Requires time, lang, and value.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TimelineEntry  {

  private String eventTime;
  private String lang;
  private String eventValue;

}