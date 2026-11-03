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
  A description whose language tag is English, which every list of descriptions must include.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CveEnglishLanguageDescription  {

  private String lang;


}