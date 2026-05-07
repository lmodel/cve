package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  An object containing vulnerability information provided by a CVE Numbering Authority (CNA) for a published CVE ID. There can only be one CNA container per CVE record since there can only be one assigning CNA.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CnaPublishedContainer extends CnaContainer {

  private ProviderMetadata providerMetadata;
  private String dateAssigned;
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
  private List<String> cnaTags;
  private List<TaxonomyMapping> taxonomyMappings;

}