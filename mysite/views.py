from django.shortcuts import render

def template_as_view(template_name):
    def view(request):
        print locals()
        return render(request, template_name, locals())
    return view


