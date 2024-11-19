from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.contrib.auth.decorators import login_required

def member_list(request):
    members = Member.objects.all()
    return render(request, 'membership/members_list.html', {'members': members})

@login_required
def member_create(request):
    if request.user.is_authenticated:
        print(f"User {request.user.username} is logged in.")
    else:
        print("User is not authenticated.")

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'membership/members_form.html', {'form': form})

@login_required
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'membership/members_form.html', {'form': form})

@login_required
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'membership/member_confirm_delete.html', {'member': member})

def view_events(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    events = member.events.all()  # Assuming the ManyToManyField is named 'events'
    return render(request, 'membership/events.html', {'member': member, 'events': events})
