from flask import Flask, render_template_string, request

app = Flask(__name__)

# Yahan form submissions ko temporarily store karenge ek list me (server memory me)
submissions = []

template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0; padding: 20px;
        }
        .container {
            max-width: 500px;
            background: white;
            margin: auto;
            padding: 25px 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin: 15px 0 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            resize: vertical;
        }
        button {
            margin-top: 20px;
            width: 100%;
            padding: 10px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
        .message {
            margin-top: 20px;
            background: #d4edda;
            border: 1px solid #c3e6cb;
            padding: 10px;
            border-radius: 6px;
            color: #155724;
        }
        .submissions {
            margin-top: 40px;
        }
        .submission-item {
            background: #f8f9fa;
            border: 1px solid #ddd;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 6px;
        }
        .submission-item strong {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Contact Us</h2>
        <form method="POST" action="/">
            <label for="name">Name:</label>
            <input type="text" name="name" id="name" required>

            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required>

            <label for="message">Message:</label>
            <textarea name="message" id="message" rows="4" required></textarea>

            <button type="submit">Submit</button>
        </form>

        {% if success %}
        <div class="message">Thanks for contacting us, {{ submitted_name }}! We received your message.</div>
        {% endif %}

        {% if submissions %}
        <div class="submissions">
            <h3>All Submissions (Visible only here)</h3>
            {% for s in submissions %}
            <div class="submission-item">
                <strong>Name:</strong> {{ s.name }}<br>
                <strong>Email:</strong> {{ s.email }}<br>
                <strong>Message:</strong> {{ s.message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def contact():
    success = False
    submitted_name = ""
    if request.method == 'POST':
        # Form data ko read karo
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Data ko list me store karo (server memory me)
        submissions.append({
            'name': name,
            'email': email,
            'message': message
        })

        success = True
        submitted_name = name

    return render_template_string(template, success=success, submitted_name=submitted_name, submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
