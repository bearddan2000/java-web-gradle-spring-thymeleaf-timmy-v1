package example.model.project;

import lombok.*;
import java.util.*;

import example.common.CommonNote;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Child implements INote{
    private Integer id;
    private Integer[] notes;
    private List<String> finalNotes;

    @Override
    public List<String> getFullNotes(Note fullNotes){
        return CommonNote.joinNotes(this.notes, fullNotes);
    }

    @Override
    public void setFinalNotes(Integer[] notes, Note fullNotes){
        this.finalNotes = new ArrayList<String>();
        List<String> commonNote;

        if(notes == null){
            System.out.println("[ERROR] notes are null");
            return;
        }
        else if(fullNotes == null){
            System.out.println("[ERROR] fullNotes are null");
            return;
        }
        commonNote = CommonNote.joinNotes(notes, fullNotes);
        if(commonNote == null){
            System.out.println("[ERROR] commonNote returned null");
            return;
        }
        this.finalNotes = commonNote;
    }
}