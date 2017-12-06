from django.shortcuts import render

#Admin index - comicfire.com/admin/
def admin(request):
	return render(request, 'admin.html')