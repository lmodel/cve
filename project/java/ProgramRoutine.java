package None;

/* metamodel_version: 1.7.0 */
/* version: 5.2.0 */
import java.util.List;
import lombok.*;

/**
  An affected source code function, method, subroutine, or procedure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ProgramRoutine  {

  private String routineName;

}