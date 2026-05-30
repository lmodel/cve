package None;

/* metamodel_version: 1.11.0 */
/* version: 5.2.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A taxonomy mapping identifying the taxonomy by name and version, along with a list of relations relevant to the CVE (e.g., ATT&CK, D3FEND, CWE).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaxonomyMapping  {

  private String taxonomyName;
  private String taxonomyVersion;
  private List<TaxonomyRelation> taxonomyRelations;


}