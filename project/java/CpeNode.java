package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Defines a CPE configuration node in an applicability statement.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CpeNode  {

  private String cpeOperator;
  private boolean cpeNegate;
  private List<CpeMatch> cpeMatchCriteria;

}