#!/usr/bin/perl -w

use strict;
use warnings;
use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);


my $username = param("username");
my $email_address = param("email");
my $password = param("psw");
my $repeat_password = param("psw-repeat");

my $usr_dir = "../../../users/$username";
my $images_fol = "../../../users/$username/images";
my $usr_details = "../../../users/$username/details.txt";
my $usr_list = "../../../accounts.txt";
my $available_accounts = 10;

my $fh;


if ($password eq $repeat_password){
        if(mkdir $usr_dir){
            if (mkdir $images_fol){
                open($fh, '>>', $usr_list) or die "Could not open file '$usr_list";
    
                while( my $line = <$fh>)  {   
                    $available_accounts = $available_accounts - 1;
                }
                if($available_accounts > 0){
                    print $fh "$username$password \n";
                close $fh;
    
                    open($fh, '>', $usr_details) or die "Could not create file '$usr_details' $!";
                    print $fh "------------------------------\n";
                    print $fh "Username : $username \n";
                    print $fh "Email : $email_address \n";
                    print $fh "Password : $repeat_password \n";
                    print $fh "------------------------------\n";
                    close $fh;
                }
    
            }
            else{
                die "Unable to create image folder";
            }
    
        }
        else{
            die "Unable to create $usr_dir\n";
        }
}
else{
    die " Passwords don't match ";
}


#----------------------
#Print HTML

print "Content-Type: text/html\n\n";

print<<"EndOfHtml";

<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">

    <title>Project Name</title>
    <meta name="description" content="Project Description">
    <meta name="author" content="Justine Quiapos">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="../../css/styles.css">
    <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>


</head>

<body>
    <header>
        <nav class="topnav">
            <ul>
                <li class="home-icon"><a href="../templates/index.htm">Project Name</a></li>
            </ul>
        </nav>
    </header>

    <div id="page-desc">
    <h1>Welcome $username</h1>

    <form action="../scripts/discover.cgi" method="post" enctype="multipart/form-data">
        <input id="username_submit" type="hidden" name="username" value="$username">
        <p><button type="submit" name="submit"/> Click here to view Gallary</p>
    </form>
    </div>




    <footer>
        
    </footer>
</body>
</html>

EndOfHtml
