from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password,check_password
class Signup(View):
    def validateCustomer(self,customer):
        error_message = None
        if(not customer.first_name):
            error_message = "first Name Required!!"

        elif len(customer.first_name) < 4:
            error_message = 'first Name must be 4 char long'
        elif(not customer.last_name):
            error_message = "last Name Required!!"

        elif len(customer.last_name) < 4:
            error_message = 'last Name must be 4 char long'
        elif(not customer.phone):
            error_message = "Phone Number Required!!"     
        elif len(customer.phone) < 10:
            error_message = 'Phone no must be 10 digit'
       
        if customer.isExists():
            error_message = "Email address alredy register"
        return error_message
    def get(self,request):
        return render(request,'orders\signup.html')

    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname') 
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
        'first_name':first_name,
        'last_name':last_name,
        'phone':phone,
        'email':email
        }

        error_message = None
        customer = Customer(first_name = first_name,
        last_name = last_name,
        phone = phone,
        email = email,
        password = password)
        error_message = self.validateCustomer(customer)                    
                
        if not error_message:     
            customer.password = make_password(customer.password) 
            customer.save()
            return redirect ('homepage')
        else:
            data={
            'error':error_message,
            'values':value
                
            }
            return render(request,'orders\signup.html',data)        