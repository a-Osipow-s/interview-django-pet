from django.db import migrations
import random


def create_articles(apps, schema_editor):
    Article = apps.get_model('article', 'Article')
    ArticleAdditionalInformation = apps.get_model('article', 'ArticleAdditionalInformation')
    ArticleTag = apps.get_model('article', 'ArticleTag')
    Person = apps.get_model('person', 'Person')
    
    persons = list(Person.objects.all())
    tags = list(ArticleTag.objects.all())
    
    if not persons:
        print("No persons found. Skipping article creation.")
        return
    
    articles_data = [
        {
            "title": "Getting Started with Python for Data Science",
            "description": "Learn the fundamentals of Python programming tailored for data science applications. Covers NumPy, Pandas, and basic data manipulation techniques.",
            "full_description": "This comprehensive guide walks you through Python basics specifically designed for aspiring data scientists. We cover essential libraries like NumPy for numerical computing, Pandas for data manipulation, and Matplotlib for visualization. Perfect for beginners.",
            "is_approved": True,
            "tag_names": ["Python", "Data Science", "Tutorial"]
        },
        {
            "title": "Building RESTful APIs with Django REST Framework",
            "description": "A complete tutorial on creating robust REST APIs using Django REST Framework. Includes authentication, serialization, and best practices.",
            "full_description": "Dive deep into Django REST Framework to build professional-grade APIs. Learn about viewsets, serializers, authentication methods, permissions, and how to structure your API endpoints for scalability and maintainability.",
            "is_approved": True,
            "tag_names": ["Python", "API Development", "Web Development"]
        },
        {
            "title": "Modern JavaScript: ES6+ Features Explained",
            "description": "Explore the latest JavaScript features including arrow functions, destructuring, promises, and async/await patterns.",
            "full_description": "Master modern JavaScript with this detailed guide covering ES6 and beyond. Learn arrow functions, template literals, destructuring, spread operators, promises, async/await, and modules. Includes practical examples for each feature.",
            "is_approved": True,
            "tag_names": ["JavaScript", "Web Development", "Tutorial"]
        },
        {
            "title": "Introduction to Machine Learning with TensorFlow",
            "description": "Start your ML journey with TensorFlow. Covers neural networks, training models, and making predictions with real-world datasets.",
            "full_description": "Get hands-on with machine learning using TensorFlow. This tutorial covers building your first neural network, understanding layers, activation functions, loss functions, and optimizers. Includes practical examples with image classification.",
            "is_approved": True,
            "tag_names": ["Machine Learning", "Python", "Tutorial"]
        },
        {
            "title": "Docker Containerization for Beginners",
            "description": "Learn how to containerize your applications with Docker. Covers Dockerfile creation, image management, and container orchestration basics.",
            "full_description": "Master Docker containerization with this beginner-friendly guide. Learn to create Dockerfiles, build images, manage containers, work with volumes, and understand networking. Perfect for developers transitioning to containerized workflows.",
            "is_approved": False,
            "tag_names": ["DevOps", "Cloud Computing", "Tutorial"]
        },
        {
            "title": "Responsive Web Design with CSS Grid and Flexbox",
            "description": "Create modern, responsive layouts using CSS Grid and Flexbox. Includes practical examples and design patterns.",
            "full_description": "Build beautiful responsive websites with CSS Grid and Flexbox. Learn when to use each layout system, how to create complex layouts, and best practices for mobile-first design. Includes real-world examples and code snippets.",
            "is_approved": True,
            "tag_names": ["Web Development", "UI/UX Design", "Tutorial"]
        },
        {
            "title": "SQL Query Optimization Techniques",
            "description": "Improve database performance with advanced SQL optimization strategies. Covers indexing, query planning, and performance tuning.",
            "full_description": "Optimize your SQL queries for better performance. Learn about indexes, query execution plans, joins optimization, subquery alternatives, and caching strategies. Includes PostgreSQL and MySQL specific tips.",
            "is_approved": True,
            "tag_names": ["Database", "Performance", "Tutorial"]
        },
        {
            "title": "Building Mobile Apps with React Native",
            "description": "Cross-platform mobile development using React Native. Learn to build iOS and Android apps with a single codebase.",
            "full_description": "Create native mobile applications using React Native. This guide covers setup, components, navigation, state management with Redux, API integration, and publishing to app stores. Build once, deploy everywhere.",
            "is_approved": True,
            "tag_names": ["Mobile Development", "JavaScript", "Tutorial"]
        },
        {
            "title": "Understanding Blockchain Technology",
            "description": "Demystify blockchain concepts including distributed ledgers, consensus mechanisms, and smart contracts.",
            "full_description": "Explore blockchain technology from the ground up. Learn about blocks, chains, mining, proof of work, proof of stake, smart contracts, and decentralized applications. Includes Ethereum examples and Solidity basics.",
            "is_approved": False,
            "tag_names": ["Blockchain", "Tutorial"]
        },
        {
            "title": "Cybersecurity Best Practices for Developers",
            "description": "Essential security principles every developer should know. Covers OWASP Top 10, secure coding, and vulnerability prevention.",
            "full_description": "Protect your applications with these cybersecurity best practices. Learn about SQL injection, XSS, CSRF, authentication, authorization, encryption, and secure API design. Includes code examples and testing strategies.",
            "is_approved": True,
            "tag_names": ["Cybersecurity", "Web Development", "Tutorial"]
        },
        {
            "title": "AWS Cloud Architecture Patterns",
            "description": "Design scalable cloud solutions on AWS. Explore common architecture patterns for high availability and fault tolerance.",
            "full_description": "Master AWS architecture with proven design patterns. Learn about EC2, S3, RDS, Lambda, load balancing, auto-scaling, and disaster recovery. Build resilient, cost-effective cloud solutions.",
            "is_approved": True,
            "tag_names": ["Cloud Computing", "Architecture", "DevOps"]
        },
        {
            "title": "Test-Driven Development with Python",
            "description": "Adopt TDD methodology to write better code. Learn pytest, mocking, and test automation strategies.",
            "full_description": "Embrace test-driven development with Python. This guide covers writing tests first, using pytest, mocking dependencies, test fixtures, parametrized tests, and continuous integration. Improve code quality through testing.",
            "is_approved": True,
            "tag_names": ["Python", "Testing", "Tutorial"]
        },
        {
            "title": "GraphQL vs REST: Choosing the Right API",
            "description": "Compare GraphQL and REST APIs. Understand when to use each approach and migration strategies.",
            "full_description": "Evaluate GraphQL and REST for your next project. Learn the strengths and weaknesses of each, query complexity, over-fetching, under-fetching, tooling, and real-world use cases. Make informed architectural decisions.",
            "is_approved": False,
            "tag_names": ["API Development", "Architecture", "Web Development"]
        },
        {
            "title": "Agile Scrum: A Practical Guide",
            "description": "Implement Scrum methodology effectively. Covers sprints, ceremonies, roles, and common pitfalls to avoid.",
            "full_description": "Master Agile Scrum with this practical guide. Learn about sprints, daily standups, sprint planning, retrospectives, product backlog management, and velocity tracking. Includes real team experiences and tips.",
            "is_approved": True,
            "tag_names": ["Agile", "Career", "Tutorial"]
        },
        {
            "title": "Microservices Architecture with Node.js",
            "description": "Design and implement microservices using Node.js. Covers service communication, data management, and deployment.",
            "full_description": "Build scalable microservices with Node.js. Learn service decomposition, inter-service communication, event-driven architecture, API gateways, service discovery, and containerized deployment with Docker and Kubernetes.",
            "is_approved": True,
            "tag_names": ["JavaScript", "Architecture", "Cloud Computing"]
        },
        {
            "title": "Data Visualization with D3.js",
            "description": "Create interactive data visualizations using D3.js. Learn to build charts, graphs, and custom visual representations.",
            "full_description": "Master data visualization with D3.js. This tutorial covers selections, data binding, scales, axes, transitions, and building interactive charts. Create stunning visualizations for web applications.",
            "is_approved": True,
            "tag_names": ["JavaScript", "Data Science", "Web Development"]
        },
        {
            "title": "iOS App Development with Swift",
            "description": "Build native iOS applications using Swift. Covers UIKit, SwiftUI, and App Store deployment.",
            "full_description": "Develop professional iOS apps with Swift. Learn Swift syntax, UIKit fundamentals, SwiftUI declarative UI, Core Data, networking, push notifications, and publishing to the App Store. Includes practical projects.",
            "is_approved": False,
            "tag_names": ["Mobile Development", "Tutorial"]
        },
        {
            "title": "Kubernetes for Container Orchestration",
            "description": "Deploy and manage containerized applications with Kubernetes. Covers pods, services, deployments, and scaling.",
            "full_description": "Master Kubernetes for production deployments. Learn about pods, services, deployments, ConfigMaps, secrets, persistent volumes, ingress controllers, and monitoring. Scale applications with confidence.",
            "is_approved": True,
            "tag_names": ["DevOps", "Cloud Computing", "Tutorial"]
        },
        {
            "title": "UI Design Principles for Developers",
            "description": "Essential design principles for creating user-friendly interfaces. Covers color theory, typography, and layout.",
            "full_description": "Enhance your UI skills with fundamental design principles. Learn about color theory, typography, spacing, visual hierarchy, consistency, and accessibility. Create interfaces that users love.",
            "is_approved": True,
            "tag_names": ["UI/UX Design", "Web Development", "Tutorial"]
        },
        {
            "title": "Contributing to Open Source Projects",
            "description": "Start your open source journey. Learn how to find projects, make contributions, and collaborate with communities.",
            "full_description": "Begin contributing to open source software. This guide covers finding suitable projects, understanding contribution guidelines, making pull requests, code reviews, and building your reputation in the community.",
            "is_approved": True,
            "tag_names": ["Open Source", "Career", "Tutorial"]
        },
        {
            "title": "NoSQL Databases: MongoDB Deep Dive",
            "description": "Master MongoDB for modern applications. Covers document modeling, aggregation, and performance optimization.",
            "full_description": "Explore MongoDB in depth. Learn document-oriented data modeling, CRUD operations, aggregation pipelines, indexing strategies, sharding, replication, and best practices for production deployments.",
            "is_approved": True,
            "tag_names": ["Database", "Tutorial"]
        },
        {
            "title": "CI/CD Pipelines with GitHub Actions",
            "description": "Automate your development workflow with GitHub Actions. Build, test, and deploy applications automatically.",
            "full_description": "Implement continuous integration and deployment with GitHub Actions. Learn workflow syntax, triggers, jobs, actions marketplace, secrets management, and deploying to various platforms including AWS and Azure.",
            "is_approved": False,
            "tag_names": ["DevOps", "Testing", "Tutorial"]
        },
        {
            "title": "Web Performance Optimization Strategies",
            "description": "Speed up your websites with proven optimization techniques. Covers caching, lazy loading, and resource optimization.",
            "full_description": "Boost web performance with these optimization strategies. Learn about critical rendering path, code splitting, lazy loading, image optimization, caching strategies, CDNs, and performance monitoring tools.",
            "is_approved": True,
            "tag_names": ["Performance", "Web Development", "Tutorial"]
        },
        {
            "title": "Ethical Hacking: Penetration Testing Basics",
            "description": "Introduction to ethical hacking and penetration testing. Learn to identify and fix security vulnerabilities.",
            "full_description": "Start your ethical hacking journey. Learn reconnaissance, scanning, enumeration, exploitation, and reporting. Understand common vulnerabilities and how to test for them responsibly with proper authorization.",
            "is_approved": True,
            "tag_names": ["Cybersecurity", "Tutorial"]
        },
        {
            "title": "Software Design Patterns in Practice",
            "description": "Apply classic design patterns to solve common software problems. Covers creational, structural, and behavioral patterns.",
            "full_description": "Master software design patterns with practical examples. Learn singleton, factory, observer, strategy, decorator, and more. Understand when and how to apply each pattern for maintainable code.",
            "is_approved": True,
            "tag_names": ["Architecture", "Tutorial"]
        },
        {
            "title": "Natural Language Processing with spaCy",
            "description": "Process and analyze text data using spaCy. Covers tokenization, named entity recognition, and text classification.",
            "full_description": "Explore NLP with spaCy library. Learn tokenization, part-of-speech tagging, dependency parsing, named entity recognition, and training custom models. Build intelligent text processing applications.",
            "is_approved": False,
            "tag_names": ["Machine Learning", "Python", "Data Science"]
        },
        {
            "title": "Career Growth: From Junior to Senior Developer",
            "description": "Navigate your software engineering career path. Practical advice on skills, mentorship, and advancement strategies.",
            "full_description": "Accelerate your career growth with proven strategies. Learn technical skills to master, soft skills that matter, how to find mentors, leading projects, and positioning yourself for senior roles.",
            "is_approved": True,
            "tag_names": ["Career", "Tutorial"]
        },
        {
            "title": "Flutter Cross-Platform Development",
            "description": "Build beautiful mobile apps with Flutter. Create apps for iOS, Android, and web from a single codebase.",
            "full_description": "Master Flutter for cross-platform development. Learn Dart programming, widgets, state management, navigation, animations, platform integration, and deploying to multiple platforms simultaneously.",
            "is_approved": True,
            "tag_names": ["Mobile Development", "Tutorial"]
        },
        {
            "title": "Redis Caching Strategies for Scalability",
            "description": "Improve application performance with Redis. Learn caching patterns, data structures, and real-time features.",
            "full_description": "Optimize your applications with Redis. Explore caching strategies, data structures like strings, hashes, sets, sorted sets, pub/sub messaging, and using Redis for sessions, queues, and leaderboards.",
            "is_approved": True,
            "tag_names": ["Database", "Performance", "Tutorial"]
        },
        {
            "title": "Serverless Applications with AWS Lambda",
            "description": "Build scalable serverless applications. Learn Lambda functions, event-driven architecture, and cost optimization.",
            "full_description": "Go serverless with AWS Lambda. Learn function creation, triggers, API Gateway integration, DynamoDB connections, monitoring with CloudWatch, and building cost-effective, auto-scaling applications.",
            "is_approved": True,
            "tag_names": ["Cloud Computing", "Architecture", "DevOps"]
        },
    ]
    
    created_count = 0
    
    for article_data in articles_data:
        additional_info = ArticleAdditionalInformation.objects.create(
            full_description=article_data['full_description'],
            is_approved_by_admin=article_data['is_approved']
        )
        
        author = random.choice(persons)
        
        article = Article.objects.create(
            title=article_data['title'],
            description=article_data['description'],
            author=author,
            additional_info=additional_info
        )
        
        if tags:
            article_tags = []
            for tag_name in article_data['tag_names']:
                try:
                    tag = ArticleTag.objects.get(name=tag_name)
                    article_tags.append(tag)
                except ArticleTag.DoesNotExist:
                    pass
            
            if article_tags:
                article.tags.set(article_tags)
        
        created_count += 1
    
    print(f"Successfully created {created_count} articles with additional information.")


def reverse_func(apps, schema_editor):
    Article = apps.get_model('article', 'Article')
    ArticleAdditionalInformation = apps.get_model('article', 'ArticleAdditionalInformation')
    
    article_ids = list(Article.objects.values_list('additional_info_id', flat=True))
    
    Article.objects.all().delete()
    
    ArticleAdditionalInformation.objects.filter(id__in=article_ids).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_tags'),
    ]

    operations = [
        migrations.RunPython(create_articles, reverse_func),
    ]