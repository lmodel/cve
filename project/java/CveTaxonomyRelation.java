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
  One relationship from an item in a taxonomy to this CVE or to another item.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveTaxonomyRelation  {

  private String taxonomyId;
  private String relationshipName;
  private String relationshipValue;


}