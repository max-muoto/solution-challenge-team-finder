<?
	// Read From
	$name = $_REQUEST['name'];
	$email = $_REQUEST['email'];
	$school = $_REQUEST['school'];
	$year = $_REQUEST['year'];
	$experience = $_REQUEST['experience'];
	$major = $_REQUEST['major'];
	$career = $_REQUEST['career'];
	$tech = $_REQUEST['tech'];
	$languages = $_REQUEST['languages'];

	$language_flat = implode("|",$languages);
	$tech_flat = implode("|",$tech);

	// Read File
	$f = @file_get_contents("data.csv");

	// Add Data
	$f .= $name.",".$email.",".$school.",".$year.",".$experience.",".$career.",".$major.",".$language_flat.",".$tech_flat." \n";

	// Save File
	@file_put_contents("data.csv", $f);

	header("Location: index.html");
?>