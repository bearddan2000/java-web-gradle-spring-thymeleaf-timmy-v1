package example.services;

// Importing required classes
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;
import org.springframework.beans.factory.annotation.Autowired;

import java.time.*;
import java.time.temporal.*;
import java.time.format.*;

import java.util.List;
import java.util.ArrayList;

import example.model.project.Root;
import example.model.project.Reports;
import example.model.project.Child;
import example.model.project.INote;
import example.model.project.FullNotes;
import example.model.project.Note;

// Annotation
@Service
 
// Class
public class ProjectService {

    @Autowired
    JSONService jsonService;

	enum iterateFlag {
		CURRENT,
		HISTORICAL
	};

	private Reports getday(int index){
		Root root = jsonService.read("project.json", Root.class);
		return root.getProjects()[0].getReports()[index];
	}

	private List<String> getNotes(String filename, INote child){
		Note notes = jsonService.read(filename+".json", Note.class);
		return child.getFullNotes(notes);
	}

	private void setModelNotes(String filename, Child child, Model model){
		List<String> lst = this.getNotes(filename, child);
		model.addAttribute(filename, child);
		model.addAttribute(filename+"Notes", lst);
	}
	
	private void setModelGeneralNotes(String filename, Reports day, Model model){
		List<String> lst = this.getNotes(filename, day);
		model.addAttribute("Notes", lst);
	}

	private Reports iterateWeek(Model model, int weekday, iterateFlag flag){
		final String[] dayNames = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
		Reports day = this.getday(weekday);
		Child bus = day.getBus();
		Child bedtime = day.getBedtime();
		Child sleep = day.getSleep();
		Child eat = day.getEat();
		Child morning = day.getMorning();
		Child hygien = day.getHygien();

		if(flag == iterateFlag.HISTORICAL) {
			day.setDay(dayNames[weekday]);
			Note notes = jsonService.read("notes.json", Note.class);
			day.setFinalNotes(day.getNotes(), notes);
			notes = jsonService.read("bus.json", Note.class);
			bus.setFinalNotes(bus.getNotes(), notes);
			notes = jsonService.read("bedtime.json", Note.class);
			bedtime.setFinalNotes(bedtime.getNotes(), notes);
			notes = jsonService.read("eat.json", Note.class);
			eat.setFinalNotes(eat.getNotes(), notes);
			notes = jsonService.read("sleep.json", Note.class);
			sleep.setFinalNotes(sleep.getNotes(), notes);
			notes = jsonService.read("hygien.json", Note.class);
			hygien.setFinalNotes(hygien.getNotes(), notes);
		} else {
			model.addAttribute("day", dayNames[weekday]);
			setModelGeneralNotes("notes", day, model);
			setModelNotes("bus", bus, model);
			setModelNotes("bedtime", bedtime, model);
			setModelNotes("sleep", sleep, model);
			setModelNotes("eat", eat, model);
			setModelNotes("morning", morning, model);
			setModelNotes("hygien", hygien, model);
		}
		return day;
	}

	public void getCurrent(Model model){
		int output = 0;
		try {
			output = LocalDate.now().getDayOfWeek().getValue();
			output--; // week starts on Sunday
		}
		catch(Exception e){}
		this.iterateWeek(model, output, iterateFlag.CURRENT);
	}
	public void getHistorical(Model model){
		List<Reports> lst = new ArrayList<Reports>();
		for(int i = 0; i < 5; i++){
			Reports day = this.iterateWeek(model, i, iterateFlag.HISTORICAL);
			lst.add(day);
		}
		model.addAttribute("lst", lst);
	}
}