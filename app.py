
from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_image = None
    error = None

    if request.method == "POST":
        choice = request.form.get("type")
        data = ""

        if choice == "text":
            data = request.form.get("text", "").strip()

        elif choice == "contact":
            name = request.form.get("name", "").strip()
            phone = request.form.get("phone", "").strip()

            if name and phone:
                data = (
                    "BEGIN:VCARD\n"
                    "VERSION:3.0\n"
                    f"FN:{name}\n"
                    f"TEL:{phone}\n"
                    "END:VCARD"
                )
            else:
                error = "Enter both name and phone number."

        elif choice == "wifi":
            ssid = request.form.get("ssid", "").strip()
            password = request.form.get("password", "").strip()

            if ssid:
                data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
            else:
                error = "Enter your WiFi network name."

        if data and not error:
            img = qrcode.make(data)

            buffer = io.BytesIO()
            img.save(buffer, format="PNG")

            qr_image = base64.b64encode(
                buffer.getvalue()
            ).decode("utf-8")

        elif not data and not error:
            error = "Please enter the required information."

    return render_template(
        "index.html",
        qr_image=qr_image,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
