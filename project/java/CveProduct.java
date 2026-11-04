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
  One affected product or package, and which of its versions are affected.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveProduct  {

  private String vendor;
  private String product;
  private URI collectionURL;
  private String packageName;
  private URI packageURL;
  private List<String> cpes;
  private List<String> modules;
  private List<String> programFiles;
  private List<CveProgramRoutine> programRoutines;
  private List<String> platforms;
  private URI repo;
  private String defaultStatus;
  private List<CveProductVersion> versions;


}