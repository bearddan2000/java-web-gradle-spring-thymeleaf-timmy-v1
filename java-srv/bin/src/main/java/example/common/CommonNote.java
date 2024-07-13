package example.common;

import java.util.List;
import java.util.ArrayList;

import example.model.project.Note;

public class CommonNote {
	public static List<String> joinNotes(Integer[] notes, Note fullNotes){

        List<String> noteList = new ArrayList<String>();
        try {
        for(Integer index : notes){
            String strNotes = fullNotes.getFullnotes()[index].getNote();
            noteList.add(strNotes);
        }
        } catch(Exception e){}
        return noteList;
	}
}
