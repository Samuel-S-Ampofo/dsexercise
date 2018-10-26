4. Assignments
4.5. Scraping
The best way to get people on your social network is without letting them register at all. To accomplish that you’re going to scrape websites that contain personal data, analyze and clean up the data, and display and save it.

Objective

Create a Jupyter Notebook that scrapes and cleans and data from a website and saves that to a csv file.

What you need to master for this assignment

Everything you learned in week 1, 2, 3 and 4
Functions, function arguments and return statements
Basic knowledge of HTML and how classes, ids and other attributes can help you to fetch information
Basic knowledge of CSS queries
The bs4/BeautifulSoup library to do web scraping
How to use CSS selectors to do a query in BeautifulSoup
Use the get_text and get methods of BeautifulSoup to get text from an element, and data from attributes
Use the to_csv method of a Pandas dataframe to a CSV file
What your program should do

For this assignment you need to find a website yourself that you’re going to scrape. That website should have:

One or more pages containing names, whether fictional or not, that you can transform into a CSV file.
Those names should link to a user page containing more information on that person.
Usernames don’t need to be real names. Be creative and use Google to find a repository of user lists. Think about sporting clubs, social media sites, pages on company websites listing all employees, etcetera. Search for things like “our employees”, “member list” or maybe a couple of common names and street names.

Examples (you can't use these for the assignment!):

A club for journalists who play golf. Here is the overview page, and here’s an example of a user detail page.
A Norwegian institute for aquatic research. Here’s an overview page, and here’s a detail page.          
Here’s a list of Dutch politicians and a detail page.
Your program must:

Use the requests library to get the overview page and feed the HTML of that page to the BeautifulSoup library.
Use the select method of BeautifulSoup to make a list of the items containing the names, whether that are table rows, list elements, divs, etcetera.
Loop through that list and get the basic information out of the rows and append that as a dict to a list. You should at least get the person's name and the link to their 'detail' page. Optionally, limit this list to the first 25 people on the page.
If there are multiple 'overview pages' (paginated), you only need to get the first page.
Do some data cleaning, such as removing extraneous newlines and whitespace, combining first and last names, etcetera. 
Also get the link to the user detail page and add that to the list as well.
Convert the list with dicts to a Pandas dataframe, save it to a CSV file and display the dataframe in the Notebook.
Loop through the list again, fetch the user detail page with requests, parse that using BeautifulSoup and add user detail information to the list.
Convert the ‘expanded’ list with dicts to a Pandas dataframa and save that to a CSV file, and display the dataframe in the Notebook.
Your program must also:

Be properly commented in the code in your notebook.
Be executable using the Jupyter Notebook webapp.
Notes:

A typical assignment will be around 75 - 125 lines of code
Before re-running your scraping code doing the HTTP request, save the page to a local HTML file and load that in your code. This is faster and lessens the change that the website will block your IP. However, your submitted assignment needs to fetch the data from an URL, not a HTML file!
If you hit a site that doesn’t have a list but a search box try hitting enter or searching for the character ‘a’ or something like that.
The difficulty of scraping can widely differ between websites. It depends on the structure of the HTML, if the content is dynamically altered with Javascript and if the website has security measures in place to make it more difficult. There are a couple of tricks you can try if things get difficult:
Some sites don’t return the HTML because they expect a user-agent header. It’s easy to do that using the requests library. Try a simple user-agent header like ‘Mozilla/5.0’.
Chrome DevTools has a really handy option to see what gets send from the browser to the web server. Right click on a request in the ‘network’ tab in DevTools → Copy → ‘Copy as cURL’. Paste in a text editor to inspect the different things you can do. Try adding the some user agent in requests, or add the Cookie string.
Extra resources for the datalab

https://blog.pusher.com/introduction-web-scraping-python/
https://css-tricks.com/how-css-selectors-work/