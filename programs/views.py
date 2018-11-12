from django.template import loader
from django.http import HttpResponse


from .models import Program

# Create your views here.

def index(request):
    programs_list = Program.objects.order_by('-end')
    globo_list = _radioFromProgramsList(programs_list, 1)
    cbn_list = _radioFromProgramsList(programs_list, 2)
    bh_list = _radioFromProgramsList(programs_list, 3)
    live_list = _live_programs(programs_list)
    template = loader.get_template('programs/index.html')
    ctx = {
        'name': 'SGR',
        'globo_list': globo_list,
        'cbn_list': cbn_list,
        'bh_list': bh_list,
        'live_list': live_list,
    }
    return HttpResponse(template.render(ctx, request))

def _radioFromProgramsList(programs, radioNumber):
    radio = []
    for program in programs:
        if program.radio == radioNumber:
            radio.append(program)
    return radio

def detail(request, program_id):
    program = Program.objects.get(pk=program_id)
    return HttpResponse("You're looking at program %s by %s that started at %s and ends at %s." % (program.name, program.radio, program.start, program.end))

def grid(request, grid_id):
    programs = Program.objects.filter(radio=grid_id)
    ctx = {
        'name': 'SGR',
        'programs': programs
    }
    template = loader.get_template('programs/grid.html')
    return HttpResponse(template.render(ctx, request))

def _live_programs(programs):
    live = []
    for p in programs:
        if (p.ptype == 2) and (p.is_live):
            live.append(p)
    for p in programs:
        if (p.is_live) and not (p.ptype == 2):
            live.append(p)
    return live

