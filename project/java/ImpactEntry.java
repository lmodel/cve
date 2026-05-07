package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  An impact entry linking an optional CAPEC attack pattern ID to one or more prose descriptions of the impact scenario.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ImpactEntry  {

  private String capecId;
  private List<MultiLangDescription> impactDescriptions;

}