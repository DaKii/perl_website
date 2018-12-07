#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw ( fatalsToBrowser );
use strict;
use warnings;

use File::Path;

my $user_dir = "../../../users/";

print header();
opendir my $dh, $user_dir or die "Could not open '$user_dir' for reading '$!'\n";
while (my $user = readdir $dh) {
    
    if ($user eq '.' or $user eq '..') {
        next;
    }

    my $dir="$user_dir/$user";

    rmtree $dir if ($user=~/\d+/);
    #rmtree $dir;

    if(-e $dir) 
    {
        print "Directory '$dir' still exists<br>\n";
    }
    else 
    {
        print "Directory '$dir' deleted.<br>\n";
    }
}
