from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

# HTML пульта
HTML = """
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Linux Remote</title>
    <style>
        body {
            max-width: 400px;
            margin: auto;
            font-family: sans-serif;
            text-align: center;
        }

        button {
            width: 100px;
            height: 60px;
            margin: 5px;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h2>Пульт до Linux</h2>
    <form method="POST">
        <button name="key" value="Up">⬆️</button><br>
        <button name="key" value="Left">⬅️</button>
        <button name="key" value="Down">⬇️</button>
        <button name="key" value="Right">➡️</button><br><br>
        <button name="key" value="Return">Enter</button>
        <button name="key" value="Escape">Esc</button><br><br>
        <button name="key" value="XF86AudioRaiseVolume">&#x1F50A; Volume +</button>
        <button name="key" value="XF86AudioPlay">&#x23EF; Play/Pause</button>
        <button name="key" value="XF86AudioLowerVolume">&#x1F50A; Volume -</button><br><br>
        <button name="key" value="alt+F4">❌</button>
        <button name="key" value="Alt+Tab">🔄 Alt+Tab</button>
        <button name="key" value="Win+Space">🌐</button>
        <button name="key" value="space">Пробіл</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def remote():
        if request.method == "POST":
                key = request.form.get("key")
                if key:
                        try:
                                subprocess.run(["xdotool", "key", key], check=True)
                        except subprocess.CalledProcessError as e:
                                print(f"[Помилка xdotool]: {e}")
        return render_template_string(HTML)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8000)


#just testing3123123