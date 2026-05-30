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
  Information about the set of products and services affected by a vulnerability. At least one of (vendor + product) or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.
Note: this class deliberately does NOT inherit from ``vulnerability_core.Product``. The upstream CVE ``product`` definition uses a multivalued ``versions`` slot (range ``VersionEntry``), which conflicts with ``Product.version`` (singular string). The ``vendor``, ``name`` (= upstream ``product``), and ``platforms`` slots are reused from the core schema directly. Semantic equivalence is preserved via ``exact_mappings``.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedProduct  {

  private String vendor;
  private String name;
  private List<String> platforms;
  private URI collectionUrl;
  private String packageName;
  private List<String> cpes;
  private List<String> modules;
  private List<String> programFiles;
  private List<ProgramRoutine> programRoutines;
  private URI repo;
  private String defaultStatus;
  private List<VersionEntry> versions;
  private URI packageUrl;


}