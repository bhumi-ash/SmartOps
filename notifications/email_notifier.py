def send_email(result):

    try:

        msg = EmailMessage()

        msg["Subject"] = "SmartOps Alert"

        msg["From"] = EMAIL_ADDRESS

        msg["To"] = EMAIL_ADDRESS

        msg.set_content(
            f"""
SmartOps Recovery Notification

Container : {result['container']}

Action    : {result['action']}

Status    : {"Success" if result["success"] else "Failed"}

Message   : {result['message']}
"""
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

            smtp.starttls()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)

        return True

    except Exception as e:

        print(f"Email notification failed: {e}")

        return False