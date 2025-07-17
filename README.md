
# 🤖 Instagram Account Miner

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Windows/Linux](https://img.shields.io/badge/Windows-CLI-lightgrey)

A fun and powerful tool to **automate Instagram account creation** using Selenium.  
Built just for learning and experimentation — **not for abuse**.

---

## ✨ Features

- 🔄 Auto-fills Instagram signup form
- 📧 Uses your emails or phone numbers for verification
- 📝 Logs created accounts in `data/output.txt`
- 🌈 Colorful terminal + cool ASCII animations
- 🧠 Handles reCAPTCHA and manual confirmation steps
- 💻 Works on both **Windows** and **Linux**

---

## ⚠️ Disclaimer

> This tool is made for **educational and ethical** purposes only.  
> Misusing it may violate Instagram's [Terms of Service](https://help.instagram.com/581066165581870).  
> **You are responsible for how you use it.**

---

## 📁 Project Structure

```
├── config/
│   ├── chromedriver          # ChromeDriver for Linux
│   ├── chromedriver.exe      # ChromeDriver for Windows
│   ├── config.py             # Configs, imports, helpers
│   └── __init__.py
├── data/
│   ├── .numb.txt             # Username number counter
│   ├── .save_file.txt        # Account ID counter
│   └── output.txt            # Created account logs
├── main.py                   # Main script to run the program
└── requirment.txt            # Python dependencies
```

---

## ⚙️ Requirements

- Python 3.11 (recommended)
- Selenium 4.10.0
- Google Chrome browser
- Matching version of ChromeDriver

Install packages:

```bash
pip install -r requirment.txt
```

---

## 🚀 How to Use

1. Put the right `chromedriver` file in the `config/` folder.
2. Run the main script:

```bash
python main.py
```

3. Enter 3 emails or phone numbers (used for verification).
4. Choose how many accounts to create.
5. Manually:
   - Solve the reCAPTCHA
   - Enter the confirmation code
6. You're done! 🎉 Accounts will be saved in `data/output.txt`.

---

## versions : 
<br>
<a href = "https://github.com/Amirhosin282/account_miner/releases"> all versins<a> 

## 🧾 Output Example

```
id         username                password          E-mail             date and time 
1          user123                Aa@123456         test@mail.com      2025-07-17 -- 10:15:30
```

![Version Timeline](https://capsule-render.vercel.app/api?type=rect&color=gradient&height=5&section=footer)

#  ماینر حساب اینستاگرام

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Windows/Linux](https://img.shields.io/badge/Windows-CLI-lightgrey)

یه ابزار جالب و خودکار برای ساخت چندتا حساب اینستاگرامی 😎  
این ابزار برای **یادگیری و آزمایش شخصی** ساخته شده. لطفاً ازش **سوءاستفاده نکن!**

---

## ✨ قابلیت‌ها

- ✍️ پر کردن خودکار فرم ثبت‌نام اینستاگرام
- 📲 استفاده از ایمیل یا شماره‌هایی که وارد می‌کنی
- 🗂 ذخیره مشخصات حساب‌ها در `data/output.txt`
- 🎨 ترمینال رنگی + بنرهای جذاب ASCII
- 🧩 قابلیت عبور دستی از reCAPTCHA و وارد کردن کد تأیید
- 💻 اجرا روی ویندوز و لینوکس

---

## ⚠️ هشدار

> این ابزار فقط برای **آموزش و تست شخصی** طراحی شده.  
> استفاده‌ی نادرست ازش ممکنه خلاف [قوانین استفاده از اینستاگرام](https://help.instagram.com/581066165581870) باشه.  
> **مسئولیت استفاده با خودته.**

---

## 📁 ساختار پروژه

```
├── config/
│   ├── chromedriver          # درایور برای لینوکس
│   ├── chromedriver.exe      # درایور برای ویندوز
│   ├── config.py             # تنظیمات و توابع اصلی
│   └── __init__.py
├── data/
│   ├── .numb.txt             # شمارنده نام کاربری
│   ├── .save_file.txt        # شمارنده آیدی
│   └── output.txt            # خروجی حساب‌ها
├── main.py                   # فایل اصلی اجرای برنامه
└── requirment.txt            # کتابخونه‌های پایتون
```

---

## ⚙️ پیش‌نیازها

- پایتون 3.11 (پیشنهاد میشه)
- Selenium نسخه 4.10.0
- مرورگر Google Chrome
- ChromeDriver متناسب با مرورگرت

نصب کتابخونه‌ها:

```bash
pip install -r requirment.txt
```

---

## 🚀 روش استفاده

1. درایور مناسب سیستم‌عاملتو بذار تو پوشه `config/`
2. اجرای اسکریپت:

```bash
python main.py
```

3. سه ایمیل یا شماره تلفن وارد کن (برای تأیید حساب‌ها)
4. تعداد حساب‌هایی که می‌خوای بسازی رو وارد کن
5. دستی:
   - reCAPTCHA رو حل کن
   - کد تأیید رو وارد کن
6. تمام! 🎉 اطلاعات حساب‌ها توی `data/output.txt` ذخیره می‌شه

---

## 🧾 نمونه خروجی

```
id         username                password          E-mail             date and time 
1          user123                Aa@123456         test@mail.com      2025-07-17 -- 10:15:30
```

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=80&section=footer&fontSize=30)
