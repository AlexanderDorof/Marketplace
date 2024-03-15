from django.test import TestCase
from dateutil.relativedelta import relativedelta
from django.utils import timezone

from .models import Car, Favorite, User


class CarTestCase(TestCase):
    def setUp(self):
        self.PERIOD = [6, 12, 24, 36, 60]
        self.current_date = timezone.now().date()
        favorite = Favorite.objects.create()
        user_alex = User.objects.create(name="Alex", surname="Petrov", favorite=favorite)
        Car.objects.create(brand="BMW", model="x5", slug="BMW-x5", year_produced=2000, seller=user_alex)
        Car.objects.create(brand="Toyota", model="Prius", slug="Toyota-Prius", year_produced=2022, seller=user_alex)
        for i in range(5):
            Car.objects.create(brand=f"BMW_{i}", model=f"x5_{i}", slug=f"BMW-x5_{i}", guarantee_period=self.PERIOD[i],
                               seller=user_alex)

    def test_car_instance_display(self):
        """correct diplaying of models instances"""
        car_1 = Car.objects.get(brand="BMW")
        car_2 = Car.objects.get(brand="Toyota")
        self.assertEqual(car_1.__str__(), 'BMW x5 2000')
        self.assertEqual(car_2.__str__(), 'Toyota Prius 2022')

    def test_car_instance_guarantee(self):
        """correct diplaying of models instances"""
        for i in range(5):
            future_date = self.current_date + relativedelta(months=self.PERIOD[i])
            self.assertEqual(Car.objects.get(brand=f"BMW_{i}").guarantee, future_date)
