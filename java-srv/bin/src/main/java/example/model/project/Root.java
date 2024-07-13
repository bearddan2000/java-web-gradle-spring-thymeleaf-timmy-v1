package example.model.project;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Root {
    private Projects[] projects;
}