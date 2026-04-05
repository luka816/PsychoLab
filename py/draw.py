# left  right center
# "left arrow" , "right arrow"
# "<"    ">"

""" data=[["wiqa", "ჭიქა", "center",0,0, "left arrow", "<", 5,6,7],
      ["vashli", "ვაშლი", "center",0,0, "left arrow", "<", 8,9,10],
      ["guli", "გული", "center",0,0, "right arrow", ">", 11,12,13],
      ["wigni", "წიგნი", "center",0,0, "right arrow", ">", 14,15,16],
      ["chaidani", "ჩაიდანი", "custom",-124.6,0, "right arrow", ">", 17,18,19],
      ["yvavili", "ყვავილი", "custom",-124.6,0, "right arrow", ">", 20,21,22]] """

data=[["kubi", "კუბი", "custom",-124.6,0, "left arrow", "<", 23,24,25],
      ["kalata", "კალათა", "custom",-124.6,0, "left arrow", "<", 26,27,28],
      ["telefoni", "ტელეფონი", "custom",124.6,0, "right arrow", ">", 29,30,31],
      ["manqana", "მანქანა", "custom",124.6,0, "right arrow", ">", 32,33,34],
      ["satvale", "სათვალე", "custom",124.6,0, "left arrow", "<", 35,36,37],
      ["gemi", "გემი", "custom",124.6,0, "left arrow", "<", 38,39,40]
]

font_size=24


def writer(word_eng, word_geo, position,x,y, arrow_name, arrow_text, id_1, id_2, id_3):
    text=f'''
    {{
                        "id": {id_1},
                        "itemType": "stimulus",
                        "type": "text",
                        "name": "{word_eng}",
                        "listId": 1,
                        "position": "{position}",
                        "customX": {x},
                        "customY": {y},
                        "delay": 0,
                        "delayType": "interval",
                        "delayMin": 5000,
                        "delayMax": 10000,
                        "duration": 150,
                        "responseKey": "Space",
                        "allowAnyKey": false,
                        "backgroundColor": "#ffffff",
                        "randomPosition": false,
                        "randomSectors": [],
                        "text": "{word_geo}",
                        "fontSize": {font_size},
                        "fontColor": "#000000",
                        "fontFamily": "Arial",
                        "lines": 1,
                        "lineSpacing": 1.5,
                        "shape": "circle",
                        "shapeSize": "medium",
                        "shapeWidth": 50,
                        "shapeHeight": 50,
                        "shapeColor": "#FFFFFF",
                        "shapeStyle": "fill",
                        "shapeStrokeWidth": 2,
                        "imageUrl": "https://lh3.googleusercontent.com/pw/AP1GczMQWOanSrbnT2iF4H23Tdn-mBImHLRasTMRz8i-C2kzAmRym6Kp6gaupoHwpdEkEGhXES23HJVpboTvb_WjY5MsKmcFh3GhqP-B2qZFyl7tYkaa0QEckYnBnOnrt1Vxuu0YsNLUaCHDA0c3wNGPdnUw=w855-h641-s-no-gm?authuser=0",
                        "imageWidth": 200,
                        "imageHeight": 200,
                        "audioUrl": "",
                        "audioRepeat": 1,
                        "audioVolume": 100
                    }},
                    {{
                        "id": {id_2},
                        "itemType": "stimulus",
                        "type": "image",
                        "name": "mask",
                        "listId": 1,
                        "position": "center",
                        "customX": 0,
                        "customY": 0,
                        "delay": 0,
                        "delayType": "fixed",
                        "delayMin": 0,
                        "delayMax": 0,
                        "duration": 1000,
                        "responseKey": "Space",
                        "allowAnyKey": false,
                        "backgroundColor": "#ffffff",
                        "randomPosition": false,
                        "randomSectors": [],
                        "text": "text stimul",
                        "fontSize": 32,
                        "fontColor": "#000000",
                        "fontFamily": "Arial",
                        "lines": 1,
                        "lineSpacing": 1.5,
                        "shape": "circle",
                        "shapeSize": "medium",
                        "shapeWidth": 50,
                        "shapeHeight": 50,
                        "shapeColor": "#FFFFFF",
                        "shapeStyle": "fill",
                        "shapeStrokeWidth": 2,
                        "imageUrl": "images/mask.jpg",
                        "imageWidth": "3000",
                        "imageHeight": "3000",
                        "audioUrl": "",
                        "audioRepeat": 1,
                        "audioVolume": 100
                    }},
                    {{
                        "id": {id_3},
                        "itemType": "stimulus",
                        "type": "text",
                        "name": "{arrow_name}",
                        "listId": 1,
                        "position": "center",
                        "customX": 0,
                        "customY": 0,
                        "delay": 0,
                        "delayType": "fixed",
                        "delayMin": 0,
                        "delayMax": 0,
                        "duration": -1,
                        "responseKey": "Space",
                        "allowAnyKey": false,
                        "backgroundColor": "#ffffff",
                        "randomPosition": false,
                        "randomSectors": [],
                        "text": "{arrow_text}",
                        "fontSize": "200",
                        "fontColor": "#0008ff",
                        "fontFamily": "Arial",
                        "lines": 1,
                        "lineSpacing": 1.5,
                        "shape": "circle",
                        "shapeSize": "medium",
                        "shapeWidth": 50,
                        "shapeHeight": 50,
                        "shapeColor": "#FFFFFF",
                        "shapeStyle": "fill",
                        "shapeStrokeWidth": 2,
                        "imageUrl": "https://lh3.googleusercontent.com/pw/AP1GczMQWOanSrbnT2iF4H23Tdn-mBImHLRasTMRz8i-C2kzAmRym6Kp6gaupoHwpdEkEGhXES23HJVpboTvb_WjY5MsKmcFh3GhqP-B2qZFyl7tYkaa0QEckYnBnOnrt1Vxuu0YsNLUaCHDA0c3wNGPdnUw=w855-h641-s-no-gm?authuser=0",
                        "imageWidth": 200,
                        "imageHeight": 200,
                        "audioUrl": "",
                        "audioRepeat": 1,
                        "audioVolume": 100
                    }}''' 
    return text


results = []

for row in data:
    results.append(writer(*row))

final_output = "[\n" + ",\n".join(results) + "\n]"
print(final_output)
    
# print(writer("botli", "ბოთლი","right",14,15,16))

