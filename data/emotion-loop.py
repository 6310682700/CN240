from csv import reader

with open('legend-2.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)

    count = 0
    happiness = 0
    anger = 0
    surprise = 0
    disgust = 0
    fear = 0
    neutral = 0
    sadness = 0
    contempt = 0

    for row in csv_reader:
        count += 1
        if row[2].lower() == "happiness":
            happiness += 1
        elif row[2].lower() == "anger":
            anger += 1
        elif row[2].lower() == "surprise":
            surprise += 1
        elif row[2].lower() == "disgust":
            disgust += 1
        elif row[2].lower() == "fear":
            fear += 1
        elif row[2].lower() == "neutral":
            neutral += 1
        elif row[2].lower() == "sadness":
            sadness += 1
        elif row[2].lower() == "contempt":
            contempt += 1
        else:
            print(row[2])

print("All = ", count)
print("Happiness = ", happiness)
print("Anger = ", anger)
print("Surprise = ", surprise)
print("Disgust = ", disgust)
print("Fear = ", fear)
print("Neutral = ", neutral)
print("Sadness = ", sadness)
print("Contempt = ", contempt)