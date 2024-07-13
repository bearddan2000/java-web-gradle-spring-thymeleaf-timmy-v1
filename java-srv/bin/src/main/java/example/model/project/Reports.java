package example.model.project;

import lombok.*;
import java.util.*;

import example.common.CommonNote;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Reports implements INote {
    private String day;
    private Character id;
    private Child bus;
    private Child bedtime;
    private Child sleep;
    private Child eat;
    private Child morning;
    private Child hygien;
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