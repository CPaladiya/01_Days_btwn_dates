#calculated number of days in a year

def Days_btwn_dates(month1,day1,year1,month2,day2,year2):
    """
    Return a number of days between two dates

    parameters:
    dates(int) - month,day,year

    Returns:
    (int) - number of days between two dates (it does include the initial day and ignores the last day.)
    """
    if year1>year2:
        raise Exception('The date2 has to be earlier than date1. No time travel allowed.')
        print('ran1')
    elif year1==year2 and month1>month2:
        raise Exception('The date2 has to be earlier than date1. No time travel allowed.')
        print('ran2')
    elif year1==year2 and month1==month2 and day1>day2:
        raise Exception('The date2 has to be earlier than date1. No time travel allowed.')
        print('ran3')

    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    m_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

    #program to calculate the days on and after day1 
    if year1%4==0: #leap year scenario
        day_after_day1 = sum([days if i+1>month1 else 0 for i,days in enumerate(m_leap)])
        day_after_day1 += m_leap[month1-1] - day1+1 #remaining days in a month towards end of the year
        print(day_after_day1)
    else: #simple year scenario
        day_after_day1 = sum([days if i+1>month1 else 0 for i,days in enumerate(m)])
        day_after_day1 += m[month1-1] - day1+1 #remaining days in a month towards end of the year
        print(day_after_day1)

    #program to calculate the days before day2
    if year2%4==0:#leap year scenario
        day_before_day2 = sum([days if i+1<month2 else 0 for i,days in enumerate(m_leap)])
        day_before_day2 += day2-1 #remaining days in a month towards start of the year
        print(day_before_day2)
    else:#simple year scenario
        day_before_day2 = sum([days if i+1<month2 else 0 for i,days in enumerate(m)])
        day_before_day2 += day2-1 #remaining days in a month towards start of the year
        print(day_before_day2)

    #calculate the time between years
    if year2-year1>1: #days in middle years
        year = [i for i in range(year1+1,year2)]
        days_inbet_years = sum([366 if one_year%4==0 else 365 for one_year in year])
        print(days_inbet_years)
    elif year2-year1 == 0 and year1%4==0: #operator to_balance days when both date has same year and a leap year
        days_inbet_years = -366
    elif year2-year1 == 0: #operator to_balance days when both date has same year and simple year
        days_inbet_years = -365
    else:
        days_inbet_years = 0 #both dates is in consecutive year
    
    total_days = days_inbet_years + day_after_day1 + day_before_day2
    return total_days