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
  An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a rejected CVE ID. There can only be one CNA container per CVE record.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CnaRejectedContainer extends CnaContainer {

  private ProviderMetadata providerMetadata;
  private List<MultiLangDescription> rejectedReasons;
  private List<String> replacedBy;


}