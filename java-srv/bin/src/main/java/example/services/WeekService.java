package example.services;

// Importing required classes
import org.springframework.stereotype.Service;

import org.springframework.ui.Model;
import org.springframework.beans.factory.annotation.Autowired;

import example.model.week.Weeks;
import example.model.week.Week;

// Annotation
@Service
 
// Class
public class WeekService {

    @Autowired
    JSONService jsonService;

	public void getWeek(int index, Model model){
		Weeks weeks = jsonService.read("week.json", Weeks.class);
		Week w = weeks.getWeeks()[index];
		model.addAttribute("number", ""+(20-index));
		model.addAttribute("from", w.getFrom());
		model.addAttribute("to", w.getTo());
	}
}