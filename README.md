# portofilo
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .details {
            margin-bottom: 20px;
        }
        .details strong {
            color: #333;
        }
        .skills-list {
            list-style-type: square;
            padding-left: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Student Details</h1>
        <div class="details">
            <p><strong>Name:</strong> Anusha Satya</p>
            <p><strong>Course:</strong> B.Tech</p>
            <p><strong>Year:</strong> 2nd Year</p>
            <p><strong>College:</strong> Visakha Institute of Engineering and Technology</p>
        </div>
        <div class="details">
            <strong>Technical Skills:</strong>
            <ul class="skills-list">
                <li>C Language</li>
                <li>Python</li>
            </ul>
        </div>
    </div>

</body>
</html>
/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f9;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    width: 100%;
    text-align: center;
}

h1 {
    color: #333;
    margin-bottom: 20px;
}

.details {
    margin-bottom: 20px;
    text-align: left;
}

.details strong {
    color: #333;
    font-weight: bold;
}

.skills-list {
    list-style-type: none;
    padding-left: 0;
}

.skills-list li {
    background: #f0f0f0;
    padding: 8px;
    margin: 5px 0;
    border-radius: 4px;
}

.skills-list li:hover {
    background-color: #e1e1e1;
}
