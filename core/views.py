from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import InquiryForm
from urllib.parse import quote

def home(request):
    form = InquiryForm()
    return render(request, 'home.html', {'form': form})

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact_page(request):
    form = InquiryForm()
    return render(request, 'contact.html', {'form': form})

def contact_submit(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # Get cleaned data without saving to DB
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            phone = data.get('phone')
            service = data.get('service')
            booking_date = data.get('booking_date').strftime('%B %d, %Y') if data.get('booking_date') else 'Not specified'
            message = data.get('message') or 'No message provided'
            
            # Determine submission type (default to both)
            submit_type = request.POST.get('submit_type', 'both')
            
            # Format message for Email and WhatsApp
            email_body = (
                f"New Inquiry from GSS CAR Makeovers\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Service: {service}\n"
                f"Preferred Date: {booking_date}\n"
                f"Message: {message}"
            )
            
            # Send Email
            try:
                send_mail(
                    subject=f"New Inquiry: {service} - {name}",
                    message=email_body,
                    from_email='gsscarmakeovers@gmail.com',
                    recipient_list=['gsscarmakeovers@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                pass

            # Construct WhatsApp URL
            whatsapp_number = "919962511881"
            whatsapp_body = (
                f"*New Inquiry from GSS CAR Makeovers*\n\n"
                f"*Name:* {name}\n"
                f"*Email:* {email}\n"
                f"*Phone:* {phone}\n"
                f"*Service:* {service}\n"
                f"*Date:* {booking_date}\n"
                f"*Message:* {message}"
            )
            whatsapp_url = f"https://wa.me/{whatsapp_number}?text={quote(whatsapp_body)}"
            
            return JsonResponse({
                'status': 'success', 
                'message': 'Your inquiry has been sent successfully!',
                'whatsapp_url': whatsapp_url,
                'submit_type': submit_type
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return redirect('home')
