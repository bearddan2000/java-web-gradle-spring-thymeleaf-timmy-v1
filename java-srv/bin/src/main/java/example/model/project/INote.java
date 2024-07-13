package example.model.project;
import java.util.List;

public interface INote{
    void setFinalNotes(Integer[] notes, Note fullNotes);
    List<String> getFullNotes(Note fullNotes);
}