from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# HTML-кнопки
HTML = """
<!doctype html>
<title>Linux Remote</title>
<h2>Пульт до Linux</h2>
<form method="POST">
  <button name="key" value="Up">⬆️</button><br>
  <button name="key" value="Left">⬅️</button>
  <button name="key" value="Down">⬇️</button>
  <button name="key" value="Right">➡️</button><br><br>
  <button name="key" value="Return">Enter</button>
  <button name="key" value="Escape">Esc</button><br><br>
  <button name="key" value="XF86AudioPlay">⏯️ Play/Pause</button>
  <button name="key" value="XF86AudioRaiseVolume">🔊 Volume +</button>
  <button name="key" value="XF86AudioLowerVolume">🔉 Volume -</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def remote():
    if request.method == "POST":
        key = request.form["key"]
        subprocess.run(["xdotool", "key", key])
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
