package example.services;

// Importing required classes
import org.springframework.stereotype.Service;
 
import java.io.File;
import java.io.IOException;
import com.fasterxml.jackson.databind.ObjectMapper;

// Annotation
@Service
 
// Class
public class JSONService {

	public <T> T read(String filename, Class<T> c){
		if(filename.contains("0"))
			filename = filename.substring(2);
		// create Object Mapper
		ObjectMapper mapper = new ObjectMapper();

		// read JSON file and map/convert to java POJO
		try {
			T someClassObject = mapper.readValue(new File("src/main/resources/" + filename), c);
			// System.out.println(someClassObject);
			return someClassObject;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}
}