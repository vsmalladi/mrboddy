<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd"
    >
<html lang="en">
<head>
    <title>Clue-Less by Boddy, Inc.</title>
</head>
<body>
    %if state == False and players < 6:
        Welcome to Clue-Less! There are ${players}
        players waiting to play.
        <a href="${request.route_url('submit')}">Join Game</a>

    %else:
        There is already a came in progress. Come back later.
    %endif
    

    
</body>
</html>
