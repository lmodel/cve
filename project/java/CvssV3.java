package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  CVSS version 3.x scoring object covering both CVSS 3.0 and CVSS 3.1. The two versions share an identical metric model; the 3.1 spec was a clarification, not a structural change. The cvss3_version slot distinguishes between them. Requires version ('3.0' or '3.1'), vectorString, baseScore, and baseSeverity.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV3  {

  private String cvss3Version;
  private String cvss3VectorString;
  private String cvss3AttackVector;
  private String cvss3AttackComplexity;
  private String cvss3PrivilegesRequired;
  private String cvss3UserInteraction;
  private String cvss3Scope;
  private String cvss3ConfidentialityImpact;
  private String cvss3IntegrityImpact;
  private String cvss3AvailabilityImpact;
  private float cvss3BaseScore;
  private String cvss3BaseSeverity;
  private String cvss3ExploitCodeMaturity;
  private String cvss3RemediationLevel;
  private String cvss3ReportConfidence;
  private Float cvss3TemporalScore;
  private String cvss3TemporalSeverity;
  private String cvss3ConfidentialityRequirement;
  private String cvss3IntegrityRequirement;
  private String cvss3AvailabilityRequirement;
  private String cvss3ModifiedAttackVector;
  private String cvss3ModifiedAttackComplexity;
  private String cvss3ModifiedPrivilegesRequired;
  private String cvss3ModifiedUserInteraction;
  private String cvss3ModifiedScope;
  private String cvss3ModifiedConfidentialityImpact;
  private String cvss3ModifiedIntegrityImpact;
  private String cvss3ModifiedAvailabilityImpact;
  private Float cvss3EnvironmentalScore;
  private String cvss3EnvironmentalSeverity;

}