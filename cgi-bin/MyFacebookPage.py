#!/usr/bin/env python
import cgi
import csv

postForm = cgi.FieldStorage()
currentusername = postForm.getvalue("username")

#prints all registered members in a list
def printMembers():
	with open('members.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		print "<ul>"
		for row in reader:
			print "<li>" + row[1] + "</li>"
		print "</ul>"

#prints user's friends list (up to 10 posts)
def printFeed():
	with open('topic.csv','r') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print row[0]
			print "<br>"

#appends username and new post to csv
def addPost():
	if (postForm.getvalue('formname') == "addpost"):
		with open('topic.csv', 'a') as csvfile:
                	csvfile.write(currentusername + '\n')
			csvfile.write(postForm.getvalue('joke') + '\n')

#append member name to user's row in members.csv
def addFriend():
	if (postForm.getvalue("formname") == "addfriend"):
		new_rows_list = []
		with open('members.csv', 'r') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				if row[1] == currentusername:
					new_row = row + postForm.getvalue("friend").split()
					new_rows_list.append(new_row)
				else:
					new_rows_list.append(row)
		with open('members.csv','w') as csvfile:
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
                        <td width="462" height="546" valign="top" rowspan="3">
                            <p align="center"><font size="5"><b> CS Funnies News Feed </b></font></p>
                            <p align="center"> """

printFeed()

print """
			   </p>
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
				<input type="hidden" name="username" value='""" + currentusername + """'>                                			    <input type="hidden" name="formname" value="addfriend">
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
                                <p align="center"><strong>Members</strong></p> """

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

