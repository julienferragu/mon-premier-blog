from django.shortcuts import render, get_object_or_404, redirect
from .forms import MountaineerActivityForm
from django.db import transaction
from .models import Activity, Mountaineer
from django.http import HttpResponseBadRequest


def post_list(request):
    mountaineer = Mountaineer.objects.all()

    activities = Activity.objects.all()
    return render(request, 'climbingapp/post_list.html', {'mountaineers': mountaineer, 'activities' : activities})


def change_mountaineer_activity(request, mountaineer_id):
    mountaineer = get_object_or_404(Mountaineer, id_mountaineer=mountaineer_id)

    previous_activity = get_object_or_404(Activity, id_activity = mountaineer.activity.id_activity)
    if request.method == 'POST':
        form = MountaineerActivityForm(request.POST, instance=mountaineer)
        if form.is_valid():
            new_activity = form.cleaned_data['activity']
            
            if new_activity.availability == 'busy':
                return HttpResponseBadRequest("Cannot change to a busy activity.")

            if new_activity.category=='Training' or new_activity.category=='Climbing':
                if mountaineer.state!='Refreshed':
                    return HttpResponseBadRequest("Climber is not refreshed.")
                if new_activity.id_activity == 'Everest' or new_activity.id_activity == 'K2':
                    if mountaineer.oxygen == 'Empty':
                        return HttpResponseBadRequest("Sorry, the climber needs oxygen for this peak")
                mountaineer.state = 'Exhausted' 
                mountaineer.oxygen = 'Empty' 
                mountaineer.save()

            elif new_activity.category=='Shopping':
                if mountaineer.oxygen=='Full':
                    return HttpResponseBadRequest("Climber does not need oxygen.")
                mountaineer.oxygen = 'Full' 
                mountaineer.save()

            elif new_activity.id_activity == 'Bedroom':
                if mountaineer.state != 'Exhausted':
                    return HttpResponseBadRequest("Climber does not need rest.")
                mountaineer.state = 'Hungry'
                mountaineer.save()
               

            elif new_activity.id_activity == 'Dining room':
                if mountaineer.state != 'Hungry':
                    return HttpResponseBadRequest("Climber does not need to eat.")
                mountaineer.state = 'Refreshed'
                mountaineer.save()

            with transaction.atomic():
    
                previous_activity.availability = 'vacant'
                previous_activity.save()
                mountaineer.activity.save()
                new_activity.availability = 'busy'
                new_activity.save()
                mountaineer.activity = new_activity
                mountaineer.save()
        

        return redirect('post_list')

    else:
        form = MountaineerActivityForm(instance=mountaineer)

    return render(request, 'change_mountaineer_activity.html', {'form': form, 'mountaineer': mountaineer})





