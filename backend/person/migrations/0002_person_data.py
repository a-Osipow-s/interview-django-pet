from django.db import migrations
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import date


def create_sample_persons(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    Person = apps.get_model('person', 'Person')

    persons_data = [
        {"username": "jsmith", "email": "jsmith@yopmail.com", "first_name": "John", "last_name": "Smith", 
         "bio": "Software engineer with passion for AI and machine learning", "company": "TechCorp", 
         "job_title": "Senior Software Engineer", "birth_date": date(1990, 5, 15), "experience": 8.5},
        
        {"username": "mjohnson", "email": "mjohnson@yopmail.com", "first_name": "Maria", "last_name": "Johnson",
         "bio": "Digital marketing specialist focused on social media strategies", "company": "MarketGenius",
         "job_title": "Marketing Manager", "birth_date": date(1988, 3, 22), "experience": 10.0},
        
        {"username": "dwilliams", "email": "dwilliams@yopmail.com", "first_name": "David", "last_name": "Williams",
         "bio": "Product designer creating intuitive user experiences", "company": "DesignHub",
         "job_title": "Lead UX Designer", "birth_date": date(1992, 7, 8), "experience": 6.0},
        
        {"username": "sbrown", "email": "sbrown@yopmail.com", "first_name": "Sarah", "last_name": "Brown",
         "bio": "Data scientist specializing in predictive analytics", "company": "DataMinds",
         "job_title": "Senior Data Scientist", "birth_date": date(1991, 11, 30), "experience": 7.5},
        
        {"username": "rjones", "email": "rjones@yopmail.com", "first_name": "Robert", "last_name": "Jones",
         "bio": "DevOps engineer automating cloud infrastructure", "company": "CloudScale",
         "job_title": "DevOps Engineer", "birth_date": date(1989, 1, 12), "experience": 9.0},
        
        {"username": "lgarcia", "email": "lgarcia@yopmail.com", "first_name": "Lisa", "last_name": "Garcia",
         "bio": "Full-stack developer building scalable web applications", "company": "WebSolutions",
         "job_title": "Full Stack Developer", "birth_date": date(1993, 9, 5), "experience": 5.0},
        
        {"username": "mmiller", "email": "mmiller@yopmail.com", "first_name": "Michael", "last_name": "Miller",
         "bio": "Project manager coordinating agile development teams", "company": "AgileWorks",
         "job_title": "Project Manager", "birth_date": date(1987, 6, 18), "experience": 11.5},
        
        {"username": "jdavis", "email": "jdavis@yopmail.com", "first_name": "Jennifer", "last_name": "Davis",
         "bio": "Content strategist crafting compelling brand narratives", "company": "ContentPro",
         "job_title": "Content Strategist", "birth_date": date(1994, 2, 28), "experience": 4.5},
        
        {"username": "wrodriguez", "email": "wrodriguez@yopmail.com", "first_name": "William", "last_name": "Rodriguez",
         "bio": "Cybersecurity analyst protecting digital assets", "company": "SecureNet",
         "job_title": "Security Analyst", "birth_date": date(1990, 8, 14), "experience": 8.0},
        
        {"username": "emartinez", "email": "emartinez@yopmail.com", "first_name": "Emily", "last_name": "Martinez",
         "bio": "Mobile app developer creating iOS and Android applications", "company": "AppFactory",
         "job_title": "Mobile Developer", "birth_date": date(1995, 4, 7), "experience": 3.5},
        
        {"username": "jhernandez", "email": "jhernandez@yopmail.com", "first_name": "James", "last_name": "Hernandez",
         "bio": "Business analyst bridging tech and business requirements", "company": "BizTech",
         "job_title": "Business Analyst", "birth_date": date(1988, 12, 3), "experience": 10.5},
        
        {"username": "alopez", "email": "alopez@yopmail.com", "first_name": "Amanda", "last_name": "Lopez",
         "bio": "Graphic designer specializing in brand identity", "company": "CreativeStudio",
         "job_title": "Senior Graphic Designer", "birth_date": date(1992, 10, 20), "experience": 6.5},
        
        {"username": "cgonzalez", "email": "cgonzalez@yopmail.com", "first_name": "Christopher", "last_name": "Gonzalez",
         "bio": "Systems architect designing enterprise solutions", "company": "EnterpriseTech",
         "job_title": "Solutions Architect", "birth_date": date(1986, 5, 9), "experience": 13.0},
        
        {"username": "kwilson", "email": "kwilson@yopmail.com", "first_name": "Karen", "last_name": "Wilson",
         "bio": "HR manager fostering positive workplace culture", "company": "PeopleFirst",
         "job_title": "HR Manager", "birth_date": date(1989, 7, 25), "experience": 9.5},
        
        {"username": "danderson", "email": "danderson@yopmail.com", "first_name": "Daniel", "last_name": "Anderson",
         "bio": "Frontend developer with expertise in React and Vue", "company": "FrontendMasters",
         "job_title": "Frontend Developer", "birth_date": date(1993, 3, 16), "experience": 5.5},
        
        {"username": "nthomas", "email": "nthomas@yopmail.com", "first_name": "Nancy", "last_name": "Thomas",
         "bio": "Quality assurance engineer ensuring software excellence", "company": "QualityFirst",
         "job_title": "QA Engineer", "birth_date": date(1991, 11, 11), "experience": 7.0},
        
        {"username": "ktaylor", "email": "ktaylor@yopmail.com", "first_name": "Kevin", "last_name": "Taylor",
         "bio": "Database administrator optimizing data performance", "company": "DataSystems",
         "job_title": "Database Administrator", "birth_date": date(1987, 9, 2), "experience": 12.0},
        
        {"username": "bmoore", "email": "bmoore@yopmail.com", "first_name": "Barbara", "last_name": "Moore",
         "bio": "Technical writer documenting complex systems", "company": "DocuTech",
         "job_title": "Technical Writer", "birth_date": date(1994, 6, 30), "experience": 4.0},
        
        {"username": "jjackson", "email": "jjackson@yopmail.com", "first_name": "Joseph", "last_name": "Jackson",
         "bio": "Cloud architect designing scalable infrastructure", "company": "CloudNative",
         "job_title": "Cloud Architect", "birth_date": date(1988, 2, 17), "experience": 10.0},
        
        {"username": "smartin", "email": "smartin@yopmail.com", "first_name": "Susan", "last_name": "Martin",
         "bio": "Scrum master facilitating agile transformations", "company": "AgileCoach",
         "job_title": "Scrum Master", "birth_date": date(1990, 8, 8), "experience": 8.0},
        
        {"username": "tlee", "email": "tlee@yopmail.com", "first_name": "Thomas", "last_name": "Lee",
         "bio": "Backend developer building robust API services", "company": "APIWorks",
         "job_title": "Backend Developer", "birth_date": date(1992, 12, 1), "experience": 6.0},
        
        {"username": "mperez", "email": "mperez@yopmail.com", "first_name": "Michelle", "last_name": "Perez",
         "bio": "UX researcher understanding user needs and behaviors", "company": "UserInsights",
         "job_title": "UX Researcher", "birth_date": date(1995, 5, 19), "experience": 3.0},
        
        {"username": "cthompson", "email": "cthompson@yopmail.com", "first_name": "Charles", "last_name": "Thompson",
         "bio": "Network engineer maintaining critical infrastructure", "company": "NetCore",
         "job_title": "Network Engineer", "birth_date": date(1989, 10, 27), "experience": 9.0},
        
        {"username": "lwhite", "email": "lwhite@yopmail.com", "first_name": "Linda", "last_name": "White",
         "bio": "SEO specialist optimizing web presence", "company": "SearchMax",
         "job_title": "SEO Specialist", "birth_date": date(1991, 4, 14), "experience": 7.5},
        
        {"username": "rharris", "email": "rharris@yopmail.com", "first_name": "Richard", "last_name": "Harris",
         "bio": "Machine learning engineer developing AI models", "company": "AILabs",
         "job_title": "ML Engineer", "birth_date": date(1993, 1, 23), "experience": 5.0},
        
        {"username": "psanchez", "email": "psanchez@yopmail.com", "first_name": "Patricia", "last_name": "Sanchez",
         "bio": "Product owner defining product roadmaps", "company": "ProductVision",
         "job_title": "Product Owner", "birth_date": date(1988, 7, 6), "experience": 11.0},
        
        {"username": "mclark", "email": "mclark@yopmail.com", "first_name": "Mark", "last_name": "Clark",
         "bio": "Software architect designing distributed systems", "company": "SystemDesign",
         "job_title": "Software Architect", "birth_date": date(1985, 3, 31), "experience": 14.5},
        
        {"username": "dramirez", "email": "dramirez@yopmail.com", "first_name": "Donna", "last_name": "Ramirez",
         "bio": "Customer success manager ensuring client satisfaction", "company": "ClientFirst",
         "job_title": "Customer Success Manager", "birth_date": date(1990, 11, 9), "experience": 8.5},
        
        {"username": "plewis", "email": "plewis@yopmail.com", "first_name": "Paul", "last_name": "Lewis",
         "bio": "Site reliability engineer maintaining system uptime", "company": "ReliableOps",
         "job_title": "SRE", "birth_date": date(1992, 6, 21), "experience": 6.5},
        
        {"username": "crobinson", "email": "crobinson@yopmail.com", "first_name": "Carol", "last_name": "Robinson",
         "bio": "Financial analyst driving data-driven decisions", "company": "FinTech Solutions",
         "job_title": "Financial Analyst", "birth_date": date(1987, 9, 13), "experience": 12.5},
        
        {"username": "swalker", "email": "swalker@yopmail.com", "first_name": "Steven", "last_name": "Walker",
         "bio": "Game developer creating immersive experiences", "company": "GameStudio",
         "job_title": "Game Developer", "birth_date": date(1994, 2, 4), "experience": 4.5},
        
        {"username": "byoung", "email": "byoung@yopmail.com", "first_name": "Betty", "last_name": "Young",
         "bio": "Brand manager building strong market presence", "company": "BrandBuilders",
         "job_title": "Brand Manager", "birth_date": date(1989, 12, 18), "experience": 9.5},
        
        {"username": "eallen", "email": "eallen@yopmail.com", "first_name": "Edward", "last_name": "Allen",
         "bio": "Blockchain developer exploring decentralized solutions", "company": "ChainTech",
         "job_title": "Blockchain Developer", "birth_date": date(1991, 8, 26), "experience": 7.0},
        
        {"username": "hking", "email": "hking@yopmail.com", "first_name": "Helen", "last_name": "King",
         "bio": "Operations manager streamlining business processes", "company": "EfficiencyPro",
         "job_title": "Operations Manager", "birth_date": date(1986, 5, 7), "experience": 13.5},
        
        {"username": "jwright", "email": "jwright@yopmail.com", "first_name": "Jason", "last_name": "Wright",
         "bio": "Embedded systems engineer working on IoT devices", "company": "IoTInnovate",
         "job_title": "Embedded Engineer", "birth_date": date(1993, 10, 15), "experience": 5.5},
        
        {"username": "dscott", "email": "dscott@yopmail.com", "first_name": "Dorothy", "last_name": "Scott",
         "bio": "Sales engineer bridging technical and business needs", "company": "SalesTech",
         "job_title": "Sales Engineer", "birth_date": date(1990, 4, 2), "experience": 8.0},
        
        {"username": "agreen", "email": "agreen@yopmail.com", "first_name": "Andrew", "last_name": "Green",
         "bio": "Computer vision engineer developing image processing systems", "company": "VisionAI",
         "job_title": "Computer Vision Engineer", "birth_date": date(1992, 1, 29), "experience": 6.0},
        
        {"username": "sbaker", "email": "sbaker@yopmail.com", "first_name": "Sandra", "last_name": "Baker",
         "bio": "Compliance officer ensuring regulatory adherence", "company": "ComplianceFirst",
         "job_title": "Compliance Officer", "birth_date": date(1988, 11, 5), "experience": 10.5},
        
        {"username": "radams", "email": "radams@yopmail.com", "first_name": "Ryan", "last_name": "Adams",
         "bio": "Platform engineer building developer tools", "company": "DevTools",
         "job_title": "Platform Engineer", "birth_date": date(1991, 7, 12), "experience": 7.5},
        
        {"username": "knelson", "email": "knelson@yopmail.com", "first_name": "Kimberly", "last_name": "Nelson",
         "bio": "Learning and development specialist training teams", "company": "SkillUp",
         "job_title": "L&D Specialist", "birth_date": date(1994, 3, 24), "experience": 4.0},
        
        {"username": "bcarter", "email": "bcarter@yopmail.com", "first_name": "Brian", "last_name": "Carter",
         "bio": "Release manager coordinating software deployments", "company": "DeployPro",
         "job_title": "Release Manager", "birth_date": date(1987, 12, 10), "experience": 11.5},
        
        {"username": "mmitchell", "email": "mmitchell@yopmail.com", "first_name": "Michelle", "last_name": "Mitchell",
         "bio": "Accessibility specialist ensuring inclusive design", "company": "AccessibleTech",
         "job_title": "Accessibility Specialist", "birth_date": date(1990, 6, 17), "experience": 8.5},
        
        {"username": "gperez", "email": "gperez2@yopmail.com", "first_name": "George", "last_name": "Perez",
         "bio": "API developer creating integration solutions", "company": "APIConnect",
         "job_title": "API Developer", "birth_date": date(1993, 9, 3), "experience": 5.0},
        
        {"username": "eroberts", "email": "eroberts@yopmail.com", "first_name": "Elizabeth", "last_name": "Roberts",
         "bio": "Change management consultant facilitating transitions", "company": "ChangeLeaders",
         "job_title": "Change Management Consultant", "birth_date": date(1989, 2, 20), "experience": 9.0},
        
        {"username": "jturner", "email": "jturner@yopmail.com", "first_name": "Jeffrey", "last_name": "Turner",
         "bio": "Performance engineer optimizing application speed", "company": "FastApps",
         "job_title": "Performance Engineer", "birth_date": date(1991, 5, 28), "experience": 7.0},
        
        {"username": "dphillips", "email": "dphillips@yopmail.com", "first_name": "Deborah", "last_name": "Phillips",
         "bio": "Event coordinator organizing tech conferences", "company": "EventTech",
         "job_title": "Event Coordinator", "birth_date": date(1988, 10, 8), "experience": 10.0},
        
        {"username": "kcampbell", "email": "kcampbell@yopmail.com", "first_name": "Kenneth", "last_name": "Campbell",
         "bio": "Infrastructure engineer building resilient systems", "company": "InfraCore",
         "job_title": "Infrastructure Engineer", "birth_date": date(1992, 4, 11), "experience": 6.5},
        
        {"username": "lparker", "email": "lparker@yopmail.com", "first_name": "Laura", "last_name": "Parker",
         "bio": "Automation engineer streamlining workflows", "company": "AutomatePro",
         "job_title": "Automation Engineer", "birth_date": date(1995, 1, 6), "experience": 3.5},
        
        {"username": "tevans", "email": "tevans@yopmail.com", "first_name": "Timothy", "last_name": "Evans",
         "bio": "Integration specialist connecting enterprise systems", "company": "IntegrationHub",
         "job_title": "Integration Specialist", "birth_date": date(1990, 8, 19), "experience": 8.0},
        
        {"username": "redwards", "email": "redwards@yopmail.com", "first_name": "Rebecca", "last_name": "Edwards",
         "bio": "Innovation consultant driving digital transformation", "company": "InnovateNow",
         "job_title": "Innovation Consultant", "birth_date": date(1986, 11, 25), "experience": 12.0},
    ]
    
    for data in persons_data:
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        
        Person.objects.create(
            user=user,
            bio=data['bio'],
            company=data['company'],
            job_title=data['job_title'],
            birth_date=data['birth_date'],
            experience=data['experience']
        )


def reverse_func(apps, schema_editor):
    User = get_user_model()
    
    usernames = [
        "jsmith", "mjohnson", "dwilliams", "sbrown", "rjones", "lgarcia", "mmiller",
        "jdavis", "wrodriguez", "emartinez", "jhernandez", "alopez", "cgonzalez",
        "kwilson", "danderson", "nthomas", "ktaylor", "bmoore", "jjackson", "smartin",
        "tlee", "mperez", "cthompson", "lwhite", "rharris", "psanchez", "mclark",
        "dramirez", "plewis", "crobinson", "swalker", "byoung", "eallen", "hking",
        "jwright", "dscott", "agreen", "sbaker", "radams", "knelson", "bcarter",
        "mmitchell", "gperez", "eroberts", "jturner", "dphillips", "kcampbell",
        "lparker", "tevans", "redwards"
    ]
    
    User.objects.filter(username__in=usernames).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_persons, reverse_func),
    ]