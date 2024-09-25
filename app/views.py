from django.shortcuts import HttpResponse,render
import random
from .models import User
from datetime import datetime
quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Do not wait to strike till the iron is hot, but make it hot by striking. – William Butler Yeats",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "Opportunities don't happen, you create them. – Chris Grosser",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "The only person you are destined to become is the person you decide to be. – Ralph Waldo Emerson",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "Whether you think you can or you think you can’t, you’re right. – Henry Ford",
    "If you want to achieve greatness stop asking for permission. – Anonymous",
    "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "Don't be afraid to give up the good to go for the great. – John D. Rockefeller",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "If you are not willing to risk the usual, you will have to settle for the ordinary. – Jim Rohn",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "What seems to us as bitter trials are often blessings in disguise. – Oscar Wilde",
    "You learn more from failure than from success. Don’t let it stop you. Failure builds character. – Unknown",
    "The successful warrior is the average man, with laser-like focus. – Bruce Lee",
    "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. – Colin Powell",
    "The only way to achieve the impossible is to believe it is possible. – Charles Kingsleigh",
    "The man who has confidence in himself gains the confidence of others. – Hasidic Proverb",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
    "You may have to fight a battle more than once to win it. – Margaret Thatcher",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "The only place where success comes before work is in the dictionary. – Vidal Sassoon",
    "There are two kinds of people who will tell you that you cannot make a difference in this world: those who are afraid to try and those who are afraid you will succeed. – Ray Goforth",
    "Do what you love and the money will follow. – Marsha Sinetar",
    "Dream big and dare to fail. – Norman Vaughan",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "A person who never made a mistake never tried anything new. – Albert Einstein",
    "It’s not about ideas. It’s about making ideas happen. – Scott Belsky",
    "I never dreamed about success, I worked for it. – Estée Lauder",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Try not to become a man of success, but rather try to become a man of value. – Albert Einstein",
    "Knowledge is being aware of what you can do. Wisdom is knowing when not to do it. – Anonymous",
    "The only person you should try to be better than is the person you were yesterday. – Anonymous",
    "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. – Christian D. Larson",
    "You don’t have to see the whole staircase, just take the first step. – Martin Luther King, Jr.",
    "Success is how high you bounce when you hit bottom. – George S. Patton",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "Success is the sum of small efforts, repeated day-in and day-out. – Robert Collier",
    "Failure is the condiment that gives success its flavor. – Truman Capote",
    "Challenges are what make life interesting and overcoming them is what makes life meaningful. – Joshua J. Marine",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. – Roy T. Bennett",
    "If you want to live a happy life, tie it to a goal, not to people or things. – Albert Einstein",
    "Don't count the days, make the days count. – Muhammad Ali",
    "You must expect great things of yourself before you can do them. – Michael Jordan",
    "The road to success and the road to failure are almost exactly the same. – Colin R. Davis",
    "Success is not how high you have climbed, but how you make a positive difference to the world. – Roy T. Bennett",
    "Life is 10% what happens to you and 90% how you react to it. – Charles R. Swindoll",
    "When you stop chasing the wrong things, you give the right things a chance to catch you. – Lolly Daskal",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "A goal is not always meant to be reached; it often serves simply as something to aim at. – Bruce Lee",
    "I am not a product of my circumstances. I am a product of my decisions. – Stephen Covey",
    "Success is to wake up each morning and consciously decide that today will be the best day of your life. – Ken Poirot",
    "The biggest adventure you can take is to live the life of your dreams. – Oprah Winfrey",
    "Action is the foundational key to all success. – Pablo Picasso",
    "Don’t let the fear of losing be greater than the excitement of winning. – Robert Kiyosaki",
    "Success is liking yourself, liking what you do, and liking how you do it. – Maya Angelou",
    "Success is not the absence of failure; it’s the persistence through failure. – Aisha Tyler",
    "If you cannot do great things, do small things in a great way. – Napoleon Hill",
    "Success is the ability to go from failure to failure without losing your enthusiasm. – Winston Churchill",
    "You are confined only by the walls you build yourself. – Anonymous",
    "What we achieve inwardly will change outer reality. – Plutarch",
    "Success is the result of preparation, hard work, and learning from failure. – Colin Powell",
    "If you want to lift yourself up, lift up someone else. – Booker T. Washington",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "Success means having the courage, the determination, and the will to become the person you believe you were meant to be. – George A. Sheehan",
    "Always bear in mind that your own resolution to succeed is more important than any other. – Abraham Lincoln",
    "If you believe it will work out, you’ll see opportunities. If you believe it won’t, you will see obstacles. – Wayne Dyer"
]

def home(request):
    current_time = datetime.now().strftime("%Y")
    random_quote = random.choice(quotes)
    context = {
        "quote":random_quote,
        "current_time":current_time,
    }

    return render(request,'index.html',context)


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        User.objects.create(name=name, email=email)
        
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
    return render(request,"index.html",context)