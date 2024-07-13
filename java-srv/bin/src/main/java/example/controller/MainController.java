package example.controller;

import org.springframework.ui.Model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import example.services.WeekService;
import example.services.ProjectService;

@Controller
public class MainController {

    @Autowired
    WeekService weekService;
	
	@Autowired
	ProjectService projectService;

	@RequestMapping(path="/", method=RequestMethod.GET)
	public String getIndex(Model model){
		final String title = "Main";
		model.addAttribute("title", title);
		weekService.getWeek(0, model);
		return "index";
	}
	
	@RequestMapping(path="/current", method=RequestMethod.GET)
	public String getCurrent(Model model){
		final String title = "Current";
		model.addAttribute("title", title);
		weekService.getWeek(0, model);
		projectService.getCurrent(model);
		return "current";
	}

	@RequestMapping(path="/historical", method=RequestMethod.GET)
	public String getHistorical(Model model){
		final String title = "Historical";
		model.addAttribute("title", title);
		weekService.getWeek(0, model);
		projectService.getHistorical(model);
		return "historical";
	}
}
