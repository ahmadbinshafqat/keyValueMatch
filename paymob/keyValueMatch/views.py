import csv
from django.shortcuts import render
from difflib import SequenceMatcher

# Create your views here.

def index(request):
    file = open('static/Dummy medical dataset.csv')     # reading the csv file
    rows=[]
    csv_reader = csv.reader(file)
    next(csv_reader)    # skipping first row

    for row in csv_reader:
        rows.append({row[0]: row[1]})
    all_keys = set().union(*(d.keys() for d in rows))   # extracting unique keys for dropdown
    file.close()

    return render(request, 'static/templates/index.html',{'keys': all_keys})

def stringMatchPercentage(request):
    key = request.POST.get('key')       # getting key to search against
    file = open('static/Dummy medical dataset.csv')
    csv_reader = csv.reader(file)
    next(csv_reader)

    diction = {}
    for row in csv_reader:
        if key == row[0] and row[1] != "" and row[1] is not None:
            for value in csv_reader:
                    similarity = SequenceMatcher(None, row[1], value[1]).ratio()      # finding the similarity between key and value    
                    similarity=round(similarity*100, 2)
                    if similarity > 50:         # return data if similarity is above 50%
                        diction.update({value[1]: similarity})
    file.close()        #closing file
    return render(request, 'static/templates/string-matching-percentage.html', {'key': key, "diction": diction})