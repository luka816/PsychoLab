#font size ( 24px )

""" data=[["qudi", "ქუდი", "center", 0, 0, 5,6,7],
      ["botli", "ბოთლი", "center", 0, 0, 8,9,10],
      ["chaquchi", "ჩაქუჩი", "center", 0, 0,  11,12,13],
      ["nacheri", "ნაჭერი", "center", 0, 0,  14,15,16],
      ["fanqari", "ფანქარი", "custom", -124.6, 0,  17,18,19],
      ["tafa", "ტაფა", "custom", -124.6, 0,  20,21,22]] """

data=[["xe", "ხე", "custom", -124.6, 0, 23,24,25],
      ["fanjara", "ფანჯარა", "custom", -124.6, 0, 26,27,28],
      ["gitara", "გიტარა", "custom", 124.6, 0, 29,30,31],
      ["pica", "პიცა", "custom", 124.6, 0, 32,33,34],
      ["kalami", "კალამი", "custom", 124.6, 0, 35,36,37],
      ["yinuli", "ყინული", "custom", 124.6, 0, 38,39,40]
]

font_size=24


def writer(word_eng, word_geo, position, x, y, id_1, id_2, id_3):
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
                        "type": "shape",
                        "name": "circle",
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
                        "text": "text stimul",
                        "fontSize": 32,
                        "fontColor": "#000000",
                        "fontFamily": "Arial",
                        "lines": 1,
                        "lineSpacing": 1.5,
                        "shape": "circle",
                        "shapeSize": "large",
                        "shapeWidth": 50,
                        "shapeHeight": 50,
                        "shapeColor": "#ff0000",
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
    
#print(writer("botli", "ბოთლი","right",14,15,16))

results = []

for row in data:
    results.append(writer(*row))

final_output = "[\n" + ",\n".join(results) + "\n]"
print(final_output)

