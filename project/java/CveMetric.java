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
  One scoring of the vulnerability, in a CVSS version or another format, and where it applies.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveMetric  {

  private String format;
  private List<CveMetricScenario> scenarios;
  private CvssV40 cvssV40;
  private CvssV31 cvssV31;
  private CvssV30 cvssV30;
  private CvssV20 cvssV20;
  private CveOtherMetric other;


}