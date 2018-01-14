from django.db import models

# Create your models here.
class BusOrganisation(models.Model):
    '''
    Class to define a bus company
    '''
    name = models.CharField(max_length=255)

    logo = models.ImageField(upload_to="logo-pic/", blank=True) 

    def __str__(self):
        return self.name

    @classmethod
    def get_bus_organisations(cls):
        '''
        Function to get all the buses in the database

        Return
            bus_organisations : list of all the Bus Organisation objects in the database
        '''
        bus_organisations = cls.objects.all()

        return bus_organisations

    @classmethod
    def get_single_bus_organisation(cls, bus_organisation_id):
        '''
        Function to get a bus organisation with the specific id 

        Args
            bus_organisation_id : the bus organisation id 

        Return
            single_bus_origanisation : Bus Organisation object with the specified id 
        '''
        single_bus_origanisation = cls.objects.get(id=bus_organisation_id)

        return single_bus_origanisation

class Route(models.Model):
    '''
    Class to define a bus route
    '''
    departure_location = models.CharField(max_length=255)

    destination_location = models.CharField(max_length=255)

    def __str__(self):
        return self.departure_location + '-' + self.destination_location

    @classmethod
    def get_routes(cls):
        '''
        Function to get all the bus routes in the database

        Return
            routes : list of all the Route objects in the database
        '''
        routes = cls.objects.all()

        return routes

    @classmethod
    def get_single_route(cls, route_id):
        '''
        Function to get a bus route with the specific id 

        Args
            route_id : the bus route id 

        Return
            single_route : Route object with the specified id 
        '''
        single_route = cls.objects.get(id=route_id)

        return single_route

class Bus(models.Model):
    '''
    Class to define a bus 
    '''
    bus_organisation = models.ForeignKey(BusOrganisation, on_delete=models.CASCADE)

    number_plate = models.CharField(max_length=50)

    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bus_organisation.name + ' Bus No.' + self.id

    @classmethod
    def get_buses(cls):
        '''
        Function to get all the buses in the database

        Return
            buses : list of all the Bus objects in the database
        '''
        buses = cls.objects.all()

        return buses

    @classmethod
    def get_single_bus(cls, bus_id):
        '''
        Function to get a bus with the specific id 

        Args
            bus_id : the bus id 

        Return
            single_bus : Bus object with the specified id 
        '''
        single_bus = cls.objects.get(id=bus_id)

        return single_bus

    @classmethod
    def get_bus_organisation_buses(cls, bus_organisation_id):
        '''
        Function to get buses belonging to the bus organisation with the specific id 

        Args
            bus_organisation_id : the bus organisation id 

        Return
            bus_origanisation_buses : list of all the Bus objects in the database with the specified bus organisation id
        '''
        bus_origanisation_buses = cls.objects.filter(bus_organisation=bus_organisation_id)

        return bus_origanisation_buses

    @classmethod
    def get_route_buses(cls, route_id):
        '''
        Function to get buses belonging to the bus route with the specific id 

        Args
            route_id : the route id 

        Return
            route_buses : list of all the Bus objects in the database with the specified route id
        '''
        route_buses = cls.objects.filter(route=route_id)

        return route_buses

class Schedule(models.Model):
    '''
    Class to define a bus schedule
    '''
    departure_time = models.DateTimeField(auto_now_add=False)

    arrival_time = models.DateTimeField(auto_now_add=False)

    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return self.bus.bus_organisation.name + 'Bus No.' + self.bus.id + 'Schedule No.' + self.id

    @classmethod
    def get_schedules(cls):
        '''
        Function to get all the bus schedules in the database

        Return
            schedules : list of all the Schedule objects in the database
        '''
        schedule = cls.objects.all()

        return schedule

    @classmethod
    def get_single_schedule(cls, schedule_id):
        '''
        Function to get a bus schedule with the specific id 

        Args
            schedule_id : the bus schedule id 

        Return
            single_schedule : Schedule object with the specified id 
        '''
        single_schedule = cls.objects.get(id=schedule_id)

        return single_schedule

    @classmethod
    def get_bus_schedules(cls, bus_id):
        '''
        Function to get schedules belonging to the bus with the specific id 

        Args
            bus_id : the bus id 

        Return
            bus_schedules : list of all the Schedule objects in the database with the specified bus id
        '''
        bus_schedules = cls.objects.filter(bus=bus_id)

        return bus_schedules

    @classmethod
    def get_travel_estimation(cls, schedule_id):
        '''
        Function to get the travel time estinmation for a bus schedule with the specific id 

        Args
            schedule_id : the bus schedule id 

        Return
            travel_estimation : Travel time estimation for the specified schedule
        '''
        schedule = cls.objects.get(id=schedule_id)

        calculate_travel_estimation = schedule.arrival_time - schedule.departure_time

        travel_estimation = str(calculate_travel_estimation.seconds//3600) + ' hours ' + str(calculate_travel_estimation.seconds//60 % 60) + ' minutes'

        return travel_estimation




