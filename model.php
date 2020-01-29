<html lang="en-US">
	<head>
	<meta charset="UTF-8">
	<title></title>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<style>
@media only screen 
and (min-device-width : 375px) 
and (max-device-width : 667px) { 
h1 { color: #000000; font-family: 'Raleway',sans-serif; font-size: 22px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }
		#container .grid li { float: left; width: 950px; height: 1050px; border-right: 1px dotted #CCC; border-bottom: 1px dotted #CCC; padding: 10px; }


}

@media only screen
and (min-device-width : 375px)
and (max-device-width : 812px)
and (-webkit-device-pixel-ratio : 3)
and (orientation : portrait) { /* STYLES GO HERE */
h1 { color: #000000; font-family: 'Raleway',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }
		#container .grid li { float: left; width: 950px; height: 1050px; border-right: 1px dotted #CCC; border-bottom: 1px dotted #CCC; padding: 10px; }


 }
h1 { color: #000000; font-family: 'Raleway',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase; }
		#container .grid li { float: left; width: 950px; height: 1050px; border-right: 1px dotted #CCC; border-bottom: 1px dotted #CCC; padding: 10px; }

</style>

		<script type="text/javascript">
				$(function(){
					$('button').click(function(e) {
						if($(this).hasClass('list')) {
							 $('#container ul').removeClass('grid').addClass('list');
							 $('ul li div').removeClass('h').addClass('v');
						}
						else if ($(this).hasClass('grid')) {
						    $('#container ul').removeClass('list').addClass('grid'); 
						    $('ul li div').removeClass('v').addClass('h');
						}
					});
				}); 
		</script>
	</head>
<body>

<div id="container">
	
	<div class="buttons">
	    <button class="grid">Grid View</button>
	    <button class="list">List View</button>
	</div>


<?php
$user_id=$_GET['user_id'];
$conn = mysqli_connect('localhost', 'root', 'password', 'database');
if (!$conn) {
    die('Could not connect: ' . mysqli_error());
}
echo 'Connected successfully';
echo '<nav><a href="videos.php?user_id=' . $user_id . '">Videos</a></nav>';
//echo "<a href src='./videos.php".$user_id."'>Videos</a>";
$sql = "SELECT id, username, photo_url,likes FROM Photos WHERE user_id = '".$user_id."'";
$result = mysqli_query($conn, $sql);
echo $user_id;
if (mysqli_num_rows($result) > 0) {
    // output data of each row
    echo '<ul class="grid">';

    while($row = mysqli_fetch_assoc($result)) {
    echo '<li>';
   echo "id: " . $row["id"]. " - Name: " . $row["username"]. " " . '<img height="100%" width="100%" src='.$row["photo_url"].'>   <p><br>Likes: '.$row["likes"]."<br><p>";
    echo '</li>';
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>


</body>
</html>
