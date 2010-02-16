import random
import Image, ImageFont, ImageDraw
from os.path import join
from dikulan.utils import root_path, local
from cStringIO import StringIO

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def _generate_challenge():
    challenge = "".join(random.sample(characters,10))
    local.session["captcha_challenge"] = challenge
    return challenge

def _get_png(buf):
    color_text = 255, 255, 255
    color_background = 0, 0, 0
    fontpath = join(root_path, "resources","verdana.ttf")
    image = Image.new("RGB",(220,70),color_background)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 25)
    draw.text((10, 20), _generate_challenge(), font=font, fill=color_text)
    image.save(buf, "png")
    
def render_captcha(response):
    buf = StringIO()
    _get_png(buf)
    response.mimetype ="image/png"
    

    response.data = buf.getvalue()
