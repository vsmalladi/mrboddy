<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en">
<head>
    <title>Clue-Less by Boddy, Inc.</title>
</head>
<body>
    <!-- This is the main game page-->
    
    <h1>Clue-Less!</h1>
    
    <div>
        <div> <!--display board here. probably just an image needed--> </div>
        <div>
            <div> <!--Move button here (jQuery toggle) --> </div>
            <div> <!--Suggestion button here (jQuery toggle) --> </div>
            <div> <!--Accusation button here (jQuery toggle) --> </div>
            <div> <!--Disprove suggestion button here (jQuery toggle) --> </div>
        </div>
        <div>
            <!--create listbox for hand of cards-->
            <!--believe a list of cards will need to be passed to template from python-->
            <select size=${cards.size} name="card_hand">
                % for c in cards:                
                    <option>${c.name}
            </select>
        </div>
        <div> <!--User info goes here (jQuery.ajax) --> </div>
        <div> <!--History goes here (jQuery.ajax) --> </div>
    </div>
    
</body>
</html>
