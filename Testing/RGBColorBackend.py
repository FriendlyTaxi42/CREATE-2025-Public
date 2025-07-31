"""
This is a template for a Flask file for developing your web apps. 
Feel free to fork and clone this to modify as needed, or if you prefer, start from scratch on a new file.

Please ensure that this file is located in the main directory of your project.

To run, cd into your project directory and then run the following command:
flask --app (name of your project) run --debug
"""

from flask import Flask, render_template, request # imports

import colorsys
import math


def convertrgb(r, g, b):
    # Normalize RGB values to 0.0-1.0 range
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # Convert RGB to HLS
    hls_h, hls_l, hls_s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)

    hls_h *= 360
    hls_l *= 100
    hls_s *= 100

    return hls_h, hls_l, hls_s

def convertroundrgb(r, g, b):
    # Normalize RGB values to 0.0-1.0 range
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    # Convert RGB to HLS
    hls_h, hls_l, hls_s = colorsys.rgb_to_hls(r_norm, g_norm, b_norm)

    hls_h *= 360
    hls_l *= 100
    hls_s *= 100

    hls_h = round(hls_h, 2)
    hls_l = round(hls_l, 2)
    hls_s= round(hls_s, 2)

    return hls_h, hls_l, hls_s

def converthsl(h, s, l):
    h /= 360
    s /= 100
    l /= 100

    r, g, b = colorsys.hls_to_rgb(h, l, s)

    r *= 255
    g *= 255
    b *= 255

    return r, g, b

def convertroundhsl(h, s, l):
    h /= 360
    s /= 100
    l /= 100

    r, g, b = colorsys.hls_to_rgb(h, l, s)

    r *= 255
    g *= 255
    b *= 255

    r = round(r)
    g = round(g)
    b = round(b)

    return r, g, b

def complementrgb(r,g,b):
    if r == 0 and g == 0 and b == 0:
        return 255, 255, 255
    elif r == 255 and g == 255 and b == 255:
        return 0, 0, 0
    else:
        hls_h, hls_l, hls_s = convertrgb(r, g, b)

        hls_h += 180
        if hls_h >= 360:
            hls_h -= 360

        r, g, b = converthsl(hls_h, hls_s, hls_l)

        r = round(r)
        g = round(g)
        b = round(b)

        return r, g, b

def complementhls(h, l, s):
    if h == 0 and l == 0 and s == 0:
        return 0, 100, 0
    elif h == 0 and l == 100 and s == 0:
        return 0, 0, 0
    else:
        h += 180
        if h >= 360:
            h -= 360

    return h, l, s

def rgbtohex(r, g, b):
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

def hextorgb(hexcode):
    r, g, b = (tuple(int(hexcode[i:i+2], 16) for i in (1, 3, 5)))
    return r, g, b

def complementhex(hexcode):
    r, g, b = (tuple(int(hexcode[i:i+2], 16) for i in (1, 3, 5)))
    return rgbtohex(complementrgb(r, g, b))

app = Flask(__name__) # create Flask app



"""
Don't delete the code below! Needed for running the app.
"""
@app.route("/", methods=["GET", "POST"])
def index():
    r = 37
    g = 99
    b = 235
    if request.method == "POST":
        try:
            r = int(request.form.get("r", r))
            g = int(request.form.get("g", g))
            b = int(request.form.get("b", b))
        except Exception:
            r = 37
            g = 99
            b = 235
    oghex = rgbtohex(r, g, b)
    og_color = "#" + oghex
    cr, cg, cb = complementrgb(r, g, b)
    hexcode = rgbtohex(cr, cg, cb)
    comp_color = "#" + hexcode
    return render_template(
        'RGBColor.html', 
        og_color = og_color, 
        comp_color=comp_color,
        r = r, g = g, b = b
    )


if __name__ == "__main__":
    app.run(debug=True)




