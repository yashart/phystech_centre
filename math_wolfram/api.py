from flask import Flask, request, jsonify
import interfaces
import ConfigParser
app = Flask(__name__)

@app.route('/api/latex_api', methods=['GET'])
def latex_api_text():
    error = None
    conf = ConfigParser.RawConfigParser()
    conf.read('config.conf')
    img_path = str(conf.get('latex', 'pictures_path'))
    txt = ''
    img_path = ''
    if request.method == 'GET':
        txt = str(request.args.get('plain'))
        str(request.args.get('generate_img'))
        if(str(request.args.get('generate_img')) == 'yes'):
            latexText = interfaces.txt_to_latex(txt)
            return jsonify({"latex_txt": latexText,
                            "img_path": interfaces.latex_to_image(latexText,  img_path)})
        return jsonify({"latex_txt": interfaces.txt_to_latex(txt),
                        "img_path": 'None'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5022)
