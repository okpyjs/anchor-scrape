# Create Bot to Crawl Websites & Return Information on Internal Links

I need a simple bot that crawls websites page source to count and list the incoming “internal links” and “anchor text” to the URL that user inputs.

The deliverable will consist of two pages.

PAGE ONE: User Entry
- User will enter URL that they want to know how many internal links are pointed at it
- Submit button

PAGE TWO: Reports Data Found
- While program is working it will have an “in progress” icon
- Returns a pie chart at the top of the page showing the amount of each anchor text used up to 9 and then 10 will be all the rest and called “other”
- Returns the total inner links pointing to URL of user’s input
IN TABLE UNDERNEATH
- Returns the URL of each inner link found
- Returns the anchor text of each inner link found


# How to run
1. install python
2. install virtual venv and requirements.txt
```py
py -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```
3. run server
```py
py app.py
```
4. run app
http://localhost:5000

### using .bat file for windows
doublick ready.bat <br>
doublick run.bat
- run app
http://localhost:5000
