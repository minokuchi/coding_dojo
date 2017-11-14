var daysUntilMyBirthday = 60;

for (daysUntilMyBirthday; daysUntilMyBirthday >=0; daysUntilMyBirthday--) 
{
    if (daysUntilMyBirthday >=30)
    {
    console.log(daysUntilMyBirthday, "days until my birthday. Such a long tine ...");
    }
    else if (daysUntilMyBirthday <30 && daysUntilMyBirthday >5)
    {
    console.log(daysUntilMyBirthday, "days until my birthday. Less than a month away!");
    }
    else if (daysUntilMyBirthday <5 && daysUntilMyBirthday >=2)
    {
    console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY. WOOHOO! I\"M GONNA HAVE PARTY");
    }
    else if (daysUntilMyBirthday ==1)
    {
    console.log(daysUntilMyBirthday, "DAY UNTIL MY BIRTHDAY. WOOHOO! I\"M GONNA HAVE A REALLY BIG PARTY");
    }
    else if (daysUntilMyBirthday ==0)
    {
    console.log("*** HAPPY BIRTHDAY TO ME! HAPPY BIRTHDAY TO ME! HAPPY BIRTHDAY TO ME! ***")
    }
}
