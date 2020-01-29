<html lang="en-US">
	<head>
	<meta charset="UTF-8">
    <title>Your website title</title>
 <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
   <link rel="stylesheet" href="css/style.css">
	</head>
<style>

@media only screen 
and (min-device-width : 375px) 
and (max-device-width : 667px) { 
h1 { color: #000000; font-family: 'Raleway',sans-serif; font-size: 22px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }
		#container .grid li { float: left; width: 150px; height: 150px; border-right: 1px dotted #CCC; border-bottom: 1px dotted #CCC; padding: 10px; }


}

@media only screen
and (min-device-width : 375px)
and (max-device-width : 812px)
and (-webkit-device-pixel-ratio : 3)
and (orientation : portrait) { /* STYLES GO HERE */
h1 { color: #000000; font-family: 'Raleway',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }
		#container .grid li { float: left; width: 150px; height: 150px; border-right: 1px dotted #CCC; border-bottom: 1px dotted #CCC; padding: 10px; }


 }


</style>
<body>
<div id="banner" height="200px"> <h1>Rankbabes.com - Search Engine For Babes</h1></div>
<div id="menu" height="200px"> <b>Home | Top 100 Babes | Top Liked Photos</b></div>

<div id="container">
	
	<div class="buttons">
	    <button class="grid">Grid View</button>
	    <button class="list">List View</button>
	</div>
</h3>All Babes</h3>



<?php
$conn = mysqli_connect('localhost', 'root', 'password', 'database');
if (!$conn) {
    die('Could not connect: ' . mysqli_error());
}
//echo 'Connected successfully';
$sql = "SELECT id, user_id, username,full_name, profile_pic_url FROM Models LIMIT 0, 1000";
$result = mysqli_query($conn, $sql);


if (mysqli_num_rows($result) > 0) {
    // output data of each row
    echo '<ul class="grid">';

    while($row = mysqli_fetch_assoc($result)) {
        echo '<li>';
        echo '<a href=model.php?user_id=';
        echo $row["user_id"];
        echo '>';
    echo "<p class='username'>" . $row["full_name"]. "<h6 style='font-size:10px; color: black; outline: none; text-decoration: none;'>instagram:".$row["username"]. '</h6><a href=model.php?user_id='.$row[user_id].'><img class="profile_pic" height="65%" width="65%" src='.$row["profile_pic_url"]."><br></a></p>";
    echo '</a>';
    echo '</li>';
	}
	echo '</ul></div>';
} else {
    echo "0 results";
}


mysqli_close($conn);
?>
<a href ="/">page</a> | <a href ="/page2.php">page 2</a> | <a href ="/page3.php">page 3 </a>| <a href ="/page4.php">page 4</a>
<p><p><p><p><p>
<div>
<h4>All photos and videos are direcly linked from instagrams own developer <a href="https://developers.facebook.com/docs/instagram-basic-display-api/">api</a> no images or videos are storaged on this website</h4>
<p>
<h5>If you dont want your profile on this website send me a dm on instagram @maskofshiva<h5>
</div>
</body>
</html>
[pcs@pc
