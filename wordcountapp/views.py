from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    import re
    text = re.sub('[!@#$%^&*()_+-=<>}{\'\"\[\]?/.\,]','',text)
    words = text.split()
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    from operator import itemgetter
    sorted_dict = sorted(word_dictionary.items(), key=itemgetter(1), reverse=True)
    top = sorted_dict[0]
    topword = top[0]
    topcount = top[1]

    average_count = round(sum(word_dictionary.values())/len(word_dictionary),2)
    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary' : word_dictionary.items(), 'average' : average_count, 'topword' : topword, 'topcount':topcount })