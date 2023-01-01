import re
from datetime import datetime

def get_year(inputdate):
    try:
        year_value = re.findall("\\d{4}", inputdate)
        year_value = year_value[0]
    except:
        year_value = datetime.now().year
    return year_value

def get_month(inputdate):
    regex_pattern1 = "jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"
    regex_pattern2 = "mei|agu|okt|nop|des"
    regex_pattern3 = "\\d{4}[\\-\\/]\\d{2}[\\-\\/]\\d{2}"
    regex_pattern4 = "\\d{2}[\\-\\/]\\d{2}[\\-\\/]\\d{4}"
    dict_month = {
        "mei":"may",
        "agu":"aug",
        "okt":"oct",
        "nop":"nov",
        "des":"dec",
        "01":"jan",
        "02":"feb",
        "03":"mar",
        "04":"apr",
        "05":"may",
        "06":"jun",
        "07":"jul",
        "08":"aug",
        "09":"sep",
        "10":"oct",
        "11":"nov",
        "12":"dec"
    }
    month = re.findall(regex_pattern1, inputdate.lower())
    if not month:
        month2 = re.findall(regex_pattern2, inputdate.lower())
        if not month2:
            #to match timeframe YYYY-MM-DD or YYYY/MM/DD
            month3 = re.findall(regex_pattern3, inputdate.lower())
            if not month3:
                #to match timeframe MM-DD-YYYY or MM/DD/YYYY
                month4 = re.findall(regex_pattern4, inputdate.lower())
                month4_val = re.sub("[\\-\\/]", "", month4[0])
                if int(month4_val[0:2]) > 12:
                    # to match timeframe DD-MM-YYYY or DD/MM/YYYY
                    month_value = dict_month[(month4_val[2:4])]
                else:
                    month_value = dict_month[(month4_val[0:2])]
            else:
                month3_val = re.sub("[\\-\\/]", "", month3[0])
                if int(month3_val[4:6]) > 12:
                    month_value = dict_month[(month3_val[-2:])]
                elif int(month3_val[-2:]) > 12:
                    month_value = dict_month[(month3_val[4:6])]
                else:
                    month_value = dict_month[(month3_val[4:6])]
        else:
            month_value = dict_month[month2[0]]
    else:
        month_value = month[0]
    return month_value.title()

def get_day(inputdate):
    date_pattern1 = "[A-Za-z]{3,}[\\-\\/]\\d{2}[\\-\\/]\\d{4}"
    date_pattern2 = "\\d{4}[\\-\\/]\\d{2}[\\-\\/]\\d{2}"
    date_pattern3 = "\\d{2}[\\-\\/]\\d{2}[\\-\\/]\\d{4}"
    date_pattern4 = "\\d{1,2}[\\-\\/ ][A-Za-z]{3,}[\\-\\/ ]\\d{4}"
    date_data = re.findall(date_pattern1, inputdate)
    if not date_data:
        date_data2 = re.findall(date_pattern2, inputdate)
        if not date_data2:
            date_data3 = re.findall(date_pattern3, inputdate)
            if not date_data3:
                date_data4 = re.findall(date_pattern4, inputdate)
                if not date_data4:
                    day_value = ""
                else:
                    date_data4 = re.sub("[\\-\\/ ][A-Za-z]{3,}[\\-\\/ ]\\d{4}", "", date_data4[0])
                    day_value = date_data4
            else:
                date_data3 = re.sub("\\D","", date_data3[0])
                if int(date_data3[:2]) > 12:
                    day_value = date_data3[:2]
                elif int(date_data3[2:4]) > 12:
                    day_value = date_data3[2:4]
                else:
                    day_value = date_data3[2:4]
        else:
            day_data = re.sub("\\D", "", date_data2[0])
            if int(day_data[-2:]) > 12:
                day_value = day_data[-2:]
            elif int(day_data[-4:-2]) > 12:
                day_value = day_data[-4:-2]
            else:
                day_value = day_data[-2:]
    else:
        day_value = re.sub("\\D", "", date_data[0])
        day_value = day_value[-6:-4]
    return day_value

def get_hour(inputdate):
    pattern1 = "\\d{1,2}[\\.\\:]\\d{2}[\\.\\:]\\d{2}\\s[APap][mM]"
    pattern2 = "\\d{1,2}[\\.\\:]\\d{2}[\\.\\:]\\d{2}"
    pattern3 = "\\d{1,2}[\\.\\:]\\d{2}\\s[APap][mM]"
    pattern4 = "\\d{1,2}[\\.\\:]\\d{2}"
    time_data = re.findall(pattern1, inputdate)
    if not time_data:
        time_data2 = re.findall(pattern2, inputdate)
        if not time_data2:
            time_data3 = re.findall(pattern3, inputdate)
            if not time_data3:
                time_data4 = re.findall(pattern4, inputdate)
                if not time_data4:
                    hour_value = "00"
                else:
                    hour_value = format_hour(time_data4[0])
            else:
                hour_value = check_abbreviation(time_data3[0])
        else:
            hour_value = format_hour(time_data2[0])
    else:
        hour_value = check_abbreviation(time_data[0])
    return hour_value

def check_abbreviation(time_data):
    time_data = re.sub("\\s", "", time_data)
    hour = re.findall("\\d{1,2}", time_data[:2])
    hour = hour[0]
    time_abbrev = time_data[-2:]
    if time_abbrev.lower() == "am":
        if int(hour) == 12:
            hour_value = "00"
        elif int(hour) < 10:
            hour_value = "0" + str(int(hour))
        else:
            hour_value = str(hour)
    elif time_abbrev.lower() == "pm":
        if hour == "12":
            hour_value = "12"
        elif int(hour) > 12:
            hour_value = str(hour)
        else:
            hour_value = str(int(hour) + 12)
    else:
        hour_value = ""
    return hour_value

def format_hour(time_data):
    hour = re.findall("\\d{1,2}", time_data[:2])
    hour = hour[0]
    if int(hour) == 12:
        hour_value = "00"
    elif int(hour) < 10:
        hour_value = "0" + str(int(hour))
    else:
        hour_value = str(hour)
    return hour_value

def get_minute(inputdate):
    time_pattern1 = "\\d{1,2}[\\.\\:]\\d{2}[\\.\\:]\\d{2}"
    time_pattern2 = "\\d{1,2}[\\.\\:]\\d{2}"
    time_data = re.findall(time_pattern1, inputdate)
    if not time_data:
        time_data2 = re.findall(time_pattern2, inputdate)
        if not time_data2:
            minute_value = "00"
        else:
            minute = time_data2[0][-2:]
            minute_value = minute
    else:
        minute = time_data[0][-5:-3]
        minute_value = minute
    return minute_value

def get_second(inputdate):
    time_pattern1 = "\\d{1,2}[\\.\\:]\\d{2}[\\.\\:]\\d{2}"
    time_pattern2 = "\\d{1,2}[\\.\\:]\\d{2}"
    time_data = re.findall(time_pattern1, inputdate)
    if not time_data:
        time_data2 = re.findall(time_pattern2, inputdate)
        if time_data2:
            second_value = "00"
        else:
            second_value = "00"
    else:
        second = time_data[0][-2:]
        second_value = second
    return second_value


def main():
    inputdate ="2022-13-30 01:13:27 AM"

    checkday = get_day(inputdate)
    checkmonth = get_month(inputdate)
    checkyear = get_year(inputdate)
    checkhour = get_hour(inputdate)
    checkminute = get_minute(inputdate)
    checksecond = get_second(inputdate)
    print(checkmonth+"-"+checkday+"-"+checkyear+" "+checkhour+":"+checkminute+":"+checksecond)

if __name__ == "__main__":
    main()
