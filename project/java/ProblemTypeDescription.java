package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Individual problem type description entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProblemTypeDescription  {

  private String lang;
  private String problemDescription;
  private String cweId;
  private String problemSourceType;
  private List<CveReference> problemReferences;

}