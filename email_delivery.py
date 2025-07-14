#!/usr/bin/env python3
# Email Delivery System for Tarot and Palm Readings

import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

class EmailDeliverySystem:
    def __init__(self, smtp_server="smtp.example.com", smtp_port=587, 
                 sender_email="readings@wildflowerstarot.com", 
                 sender_password="your_password_here"):
        """Initialize the email delivery system with SMTP settings."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_tarot_reading_email(self, recipient_email, recipient_name, order_id, pdf_path, spread_type):
        """
        Send a tarot reading email with PDF attachment.
        
        Args:
            recipient_email (str): Customer's email address
            recipient_name (str): Customer's name
            order_id (str): Unique order identifier
            pdf_path (str): Path to the generated PDF file
            spread_type (str): Type of tarot spread
        
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        subject = f"Your {spread_type} Tarot Reading from Wildflowers Tarot"
        
        # Email body in HTML format
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .logo {{ font-family: 'Georgia', serif; font-size: 24px; color: #6b4e71; margin: 0; }}
                .content {{ margin: 20px 0; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #666; text-align: center; }}
                .button {{ display: inline-block; background-color: #6b4e71; color: white; padding: 10px 20px; 
                          text-decoration: none; border-radius: 5px; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 class="logo">Wildflowers Tarot</h1>
                    <p>Spiritual guidance for life's journey</p>
                </div>
                
                <div class="content">
                    <p>Dear {recipient_name},</p>
                    
                    <p>Thank you for choosing Wildflowers Tarot for your {spread_type} reading. Your personalized reading is now ready and attached to this email as a PDF document.</p>
                    
                    <p>In this reading, we've interpreted the cards you selected to provide guidance and insight into your question or situation. We hope you find the reading illuminating and helpful on your journey.</p>
                    
                    <p>To view your reading:</p>
                    <ol>
                        <li>Open the attached PDF file</li>
                        <li>If prompted for a password, use your order number: <strong>{order_id}</strong></li>
                    </ol>
                    
                    <p>If you have any questions about your reading or would like to book a follow-up session, please don't hesitate to contact us.</p>
                    
                    <p>Wishing you clarity and guidance,</p>
                    <p>The Wildflowers Tarot Team</p>
                    
                    <a href="https://www.wildflowerstarot.com/account" class="button">View Your Account</a>
                </div>
                
                <div class="footer">
                    <p>© {datetime.now().year} Wildflowers Tarot. All rights reserved.</p>
                    <p>This email was sent to {recipient_email} regarding order #{order_id}.</p>
                    <p><a href="https://www.wildflowerstarot.com">www.wildflowerstarot.com</a> | <a href="mailto:info@wildflowerstarot.com">info@wildflowerstarot.com</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Plain text alternative
        text_body = f"""
        Dear {recipient_name},
        
        Thank you for choosing Wildflowers Tarot for your {spread_type} reading. Your personalized reading is now ready and attached to this email as a PDF document.
        
        In this reading, we've interpreted the cards you selected to provide guidance and insight into your question or situation. We hope you find the reading illuminating and helpful on your journey.
        
        To view your reading:
        1. Open the attached PDF file
        2. If prompted for a password, use your order number: {order_id}
        
        If you have any questions about your reading or would like to book a follow-up session, please don't hesitate to contact us.
        
        Wishing you clarity and guidance,
        The Wildflowers Tarot Team
        
        Visit your account: https://www.wildflowerstarot.com/account
        
        © {datetime.now().year} Wildflowers Tarot. All rights reserved.
        This email was sent to {recipient_email} regarding order #{order_id}.
        www.wildflowerstarot.com | info@wildflowerstarot.com
        """
        
        return self._send_email(recipient_email, subject, text_body, html_body, pdf_path)
    
    def send_palm_reading_email(self, recipient_email, recipient_name, order_id, pdf_path):
        """
        Send a palm reading email with PDF attachment.
        
        Args:
            recipient_email (str): Customer's email address
            recipient_name (str): Customer's name
            order_id (str): Unique order identifier
            pdf_path (str): Path to the generated PDF file
        
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        subject = "Your Palm Reading from Wildflowers Tarot"
        
        # Email body in HTML format
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .logo {{ font-family: 'Georgia', serif; font-size: 24px; color: #6b4e71; margin: 0; }}
                .content {{ margin: 20px 0; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #666; text-align: center; }}
                .button {{ display: inline-block; background-color: #6b4e71; color: white; padding: 10px 20px; 
                          text-decoration: none; border-radius: 5px; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 class="logo">Wildflowers Tarot</h1>
                    <p>Spiritual guidance for life's journey</p>
                </div>
                
                <div class="content">
                    <p>Dear {recipient_name},</p>
                    
                    <p>Thank you for choosing Wildflowers Tarot for your palm reading. Your personalized reading is now ready and attached to this email as a PDF document.</p>
                    
                    <p>In this reading, we've analyzed the unique lines and features of your palms to provide insights into your life path, personality traits, and potential future. We hope you find the reading illuminating and helpful on your journey.</p>
                    
                    <p>To view your reading:</p>
                    <ol>
                        <li>Open the attached PDF file</li>
                        <li>If prompted for a password, use your order number: <strong>{order_id}</strong></li>
                    </ol>
                    
                    <p>If you have any questions about your reading or would like to book a follow-up session, please don't hesitate to contact us.</p>
                    
                    <p>Wishing you clarity and guidance,</p>
                    <p>The Wildflowers Tarot Team</p>
                    
                    <a href="https://www.wildflowerstarot.com/account" class="button">View Your Account</a>
                </div>
                
                <div class="footer">
                    <p>© {datetime.now().year} Wildflowers Tarot. All rights reserved.</p>
                    <p>This email was sent to {recipient_email} regarding order #{order_id}.</p>
                    <p><a href="https://www.wildflowerstarot.com">www.wildflowerstarot.com</a> | <a href="mailto:info@wildflowerstarot.com">info@wildflowerstarot.com</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Plain text alternative
        text_body = f"""
        Dear {recipient_name},
        
        Thank you for choosing Wildflowers Tarot for your palm reading. Your personalized reading is now ready and attached to this email as a PDF document.
        
        In this reading, we've analyzed the unique lines and features of your palms to provide insights into your life path, personality traits, and potential future. We hope you find the reading illuminating and helpful on your journey.
        
        To view your reading:
        1. Open the attached PDF file
        2. If prompted for a password, use your order number: {order_id}
        
        If you have any questions about your reading or would like to book a follow-up session, please don't hesitate to contact us.
        
        Wishing you clarity and guidance,
        The Wildflowers Tarot Team
        
        Visit your account: https://www.wildflowerstarot.com/account
        
        © {datetime.now().year} Wildflowers Tarot. All rights reserved.
        This email was sent to {recipient_email} regarding order #{order_id}.
        www.wildflowerstarot.com | info@wildflowerstarot.com
        """
        
        return self._send_email(recipient_email, subject, text_body, html_body, pdf_path)
    
    def send_order_confirmation_email(self, recipient_email, recipient_name, order_id, order_type, price):
        """
        Send an order confirmation email.
        
        Args:
            recipient_email (str): Customer's email address
            recipient_name (str): Customer's name
            order_id (str): Unique order identifier
            order_type (str): Type of order (tarot or palm reading)
            price (float): Order price
        
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        subject = f"Order Confirmation - Wildflowers Tarot #{order_id}"
        
        # Email body in HTML format
        html_body = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Arial', sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ text-align: center; margin-bottom: 30px; }}
                .logo {{ font-family: 'Georgia', serif; font-size: 24px; color: #6b4e71; margin: 0; }}
                .content {{ margin: 20px 0; }}
                .order-details {{ background-color: #f5f0f6; padding: 15px; border-radius: 5px; margin: 20px 0; }}
                .footer {{ margin-top: 40px; font-size: 12px; color: #666; text-align: center; }}
                .button {{ display: inline-block; background-color: #6b4e71; color: white; padding: 10px 20px; 
                          text-decoration: none; border-radius: 5px; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 class="logo">Wildflowers Tarot</h1>
                    <p>Spiritual guidance for life's journey</p>
                </div>
                
                <div class="content">
                    <p>Dear {recipient_name},</p>
                    
                    <p>Thank you for your order with Wildflowers Tarot. We're delighted to confirm that your order has been received and is being processed.</p>
                    
                    <div class="order-details">
                        <h3>Order Details</h3>
                        <p><strong>Order Number:</strong> {order_id}</p>
                        <p><strong>Order Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
                        <p><strong>Service:</strong> {order_type}</p>
                        <p><strong>Amount:</strong> ${price:.2f}</p>
                    </div>
                    
                    <p>What happens next?</p>
                    <ul>
                        <li>Your reading is being prepared with care and attention to detail.</li>
                        <li>You will receive your reading via email within {'24 hours' if 'Tarot' in order_type else '48 hours'}.</li>
                        <li>The reading will be delivered as a PDF attachment to the email address you provided.</li>
                    </ul>
                    
                    <p>If you have any questions about your order, please don't hesitate to contact us.</p>
                    
                    <p>Thank you for choosing Wildflowers Tarot for your spiritual guidance needs.</p>
                    
                    <p>Warm regards,</p>
                    <p>The Wildflowers Tarot Team</p>
                    
                    <a href="https://www.wildflowerstarot.com/account" class="button">View Your Order</a>
                </div>
                
                <div class="footer">
                    <p>© {datetime.now().year} Wildflowers Tarot. All rights reserved.</p>
                    <p>This email was sent to {recipient_email} regarding order #{order_id}.</p>
                    <p><a href="https://www.wildflowerstarot.com">www.wildflowerstarot.com</a> | <a href="mailto:info@wildflowerstarot.com">info@wildflowerstarot.com</a></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Plain text alternative
        text_body = f"""
        Dear {recipient_name},
        
        Thank you for your order with Wildflowers Tarot. We're delighted to confirm that your order has been received and is being processed.
        
        Order Details:
        - Order Number: {order_id}
        - Order Date: {datetime.now().strftime('%B %d, %Y')}
        - Service: {order_type}
        - Amount: ${price:.2f}
        
        What happens next?
        - Your reading is being prepared with care and attention to detail.
        - You will receive your reading via email within {'24 hours' if 'Tarot' in order_type else '48 hours'}.
        - The reading will be delivered as a PDF attachment to the email address you provided.
        
        If you have any questions about your order, please don't hesitate to contact us.
        
        Thank you for choosing Wildflowers Tarot for your spiritual guidance needs.
        
        Warm regards,
        The Wildflowers Tarot Team
        
        View your order: https://www.wildflowerstarot.com/account
        
        © {datetime.now().year} Wildflowers Tarot. All rights reserved.
        This email was sent to {recipient_email} regarding order #{order_id}.
        www.wildflowerstarot.com | info@wildflowerstarot.com
        """
        
        return self._send_email(recipient_email, subject, text_body, html_body)
    
    def _send_email(self, recipient_email, subject, text_body, html_body, attachment_path=None):
        """
        Send an email with optional PDF attachment.
        
        Args:
            recipient_email (str): Recipient's email address
            subject (str): Email subject
            text_body (str): Plain text email body
            html_body (str): HTML email body
            attachment_path (str, optional): Path to attachment file
        
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"Wildflowers Tarot <{self.sender_email}>"
            msg['To'] = recipient_email
            
            # Attach parts
            part1 = MIMEText(text_body, 'plain')
            part2 = MIMEText(html_body, 'html')
            msg.attach(part1)
            msg.attach(part2)
            
            # Attach PDF if provided
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, 'rb') as file:
                    attachment = MIMEApplication(file.read(), _subtype="pdf")
                    attachment.add_header('Content-Disposition', 'attachment', 
                                         filename=os.path.basename(attachment_path))
                    msg.attach(attachment)
            
            # Connect to server and send
            # Note: In a production environment, use proper error handling and secure connection
            # This is a simplified example
            print(f"[DEMO MODE] Email would be sent to {recipient_email}")
            print(f"Subject: {subject}")
            print(f"Attachment: {attachment_path if attachment_path else 'None'}")
            
            # Uncomment for actual sending in production
            """
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            """
            
            return True
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create email delivery system
    email_system = EmailDeliverySystem()
    
    # Example order confirmation
    email_system.send_order_confirmation_email(
        "customer@example.com",
        "Jane Smith",
        "WFT12345",
        "Celtic Cross Tarot Reading",
        45.00
    )
    
    # Example tarot reading delivery
    email_system.send_tarot_reading_email(
        "customer@example.com",
        "Jane Smith",
        "WFT12345",
        "/path/to/tarot_reading.pdf",
        "Celtic Cross"
    )
    
    # Example palm reading delivery
    email_system.send_palm_reading_email(
        "customer@example.com",
        "John Doe",
        "WFT67890",
        "/path/to/palm_reading.pdf"
    )
