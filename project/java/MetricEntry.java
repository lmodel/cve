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
  A metric entry containing scoring data in one of the CVSS formats (v4.0, v3.x, v2.0) or a custom format, with optional applicability scenarios. At least one of cvss_v4_0, cvss_v3, cvss_v2_0, or other_metric is required. CVSS 3.0 and 3.1 are both represented by CvssV3 (distinguished by the cvss3_version slot).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MetricEntry  {

  private String metricFormat;
  private List<MetricScenario> metricScenarios;
  private CvssV40 cvssV40;
  private CvssV3 cvssV3;
  private CvssV20 cvssV20;
  private OtherMetric otherMetric;


}