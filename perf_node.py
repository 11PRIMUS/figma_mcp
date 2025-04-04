import json
import hashlib

def rgba_to_hex(rgba):
    """
    convert an RGBA dict into a #RRGGBB hex string 
    """
    r = int(rgba["r"] * 255)
    g = int(rgba["g"] * 255)
    b = int(rgba["b"] * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

def style_hash(style_data):
    """
    create a hash from style data
    """
    style_str = json.dumps(style_data, sort_keys=True)
    return hashlib.md5(style_str.encode()).hexdigest()

def figma_align_to_flex(figma_val):
    """
    figma alignment to flex
    """
    align_map = {
        "MIN": "flex-start",
        "CENTER": "center",
        "MAX": "flex-end",
        "SPACE_BETWEEN": "space-between"
    }
    return align_map.get(figma_val, "flex-start")

def get_fill_style_id(fills, styles):
    """
    fill style id.
    """
    if not fills or len(fills) == 0 or fills[0].get("visible", True) == False:
        return None
    
    fill = fills[0]
    
    if fill["type"] == "SOLID":
        color = fill["color"]
        opacity = fill.get("opacity", 1)
        
        #style object
        style_data = {
            "backgroundColor": rgba_to_hex(color),
            "opacity": opacity
        }
        
        style_id = style_hash(style_data)
        
        #style to dit
        if style_id not in styles:
            styles[style_id] = style_data
        
        return style_id

    
    return None




