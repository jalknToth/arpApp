from django.shortcuts import render

def index(request):
    # Example: Fetching workflow names (replace with your actual logic)
    workflows = ["Workflow 1", "Workflow 2"] # Get this from database or rpa_workflows folder
    return render(request, 'index.html', {'workflows': workflows})