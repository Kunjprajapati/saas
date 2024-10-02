from django.shortcuts import render
from django.http import HttpResponse
from visits.models import VisitsModel


# Function To Fetch Data from python code to the WebApp UI
def indexFunc(request, *args, **kwargs):
    # Showing the variable output to the webUI, Which is in the Dictionry formate. 
    kunj_title = "Index"
    kunj_desc = "Hello from the index html page"

    
    toShowDIctionary = {
        "showTitle" : kunj_title, 
        "showDesc" : kunj_desc,
        
    }
    return render(request, "index.html", toShowDIctionary)

def homefunc(request, *args, **kwargs): 
    """
    Core Logic To Build the Function!!
    """
    # Performing Model Related operation. 
    total_qs = VisitsModel.objects.all()
    page_qs = VisitsModel.objects.filter(path = request.path)

    showDictionary = {
        "PageCounts" : page_qs.count(), 
        "TotalCounts" : total_qs.count()
    }

    # Fetching the path from the user 
    storePath = request.path
    print(f"This is getting stored: {storePath}")
    VisitsModel.objects.create(path = request.path)

    return render(request, 'home.html', showDictionary)


