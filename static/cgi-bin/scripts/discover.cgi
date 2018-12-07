#!/usr/bin/perl -w

use strict;
use warnings;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
use File::Basename;


my $user_dir = '../../../users/';
#limits the file upload to 12MB;
$CGI::POST_MAX = 1024 * 12000;
my $safe_filename_characters = "a-zA-Z0-9_.-";
#change upload_dir;

my $query = new CGI;
my $filename = $query->param("photo");
my $username = $query->param("username");
chomp($username);
my $user_image_directory = "../../../users/$username/images";

if ($filename ne "" && $username ne ""){
    my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
    $filename = $name . $extension;
    $filename =~ tr/ /_/;
    $filename =~ s/[^$safe_filename_characters]//g;
    
    if ( $filename =~ /^([$safe_filename_characters]+)$/ )
    {
    $filename = $1;
    }
    else
    {
    die "Filename contains invalid characters";
    }
    
    my $upload_filehandle = $query->upload("photo");
    
    open ( UPLOADFILE, ">$user_image_directory/$filename" ) or die "$!";
    binmode UPLOADFILE;

    while ( <$upload_filehandle> )
        {
        print UPLOADFILE;
        }
    
    close UPLOADFILE;
}

print $query->header ();
print <<END_HTML;
<!doctype html>

<html lang="en">
<head>
    <meta charset="utf-8">

    <title>Discover</title>
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
                <li class="home-icon"><a href="../../../templates/index.htm">Project</a></li>
                <li><a href="./discover.cgi">Discover</a></li>
            </ul>
        </nav>
    </header>

    <div id="page-desc">
        <h1>Discovering new talents</h1>
        <h3>Here are the top uploads</h3>
    </div>

    <form action="discover.cgi" method="post" enctype="multipart/form-data">
        <p>Photo to Upload: <input type="file" name="photo" /></p>
        <p><input type="text" name="username" value="Username"/></p>
        <p><input type="submit" name="guest" value="Upload" /></p>
    </form>

END_HTML

    opendir my $dh, $user_dir or die "Could not open '$user_dir' for reading '$!'\n";
    while (my $user = readdir $dh) {
        if ($user eq '.' or $user eq '..') {
            next;
        }
        opendir my $usrh, "../../../users/$user/images" or die "Could not open $user image folder for reading '$!' \n";
        while(my $img = readdir $usrh){
            if($img eq '.' or $img eq '..'){
                next;
            }else{
                print<<IMG; 
                <a href="$user_dir/$user/images/$img">
                <div class="gallery-container">
                    <div class="gallery">
                        <div class="desc">$img</div>
                        <a href="$user_dir/$user/images/$img"><img src="$user_dir/$user/images/$img" width="60" height="60">
                        <div class="desc">Uploaded by $user</div>
                    </div>
                </div>
                </a>
IMG
            }
        }
        closedir $usrh;
    }
    closedir $dh;

print<<END_HTML;
</body>
</html>
END_HTML
