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
  How the vulnerability relates to one version of an outside taxonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveTaxonomyMapping  {

  private String taxonomyName;
  private String taxonomyVersion;
  private List<CveTaxonomyRelation> taxonomyRelations;


}