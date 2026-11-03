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
  What an Authorized Data Publisher adds to a record beside the assigning authority's account.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveAdpContainer  {

  private CveProviderMetadata providerMetadata;
  private ZonedDateTime datePublic;
  private String title;
  private List<CveDescription> descriptions;
  private List<CveProduct> affected;
  private List<CveCpeApplicabilityElement> cpeApplicability;
  private List<CveProblemType> problemTypes;
  private List<CveReference> references;
  private List<CveImpact> impacts;
  private List<CveMetric> metrics;
  private List<CveDescription> configurations;
  private List<CveDescription> workarounds;
  private List<CveDescription> solutions;
  private List<CveDescription> exploits;
  private List<CveTimelineEvent> timeline;
  private List<CveCredit> credits;
  private CveSource source;
  private List<String> tags;
  private List<CveTaxonomyMapping> taxonomyMappings;


}