from django.shortcuts import HttpResponse,render
import random
from .models import User
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "The best way to predict the future is to create it. - Peter Drucker",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Your time is limited, don't waste it living someone else’s life. - Steve Jobs",
    "Don’t count the days, make the days count. - Muhammad Ali",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "If you can dream it, you can achieve it. - Zig Ziglar",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It always seems impossible until it’s done. - Nelson Mandela",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela"
    ]
def home(request):
    
    
    
    random_quote = random.choice(quotes)
    context = {
        "quote":random_quote,
    }

    return render(request,'index.html',context)


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        User.objects.create(name=name, email=email)
        # Ensure both fields are present before creating the user
        if name and email:
            User.objects.create(name=name, email=email)
            print("hyyyy")
            context = {
                'quote': random.choice(quotes),
                'success_message': "Form submitted successfully!"
            }
        else:
            print("error on something")
            context = {
                'quote': random.choice(quotes),
                'error_message': "Please fill out all fields!"
            }
        user = User.objects.all()
        context = {
            "users":user
        }
        return render(request,"userDetail.html",context)
    else:
        # If the request is not POST, just render the page without submission
        context = {
            'quote': random.choice(quotes)
        }
        return HttpResponse("hyyy")
    return render(request,"index.html",context)