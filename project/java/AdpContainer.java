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
  An object containing vulnerability information provided by an Authorized Data Publisher (ADP). Multiple ADPs can provide containers for a single CVE ID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AdpContainer  {

  private ProviderMetadata providerMetadata;
  private String datePublic;
  private String title;
  private List<MultiLangDescription> descriptions;
  private List<AffectedProduct> affected;
  private List<CpeApplicabilityElement> cpeApplicability;
  private List<ProblemType> problemTypes;
  private List<CveReference> cveReferences;
  private List<ImpactEntry> impacts;
  private List<MetricEntry> metrics;
  private List<MultiLangDescription> configurationsText;
  private List<MultiLangDescription> workarounds;
  private List<MultiLangDescription> solutions;
  private List<MultiLangDescription> exploits;
  private List<TimelineEntry> timeline;
  private List<CreditEntry> credits;
  private SourceInformation cnaSource;
  private List<String> adpTags;
  private List<TaxonomyMapping> taxonomyMappings;


}