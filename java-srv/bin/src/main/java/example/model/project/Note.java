package example.model.project;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Note {
    private FullNotes[] fullnotes;
}