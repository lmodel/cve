package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  A relationship between a taxonomy item and a CVE or another taxonomy item. Provides subject (taxonomyId), predicate (relationshipName), and object (relationshipValue).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaxonomyRelation  {

  private String taxonomyId;
  private String relationshipName;
  private String relationshipValue;

}