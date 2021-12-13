from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os, time
os.environ['TZ'] = 'US/Mountain'
from django.core.exceptions import MultipleObjectsReturned

from ratemylandlord.models import Landlord, Property, Rating
#becca was here.

#Madaleine Was Here lolzzzzzzzzzzzzz

#can you see this

def indexPageView(request) :
    return render(request, 'ratemylandlord/index.html')

def editReviewsPageView(request, editID) :
    data = Rating.objects.get(id = editID)
    context = {
        "rate" : data
    }
    return render(request, 'ratemylandlord/editreviews.html', context)

def landlordDetailPageView(request, detailID):
    data = Landlord.objects.get(id = detailID)
    props = Property.objects.filter(landlord = data.id)
    context = {
        "landlord" : data,
        "properties" : props
    }
    return render(request, 'ratemylandlord/landlorddetail.html', context)

def propertyDetailPageView(request, detailID):
    data = Property.objects.get(id = detailID)
    rates = Rating.objects.filter(properties = data.id)
    context = {
        "property" : data,
        "ratings" : rates
    }
    return render(request, 'ratemylandlord/propertydetail.html', context)

def updateReviewsPageView(request) :
    if request.method == 'POST':
        editID = request.POST['editid']
        rating = Rating.objects.get(id=editID)
        #put landlord name here
        rating.rating = request.POST['rating']
        rating.date_submitted = datetime.today()
        rating.property_condition = request.POST['propertycondition']
    
        if request.POST.get('poormanagement', False) == 'on':
            rating.poor_management = True
        else:
            rating.poor_management = False

        if request.POST.get('hiddenfees', False) == 'on':
            rating.hidden_fees = True
        else:
            rating.hidden_fees = False

        if request.POST.get('privacy', False) == 'on':
            rating.lack_of_privacy = True
        else:
            rating.lack_of_privacy = False

        if request.POST.get('funds', False) == 'on':
            rating.unreturned_funds = True
        else:
            rating.unreturned_funds = False

        if request.POST.get('safety', False) == 'on':
            rating.safety_concerns = True
        else:
            rating.safety_concerns = False

        if request.POST.get('appliances', False) == 'on':
            rating.appliance_issues = True
        else:
            rating.appliance_issues = False

        if request.POST.get('mold', False) == 'on':
            rating.mold = True
        else:
            rating.mold = False

        if request.POST.get('pests', False) == 'on':
            rating.pests = True
        else:
            rating.pests = False

        if request.POST.get('utilities', False) == 'on':
            rating.utilities = True
        else:
            rating.utilities = False

        if request.POST.get('neigh', False) == 'on':
            rating.neighborhood_problems = True
        else:
            rating.neighborhood_problems = False

        if request.POST.get('parking', False) == 'on':
            rating.parking = True
        else:
            rating.parking = False

        if request.POST.get('badcont', False) == 'on':
            rating.bad_contracts = True
        else:
            rating.bad_contracts = False

        if request.POST.get('rent', False) == 'on':
            rating.change_in_rent = True
        else:
            rating.change_in_rent = False
        rating.other_notes = request.POST['othernotes']
        rating.save()
    data = Rating.objects.all()
    context = {
        "ratings" : data
    }
    return render(request, 'ratemylandlord/viewreviews.html', context)

def aboutPageView(request) :
    return render(request, 'ratemylandlord/about.html')

def addReviewsPageView(request) :
    if request.method == 'POST':    
        property = Property()

        landy = request.POST['landlord']
        property.landlord = Landlord.objects.get(management_company=landy)
        property.property_name = request.POST['propertyName']
        property.street_address = request.POST['streetAddress']
        property.city = request.POST['city']
        property.state = request.POST['state']
        property.zipcode = request.POST['zip']

        property.save()
        data = Property.objects.all()
        context = {
            "proplist" : data
        }
        return render(request, 'ratemylandlord/addreviews.html', context)
    else:
        data = Property.objects.all()
        context = {
            "proplist" : data
        }
        return render(request, 'ratemylandlord/addreviews.html', context)

def viewReviewsPageView(request) :
    if request.method == 'POST':
        rating = Rating()
        prop = request.POST['property']
        try :
            rating.properties = Property.objects.get(property_name=prop)
        except MultipleObjectsReturned:
            rating.properties = Property.objects.filter(property_name=prop).first()
        rating.users = request.POST['nickname']
        rating.rating = request.POST['rating']
        if request.POST.get('poormanagement', False) == 'on':
            rating.poor_management = True
        else:
            rating.poor_management = False

        if request.POST.get('hiddenfees', False) == 'on':
            rating.hidden_fees = True
        else:
            rating.hidden_fees = False

        if request.POST.get('utilities', False) == 'on':
            rating.utilities = True
        else:
            rating.utilities = False

        if request.POST.get('privacy', False) == 'on':
            rating.lack_of_privacy = True
        else:
            rating.lack_of_privacy = False

        if request.POST.get('funds', False) == 'on':
            rating.unreturned_funds = True
        else:
            rating.unreturned_funds = False

        rating.property_condition = request.POST['condition']

        if request.POST.get('safety', False) == 'on':
            rating.safety_concerns = True
        else:
            rating.safety_concerns = False

        if request.POST.get('appliances', False) == 'on':
            rating.appliance_issues = True
        else:
            rating.appliance_issues = False

        if request.POST.get('mold', False) == 'on':
            rating.mold = True
        else:
            rating.mold = False

        if request.POST.get('pests', False) == 'on':
            rating.pests = True
        else:
            rating.pests = False

        if request.POST.get('neigh', False) == 'on':
            rating.neighborhood_problems = True
        else:
            rating.neighborhood_problems = False

        if request.POST.get('parking', False) == 'on':
            rating.parking = True
        else:
            rating.parking = False

        if request.POST.get('badcont', False) == 'on':
            rating.bad_contracts = True
        else:
            rating.bad_contracts = False

        if request.POST.get('rent', False) == 'on':
            rating.change_in_rent = True
        else:
            rating.change_in_rent = False

        rating.other_notes = request.POST['notes']
        rating.save()
    
        data = Rating.objects.all()
        context = {
            "ratings" : data
        }
        return render(request, 'ratemylandlord/viewreviews.html', context)

    else:
        data = Rating.objects.all()
        context = {
            "ratings" : data
        }
        return render(request, 'ratemylandlord/viewreviews.html', context)

def deletePageView(request, deleteID):
    data = Rating.objects.get(id = deleteID)
    data.delete()
    return viewReviewsPageView(request)
    #Connor was here

def addLandlordPageView(request):
    data = Landlord.objects.all()

    context = {
        "landies" : data
    }
    return render(request, 'ratemylandlord/addlandlord.html', context)

def addPropertyPageView(request):
    if request.method == 'POST':
        landlord = Landlord()

        landlord.first_name = request.POST['firstName']
        landlord.last_name = request.POST['lastName']
        landlord.management_company = request.POST['mancomp']

        landlord.save()

        data = Landlord.objects.all()
        prop = Property.objects.all()

        context = {
            "landies" : data,
            "propies" : prop
        }
        return render(request, 'ratemylandlord/addproperty.html', context)

    else:
        data = Landlord.objects.all()
        prop = Property.objects.all()

        context = {
            "landies" : data,
            "propies" : prop
        }
        return render(request, 'ratemylandlord/addproperty.html', context)