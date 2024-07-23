import dash

app = dash.Dash(__name__, requests_pathname_prefix="/dash1/")
server = app.server
app.layout = [dash.html.H1(children="ERSTE", style={"textAlign": "center"})]


# @app.server.errorhandler(Exception)
# def handle_error(e):
#     return f"<h1>Error: {str(e)}</h1>", 500


if __name__ == "__main__":
    app.run(debug=True)
