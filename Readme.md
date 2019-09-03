This program is aimed at parse a course schadule into importable csv file for Google Calendar.

To run this program, input "python main.py" with options including:
-f: str, the path of the course schedule which should be a csv file
-t: str, the path in which the generated importable calendat csv file will be saved
-s: str, the start date of the semester which should be of format: Month-Day-Year
-e: str, the end date of the semester which should be of format: Month-Day-Year

Additional:
The course schedule file should have the properties below:
    course_name,
    start_time,
    end_time,
    weekdays,
    descirption,
    location
where start_time and end_time should be of format like 8:00 AM. Weekdays should be a string, in which the days (indexed from 0) in the week that one will have this course are splitted by ";". For instance, "0;2" means this course is on Monday and Wednesday. Location should be a full name of the building which can be found on Google Maps.

course_schedule.csv and calendar.csv is the demo data file.

After this is done. Open Google Calendar. Click on Settings on the upper-right corner. Click on the Import/Export on the left. Choose the generated calendar.csv as the file that need to be imported and done.