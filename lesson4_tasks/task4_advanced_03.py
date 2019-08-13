
scheduleDict = {
    'pupil1': {'Odie': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil2': {'Mike': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil3': {'Dustin': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil4': {'Lucas': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil5': {'Joyce': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil6': {'Nancey': {
        'English',
        'Ukrainian',
        'Russian'
    }},
    'pupil7': {'Johnatan': {
        'English',
        'Russian'
    }},
    'pupil8': {'Hopper': {
        'English',
        'Ukrainian',
        'Russian',
        'Spanish'
    }},
    'pupil9': {'Max': {
        'English',
        'Ukrainian',
        'Russian',
        'German'
    }},
    'pupil10': {'Bob': {
        'English',
        'Ukrainian',
        'Belarussian',
        'Russian',
        'French'
    }},
}

dictOfPupilLang = {}
for pupil in scheduleDict:
    print('')
    for name in scheduleDict[pupil]:
        counter = len(scheduleDict[pupil][name])
        dictOfPupilLang[name] = counter
        print(name+' knows ' + str(counter)+' languages')
        for language in scheduleDict[pupil][name]:
            print(language)

max_val = max(dictOfPupilLang.values())
max_key = max(dictOfPupilLang, key=lambda k: dictOfPupilLang[k])
print('')
print(max_key+' knows '+ str(max_val)+ ' languages. This is the largest number among pupils in the class')