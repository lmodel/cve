package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  CVSS version 2.0 scoring object. Requires version ('2.0'), vectorString, and baseScore.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV20  {

  private String cvss2Version;
  private String cvss2VectorString;
  private String cvss2AccessVector;
  private String cvss2AccessComplexity;
  private String cvss2Authentication;
  private String cvss2ConfidentialityImpact;
  private String cvss2IntegrityImpact;
  private String cvss2AvailabilityImpact;
  private float cvss2BaseScore;
  private String cvss2Exploitability;
  private String cvss2RemediationLevel;
  private String cvss2ReportConfidence;
  private Float cvss2TemporalScore;
  private String cvss2CollateralDamagePotential;
  private String cvss2TargetDistribution;
  private String cvss2ConfidentialityRequirement;
  private String cvss2IntegrityRequirement;
  private String cvss2AvailabilityRequirement;
  private Float cvss2EnvironmentalScore;

}