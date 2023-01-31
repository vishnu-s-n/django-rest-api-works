# from django.core.mail import send_mail
# import random
# from django.conf import settings
# from account.models import accountUserModel,accountUserLoginOtpModel
#
# def send_otp_email(email):
#     subject="Your Acoount Varification OTP"
#     otp=random.randint(1000,9999)
#     message=f"Your otp is {otp}"
#     email_from=settings.EMAIL_HOST
#     send_mail (subject,message,email_from,[email])
#     user=accountUserModel.objects.get(email=email)
#     user=accountUserLoginOtpModel.objects.create(otp=otp,owner=user,active=True)
#     user_obj=accountUserModel.objects.get(email=email)
#     user_obj.otp=otp
#     user_obj.save()
#
#
# # send_mail(
#     #     "Your OTP is",
#     #     f"Your otp will generated",
#     #     "ivishnu.ms@gmail.com",
#     #     ["techievs16@gmail.com"]
#     # )