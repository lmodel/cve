package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Source information (who discovered it, who researched it, etc.) and optionally a chain of CNA information. This is an open object — at least one property must be present.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SourceInformation  {

  private List<String> sourceDefects;
  private String sourceAdvisory;
  private String sourceDiscovery;

}