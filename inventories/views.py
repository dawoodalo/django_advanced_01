from django.shortcuts import render
from .models import Inventory

def inventory_list(request):

	context = {
		"inventory":Inventory.objects.all()
	}
	return render(request, 'inventory_list.html', context)

 