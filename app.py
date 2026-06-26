from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>

<title>Containerized Flask Application</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,Helvetica,sans-serif;
}

body{
background:linear-gradient(135deg,#0f172a,#2563eb);
display:flex;
justify-content:center;
align-items:center;
min-height:100vh;
}

.container{
width:900px;
background:white;
padding:40px;
border-radius:20px;
box-shadow:0 20px 40px rgba(0,0,0,0.35);
text-align:center;
}

h1{
color:#2563eb;
margin-bottom:10px;
}

.subtitle{
color:#555;
margin-bottom:25px;
font-size:18px;
}

.status{
background:#22c55e;
color:white;
padding:15px;
border-radius:10px;
font-size:18px;
font-weight:bold;
margin-bottom:30px;
}

.grid{
display:grid;
grid-template-columns:repeat(2,1fr);
gap:20px;
}

.card{
background:#f3f4f6;
padding:20px;
border-radius:12px;
border-left:6px solid #2563eb;
transition:.3s;
}

.card:hover{
transform:translateY(-5px);
}

.card h3{
color:#2563eb;
margin-bottom:10px;
}

.services{
margin-top:30px;
display:flex;
justify-content:center;
flex-wrap:wrap;
gap:12px;
}

.service{
background:#2563eb;
color:white;
padding:10px 18px;
border-radius:25px;
font-weight:bold;
}

.footer{
margin-top:35px;
padding-top:20px;
border-top:1px solid #ddd;
color:#555;
}

.footer strong{
color:#2563eb;
}

</style>

</head>

<body>

<div class="container">

<h1>Containerized Flask Application</h1>

<p class="subtitle">
Dockerized Python Flask Application deployed using Amazon ECS
</p>

<div class="status">
Container Running Successfully
</div>

<div class="grid">

<div class="card">
<h3>Python Flask</h3>
<p>REST Application running inside Docker.</p>
</div>

<div class="card">
<h3>Docker Container</h3>
<p>Application packaged into a lightweight container.</p>
</div>

<div class="card">
<h3>Amazon ECR</h3>
<p>Container image securely stored in ECR.</p>
</div>

<div class="card">
<h3>Amazon ECS</h3>
<p>Container deployed and managed by ECS.</p>
</div>

</div>

<div class="services">

<div class="service">Python</div>

<div class="service">Flask</div>

<div class="service">Docker</div>

<div class="service">Amazon ECR</div>

<div class="service">Amazon ECS</div>

</div>

<div class="footer">

<h3>Capstone Project 8</h3>

<p><strong>Project:</strong> Containerized Flask Application</p>

<p><strong>Developed By:</strong> Vishakha Mantalwad</p>

</div>

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)