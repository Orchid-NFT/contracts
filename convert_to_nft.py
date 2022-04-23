import os
import json
import random

imagesPath = "images/"
metadataPath = "metadata/"
jsonPath = "metadata.json"
ipfsHash = "QmUNeSLNofHAF1P5Sz1Xh6bRUz3iXevmE33jwPsqNqDfgi"

f = open(jsonPath)
json_data = json.load(f)

defaultMetadata = {
	"name": "",
	"description": "",
	"image": "https://gateway.pinata.cloud/ipfs/QmVq5hp8ax5pCV1FiSe53obvznZwJvHFzcGNSfWizRpBXc/10.jpeg",
	"properties": {}
}

index = 0
waterRankList = list(range(48))
airRankingList = list(range(48))
founaRakingList = list(range(48))
for imageName in os.listdir(imagesPath):
    waterRanking = random.choice(waterRankList)
    airRanking = random.choice(airRankingList)
    founaRaking = random.choice(founaRakingList)
    waterRankList.remove(waterRanking)
    airRankingList.remove(airRanking)
    founaRakingList.remove(founaRaking)

    imageData = json_data[index]

    defaultMetadata["name"] = imageData["Name"]
    defaultMetadata["description"] = "Unique park with beautiful scenery"
    defaultMetadata["image"] = "https://gateway.pinata.cloud/ipfs/" + ipfsHash + "/" + imageName
    defaultMetadata["properties"] = {
        "Place": imageData["Place"],
        "Annual visitors": imageData["Annual visitors"],
        "Water ranking": waterRanking,
        "Air ranking": airRanking,
        "Founa ranking": founaRaking
    }

    hexNum = hex(index)[1:][1:]
    if len(hexNum)==1:
        padding = "000000000000000000000000000000000000000000000000000000000000000"
    else:
        padding = "00000000000000000000000000000000000000000000000000000000000000"

    with open(metadataPath + padding + hexNum + ".json",'w') as data: 
      data.write(json.dumps(defaultMetadata))

    index = index+1

    



