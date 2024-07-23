import dash

app = dash.Dash(__name__, requests_pathname_prefix="/dash1/")
server = app.server
app.layout = [dash.html.H1(children="ERSTE DASH APP", style={"textAlign": "center"})]

if __name__ == "__main__":
    app.run(debug=True)
