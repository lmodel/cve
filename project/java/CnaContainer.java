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
  Abstract base for CNA containers (published and rejected). Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CnaPublishedContainer``, ``CnaRejectedContainer``); slot-level ``any_of`` on the ``cna`` slot preserves the choice for generators.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CnaContainer  {



}