#!/usr/bin/perl
print "Content-type:text/html\n\n";
print "<html>";
use strict;
use CGI ':standard';

my $newUser = 1;
my $name = param('name');
my $username= param('username');
my $password= param('password');

#if none of the fields were filled out
if(($name eq "") || ($username eq "") || ($password eq "")){
	print qq(<div align = "center">);
	print qq(<body>);
	print qq(<h1> COMPSCI FUNNIES </h1>);
	print qq(<br>);
	print qq(Please fill in every field! We need all your info!);
	print qq(<br>);
	print qq(<a href="../newmembers.html"> I WANT TO TRY AGAIN </a>);
	print qq(<br>);
	print qq(<a href="../welcome.html"> BACK TO THE WELCOME PAGE! </a>);
	print qq(<br>);
	print qq(<img src="http://40.media.tumblr.com/tumblr_lkdkryTFbR1qiinzao1_400.png">);
	print qq(</body>);
	print qq(</div>);
}
#no commas
elsif((index($name, ",") != -1) || (index($username, ",") != -1) || (index($password, ",")!=-1)){
	print qq(<div align = "center">);
	print qq(<body>);
	print qq(<h1> COMPSCI FUNNIES </h1>);
	print qq(<br>);
	print qq(NO COMMAS! YOU SHOULD KNOW THIS);
	print qq(<br>);
	print qq(<a href="../newmembers.html"> You may try again. </a>);
	print qq(<br>);
	print qq(<a href="../welcome.html"> BACK TO THE WELCOME PAGE! </a>);
	print qq(<br>);
	print qq(<img src="https://s-media-cache-ak0.pinimg.com/236x/c0/2a/44/c02a44df96e32340d96e334e61a5ec04.jpg">);
	print qq(</body>);
	print qq(</div>);
}
#no blank spaces allowed
elsif((index($name, " ") != -1) || (index($username, " ") != -1) || (index($password, " ")!=-1)){
        print qq(<div align = "center">);
        print qq(<body>);
        print qq(<h1> COMPSCI FUNNIES </h1>);
        print qq(<br>);
        print qq(I'm pretty sure we said no spaces.);
        print qq(<br>);
        print qq(<a href="../newmembers.html"> You may try again. </a>);
        print qq(<br>);
        print qq(<a href="../welcome.html"> BACK TO THE WELCOME PAGE! </a>);
        print qq(<br>);
        print qq(<img src="https://s-media-cache-ak0.pinimg.com/236x/c0/2a/44/c02a44df96e32340d96e334e61a5ec04.jpg">);
        print qq(</body>);
        print qq(</div>);
}

#we heard some people were going around vandalizing sites filling in with html.
elsif((index($name, "<") != -1) || (index($username, "<") != -1) || (index($password, "<")!=-1) || (index($name, ">") != -1) || (index($username, ">") != -1) || (index($password, ">")!=-1) ){
        print qq(<div align = "center">);
        print qq(<body>);
        print qq(<h1> COMPSCI FUNNIES </h1>);
        print qq(<br>);
        print qq(Why did you put "<>"? Are you trying to vandalize our site? NOT ALLOWED.);
        print qq(<br>);
        print qq(<a href="../newmembers.html"> You may try again. </a>);
        print qq(<br>);
        print qq(<a href="../welcome.html"> BACK TO THE WELCOME PAGE! </a>);
        print qq(<br>);
        print qq(<img src="https://s-media-cache-ak0.pinimg.com/236x/c0/2a/44/c02a44df96e32340d96e334e61a5ec04.jpg">);
        print qq(</body>);
        print qq(</div>);
}



#if all fields are good we verify if username is taken
else{
	my $file = "../data/members.csv";
	open(my $fh1,$file) or die "cannot open $file :$!";
	while(my $line = <$fh1>){ #we read lines one by one to verify if user exists already
		#chomp($line);	
		my ($currentName, $currentUsername, $currentPassword)  = split(',', $line);	
		#if username they want is equal to the one in the current line
		if($currentUsername eq $username){
			$newUser=0;
			print qq(<div align = "center">);
			print qq(<body>);
			print qq(<h1>COMPSCI FUNNIES </h1>);
			print qq(<br>);
			print qq(We are so sorry -  Someone beat you to that username! Please pick another.);
			print qq(<br>);
			print qq(<a href="../newmembers.html"> go back and pick another cooler name! </a>);
			print qq(<br>);
			print qq(<a href="../welcome.html"> BACK TO THE WELCOME PAGE!</a>);
			print qq(<br>);
			print qq(<img src="http://dotnetslackers.com/Community/blogs/xun/blog/art-programming.jpg">);
			print qq(</body>);
			print qq(</div>);
			last;
		}
	}
	close($fh1);
	
	#if the username was not equal to any of the other ones, we append it to the members file
	#open(my $fh, '>>', $filename);
	if($newUser==1){
		open(my $fh, '>>', $file);
		print $fh "$name,$username,$password\n";
		print qq(<div align = "center">);
		print qq(<body>);
		print qq(<h1> COMPSCI FUNNIES </h1>);
		print qq(<br>);
		print qq(The registration was successful);
		print qq(<br>);
		print qq(YOU ARE NOW ONE OF US! WELCOME!);
		print qq(<br>);               
		print qq(<a href="../welcome.html"><font size="6">Go back to the welcome page to login!</font></a>);
		print qq(<br>);
                print qq(<img src="https://sarahbrooks55.files.wordpress.com/2015/02/photo-2.gif">);
		print qq(</body>);
		print qq(</div>);
	}
}

 #-- Signature -->
	print qq(<div align = center>);
	print qq(<font size=\"1\"> Website made by Andrea Horqque and Sophia Lim 2015 </font>);
        print qq(</div>);


exit 0;	
	









 
