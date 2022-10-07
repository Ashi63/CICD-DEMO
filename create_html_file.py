import os

def write_html():
    # create a new html file in write mode
    html_file = open('demo_html.html','w')

    # html code will go in file demo_html.html
    html_template = """
                        <html>
                            <head>
                                <title> Title </title>
                            </head> 
                            <body>
                                <h2> Welcome to Hello World..!! </h2>
                                <p> Code has been loaded to html file </p>
                            </body>
                        </html>
                    """
    # write code to file
    html_file.write(html_template)

    # close the file
    html_file.close()
    
def create_html(): 
    if 'demo_html.html' in os.listdir():
        print("file exits")
    else:
        write_html()
        print("file created")
        
