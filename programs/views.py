from django.template import loader
from django.http import HttpResponse


from .models import Program

# Create your views here.

def index(request):
    programs_list = Program.objects.order_by('-end')
    globo_list = radioFromProgramsList(programs_list, 1)
    cbn_list = radioFromProgramsList(programs_list, 2)
    bh_list = radioFromProgramsList(programs_list, 3)
    template = loader.get_template('programs/index.html')
    ctx = {
        'name': 'Sistema Globo de Radio',
        'globo_list': globo_list,
        'cbn_list': cbn_list,
        'bh_list': bh_list,
    }
    return HttpResponse(template.render(ctx, request))

def radioFromProgramsList(programs, radioNumber):
    radio = []
    for program in programs:
        if program.radio == radioNumber:
            radio.append(program)
    return radio

def detail(request, program_id):
    return HttpResponse("You're looking at program %s." % program_id)