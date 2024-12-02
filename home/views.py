from django.shortcuts import render

# Create your views here.
def home(request):
    peopes =[
        {"name":"siddhi" , "age":16},
        {"name":"riya" , "age":17},
        {"name":"rutuja" , "age":18},
        {"name":"sharwari" , "age":19}
    ]
    return render(request,"index.html",context={"ppls":peopes})
