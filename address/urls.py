from django.urls import path
from .views import home, add_address_method, aaddr, done, get_data, update_address, update_record, delete_record


urlpatterns = [
    path('homepg', home, name='w_home'),
    path('addaddr', add_address_method, name='w_addaddr'),
    path('addA', aaddr, name='w_addA'),
    path('added', done, name='w_added'),
    path('displayD', get_data, name='w_displayD'),
    path('updateD/<int:id>', update_address, name='w_updateD'),
    path('updateD/updateR/<int:id>', update_record, name='w_updateR'),
    path('w_deleter/<int:_id>', delete_record, name='w_deleter')
]
