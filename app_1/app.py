from dash import Dash, html, dcc, callback, Output, Input

app = Dash()
server = app.server
app.layout = [html.H1(children="DASH APP: UNO", style={"textAlign": "center"})]

if __name__ == "__main__":
    app.run(debug=True)
