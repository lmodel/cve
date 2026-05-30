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
  Abstract base for CVE Record metadata. Represents either a Published or Rejected record's metadata. All fields are controlled by CVE Services. Polymorphism is provided via ``is_a`` on the two concrete subclasses (``CveMetadataPublished``, ``CveMetadataRejected``); slot-level ``any_of`` on the ``cve_metadata`` slot preserves the choice for generators (e.g. JSON Schema ``anyOf``).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CveMetadata  {



}