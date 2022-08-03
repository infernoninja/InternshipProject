# InternshipProject
This is a problem I encountered during my 4 week internship and this is how I solved it. 

Basically, if you have used netsuite oracle before, you realize that sorting cases (if it is implemented in your system) is absolutely repetitive and draining. I designed
a bot using selenium python to webscrape and update these cases. It is partial automated as some cases are one of a kind, but it can be automated even further if I had more
time. It looks for a very specific substring in a string acquired from the case title and updates it accordingly. If it does not find the 5 substrings listed, then it
asks for user inputs if it finds that three of the inputs are empty. I can use some_web_element.send_keys(some_variable) because the system actually uses a dropdown system
where you can type and it automatically fills in the correct field. 
