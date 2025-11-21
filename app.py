from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "ปัณณวิชญ์ "
    student_id = "67111352"
    photo = "me1.jpg"
    return render_template("home.html", name=name, student_id=student_id, photo=photo)

@app.route("/git")
def git_page():
    summary = """
    Git คือระบบควบคุมเวอร์ชัน ที่ช่วยให้เราจัดการไฟล์และทำงานร่วมกันได้
    """
    image = "git1.png"
    github_url = "https://github.com/67111352-oss/myweb/blob/main/app.py"
    return render_template("git.html", summary=summary, image=image, github_url=github_url)

@app.route("/docker")
def docker_page():
    summary = """
    Docker คือเทคโนโลยีที่ใช้สร้าง image และรัน container
    """
    image = "docker.png"
    docker_hub_url = "https://hub.docker.com/repository/docker/chaipor/simple-python-flask-web/general"
    return render_template("docker.html", summary=summary, image=image, docker_hub_url=docker_hub_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
