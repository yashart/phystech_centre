import parser
import tex_converter
import optimize
from subprocess import call
import os
import calc_polish_list
import node2polish_list


def txt_to_latex(plain_text):
    result = parser.build_tree(plain_text)
    result = optimize.optimize_bracket(result)
    texTxt = tex_converter.tex_dump(result)

    return texTxt

#-----------------------
# get latex text in "latex text" format
#
#-----------------------
def latex_to_image(latex_text, pictures_path):
    hashTex = str(hash(latex_text))
    filePath1 = hashTex[:2]
    if not os.path.exists(pictures_path + filePath1):
        os.mkdir(pictures_path + filePath1)
    filePath2 = hashTex[2:4]
    if not os.path.exists(pictures_path + filePath1 + '/' + filePath2):
        os.mkdir(pictures_path + filePath1 + '/' + filePath2)
    fileName = hashTex[4:]
    fullPath = pictures_path + filePath1 + '/' + filePath2 + '/' + fileName +'.png'
    if os.path.exists(fullPath):
        return fullPath
    call(['./tex2png/tex2png', latex_text, fullPath])

    return fullPath

#---------------------------
#check equation by points
#right_list - list of dict, which contain vars and res
#---------------------------
def check_equation(plain_text, right_list):
    node = parser.build_tree(plain_text)
    node = optimize.optimize_bracket(node)
    polishList = node2polish_list.node2list(node)
    for point in right_list:
        polishNumsList = calc_polish_list.vars_to_nums(polishList, point)
        result = calc_polish_list.calc_polish_list(polishNumsList)
        if(float(point['res']) != result):
            return False

    return True


if __name__ == "__main__":
    latex_to_image(r'\alpha > \beta')
