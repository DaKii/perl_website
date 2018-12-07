#!/usr/bin/perl -w

use strict;
use warnings;
use CGI qw(:standard -debug);
use CGI::Carp qw ( fatalsToBrowser );

my $query = new CGI;
my $cookie = new CGI;

my $username = $query->param("uname");
chomp($username);
my $password = $query->param("psw");
chomp($password);
my $usr_list = "../../../accounts.txt";

print $query->header ();
print<<SOH;
<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">

    <title>User Profile</title>
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
                <li class="home-icon"><a href="../../../templates/index.htm">Project Name</a></li>
                <li><a href="../../../templates/user-page.html">Log in</a></li>
            </ul>
        </nav>
    </header>
    <div id="main">
SOH

    open(my $fh, '<', $usr_list) or die "Could not open file '$usr_list' $!";

    my $id = $username . $password;

    while (my $row = <$fh>) {
        chomp $row;
        if($row eq $id){
        print<<MAIN;
            <div id="login-container">
                <h1 class="login-user-h1"> Welcome $username </h1>
                    <a href="discover.cgi" class="login-btn"> Click here to view Gallary</a>
                </form>
            </div>
MAIN
            # (-name => '$username',
            # 			                     -value => '$id',
            #                                  -expires => '+3M'
            #                                );
            # print header(-cookie=>$user_cookie);
            last;
        }
    }
    close $fh;

print<<EOH;

    </div>
    <footer>
        
    </footer>
</body>
</html>

EOH
