import colorsys
import math

import colorsys

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
    h += 180
    if h >= 360:
        h -= 360

    return h, l, s

    




print(convertroundrgb(192, 64, 1))
print(convertroundhsl(19.79057, 98.96373, 37.84313725))
print(complementrgb(192, 64, 1))





