var HOUR = 7;
var MINUTE = 7;
var PERIOD = "PM";

if (HOUR == 7 && MINUTE <15 && PERIOD =="AM") 
{
    console.log("It's a little past 7 in the morning");
}
else if (HOUR == 7 && MINUTE <15 && PERIOD =="PM") 
{
    console.log("It's a little past 7 in the evening");
}
else if (HOUR == 7 && MINUTE >=15 && MINUTE <30 && PERIOD == "AM" )
{
    console.log("It's about a quarter past 7 in the morning");
}
else if (HOUR == 7 && MINUTE >=15 && MINUTE <30 && PERIOD == "PM" )
{
    console.log("It's about a quarter past 7 in the evening");
}
else if (HOUR == 7 && MINUTE >=30 && MINUTE <45 && PERIOD == "AM" )
{
    console.log("It's about half past 7 in the morning");
}
else if (HOUR == 7 && MINUTE >=30 && MINUTE <45 && PERIOD == "PM" )
{
    console.log("It's about half past 7 in the evening");
}
else if (HOUR == 7 && MINUTE >=45 && PERIOD == "AM" )
{
    console.log("It's quarter of 8 in the morning");
}
else if (HOUR == 7 && MINUTE >=45 && PERIOD == "PM" )
{
    console.log("It's quarter of 8 in the evening");
}
