from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.permissions import AllowAny
from . models import *
from rest_framework import generics
from . serializers import *
from . forms import *
from django.contrib import messages
import requests
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required




# Create your views here.
class DestCreate(generics.ListCreateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer
    permission_classes = [AllowAny]


class DestDetails(generics.RetrieveAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

class DestUpdate(generics.RetrieveUpdateAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

class DestDelete(generics.DestroyAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

class DestSearch(generics.ListAPIView):
    queryset = Destinations.objects.all()
    serializer_class = DestSerializer

    def get_queryset(self):
        name = self.kwargs.get('Title')
        return Destinations.objects.filter(Title__icontains=name)

def dest_create(request):
    if request.method == 'POST':
        form = DestForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Create an instance of the form but don't save to the database yet
                destination = form.save(commit=False)

                # Set the creator as the current logged-in user
                destination.creator = request.user

                # Save the destination to the database
                destination.save()  # Now save the object

                # Display success message
                messages.success(request, "Movie created successfully")

                # Redirect to the list of destinations or any other page
                return redirect('listdest')
            except Exception as e:
                # Catch any general exceptions and display an error message
                messages.error(request, f'An error occurred: {str(e)}')
        else:
            # If the form is invalid, display an error message
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        # If the request method is GET, display a blank form
        form = DestForm()

    # Render the form template
    return render(request, "destcreate.html", {'form': form})

def list_dest(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    if query:
        movies = Destinations.objects.filter(Title__icontains=query)  # Filter movies by title
    else:
        movies = Destinations.objects.all()  # Return all movies if no search query

    return render(request, 'index.html', {'movies': movies, 'query': query})


    dest = Destinations.objects.all()
    return render(request,'index.html',{'dest':dest})


@login_required
def update_dest(request,id):
    # Fetch the destination object based on the provided id
    destination = get_object_or_404(Destinations, id=id)

    # Check if the logged-in user is the creator of the destination
    if destination.creator != request.user:
        return HttpResponseForbidden("You are not allowed to edit this movie.")

    # If the form is submitted via POST
    if request.method == 'POST':
        # Bind the form to the POST data and files, and associate it with the existing instance
        form = DestForm(request.POST, request.FILES, instance=destination)

        # Validate the form data
        if form.is_valid():
            # Save the updated destination object to the database
            form.save()
            # Display a success message and redirect to the destination list page
            messages.success(request, 'Movie updated successfully.')
            return redirect('listdest')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Form is not valid. Please correct the errors below.')
    else:
        # If the request is a GET request, pre-populate the form with the destination data
        form = DestForm(instance=destination)

    # Render the update page with the form
    return render(request, 'destinationupdate.html', {'form': form, 'destination': destination})

def dest_fetch(request, id):
    dests = get_object_or_404(Destinations, id=id)
    return render(request, 'dest_fetch.html', {'dests': dests})

@login_required
def dest_delete(request, id):
    # Fetch the destination object based on the provided id
    destination = get_object_or_404(Destinations, id=id)

    # Check if the logged-in user is the creator of the destination
    if destination.creator != request.user:
        return HttpResponseForbidden("You are not allowed to delete this movie.")

    if request.method == 'POST':
        # Delete the destination from the database
        destination.delete()

        # Display a success message
        messages.success(request, "Movie deleted successfully.")

        # Redirect to the list of destinations or any other page
        return redirect('listdest')

    # Render a confirmation page before deleting
    return render(request, 'confirm_delete.html', {'destination': destination})


@login_required
def add_review(request, destination_id):
    destination = get_object_or_404(Destinations, id=destination_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.destination = destination
            review.user = request.user
            review.save()
            return redirect('listdest')
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'destination': destination})







