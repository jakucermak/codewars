def int_to_hex(v):
    hex = {
        1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"
    }
    vals = ''
    r = v

    vals = vals+ hex[int(r/16)]
    vals = vals+ hex[int((r%16)*16)]

    return vals


def rgb(r, g, b):

    hex_r = int_to_hex(r)
    hex_g = ''
    hex_b = ''



#print(rgb(0,0,0),"000000", "testing zero values")
#print(rgb(1,2,3),"010203", "testing near zero values")
print(rgb(255,255,255), "FFFFFF", "testing max values")
print(rgb(254,253,252), "FEFDFC", "testing near max values")
print(rgb(-20,275,125), "00FF7D", "testing out of range values")