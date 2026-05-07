package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  Problem type information (e.g., CWE identifier). Wraps one or more problem type descriptions. The CNA requirement is [PROBLEMTYPE].
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProblemType  {

  private List<ProblemTypeDescription> problemTypeDescriptions;

}