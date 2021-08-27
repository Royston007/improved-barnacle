# improved-barnacle
Work Samples in Python and JavaScript for various scenarios such as Josephus algorithm and Asynchronous data table updates 
1. MVCApplication1 contains required code for Asynchrnous datatable updates without page reloads performed by user.
   Controller logic uses static keyword to provide database-like save operation until the time ASP.NET dev server is running.
   1. Run InitF() in console
   2. Run AutoSync method in console as follows:
      AutoSync('http://localhost:13906/Home/Getdetails',null,'#main-div','#tblEmpResults',10000)

2. Josephus.py is the source code for Josephus algorithm solution using Circular LinkedList in Python.
   Code is mainly divided into two parts: 
   i. Initializing Circular LinkedList with custom length
   ii. While loop to set the next next pointer to the current objects next pointer to create logic of an alternate step taken.
   To Run application, please follow flask run command sequence in the .py script in the comments section
