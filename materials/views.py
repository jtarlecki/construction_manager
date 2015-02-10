from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context

from forms import MaterialsForm, JobsForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf


from models import Materials, Vendors, Jobs, JobPhases

# Create your views here.
def hello(request):
	name = 'Jay'
	html = '<html><body>Hi %s. This seems to have worked!</body></html>' % name
	return HttpResponse(html)
	
def home_template(request):
	###
	name = 'Jason'
	company = 'New Market Builders'
	###
	t = get_template('home.html')
	html = t.render(Context({'name': name, 
	                         'company': company})) # key = name with contents of name variable
	return HttpResponse(html)

def materials_list(request):
	company = 'New Market Builders'	
	materials = Materials.objects.order_by('date')
	t = get_template('materials_list.html')
	context = Context({
	        'materials': materials,
	        'company': company
	})
	return HttpResponse(t.render(context))

def add(request):
	vendors = Vendors.objects.order_by('name')
	jobs = Jobs.objects.order_by('name')
	jobphases = JobPhases.objects.order_by('jobphase')
	# t = get_template('add.html')
	#context = Context({
	        #'vendors': vendors,
	        #'jobs': jobs,
	        #'jobphases': jobphases
	#})
	# return HttpResponse(t.render(context))	
	context = {
	        'vendors': vendors,
	        'jobs': jobs,
	        'jobphases': jobphases
	}
	return render(request, 'add.html', context)

def detail(request, material_id):
	try:
		material = Materials.objects.get(pk=material_id)
	except Materials.DoesNotExist:
			raise Http404("Material does not exist")
	return render(request, 'detail.html', {'material': material})
	
#def add_material(request, material_id):
	#p = get_object_or_404(Materials, pk=material_id)
	#try:
		#selected_choi

def create_job(request):
	if request.POST:
		f = JobsForm(request.POST)
		if f.is_valid():
			f.save()
		
			return HttpResponseRedirect('/add/')
		
	else:
		f = JobsForm()
	args = {}
	args.update(csrf(request))
	args['form'] = f

	return render_to_response('create_job.html', args)	
		
def create(request):
	create_job()
	if request.POST:
		form = MaterialsForm(request.POST)
		if form.is_valid():
			form.save()
			print 'form\n'
			for f in form:
				print f			
			return HttpResponseRedirect('/mat/')
		
	else:
		form = MaterialsForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('create_material.html', args)	

	