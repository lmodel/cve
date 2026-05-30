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
  A credit acknowledging a specific person, organization, or tool for work related to the research, discovery, remediation, or coordination of the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CreditEntry  {

  private String lang;
  private String creditValue;
  private String creditUser;
  private String creditType;


}