import pandas as pd
import datetime
from optparse import OptionParser

def mk_cal(courses, semester_start, semester_end):
    '''
    Courses should be a pandas.DataFrame which should have propertities
    as listed: course_name, start time, end time, weekdays, descirption,
    location.
    '''
    txt = "Subject,Start Date,Start Time,End Time,End Date,Description,Location\n"
    for i in range(len(courses)):
        course = courses.iloc[i]
        one_day = datetime.timedelta(days=1)
        for i in range(int((semester_end - semester_start) / one_day)):
            day = semester_start + i * one_day
            weekdays = [int(i) for i in course['weekdays'].split(';')]
            if day.weekday() in weekdays:
                txt += course['course_name'] + ','
                txt += str(day.month) + '/' + str(day.day) + '/' + str(day.year) + ','
                txt += course['start_time'] + ','
                txt += course['end_time'] + ','
                txt += str(day.month) + '/' + str(day.day) + '/' + str(day.year) + ','
                txt += course['description'] + ','
                txt += course['location'] + '\n'
    return txt

def read_file(path):
    return pd.read_csv(path, keep_default_na=False, dtype=str)

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_date(date):
    return datetime.datetime.strptime(date, "%m-%d-%Y")

if __name__ == '__main__':
    usage = "Parse course schedule to importable csv for google calendar"
    parser = OptionParser(usage)
    parser.add_option("-f","--from", dest="from_file", help="read course schedule",\
                    type="string")
    parser.add_option("-t", "--to", dest="to_file", help="save calendar to file",\
                    default="./calendar.csv")
    parser.add_option("-s", "--start", dest="sem_start", help="start date of semester",\
                    type="string")
    parser.add_option("-e", "--end", dest="sem_end", help="end date of semester",\
                    type="string")
    

    (options, args) = parser.parse_args()
    try:
        semester_start = parse_date(options.sem_start)
        semester_end = parse_date(options.sem_end)
    except:
        print('------------------------------------')
        print("Date format should be month-day-year")
        print('------------------------------------')
        exit()
    courses = read_file(options.from_file)
    calendar = mk_cal(courses, semester_start, semester_end)
    write_file(options.to_file, calendar)

