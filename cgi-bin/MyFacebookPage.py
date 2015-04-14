#!/usr/bin/env python
import cgi
import csv

postForm = cgi.FieldStorage()
currentusername = postForm.getvalue("username")

#prints all registered members in a list
def printMembers():
	with open('../data/members.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		print "<ul>"
		for row in reader:
			print "<li>" + row[1] + "</li>"
		print "</ul>"

#searches if element of row is friend of current user
def isFriend(elementOfTopic):
	foundFriend = False
	with open('../data/members.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] == currentusername: #finds row of current user
				for i, element in enumerate(row, start=3):
					if element == elementOfTopic:
						foundFriend = True
	return foundFriend

#prints user's friends list (up to 10 posts)
def printFeed():
	new_rows_list = []
	print_feed = []
	counter = 1 #keep track of the line we are at (odd = user, even = topic)
	topicFromFriend =0 #We know if the next line will be a topic from friend
	with open('../data/topic.csv', 'r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:	
			if counter%2==0:
				if topicFromFriend==1:
					new_rows_list.append((str(row).strip('[]')).strip("''"))		
			elif isFriend(row[0]) == True:
				new_rows_list.append("<b>" + (str(row).strip('[]')).strip("''") + "</b>")
				topicFromFriend = 1
			else: #the person is not a friend, so next line not to be appended
				topicFromFriend =0 			
			counter=counter+1	
	counter = 0
	for feed in reversed(new_rows_list):
		if counter < 20: #counting until 20 because it should be the 20 last fields
 			print_feed.append(feed)
			counter = counter+1
	print_feed.reverse() #because right now it is topic - user, rather than user, topic
	print "<br>".join(map(str, print_feed))	


#appends username and new post to csv
def addPost():
	if (postForm.getvalue('formname') == "addpost"):
		with open('../data/topic.csv', 'a') as csvfile:
	               	csvfile.write(currentusername + '\n')
			csvfile.write(postForm.getvalue('joke') + '\n')
			print "<a href=\"../welcome.html\"> Login to again to see refreshed posts </a>"


#append member name to user's row in members.csv
def addFriend():
	if (postForm.getvalue("formname") == "addfriend"):
		new_rows_list = []
		with open('../data/members.csv', 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if row[1] == currentusername:
					foundFriend = False
					for index, element in enumerate(row, start=3):
						if element == postForm.getvalue("friend"):
							foundFriend = True
							print "This user is already your friend!"
					if foundFriend == False:
						new_row = row + postForm.getvalue("friend").split()
						new_rows_list.append(new_row)
						print "This user has been added!"
						print "<a href=\"../welcome.html\"> Login again to see their posts </a>"
					else:
						new_rows_list.append(row)
				else:
					new_rows_list.append(row)
		with open('../data/members.csv','w') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerows(new_rows_list)

print"Content-Type: text/html\n\n"
print """

<html>
    <head>
        <title> CS Funnies - Feed </title>
    </head>

    <body>
        <center><br><h1> COMPSCI FUNNIES</h1>
            <table border="1" cellpadding="3" cellspacing="2" width="780" height="700" bgcolor="white">
               <!-- HEADER : Only contains title of page --> 
                <thead>
                    <tr>
                        <!-- (1) Large title with user that logged in -->
                        <td width="751" height="80" colspan="2">
                            <p align="center"><font size="7"> welcome """ + currentusername + """ </font>
                        </td>
                    </tr>
                </thead>

                <!-- BODY : Contains logout button, add button, list of members, and news feed -->
                <tbody>
                    <tr>
                        <!-- (2) Logout link -->
                        <td>
                            <p align="center">
                                <a href="../welcome.html"> Logout </a>
                            </p>
                        </td>
                        <!-- (4) 10 most recent jokes from friends -->
                        <td width="462" height="546" valign="top" rowspan="3" >
                            <p align="center"><font size="5"><b> CS Funnies News Feed </b></font></p>"""

printFeed()

print """
                        </td>
                    </tr>
                    <tr>
                        <!-- (6) Textbox to add a friend from the current users list -->
                        <td>
                            <p align="center">
                                Type in a member you wish to become friends with!
                            </p>
                                <form method="POST" action="MyFacebookPage.py">
                            <p align="center">
				<input type="hidden" name="username" value='""" + currentusername + """'>
				<input type="hidden" name="formname" value="addfriend">
				<input type="text" name="friend">
                            </p>
                            <p align="center">
				<br>
                                	<input type="submit" value="Add friend!">
				</br>
				</form> """
addFriend()

print """                   
                	</p>
                        </td>
                    </tr>
                    <tr>
                        <!-- (5) A list of all the current users -->
                        <td width="141">
                            <div>
                                <p align="center"><strong>Current Users:</strong></p> """

printMembers()

print """
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <!-- (3) Textbox with submit button -->
                        <td colspan="2">
			    <p align="center"> Post a joke (max. length = 140 characters) </p>
                            <form method="POST" action="MyFacebookPage.py">
				<input type="hidden" name="username" value='""" + currentusername + """'>
				<input type="hidden" name="formname" value="addpost">
				<input type="text" name="joke" maxlength="140" align="center">
				<input type="submit" value="Post joke!" align="center">
			    </form> 
			    <form action"MyFacebookPage.py"> 
			    </form> """

addPost()

print """
                        </td>
                    </tr>
                </tbody>
            </table>
            <!-- Signature -->
            <p>
                <font size="1"> Website made by Andrea Horqque and Sophia Lim 2015 </font>
	    </p>
"""

