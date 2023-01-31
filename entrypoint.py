import os

from flask import send_from_directory
from dotenv import load_dotenv

from app import create_app



load_dotenv()

settings_module = os.getenv('APP_SETTINGS_MODULE')
print(settings_module) 
app = create_app(settings_module)


@app.route('/media/icons/<filename>')
def media_icons(filename):
    dir_path = os.path.join(app.config['MEDIA_DIR'],
                            app.config['ICONS_IMAGES_DIR'])
    
    return send_from_directory(dir_path, filename)


@app.route('/media/logos/<filename>')
def media_logos(filename):
    dir_path = os.path.join(app.config['MEDIA_DIR'],
                            app.config['LOGOS_IMAGES_DIR'])
    
    return send_from_directory(dir_path, filename)


@app.route('/media/items/<filename>')
def media_items(filename):
    dir_path = os.path.join(app.config['MEDIA_DIR'],
                            app.config['ITEMS_IMAGES_DIR'])
    
    return send_from_directory(dir_path, filename)


# @app.route('/media/items/')
# def media_path():
#     dir_path = os.path.join(app.config['MEDIA_DIR'],
#                             app.config['ITEMS_IMAGES_DIR'])
    
#     return send_from_directory(dir_path)



#* UTILIZAR >>> flask run
# if __name__ == '__main__':
#     app.run(debug=True)