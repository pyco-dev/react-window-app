from flask import Flask, render_template
import webview
import threading


# this creates a flask webserver that serves the compiled react page
def web_server() -> None:
    app: Flask = Flask(__name__)
    
    @app.route("/")
    def index() -> render_template:
        return render_template("index.html")
    
    app.run()


# this creates a thread to run the web server and uses 
# webview to create a GUI to display the web server content
def main() -> None:
    server_thread = threading.Thread(target=web_server)
    server_thread.start()

    webview.create_window("react-window-app", "http://127.0.0.1:5000", width=1000, height=600, resizable=False)
    webview.start()


if __name__ == "__main__":
    main()