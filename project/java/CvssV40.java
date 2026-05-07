package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  CVSS version 4.0 scoring object. Requires version, vectorString, baseScore, and baseSeverity. All other fields are optional.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV40  {

  private String cvss4Version;
  private String cvss4VectorString;
  private float cvss4BaseScore;
  private String cvss4BaseSeverity;
  private String cvss4AttackVector;
  private String cvss4AttackComplexity;
  private String cvss4AttackRequirements;
  private String cvss4PrivilegesRequired;
  private String cvss4UserInteraction;
  private String cvss4VulnConfidentialityImpact;
  private String cvss4VulnIntegrityImpact;
  private String cvss4VulnAvailabilityImpact;
  private String cvss4SubConfidentialityImpact;
  private String cvss4SubIntegrityImpact;
  private String cvss4SubAvailabilityImpact;
  private String cvss4ExploitMaturity;
  private String cvss4ConfidentialityRequirement;
  private String cvss4IntegrityRequirement;
  private String cvss4AvailabilityRequirement;
  private String cvss4ModifiedAttackVector;
  private String cvss4ModifiedAttackComplexity;
  private String cvss4ModifiedAttackRequirements;
  private String cvss4ModifiedPrivilegesRequired;
  private String cvss4ModifiedUserInteraction;
  private String cvss4ModifiedVulnConfidentialityImpact;
  private String cvss4ModifiedVulnIntegrityImpact;
  private String cvss4ModifiedVulnAvailabilityImpact;
  private String cvss4ModifiedSubConfidentialityImpact;
  private String cvss4ModifiedSubIntegrityImpact;
  private String cvss4ModifiedSubAvailabilityImpact;
  private String cvss4Safety;
  private String cvss4Automatable;
  private String cvss4Recovery;
  private String cvss4ValueDensity;
  private String cvss4VulnerabilityResponseEffort;
  private String cvss4ProviderUrgency;

}