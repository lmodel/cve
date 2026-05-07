package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A status change that takes place at a specific point within a version range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VersionChange  {

  private String changeAt;
  private String changeStatus;

}