"""
    This module is used to preprocess the coordinates location
    of html elements present in the image and generate a html code
    from it
"""
import json
import os
import math
from pathlib import Path
from collections import defaultdict

static_path = os.path.join(Path(__file__).parent, "static")


class Converter:
    """
        This class is used to convert the coordinates into html code
    """

    def __init__(self):
        self.map = self.load_map()["map"]
        self.boilerplate = self.load_map()["boilerplate"]
        self.tags = self.load_map()["tags"]
        self.result = self._enrich_output()

    def load_map(self):
        """
            This method is used to load the map_data from the map.json file
            in the static folder of the project
        """
        with open(os.path.join(static_path, "map.json"), 'r', encoding='utf-8') as file:
            map_data = json.load(file)
        return map_data

    def load_result(self):
        """
            This method is used to load the result of the text file from the output of
            the module.
        """
        with open(os.path.join(static_path, "output.txt"), 'r', encoding='utf-8') as file:
            next(file)
            data = [line.strip() for line in file]

        result = []
        for item in data:
            item_list = item.split()
            xmin, ymin, xmax, ymax = float(item_list[0])/640, float(
                item_list[1])/640, float(item_list[2])/640, float(item_list[3])/640
            result.append(" ".join([item_list[5],str(xmin), str(ymin),str(xmax), str(ymax)]))
        
        return result

    def _enrich_output(self):
        result = self.load_result()
        final = []
        for tag in result:
            elements = tag.split()[:-2]
            for i in range(1, len(elements)):
                elements[i] = str(math.floor(float(elements[i])*10)/10)
            data = ' '.join(elements)
            final.append(data)
        return final

    def arrange_coordinates(self):
        """
            This method is used to read the text output.
        """
        result_dict = defaultdict(list)
        
        for item in self.result:
            row_data = {}
            label, column, row = item.split()
            row_data['row'] = float(column)
            row_data['label'] = self.map[label]
            result_dict[float(row)].append(row_data)
        return result_dict

    def arrange_row_list(self, row_data):
        """
            This method is used to arrange the items in a
            row.
        """
        result = sorted(row_data, key=lambda x: x['row'])
        return [item['label'] for item in result]

    def get_html_body(self):
        """
            This method is used to get the html code from the coordinates
            and their label
        """
        first_div = '<div class="d-flex flex-row">'
        last_div = '</div>'
        result_dict = self.arrange_coordinates()
        column_keys = sorted(list(result_dict))
        body = []
        for column_item in column_keys:
            row_list = []
            row_data = result_dict[column_item]
            placement = self.arrange_row_list(row_data)
            for tag in placement:
                tag_data = self.tags.get(tag, "").strip()
                row_list.append(tag_data)
            row_d = "\n".join(row_list)
            data = f"{first_div}\n{row_d}\n{last_div}"
            body.append(data)
        return '\n'.join(body)

    def get_html(self):
        """
            This method is used to extract the entire html code.
        """
        body = self.get_html_body()
        html_data = f"{self.boilerplate}{body}\n</body>\n</html>"
        return html_data


