
# 🤖 Instagram Account Miner

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Windows/Linux](https://img.shields.io/badge/Windows-CLI-lightgrey)
<a href = "https://github.com/Amirhosin282/account_miner/blob/main/LICENSE.md"> <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"> </a>

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
│   └── **init**.py
├── data/
│   ├── .numb.txt             # Username number counter
│   ├── .save\_file.txt        # Account ID counter
│   └── output.txt            # Created account logs
├── main.py                   # Main script to run the program
└── requirements.txt          # Python dependencies

````

---

## ⚙️ Requirements

- Python 3.11 (recommended)
- Selenium 4.10.0
- Google Chrome browser
- Matching version of ChromeDriver (automatically selected based on your OS)

Install packages:

```bash
pip install -r requirements.txt
````

---

## 🚀 How to Use

1. Run the main script:

```bash
python main.py
```

2. Enter 3 emails or phone numbers (used for verification)
3. Choose how many accounts to create
4. Manually:

   * Solve the reCAPTCHA (see note below)
   * Enter the confirmation code
5. You're done! 🎉 Accounts will be saved in `data/output.txt`

> 🔒 **Note on reCAPTCHA:**
> Instagram uses Google’s reCAPTCHA to prevent automated signups.
> This tool **does not bypass** it automatically.
> You must **manually solve the CAPTCHA and input the verification code** during each signup — this is intentional for legal and ethical reasons.

> 🌍 **Important Note:**
> To avoid errors or incomplete signups, **you must change your IP address to Switzerland** using VPN or proxy tools.
> This is due to regional differences in how Instagram handles account creation.

---

## 🔖 All Versions

➡️ [See All Releases](https://github.com/Amirhosin282/account_miner/releases)

---

## 🧾 Output Example

```
id         username                password          E-mail             date and time 
1          user123                Aa@123456         test@mail.com      2025-07-17 -- 10:15:30
```

![Version Timeline](https://capsule-render.vercel.app/api?type=rect\&color=gradient\&height=5\&section=footer)

---

#  ماینر حساب اینستاگرام

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-orange)
![Windows/Linux](https://img.shields.io/badge/Windows-CLI-lightgrey)
<a href = "https://github.com/Amirhosin282/account_miner/blob/main/LICENSE.md"> <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"> </a>

ابزاری کاربردی برای **ساخت خودکار حساب اینستاگرام** با استفاده از Selenium 🚀
ساخته شده صرفاً برای یادگیری و آزمایش — لطفاً از آن **سوءاستفاده نکنید.**

---

## ✨ قابلیت‌ها

* ✍️ پر کردن خودکار فرم ثبت‌نام اینستاگرام
* 📲 استفاده از ایمیل یا شماره تلفن جهت تأیید
* 🗂 ذخیره اطلاعات حساب‌ها در فایل `data/output.txt`
* 🎨 ترمینال رنگی با انیمیشن‌های جالب ASCII
* 🧩 انجام مراحل کپچا و تأیید دستی
* 💻 قابل اجرا روی ویندوز و لینوکس

---

## ⚠️ هشدار

> این ابزار فقط برای اهداف **آموزشی و اخلاقی** توسعه داده شده است.
> استفاده‌ی نادرست ممکن است خلاف [قوانین اینستاگرام](https://help.instagram.com/581066165581870) باشد.
> **مسئولیت استفاده از آن با شماست.**

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
└── requirements.txt          # کتابخانه‌های پایتون
```

---

## ⚙️ پیش‌نیازها

* پایتون 3.11 (پیشنهادی)
* Selenium نسخه 4.10.0
* مرورگر Google Chrome
* ChromeDriver متناسب با مرورگر (انتخاب خودکار بر اساس سیستم‌عامل)

نصب کتابخانه‌ها:

```bash
pip install -r requirements.txt
```

---

## 🚀 روش استفاده

1. اسکریپت اصلی را اجرا کنید:

```bash
python main.py
```

2. سه ایمیل یا شماره تلفن وارد کنید (برای تأیید حساب‌ها)
3. تعداد حساب‌هایی که می‌خواهید ایجاد شوند را مشخص کنید
4. به‌صورت دستی:

   * کپچا (reCAPTCHA) را حل کنید (توضیحات پایین را ببینید)
   * کد تأیید را وارد کنید
5. تمام! 🎉 اطلاعات حساب‌ها در فایل `data/output.txt` ذخیره می‌شوند

> 🔒 **درباره کپچا (reCAPTCHA):**
> اینستاگرام از کپچای گوگل برای جلوگیری از ربات‌ها استفاده می‌کند.
> این ابزار هیچ تلاشی برای عبور خودکار از کپچا ندارد.
> لازم است شما **به‌صورت دستی کپچا را حل کرده و کد تأیید را وارد کنید.**
> این محدودیت برای رعایت اصول اخلاقی و قوانین پلتفرم‌هاست.

> 🌍 **نکته مهم:**
> برای عملکرد صحیح و بدون خطا، **آی‌پی خود را به کشور سوئیس تغییر دهید** (با استفاده از VPN یا ابزارهای مشابه).
> به‌دلیل تفاوت در روند ثبت‌نام در کشورهای مختلف، ممکن است در برخی کشورها با خطا روبه‌رو شوید.

---

## 🔖 نسخه‌ها

➡️ [مشاهده تمام نسخه‌ها](https://github.com/Amirhosin282/account_miner/releases)

---

## 🧾 نمونه خروجی

```
id         username                password          E-mail             date and time 
1          user123                Aa@123456         test@mail.com      2025-07-17 -- 10:15:30
```

![Footer](https://capsule-render.vercel.app/api?type=waving\&color=gradient\&height=80\&section=footer\&fontSize=30)
