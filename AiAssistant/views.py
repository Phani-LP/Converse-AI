from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import StudentForm, ContactForm
from .models import StudentRegister, StudentContact,StudentChat
from django.contrib.auth.decorators import login_required
from google import generativeai as genai 
from ConverseAI.variables import API_KEY #for secure use of api keys
from django.contrib import messages
import markdown

def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        next_url = request.POST.get('next')  # Get the 'next' parameter

        if not next_url:  # Check if 'next' is empty
            next_url = 'home'  # Default to 'home' if 'next' is empty

        if user is None:
            try:
                from .models import UsersModel
                # Get the user by username
                user_obj_name = UsersModel.objects.get(name=u)
                
                if user_obj_name:
                    login(request, user_obj_name)
                    return redirect(next_url)
            except:# UsersModel.DoesNotExist
                # next_url = request.GET.get('next', 'home')
                messages.error(request, "User Name or Password is incorrect.")
                return redirect('login', {'next': next_url})  
            
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            messages.success(request, "Incorrect username or password, try again...")
            return render(request, 'login.html', {'next': next_url})
    else:
        # next_url = request.GET.get('next', 'home')
        # if not next_url:  # Check if 'next' is empty
        #     next_url = 'home'  # Default to 'home' if 'next' is empty  
        # "The above 3 lines are do same as below one line."
        next_url = request.GET.get('next', 'home')
        return render(request, 'login.html', {'next': next_url})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        # print(request.POST)  # Debug print
        # print(request.FILES) # Debug print
        form = StudentForm(request.POST, request.FILES) # Include request.FILES
        if form.is_valid():
            user_name = form.cleaned_data['name']
            user_password = form.cleaned_data['password']
            user = User.objects.create_user(
                username=user_name, 
                password=user_password, 
                is_superuser=True,
                is_staff=True, 
                is_active = True # to make the new user active (by default they are inactive--> can't login to admin panel)
                # to make the user unable to login panel, comment the active & staff. 
            ) #new superuser with full administrative privileges created.
            
            form.save()  # Save form data to database
            messages.success(request, "Registration successful, Now please login with your data!")
            return redirect('login')
    else:
        form = StudentForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() # Save form data to database
            form = ContactForm()
            messages.success(request, "Message sent successfully.") 
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

@login_required
def converseAI(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input') 
        try:
            # genai.configure(api_key="#Get your own key at:Google Gemini API")
            genai.configure(api_key=API_KEY)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            print(response.text)
            ai_response = response.text # not useful for user to read
            ai_response = markdown.markdown(ai_response) # will turn response to markdown
            # we use "|safe" in html to render markdown rather than just displaying it.
        except Exception as e:
            ai_response = f"An error occurred: {str(e)}" 

    else:
        user_input = ''
        ai_response = ''
    # we use "|safe" in html to render markdown rather than just displaying it.
    context = {'user_input': user_input, 'ai_response': ai_response}
    return render(request, 'chatbot.html', context)

def details(request):
    user_name = request.user.username
    data = StudentRegister.objects.filter(name=user_name)
    # print(data) #<QuerySet [<StudentRegister: Phani>]>
    # print(request.user.username) #Phani
    return render(request, 'user-details.html', {'data':data})