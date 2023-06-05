import json
import os
import math
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template


app = Flask(__name__)
static_path = os.path.join(Path(__file__).parent, "static")
picfolder = os.path.join('static', 'pics')
app.config['UPLOAD_FOLDER'] = picfolder


class Converter:
    def __init__(self):
        self.map = self.load_map()["map"]
        self.boilerplate = self.load_map()["boilerplate"]

    def load_map(self):
        """
            This method is used to load the map_data from the map.json file
            in the static folder of the project
        """
        with open(os.path.join(static_path, "map.json"), 'r', encoding='utf-8') as file:
            map_data = json.load(file)
        return map_data

    def get_html_body(self):
        """
            This method is used to get the html code from the coordinates
            and their label
        """
        pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
        final = []
        with open(os.path.join(static_path, "output.txt"), 'r', encoding='utf-8') as file:

            lines = file.readlines()

            lines.pop(0)

            for line in lines:
                liness = line.split(' ')
                linesss = liness.pop(6).strip()
                liness.append(linesss)
                final.append(liness)
            print(liness)

        body = '<div class="containers">\n'
        body+='<div class="container">\n'
        for component in final:
            if component[6] == "Image":
                
                body += f'<span class="image"style="font-size:10rem;position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px;">\n'
                body+='<img src="static/image.png" alt="image" style="max-width: 100%; max-height: 100%; object-fit: contain;" >\n</span>\n'
            if component[6] == "Label":
                body += f'<div class="Label" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">Label</div>\n'
            if component[6] == "Textbox":
                body += f'<div class="form-group" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; item-align:center">\n'
                body += '<input type="text" class="form-control" id="usr">\n'
                body += '</div>\n'
            if component[6] == "Heading":
                body+=f'<div class="heading" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;"><h2>Title</h2></div>\n'
            if component[6] == "Button":
                body+=f'<div class="Label" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">\n'

                body += '<button type="button" class="btn btn-primary">Click me</button>\n'
                body+='</div>\n'

            if component[6] == "Link":
                body+=f'<div class="Link" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">'
                body+= '<a href="#">link</a>\n'
                body+='</div>\n'
                
            if component[5] == "9":
                body+=f'<div class="Passwordbox" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">\n'
                body+= '<input type="password" id="pwd" name="pwd" minlength="8">\n'
                body+='</div>\n'
            if component[6] == "Select":
                body+=f'<div class="select" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">\n'
                body += '<select name="#" id="#">\n'
                body += '<option value="">Place Option</option>\n'
                body+="</div>\n"
            if component[5] == "10":
                body+=f'<div class="Radiobutton" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px;">\n'
                body +='<input type="radio">\n'
                body+='</div>\n'
            if component[5] == "2":
                body += f'<div class="checkbox" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px; text-align:center; justify-content:center;">\n'
                body += '<input type="checkbox" id="checkbox" name="checkbox" value="ck">\n'
                body+='</div>\n'
            if component[6]=='Textarea':
                body += f'<div class="checkbox" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px;">'
                body+='<textarea id="w3review" name="w3review" rows="4" cols="50">This is a text area please write it correctly.</textarea>'
                body+='</div>\n'
            if component[6]=='Paragraph':
                body += f'<div class="paragraph" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px;">\n'
                body+="<p>This is a paragraph. We would like to present this project to team of teacher.This is a final year project by BCT075 team of purwanchal campus.</p>"
                body+='</div>\n'
            if component[6]=='Pagination':
                body += f'<div class="pagination" style="position: absolute;left:{round(float(component[0]))}px;top:{round(float(component[1]))}px;width:{round(float(component[2]))}px;height:{round(float(component[3]))}px;">\n'
                body +='<a href="#page1">1</a>'
                body+='<a href="#page2">2</a>'
                body+='<a href="page3">3</a>'
                body+='</div>\n'

        body += '</div>\n'
        body+='</div>\n'
        print(body)
        return body

    def get_html(self):
        """
            This method is used to extract the entire html code.
        """
        body = self.get_html_body()
        html_data = f"{self.boilerplate}{body}\n</body>\n</html>"
        return html_data
