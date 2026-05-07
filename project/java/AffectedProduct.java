package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Information about the set of products and services affected by a vulnerability. At least one of (vendor + product) or (collectionURL + packageName) is required, and at least one of versions or defaultStatus is required.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AffectedProduct extends Product {

  private String collectionUrl;
  private String packageName;
  private List<String> cpes;
  private List<String> modules;
  private List<String> programFiles;
  private List<ProgramRoutine> programRoutines;
  private String repo;
  private String defaultStatus;
  private List<VersionEntry> versions;
  private String packageUrl;

}