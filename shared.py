import json


CONFIG_JSON = json.loads(open("CONFIG.json","r").read())
lang= CONFIG_JSON["lang"]
try:
    TRANSLATE_JSON = json.loads(open("assets/translations/"+lang+".json", "r").read())
except:
    TRANSLATE_JSON = json.loads(open("assets/translations/empty.json", "r").read())
def translate(tab,key,fallback):
    if key in TRANSLATE_JSON:
        return TRANSLATE_JSON[key]
    else:
        if tab in TRANSLATE_JSON:
            if key in TRANSLATE_JSON[tab]:
                return TRANSLATE_JSON[tab][key]
            else:
                return fallback
    return fallback

TEMP_MODE = True